#!/usr/bin/env python3

import argparse
import html
import json
import os
import re
import shutil
from pathlib import Path
from urllib.parse import urlparse

import git


ROOT = Path(__file__).resolve().parents[1]
SRC_PAGES = ROOT / "src" / "pages"
DOCS = ROOT / "docs"
SOURCE_CACHE = ROOT / "tools" / "source"

NYMEA_REPOS = {
    "nymea": "https://github.com/nymea/nymea",
    "nymea-plugins": "https://github.com/nymea/nymea-plugins",
    "nymea-plugin-knx": "https://github.com/nymea/nymea-plugin-knx",
    "nymea-plugins-modbus": "https://github.com/nymea/nymea-plugins-modbus",
    "nymea-plugins-zigbee": "https://github.com/nymea/nymea-plugins-zigbee",
    "nymea-plugins-zwave": "https://github.com/nymea/nymea-plugins-zwave",
}

INTEGRATION_CATEGORIES = [
    "light",
    "socket",
    "multimedia",
    "sensor",
    "heating",
    "online-service",
    "tool",
    "diy",
    "door",
    "switch",
    "notification",
    "weather",
    "appliance",
    "shading",
    "energy",
    "garage",
]


def slug(value):
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "item"


def title_from_slug(value):
    return value.replace("-", " ").title()


def underline(title, char="="):
    return f"{title}\n{char * len(title)}\n\n"


def ensure_parent(path):
    path.parent.mkdir(parents=True, exist_ok=True)


def write(path, text):
    ensure_parent(path)
    path.write_text(text, encoding="utf-8")


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def clone_or_update(name, url, branch):
    SOURCE_CACHE.mkdir(parents=True, exist_ok=True)
    target = SOURCE_CACHE / name
    if target.exists():
        try:
            repo = git.Repo(target)
            try:
                repo.git.fetch("origin", "+refs/heads/*:refs/remotes/origin/*", "--tags")
            except git.GitCommandError as error:
                print(f"Warning: could not refresh {name}; using cached checkout. {error}")
        except git.InvalidGitRepositoryError:
            shutil.rmtree(target)
            repo = git.Repo.clone_from(url, target)
    else:
        repo = git.Repo.clone_from(url, target)
    try:
        repo.git.checkout("-B", branch, f"origin/{branch}")
        repo.git.reset("--hard", f"origin/{branch}")
    except git.GitCommandError:
        # Tags and local-only refs do not have an origin/<name> tracking ref.
        repo.git.checkout(branch)
    return target


def normalize_language(language):
    mapping = {
        "c++": "cpp",
        "bash": "bash",
        "sh": "bash",
        "javascript": "javascript",
        "js": "javascript",
        "json": "json",
        "python": "python",
        "qml": "qml",
        "xml": "xml",
    }
    return mapping.get(language.strip().lower(), language.strip().lower())


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    raw = text[4:end].strip()
    data = {}
    for line in raw.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip("\"'")
    return data, text[text.find("\n", end + 1) + 1 :]


def strip_mdsvex(text):
    text = re.sub(r"<script\b.*?</script>\s*", "", text, flags=re.DOTALL)
    text = text.replace("<Code>", "").replace("</Code>", "")
    return text


def convert_inline(text, base_doc=None):
    text = text.replace("\\)", ")")
    text = re.sub(r"<br\s*/?>", "\n\n", text, flags=re.I)
    if text.count("`") % 2 == 1:
        text = text.replace("`", "\\`")
    text = re.sub(r"`([^`]+)`", r"``\1``", text)
    text = re.sub(r"``([^`]+)``(?=[A-Za-z0-9])", r"``\1`` ", text)

    def image(match):
        alt = match.group(1).strip()
        target = match.group(2).strip()
        if " " in target and not target.startswith("http"):
            target = target.split(" ")[0]
        if target.startswith("/"):
            return f'\n.. raw:: html\n\n   <img src="{html.escape(target)}" alt="{html.escape(alt)}">\n'
        if target.startswith("img/"):
            return f'\n.. raw:: html\n\n   <img src="/{html.escape(target)}" alt="{html.escape(alt)}">\n'
        if target.startswith("developers/"):
            return f'\n.. raw:: html\n\n   <img src="/img/{html.escape(target)}" alt="{html.escape(alt)}">\n'
        return f"\n.. image:: {target}\n   :alt: {alt}\n"

    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", image, text)

    def link(match):
        label = match.group(1).replace("`", "")
        target = match.group(2).strip()
        if target.startswith("#"):
            return f"`{label} <{target}>`__"
        return f"`{label} <{target}>`__"

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, text)
    text = text.replace("__*", "__ *").replace("__**", "__ **")
    return text


