# redis-chat
Chat app based on docker stack including redis, mongo, and flask


### Installing Docker Dev environement 

##### Requirements :

- Linux OS with Docker Engine
- Docker Compose

##### Steps :
- git clone the project in your **/usr/local/src** folder. 
- Build the docker image 

```bash
amao@localhost /usr/local/src/redis-chat $ docker build -t chat-flask-base .
```
- Run the stack

```bash
amao@localhost /usr/local/src/redis-chat $ docker-compose up [-d]
```

You should now have three running containers

```bash
amao@localhost /usr/local/src/redis-chat (master*) $ docker container ls -a
CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS                   PORTS                              NAMES
070506bb5404        chat-flask-base       "/bin/sh /var/www/fl…"   3 hours ago         Up 15 seconds            0.0.0.0:5000->5000/tcp             chat-flask
3b840160b186        mongo                 "docker-entrypoint.s…"   3 hours ago         Up 15 seconds            0.0.0.0:27017->27017/tcp           chat-mongo
f54faf512a8c        redis                 "docker-entrypoint.s…"   3 hours ago         Up 15 seconds            0.0.0.0:6377->6377/tcp, 6379/tcp   chat-redis
f364d6dbe553        1a68e6c90172          "/bin/sh -c 'pip3 in…"   3 hours ago         Exited (1) 3 hours ago                                      romantic_hypatia
11369e933b00        portainer/portainer   "/portainer"             4 weeks ago         Up 11 hours              0.0.0.0:9000->9000/tcp             portainer
```