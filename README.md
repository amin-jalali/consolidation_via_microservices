# Systems consolidation approach using microservices architecture

## How to run this project?

Spin up the containers:

```sh
$ docker-compose up -d --build
```

In order to run multiple instance of api_gateway and/or celery_worker
instead of last command you can run application by this command:

```sh
$ docker-compose up -d --build --scale api_gateway=<number> --scale celery_worker=<number>
```

If you wonder to check load balancing or request flow between containers, 
remove ```-d``` from above commands.


At the end you have to see something as below:


```
Creating sales                                        ... done
Creating warehouse                                    ... done
Creating consolidation_microservices_set_host_alias_1 ... done
Creating accounting                                   ... done
Creating api_gateway                                  ... done
Creating celery_worker                                ... done
Creating flower                                       ... done
```

## System user interface
Now you can simply open [http://localhost:4000](http://localhost:4000) 
to view the web app consists of (GET) blocking response model and (GET, POST) Pooling request model



## Celery task monitoring via Flower
Just open [http://localhost:5555](http://localhost:5555) 
to view a web dashboard by the help of Flower(Celery monitoring tool)


## API Documentation via Swagger
open [http://localhost:4000/api/docs/](http://localhost:4000/api/docs/) 
to view API documentations


## System unit & acceptance test
```
docker-compose exec api_gateway python -m pytest -vv
```