def convert_markdown(text, default_title=None, label=None):
    frontmatter, text = parse_frontmatter(text)
    title = frontmatter.get("title", default_title)
    text = strip_mdsvex(text)
    lines = text.splitlines()
    out = []
    in_code = False
    code_language = ""
    raw_html = []
    wrote_title = False

    if label:
        out.append(f".. _{label}:\n\n")
    if title:
        out.append(underline(title))
        wrote_title = True

    def flush_raw():
        nonlocal raw_html
        if not raw_html:
            return
        out.append(".. raw:: html\n\n")
        for raw_line in raw_html:
            out.append(f"   {raw_line}\n")
        out.append("\n")
        raw_html = []

    for line in lines:
        fence = re.match(r"^```(.*)$", line)
        if fence:
            flush_raw()
            if not in_code:
                in_code = True
                code_language = normalize_language(fence.group(1))
                # Authored Markdown contains many illustrative pseudo-code
                # snippets. Use plain literal blocks to avoid lexer warnings
                # becoming build failures.
                out.append("::\n\n")
            else:
                in_code = False
                out.append("\n")
            continue

        if in_code:
            out.append(f"   {line}\n")
            continue

        if re.match(r"^\s*<(img|a|video|iframe|br|div|span)\b", line, re.I):
            raw_html.append(line)
            continue

        flush_raw()

        if line.startswith("    ") and line.strip():
            out.append("::\n\n")
            out.append(f"   {line.strip()}\n\n")
            continue
        if line.startswith(("  ", "\t")) and line.strip() and not re.match(r"^\s*[*-]\s+", line):
            line = line.strip()

        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            heading_text = convert_inline(heading.group(2)).strip()
            level = len(heading.group(1))
            if level == 1 and wrote_title:
                level = 2
            char = "=" if level == 1 and not wrote_title else "-"
            out.append(underline(heading_text, char))
            wrote_title = True
            continue

        if line.startswith("> "):
            out.append(".. note::\n\n")
            out.append(f"   {convert_inline(line[2:])}\n\n")
            continue

        if re.match(r"^\s*\|.*", line):
            # Markdown tables are rare here; keep them in a parsed-literal block
            # rather than risking malformed RST tables.
            out.append(f"::\n\n   {line}\n\n")
            continue

        if re.match(r"^\s*([-*_])\1\1+\s*$", line):
            out.append("\n")
            continue

        if re.match(r"^\s*([*-])\s+", line) or re.match(r"^\s*\d+[.)]\s+", line):
            out.append(convert_inline(line) + "\n\n")
            continue

        out.append(convert_inline(line) + "\n")

    flush_raw()
    return "".join(out).strip() + "\n"


def copy_authored_docs():
    source_root = SRC_PAGES / "documentation"
    for md in sorted(source_root.rglob("*.md")):
        if md.name.startswith("_"):
            continue
        rel = md.relative_to(source_root).with_suffix(".rst")
        target = DOCS / "documentation" / rel
        unique_label = "doc-" + slug(str(rel.with_suffix("")))
        write(target, convert_markdown(md.read_text(encoding="utf-8"), default_title=title_from_slug(md.stem), label=unique_label))

    for directory in sorted((DOCS / "documentation").rglob("*")):
        if not directory.is_dir():
            continue
        rst_files = sorted(p for p in directory.glob("*.rst") if p.name != "index.rst")
        child_indexes = sorted(p for p in directory.iterdir() if p.is_dir() and (p / "index.rst").exists())
        if not rst_files and not child_indexes:
            continue
        index = directory / "index.rst"
        title = title_from_slug(directory.name)
        entries = [p.stem for p in rst_files] + [p.name + "/index" for p in child_indexes]
        if index.exists():
            body = index.read_text(encoding="utf-8").rstrip() + "\n\n"
            if ".. toctree::" in body:
                continue
        else:
            body = underline(title)
        body += ".. toctree::\n   :maxdepth: 2\n\n"
        body += "".join(f"   {entry}\n" for entry in entries)
        write(index, body)


