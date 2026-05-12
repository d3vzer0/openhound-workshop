# OpenHound Workshop

This repository contains materials (notebooks + slides) for the OpenHound workshop. The workshop uses the public [PokeAPI](https://pokeapi.co/) for learning how resource collection works before converting collected resources into OpenGraph.


## Workshop content

| Section | Purpose | Link |
|---|---|---|
| `notebooks/01-introduction.py` | Introduction to OpenHound and manual resource collection.ion | [![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/github/d3vzer0/openhound-workshop/blob/master/notebooks/01-introduction.py)|
| `notebooks/02-pydantic.py` | Pydantic basics and response validation | [![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/github/d3vzer0/openhound-workshop/blob/master/notebooks/02-pydantic.py)|
| `notebooks/03-dlt.py` | DLT basics and paginated API collection | |
| `notebooks/04-openhound.py` | OpenHound and the `collect -> preproc -> convert` pipeline|  |
| `notebooks/05-agents.py` | Agentic development with OpenHound skills | |


## Source API

The workshop uses PokeAPI's Pokemon list endpoint:

```text
https://pokeapi.co/api/v2/pokemon?limit=10&offset=0
```


## Current Status

This repository is under active development. 
