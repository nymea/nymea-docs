# nymea documentation

This repository builds the nymea documentation as a static Sphinx site.

## Requirements

Install the system tools:

```sh
sudo apt install python3 python3-pip python3-venv make git
```

Create a virtual environment and install the Python dependencies:

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Build

Generate documentation from the cached upstream nymea repositories and build the site:

```sh
make generate html
```

The default upstream branch is `master`. To build from another branch or tag:

```sh
make generate html BRANCH=<branch-or-tag>
```

The generated site is written to `public/`.

For local file browsing, open `public/index.html` directly. The build uses
explicit `.html` links so documentation pages can be browsed without a local web
server.

## Preview

```sh
make serve
```

Open `http://localhost:8000`.

## Clean

```sh
make clean
```

This removes the Sphinx output and generated RST files. It keeps `tools/source/`, which is used as a clone cache for upstream nymea repositories.

## LXC Build

The LXC helper creates an Ubuntu container, mounts the repository, installs the Sphinx build dependencies, and runs the same build:

```sh
./build-lxc.sh build
```

Use a different upstream branch:

```sh
./build-lxc.sh --branch=<branch-or-tag> build
```

Enter the container:

```sh
./build-lxc.sh shell
```