def load_interfaces(nymea_path):
    path = nymea_path / "libnymea" / "interfaces"
    interfaces = {}
    for file in sorted(path.glob("*.json")):
        interfaces[file.stem] = read_json(file)
    return interfaces


def generate_interfaces(nymea_path):
    parts = [underline("Interfaces")]
    for name, data in load_interfaces(nymea_path).items():
        parts.append(f".. _interface-{slug(name)}:\n\n")
        parts.append(underline(name, "-"))
        description = data.get("description")
        if description:
            parts.append(description + "\n\n")
        parts.append(".. code-block:: json\n\n")
        for line in json.dumps(data, indent=2).splitlines():
            parts.append(f"   {line}\n")
        parts.append("\n")
        extends = data.get("extends")
        if extends:
            if isinstance(extends, str):
                extends = [extends]
            links = ", ".join(f"`{item} <#interface-{slug(item)}>`__" for item in extends)
            parts.append(f"See also: {links}\n\n")
    write(DOCS / "documentation" / "resources" / "interfaces.rst", "".join(parts))


def load_api(nymea_path):
    text = (nymea_path / "tests" / "auto" / "api.json").read_text(encoding="utf-8")
    version, raw = text.split("\n", 1)
    return version, json.loads(raw)


def refs_in(value):
    refs = []
    if isinstance(value, str) and value.startswith("$ref:"):
        refs.append(value.replace("$ref:", ""))
    elif isinstance(value, list):
        for item in value:
            refs.extend(refs_in(item))
    elif isinstance(value, dict):
        for item in value.values():
            refs.extend(refs_in(item))
    return sorted(set(refs))


def api_id(key):
    key = key[0].lower() + key[1:]
    key = key.replace(".", "")
    return re.sub(r"([A-Z])", lambda m: "-" + m.group(1).lower(), key)


def json_block(value):
    lines = [".. code-block:: json\n\n"]
    for line in json.dumps(value, indent=2).splitlines():
        lines.append(f"   {line}\n")
    lines.append("\n")
    return "".join(lines)


def render_api_items(title, items, include_descriptions=True, label_prefix="api"):
    parts = [underline(title, "-")]
    for key in sorted(items):
        value = items[key]
        parts.append(f".. _{label_prefix}-{api_id(key)}:\n\n")
        parts.append(underline(key, "~"))
        if isinstance(value, dict) and include_descriptions and value.get("description"):
            parts.append(value["description"].replace("\n", "\n\n") + "\n\n")
        if isinstance(value, dict) and value.get("deprecated"):
            parts.append(f".. note:: Deprecated. {value['deprecated']}\n\n")
        if isinstance(value, dict) and value.get("params") is not None:
            parts.append("Params\n^^^^^^\n\n")
            parts.append(json_block(value["params"]))
        if isinstance(value, dict) and value.get("returns") is not None:
            parts.append("Returns\n^^^^^^^\n\n")
            parts.append(json_block(value["returns"]))
        if not isinstance(value, dict) or ("params" not in value and "returns" not in value):
            stripped = dict(value) if isinstance(value, dict) else value
            if isinstance(stripped, dict):
                stripped.pop("description", None)
                stripped.pop("deprecated", None)
            parts.append(json_block(stripped))
        refs = refs_in(value)
        if refs:
            links = ", ".join(f"`{ref} <#{label_prefix}-{api_id(ref)}>`__" for ref in refs)
            parts.append(f"See also: {links}\n\n")
    return "".join(parts)


