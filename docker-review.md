# Docker review

## 0. Resources

1. [Docker 101 Tutorial](https://www.docker.com/101-tutorial/)
2. [Docker for the Absolute Beginner](https://www.udemy.com/course/learn-docker/)

## 1. Introduction

1. for solving compatibility and dependency issue
2. Docker Containers: Hardware -> OS Kernel -> Docker -> Containers -> Software
3. VM: Hardware -> Hypervisor -> OS -> Software
4. Containers and VM can be used together
5. Docker Image: a package or a template
6. Docker Container: an instances created form an Image
7. Container are meant to exit after tasks are finish

## 2. Basic Docker Commands

1. `docker run IMAGE_NAME`: start a new container, download an image if it's not on a host
    1. `docker run -d IMAGE_NAME`: start a container with detach mode (running in a background)
    2. `docker attach CONTAINER_ID_OR_NAME`: switch back to attach mode
    3. `docker run --name CONTAINER_NAME IMAGE_NAME`: start a container with a name
2. `docker start CONTAINER_NAME`: start a container that already exist
3. `docker ps`: list running containers information
4. `docker ps -a`: list all containers information
5. `docker stop CONTAINER_ID_OR_NAME`: stop a container
6. `docker rm CONTAINER_ID_OR_NAME`: remove a container
7. `docker images` `docker image ls`: list images on a host
8. `docker rmi IMAGE_NAME`: remove a image, dependent containers have to be remove first
9. `docker pull IMAGE_NAME`: download an image
10. `docker exec CONTAINER_ID_OR_NAME COMMAND`: execute a command

## 3. Docker Run Commands

1. `docker run IMAGE_NAME:TAG`: run the specific image. tag info is on Docker Hub
2. `docker run -i IMAGE_NAME`: run with interactive mode
3. `docker run -it IMAGE_NAME`: run with interactive mode and pseudo terminal
4. `docker run -p HOST_PORT:CONTAINER_PORT IMAGE_NAME`: map a host port to a container port. for accessing a container from outside a localhost.
5. `docker run -v HOST_PATH:CONTAINER_PATH IMAGE_NAME`: map a host path to a container path. for saving volume to a localhost.
6. `docker run -e ENV_VAR=VALUE IMAGE_NAME`: run with environment variables
7. `docker inspect CONTAINER_ID_OR_NAME`: detailed information about a container
    1. for looking container ip
    2. for checking environment variables
8. `docker logs CONTAINER_ID_OR_NAME`: container logs
9. `docker run --restart always IMAGE_NAME`: always restart the container if it stops.

## 4. Docker Images

1. `docker build`: build a new image with Dockerfile in the current directory
    1. `docker build PATH`: build a new image with Dockerfile in the PATH directory
    2. `docker build -t NAME:TAG PATH`: build a new image with NAME and TAG
    3.
2. Dockerfile Example

    ```
    FROM python:3.6

    RUN pip install flask

    COPY . /opt/

    EXPOSE 8080

    WORKDIR /opt

    ENTRYPOINT ["python", "app.py"]
    ```

3. Dockerfile Instruction
    1. `FROM <image>`: Defines a base image
    2. `RUN <command>`: Executes any commands in a new layer
    3. `COPY <src> <dest>`: Copies files
    4. `WORKDIR <directory>`: Sets the working directory for the following layer
    5. `EXPOSE <port>`: Exposed ports
    6. `# <comment>`: comment
    7. `CMD <command>`: command that is run once you start the container based
        - `CMD ["COMMAND", "PARAM1"]`: also work
    8. `ENTRYPOINT <command>`: command that add before the CMD
        - `ENTRYPOINT ["COMMAND", "PARAM1"]`: also work

4. CMD and ENTRYPOINT
    1. `docker run IMAGE_NAME COMMAND`
        1. it will overwrite the CMD inside the image
        2. it will append after the ENTRYPOINT inside the image
    2. CMD Example
        1. `CMD bash` is used for creating the image
        2. `docker run my_ubuntu sleep 5`
            - docker starts a container with `sleep 5` instead of `bash`
    3. ENTRYPOINT Example
        1. `ENTRYPOINT sleep` is used for creating the image
        2. `docker run my_ubuntu 10`
            - docker starts a container with `sleep 10`
    4. Use both CMD and ENTRYPOINT
        1. `ENTRYPOINT sleep CMD 5`
        2. CMD become similar to default value
        3. `docker run my_ubuntu`: sleep 5
        4. `docker run my_ubuntu 20`: sleep 20
5. `docker history IMAGE_NAME`: show the instructions when a image builds

## 5. Example Voting Application

1. voting-app (python): show voting options
2. in-memory DB (redis): save a voting result in memory
3. worker (.NET): process a voting result
4. db (PostgreSQL): save a result permanently
5. result-app (NodeJS): read and show a result from db

### 5.1 Legacy container links

1. It's a legacy feature
2. for connecting containers by sharing network information
3. now use custom user-defined networks

## 6. Docker Compose

1. Version 1 (Legacy)
2. Version 2 and 3 (now merged)

    ```yml
    services:
      # format
      CONTAINER_NAME:
        image: IMAGE_NAME:IMAGE_TAG
        ports:
          - HOST_PORT:CONTAINER_PORT
        links:
          - LINK_CONTAINER_NAME

      # example
      web:
        build: .
        ports:
          - "8000:5000"
      db:
        image: "postgres:9.4"
        environment: 
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
    ```

3. `docker compose up`: run with Compose

### 6.1 Docker Network with Compose

1. Default Network
    1. automatically create a network named `DIRECTORY_default`
    2. connects all services to that network
2. Custom Networks
    1. Defining networks in a compose file Example

        ```yml
        # docker-compose.yml

        services:
          # only connected to the frontend network
          web:
            image: nginx:latest
            networks:
              - frontend

          # connecting to both networks
          api:
            image: my-api-image
            networks:
              - frontend
              - backend

            # only connected to the backend network
          db:
            image: postgres:16
            networks:
              - backend

        # at the top level
        networks:
          # create a network named <project>_frontend and <project>_backend
          frontend:
          backend:
        ```

    2. Connecting to an external network
        1. create the shared network

            ```bash
            docker network create shared-proxy-net
            ```

        2. declare it as an external network in

            ```yml
            services:
            # to be accessed by the external reverse proxy
              myapp:
                image: my-app-image
                networks:
                  - default  # connect to default internal network
                  - proxy    # connect to the external proxy network

            networks:
              # this is optional, as Compose handles it automatically
              default:
                driver: bridge

              # declare 'proxy' as an external network
              proxy:
                name: shared-proxy-net # specify the real name of the external network
                external: true
            ```

## 7. Docker Registry

1. `REGISTRY/USER_ACCOUNT/IMAGE_REPOSITORY`
    1. `docker.io`: default registry (DockerHub)
    2. `library`: default user account
2. Private Registry
    1. `docker login PRIVATE_REGISTRY`: login to a private registry
    2. `docker run PRIVATE_REGISTRY/USER_ACCOUNT/IMAGE_REPOSITORY`
3. Deploy Private Registry
    1. `docker run -d -p 5000:5000 --name registry registry`: docker registry image
    2. `docker image tag IMAGE_NAME localhost:5000/IMAGE_NAME`: tag a image to a registry
    3. `docker push localhost:5000/IMAGE_NAME`: push a image to a registry
    4. `curl -X GET localhost:5000/v2/_catalog`: check the list of images in a registry
  
## 8. Docker Engine

1. structure
    1. Docker CLI
    2. REST API
    3. Docker Daemon
2. PID Namespace
    1. Docker utilizes Namespaces to create an independent environment
    2. The main process in the container has a PID of 1 (like the init process)
    3. On the host, however, this same process has different, non-privileged PID
3. Control groups (cgroups)
    1. for managing Docker container's resources
    2. `docker run --cpus=.5 ubuntu`: no more than 50% cpu usage
    3. `docker run --memory=100m ubuntu`: no more than 100MB
    4. link: [Resource constraints](https://docs.docker.com/engine/containers/resource_constraints/)

## 9. Docker Storage

1. Docker Layered architecture
    1. Image Layer
        1. each Dockerfile Instruction is a layer
        2. Docker can reuse layers for other images
        3. Image Layer is read only
    2. Container Layer
        1. it's a copy of an Image Layer
        2. it can be read or written
        3. changes in a Container Layer won't affect an Image Layer
        4. it will reset all the changes after a container stop
        5. set volumes to store any changes
2. Docker Volumes
    1. `docker volume create VOLUME_FOLDER_NAME`
        1. this will create a directory under the docker/volumes
    2. `docker run -v HOST_PATH:CONTAINER_PATH IMAGE_NAME`
        1. this will mount a directory in the host to container
        2. any changes in the container directory will save to the host directory
    3. `docker run --mount type=TYPE,source=HOST_PATH,target:CONTAINER_PATH`
        1. preferred method
        2. `type=bind` mount any directory to container
        3. `type=volume` mount docker volume to container
3. Docker Storage driver
    1. Link: [Storage driver](https://docs.docker.com/engine/storage/drivers/select-storage-driver/)

## 10. Docker Network

1. Default networks
    1. bridge
        1. docker host and all other containers will connect to this network by default
    2. none
        1. containers won't connect to any networks
        2. `docker run ubuntu --network=none`
    3. host
        1. containers will use same ports as docker host
        2. `docker run ubuntu --network=host`
2. User-defined networks
    1. `docker network create --driver bridge --subnet SUBNET_IP --gateway GATEWAY_IP NETWORK_NAME`
    2. `docker network ls`: show all the networks on a docker host
    3. `docker network inspect NETWORK_NAME`: inspect a network
3. Inspect Container Network
    1. `docker inspect CONTAINER_ID_OR_NAME`
    2. looking for `"Networks"`
4. Embedded DNS
    1. docker build in DNS server
    2. container can access another container by container name
    3. Example
        1. container `web` and container `mysql`
        2. inside the `web`, you can write `mysql.connect(mysql)`

## 11. Container Orchestration

1. for automating the deployment, scaling, and management of containers
2. Docker Swarm and kubernetes
3. The details will require other classes
