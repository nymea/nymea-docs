#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
MAX_VERSIONS="${MAX_VERSIONS:-5}"
SPHINXBUILD="${SPHINXBUILD:-sphinx-build}"
PUBLIC_DIR="$ROOT_DIR/public"

cd "$ROOT_DIR"

echo "==> Building latest..."
DOCS_VERSION=latest SPHINXBUILD="$SPHINXBUILD" make generate html

# Ensure shared upstream repo cache directory exists for worktrees to symlink into
mkdir -p "$ROOT_DIR/tools/source"

# N most recent v* tags; empty string if none exist yet
TAGS=$(git tag -l 'v*' | sort -V | tail -n "$MAX_VERSIONS")

for tag in $TAGS; do
    echo "==> Building $tag..."
    WORKTREE_DIR=$(mktemp -d)

    git worktree add "$WORKTREE_DIR" "$tag"

    # Share the upstream clone cache so each version doesn't re-clone from GitHub
    rm -rf "$WORKTREE_DIR/tools/source"
    ln -s "$ROOT_DIR/tools/source" "$WORKTREE_DIR/tools/source"

    (cd "$WORKTREE_DIR" && \
        DOCS_VERSION="$tag" \
        SPHINXBUILD="$SPHINXBUILD" \
        make generate html \
            BRANCH="$tag" \
            BUILDDIR="$PUBLIC_DIR/$tag")

    git worktree remove "$WORKTREE_DIR" --force
done

# Generate switcher.json (latest first, then tags newest-to-oldest)
{
    echo "["
    echo "  {\"name\": \"latest\", \"version\": \"latest\", \"url\": \"/\"}"
    for tag in $(echo "$TAGS" | sort -V -r); do
        echo "  ,{\"name\": \"$tag\", \"version\": \"$tag\", \"url\": \"/$tag/\"}"
    done
    echo "]"
} > "$PUBLIC_DIR/switcher.json"

# Copy switcher.json into each versioned subdirectory so local serving works too
for tag in $TAGS; do
    if [ -d "$PUBLIC_DIR/$tag" ]; then
        cp "$PUBLIC_DIR/switcher.json" "$PUBLIC_DIR/$tag/switcher.json"
    fi
done

echo "==> Done. Versions: latest${TAGS:+ $(echo "$TAGS" | tr '\n' ' ')}"