def generate_api(nymea_path):
    version, api = load_api(nymea_path)
    api_root = DOCS / "documentation" / "resources" / "api"
    if api_root.exists():
        shutil.rmtree(api_root)
    api_root.mkdir(parents=True)

    # Single-page reference: Objects, Enums, Flags, Methods, Notifications
    index = [underline("API Reference")]
    index.append(f"The current JSON-RPC API version is ``{version}``.\n\n")
    index.append("For a namespace-based overview see :doc:`namespaces`.\n\n")
    index.append(render_api_items("Objects", api["types"], include_descriptions=False, label_prefix="api"))
    index.append(render_api_items("Enums", api["enums"], include_descriptions=False, label_prefix="api"))
    index.append(render_api_items("Flags", api["flags"], include_descriptions=False, label_prefix="api"))
    index.append(render_api_items("Methods", api["methods"], label_prefix="api"))
    index.append(render_api_items("Notifications", api["notifications"], label_prefix="api"))
    index.append("\n.. toctree::\n   :hidden:\n\n   namespaces\n")
    write(api_root / "index.rst", "".join(index))

    # Namespace overview — links back into index anchors
    namespaces = sorted(set(k.split(".")[0] for k in list(api["methods"]) + list(api["notifications"])))
    ns_parts = [underline("API Namespaces")]
    ns_parts.append("The API is organised into the following namespaces.\n\n")
    for ns in namespaces:
        ns_parts.append(f".. _api-namespace-{slug(ns)}:\n\n")
        ns_parts.append(underline(ns, "-"))
        ns_methods = sorted(k for k in api["methods"] if k.split(".")[0] == ns)
        ns_notifs = sorted(k for k in api["notifications"] if k.split(".")[0] == ns)
        if ns_methods:
            links = ", ".join(f":ref:`{k} <api-{api_id(k)}>`" for k in ns_methods)
            ns_parts.append(f"**Methods:** {links}\n\n")
        if ns_notifs:
            links = ", ".join(f":ref:`{k} <api-{api_id(k)}>`" for k in ns_notifs)
            ns_parts.append(f"**Notifications:** {links}\n\n")
    write(api_root / "namespaces.rst", "".join(ns_parts))

    raw = [":orphan:\n\n", underline("The complete API")]
    raw.append(f"In the following section you can find a detailed description of the current API version ``{version}``.\n\n")
    raw.append(render_api_items("Enums", api["enums"], include_descriptions=False, label_prefix="raw-api"))
    raw.append(render_api_items("Flags", api["flags"], include_descriptions=False, label_prefix="raw-api"))
    raw.append(render_api_items("Types", api["types"], include_descriptions=False, label_prefix="raw-api"))
    raw.append(render_api_items("Methods", api["methods"], label_prefix="raw-api"))
    raw.append(render_api_items("Notifications", api["notifications"], label_prefix="raw-api"))
    write(DOCS / "documentation" / "developers" / "clients" / "raw-api.rst", "".join(raw))


def generate_plugin_json_doc(nymea_path):
    template = ROOT / "tools" / "plugin-json-template.md.in"
    if not template.exists():
        return
    _version, api = load_api(nymea_path)
    unit_list = "\n".join(f"* {item}" for item in api["enums"]["Unit"])
    input_type_list = "\n".join(f"* {item}" for item in api["enums"]["InputType"])
    markdown = template.read_text(encoding="utf-8")
    markdown = markdown.replace("@@GENERATED_UNITS@@", unit_list)
    markdown = markdown.replace("@@GENERATED_INPUTTYPES@@", input_type_list)
    rst = convert_markdown(markdown, default_title="The plugin JSON file", label="doc-developers-integrations-plugin-json")
    write(DOCS / "documentation" / "developers" / "integrations" / "plugin-json.rst", rst)


def find_plugins(repo_paths):
    plugins = []
    for repo_path in repo_paths:
        for readme in repo_path.rglob("README.md"):
            plugin_dir = readme.parent
            if (plugin_dir / "meta.json").exists():
                plugins.append(plugin_dir)
    return sorted(plugins)


def plugin_info(plugin_dir):
    candidates = list(plugin_dir.glob("integrationplugin*.json"))
    if not candidates:
        return {}
    try:
        return read_json(candidates[0])
    except Exception:
        return {}


def rewrite_plugin_markdown(text, plugin_dir, repo_dir):
    repo_name = repo_dir.name
    rel_plugin = plugin_dir.relative_to(repo_dir).as_posix()

    def replace_link(match):
        prefix, alt, target = match.groups()
        parsed = urlparse(target)
        if parsed.scheme or target.startswith("#") or target.startswith("mailto:"):
            return match.group(0)
        clean_target = target.split(" ")[0]
        absolute = plugin_dir / clean_target
        if absolute.exists():
            github = f"https://github.com/nymea/{repo_name}/blob/master/{rel_plugin}/{clean_target}"
            if prefix == "!":
                github = f"https://raw.githubusercontent.com/nymea/{repo_name}/master/{rel_plugin}/{clean_target}"
            return f"{prefix}[{alt}]({github})"
        return match.group(0)

    return re.sub(r"(!?)\[([^\]]*)\]\(([^)]+)\)", replace_link, text)


