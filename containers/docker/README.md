# [Docker](https://www.docker.com)
## Description
* Primary method for building and maintaining **un-secure** containers.
* Must have root access in order to work.
* Deployable to any machine.

## Packages
The default development containers will these packages by default.  Only the essentials are included.

* [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/)
* [Oh My Zsh](https://ohmyz.sh)

## Build
```bash
docker build -t <image_id> .  # The final argument is the path to the Dockerfile
```

## Images
```bash
docker images ls                # list images
docker image rm -f <image_id>   # remove an image
```

## Shell
```bash
docker run -it --name <container_id> <image_id> bash
```

##  Docker Compose
* Allows you to create multiple different builds using different Docker files.
* The context directory can be set from the `docker_compose.yml` file.
* More options than a standard Docker file.

## Running Commands
* In Docker each `RUN` command is treated as a new shell instance.  This means that commands cannot persist across different RUN commands.

```Docker
RUN command1    # this command is run in its own shell!
RUN command2    # this command is run in its own shell!
```

## Copying Folders/Files
* If you need to copy files or directories into the Docker container, first put them in an **artifacts** directory that can be seen from the context directory.

```Docker
COPY <artifact_directory> <container_path>
```
## Context Directory

* By default Dockerfiles are only aware of what is in their **context directory**.  A context directory is the directory where a Dockerfile is located in.  It cannot access any files outside of the context directory.

* The context directory can be set from the command line or from a `docker_compose.yml` file.

* It is recommended that all folders/files be copied be placed in an **artifacts** directory that is under the context directory.

## Out of Memory
* Occasionally you will need to clean your docker images and docker volumes in order to recover memory.

```console
docker volume prune
docker image prune
docker container prune
```
