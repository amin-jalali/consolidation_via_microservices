# Systems consolidation approach using microservices architecture

## How to run this project?

Spin up the containers:

```sh
$ docker-compose up -d --build
```

At the end you have to see something as below:

```
Creating sales                                ... done
Creating consolidation_ms_set_host_alias_1    ... done
Creating api_gateway                          ... done
```

Now you can simply open [http://localhost:5000](http://localhost:5000) 
to view the web app consists of two response model
</br>