def generate_integrations(repo_paths):
    integrations_root = DOCS / "documentation" / "resources" / "integrations"
    if integrations_root.exists():
        shutil.rmtree(integrations_root)
    integrations_root.mkdir(parents=True)
    plugins = []

    for plugin_dir in find_plugins(repo_paths):
        try:
            meta = read_json(plugin_dir / "meta.json")
        except Exception:
            continue
        info = plugin_info(plugin_dir)
        name = plugin_dir.name
        readme = plugin_dir / "README.md"
        repo_dir = next(path for path in repo_paths if plugin_dir.is_relative_to(path))
        vendors = []
        for vendor in info.get("vendors", []):
            vendors.append(vendor.get("displayName", ""))
        meta = {
            "name": name,
            "title": meta.get("title", title_from_slug(name)),
            "tagline": meta.get("tagline", ""),
            "categories": meta.get("categories", []),
            "technologies": meta.get("technologies", []),
            "offline": meta.get("offline"),
            "stability": meta.get("stability", ""),
            "vendors": [vendor for vendor in vendors if vendor],
        }
        plugins.append(meta)
        body = convert_markdown(
            rewrite_plugin_markdown(readme.read_text(encoding="utf-8"), plugin_dir, repo_dir),
            default_title=meta["title"],
            label=f"integration-{slug(name)}",
        )
        header = ""
        if meta["tagline"]:
            header += meta["tagline"] + "\n\n"
        if meta["categories"]:
            header += "**Categories:** " + ", ".join(meta["categories"]) + "\n\n"
        if meta["technologies"]:
            header += "**Technologies:** " + ", ".join(meta["technologies"]) + "\n\n"
        write(integrations_root / f"{name}.rst", body.replace("\n\n", "\n\n" + header, 1) if header else body)

    plugins.sort(key=lambda item: item["title"].lower())
    index = underline("Integrations")
    index += "This section lists the currently supported nymea integrations.\n\n"
    index += ".. toctree::\n   :maxdepth: 1\n\n"
    index += "   categories\n"
    index += "".join(f"   {plugin['name']}\n" for plugin in plugins)
    write(integrations_root / "index.rst", index)

    by_category = {}
    for plugin in plugins:
        categories = plugin["categories"] or ["other"]
        for category in categories:
            by_category.setdefault(category, []).append(plugin)

    categories_index = underline("Integration Categories")
    categories_index += ".. toctree::\n   :maxdepth: 1\n\n"
    for category in sorted(by_category):
        path = integrations_root / f"category-{slug(category)}.rst"
        categories_index += f"   category-{slug(category)}\n"
        body = underline(title_from_slug(category))
        body += ".. toctree::\n   :maxdepth: 1\n\n"
        body += "".join(f"   {plugin['name']}\n" for plugin in by_category[category])
        write(path, body)
    write(integrations_root / "categories.rst", categories_index)


def generate_redirects():
    redirects = {
        "documentation/resources/integrations.html": "documentation/resources/integrations/",
        "documentation/resources/api.html": "documentation/resources/api/",
        "contact.html": "/",
    }
    target = DOCS / "_redirects"
    lines = []
    for src, dst in sorted(redirects.items()):
        lines.append(f"{src} {dst}\n")
    write(target, "".join(lines))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--branch", default="master")
    args = parser.parse_args()

    if SRC_PAGES.exists():
        copy_authored_docs()
    nymea = clone_or_update("nymea", NYMEA_REPOS["nymea"], args.branch)
    plugin_repos = [
        clone_or_update(name, url, args.branch)
        for name, url in NYMEA_REPOS.items()
        if name != "nymea"
    ]
    generate_interfaces(nymea)
    generate_api(nymea)
    generate_plugin_json_doc(nymea)
    generate_integrations(plugin_repos)
    generate_redirects()


if __name__ == "__main__":
    main()
