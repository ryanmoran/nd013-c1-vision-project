# Instructions

## Requirements

* docker

## Build
Build the image with:
```
docker build -t project-dev -f Dockerfile .
```

Create a container with:
```
docker run -v <PATH TO LOCAL PROJECT FOLDER>:/app/project/ -v <PATH TO DATA>:/data -p 3002:3002 -it project-dev bash
```
and any other flag you find useful to your system (eg, `--shm-size`).
