# OpenHound Workshop

This repository contains materials (notebooks + slides) for the OpenHound workshop. The workshop uses the public [PokeAPI](https://pokeapi.co/) for learning how resource collection works before converting collected resources into OpenGraph.


## Workshop content

| Section | Purpose | Link |
|---|---|---|
| `notebooks/01-introduction.py` | Introduction to OpenHound and manual resource collection.ion | [![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/github/d3vzer0/openhound-workshop/blob/master/notebooks/01-introduction.py)|
| `notebooks/02-pydantic.py` | Pydantic basics and response validation | [![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/github/d3vzer0/openhound-workshop/blob/master/notebooks/02-pydantic.py)|
| `notebooks/03-dlt.py` | DLT basics and paginated API collection | [![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/github/d3vzer0/openhound-workshop/blob/master/notebooks/03-dlt.py)|
| `notebooks/04-openhound.py` | OpenHound and the `collect -> preproc -> convert` pipeline|  |
| `notebooks/05-agents.py` | Agentic development with OpenHound skills | |


## Source API

The workshop uses PokeAPI's Pokemon list endpoint:

```text
https://pokeapi.co/api/v2/pokemon?limit=10&offset=0
```


## Container
You can run Marimo with the OpenCode agent as a container using any container runtime. I use the following .zshrc alias to start the container via Apple Containers. This runs Marimo and OpenCode in a local container and avoids giving the process broad host filesystem access. It still mounts your OpenCode config/state so the agent can use your existing providers. Only use this with notebooks and workspaces you trust.

Warning: OpenCode uses SQLite to maintain state and is not meant to run multiple instances at the same time. Make sure you're only running 1 OpenCode instance.

```
marimauw() {
  container run -it --rm \
    --user "$(id -u):$(id -g)" \
    -v "$PWD:$PWD" \
    -e HOME=/home/marimo \
    -v "$HOME/.config/opencode:/home/marimo/.config/opencode" \
    -v "$HOME/.local/share/opencode:/home/marimo/.local/share/opencode" \
    -v "$HOME/.local/state/opencode:/home/marimo/.local/state/opencode" \
    -v "$HOME/.cache/opencode:/home/marimo/.cache/opencode" \
    -p 127.0.0.1:2718:2718 \
    -p 127.0.0.1:3023:3023 \
    --cpus 4 \
    --memory 4g \
    -w "$PWD" \
    marimo:latest "$@"
}
```


## Current Status

This repository is under active development. 
