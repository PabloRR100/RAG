# RAG

## Project Structure

This project is defined as a UV Workspace. 

It containes a main library "rag" meant to be distributed as a Python package.    
There are also 2 application built on top of the framework, an API and a UI.  

```
├── LICENSE
├── Makefile
├── README.md
├── apps
│   ├── rag_api
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   ├── hello.py
│   │   └── pyproject.toml
│   └── rag_ui
│       ├── Dockerfile
│       ├── README.md
│       ├── hello.py
│       └── pyproject.toml
├── dist
├── docker-compose.yaml
├── packages
│   └── rag
│       ├── Makefile
│       ├── pyproject.toml
│       └── src
├── pyproject.toml
└── uv.lock
```


## RAG Framework

The idea in this repo is to provide a framework to easily create and consume RAG APIs/UIs.  
The developers should simply inherit and implement the main classes and invoke the builder methods.  

Examples: ... 
TODO (pablo): COMPLETE.  

