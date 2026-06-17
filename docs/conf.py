import os
from pathlib import Path
import re
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "nymea"
author = "nymea"
html_title = "nymea"

extensions = []
templates_path = ["_templates"]
exclude_patterns = []

html_logo = "../static/img/logo.svg"
html_favicon = "../static/img/logo.svg"
html_extra_path = ["../static"]
html_static_path = ["_static"]
html_css_files = ["nymea.css"]
html_js_files = ["nymea-copy-code.js"]
html_theme = "sphinx_book_theme"
html_context = {
    "default_mode": "dark",
}
html_theme_options = {
    "navigation_with_keys": False,
    "show_navbar_depth": 2,
    "use_download_button": False,
    "use_fullscreen_button": False,
    "use_repository_button": False,
    "pygments_light_style": "tango",
    "pygments_dark_style": "monokai",
    "switcher": {
        "json_url": "/switcher.json",
        "version_match": os.environ.get("DOCS_VERSION", "latest"),
    },
    "navbar_end": ["version-switcher"],
    "show_version_warning_banner": True,
}


def make_image_paths_relative(app, exception):
    if exception is not None or app.builder.format != "html":
        return

    output_dir = Path(app.outdir)
    image_dir = output_dir / "img"
    if not image_dir.exists():
        return

    pattern = re.compile(r'(<img\b[^>]*\bsrc=)(["\'])/img/')
    for html_file in output_dir.rglob("*.html"):
        relative_image_dir = os.path.relpath(image_dir, html_file.parent).replace(os.sep, "/")
        replacement = rf"\1\2{relative_image_dir}/"
        body = html_file.read_text(encoding="utf-8")
        updated = pattern.sub(replacement, body)
        if updated != body:
            html_file.write_text(updated, encoding="utf-8")


def setup(app):
    app.connect("build-finished", make_image_paths_relative)
