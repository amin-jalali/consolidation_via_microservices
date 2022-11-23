# Systems consolidation approach using microservices architecture

## How to run this project?

Spin up the containers:

```sh
$ docker-compose up -d --build
```

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
Now you can simply open [http://localhost:5000](http://localhost:5000) 
to view the web app consists of (GET) blocking response model and (GET, POST) Pooling request model



## Celery task monitoring via Flower
Just open [http://localhost:5555](http://localhost:5555) 
to view a web dashboard by the help of Flower(Celery monitoring tool)



## System unit & acceptance test
```
docker-compose exec api_gateway python -m pytest -vv
```