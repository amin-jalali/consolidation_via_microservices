def get_local_docs():
    return {
        "/tasks/<task_id>": {
            "get": {
                "tags": [
                    "API Gateway (Pooling strategy)"
                ],
                "summary": "return the execution state of a task",
                "description": "if task is executing it will return PENDING status, if its gone away "
                               "will return FAILURE and if its done correctly "
                               "the result will return by the status of SUCCESS.",
                "operationId": "getTaskStatus",
                "consumes": [
                    "application/json",
                ],
                "produces": [
                    "application/json",
                ],
                "parameters": [
                    {
                        "in": "body",
                        "name": "task_id",
                        "description": "task_id is given by POOL service",
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK"
                    }
                },
            }
        },
        "/pool/<group>/<service_name>": {
            "get": {
                "tags": [
                    "API Gateway (Pooling strategy)"
                ],
                "summary": "Pooling strategy, GET method in order to call a resource from API groups",
                "description": "By the help of Pooling strategy, GET method you can asynchronously call a resource"
                               " from API groups and immediately receive a unique code, in an appropriate "
                               "time interval, you can ask for response and state of your task "
                               "using /tasks/<task_id> API",
                "operationId": "getTaskStatus",
                "consumes": [
                    "application/json",
                ],
                "produces": [
                    "application/json",
                ],
                "parameters": [
                    {
                        "in": "body",
                        "name": "payload",
                        "description": "rely on resources requirements such as (sales, accounting and etc) "
                                       "which is mentioned in their own documents",
                    }
                ],
                "responses": {
                    "task_id": {
                        "description": "a code like: 211c1827-23ea-4090-b58e-fa89335e1527"
                    }
                },
            },
            "post": {
                "tags": [
                    "API Gateway (Pooling strategy)"
                ],
                "summary": "Pooling strategy, POST method in order to call a resource from API groups",
                "description": "By the help of Pooling strategy, POST method you can asynchronously call a resource"
                               " from API groups and immediately receive a unique code, in an appropriate "
                               "time interval, you can ask for response and state of your task "
                               "using /tasks/<task_id> API",
                "operationId": "getTaskStatus",
                "consumes": [
                    "application/json",
                ],
                "produces": [
                    "application/json",
                ],
                "parameters": [
                    {
                        "in": "body",
                        "name": "payload",
                        "description": "rely on resources requirements such as (sales, accounting and etc) "
                                       "which is mentioned in their own documents",
                    }
                ],
                "responses": {
                    "task_id": {
                        "description": "a code like: 211c1827-23ea-4090-b58e-fa89335e1527"
                    }
                },
            },
            "put": {
                "tags": [
                    "API Gateway (Pooling strategy)"
                ],
                "summary": "Pooling strategy, PUT method in order to call a resource from API groups",
                "description": "By the help of Pooling strategy, PUT method you can asynchronously call a resource"
                               " from API groups and immediately receive a unique code, in an appropriate "
                               "time interval, you can ask for response and state of your task "
                               "using /tasks/<task_id> API",
                "operationId": "getTaskStatus",
                "consumes": [
                    "application/json",
                ],
                "produces": [
                    "application/json",
                ],
                "parameters": [
                    {
                        "in": "body",
                        "name": "payload",
                        "description": "rely on resources requirements such as (sales, accounting and etc) "
                                       "which is mentioned in their own documents",
                    }
                ],
                "responses": {
                    "task_id": {
                        "description": "a code like: 211c1827-23ea-4090-b58e-fa89335e1527"
                    }
                },
            },
            "patch": {
                "tags": [
                    "API Gateway (Pooling strategy)"
                ],
                "summary": "Pooling strategy, PATCH method in order to call a resource from API groups",
                "description": "By the help of Pooling strategy, PATCH method you can asynchronously call a resource"
                               " from API groups and immediately receive a unique code, in an appropriate "
                               "time interval, you can ask for response and state of your task "
                               "using /tasks/<task_id> API",
                "operationId": "getTaskStatus",
                "consumes": [
                    "application/json",
                ],
                "produces": [
                    "application/json",
                ],
                "parameters": [
                    {
                        "in": "body",
                        "name": "payload",
                        "description": "rely on resources requirements such as (sales, accounting and etc) "
                                       "which is mentioned in their own documents",
                    }
                ],
                "responses": {
                    "task_id": {
                        "description": "a code like: 211c1827-23ea-4090-b58e-fa89335e1527"
                    }
                },
            },
            "delete": {
                "tags": [
                    "API Gateway (Pooling strategy)"
                ],
                "summary": "Pooling strategy, DELETE method in order to call a resource from API groups",
                "description": "By the help of Pooling strategy, DELETE method you can asynchronously call a resource"
                               " from API groups and immediately receive a unique code, in an appropriate "
                               "time interval, you can ask for response and state of your task "
                               "using /tasks/<task_id> API",
                "operationId": "getTaskStatus",
                "consumes": [
                    "application/json",
                ],
                "produces": [
                    "application/json",
                ],
                "parameters": [
                    {
                        "in": "body",
                        "name": "payload",
                        "description": "rely on resources requirements such as (sales, accounting and etc) "
                                       "which is mentioned in their own documents",
                    }
                ],
                "responses": {
                    "task_id": {
                        "description": "a code like: 211c1827-23ea-4090-b58e-fa89335e1527"
                    }
                },
            }
        },
        "/request/<group>/<service_name>": {
            "get": {
                "tags": [
                    "API Gateway (Blocking strategy)"
                ],
                "summary": "return the execution state of a task",
                "description": "If you use this endpoint, a simple HTTP (Blocking strategy) request will send to server"
                               " and after a while you'll receive the response. Based on different situation it maybe "
                               "take time to respond. if you face with this issue, "
                               "you can use Pooling strategy endpoints",
                "operationId": "getTaskStatus",
                "consumes": [
                    "application/json",
                ],
                "produces": [
                    "application/json",
                ],
                "parameters": [
                    {
                        "in": "body",
                        "name": "payload",
                        "description": "rely on resources requirements such as (sales, accounting and etc) "
                                       "which is mentioned in their own documents",
                    }
                ],
                "responses": {
                    "A Json Response": {
                        "description": "Rely on each resource requirement"
                    }
                },
            },
            "post": {
                "tags": [
                    "API Gateway (Blocking strategy)"
                ],
                "summary": "return the execution state of a task",
                "description": "If you use this endpoint, a simple HTTP (Blocking strategy) request will send to server"
                               " and after a while you'll receive the response. Based on different situation it maybe "
                               "take time to respond. if you face with this issue, "
                               "you can use Pooling strategy endpoints",
                "operationId": "getTaskStatus",
                "consumes": [
                    "application/json",
                ],
                "produces": [
                    "application/json",
                ],
                "parameters": [
                    {
                        "in": "body",
                        "name": "payload",
                        "description": "rely on resources requirements such as (sales, accounting and etc) "
                                       "which is mentioned in their own documents",
                    }
                ],
                "responses": {
                    "A Json Response": {
                        "description": "Rely on each resource requirement"
                    }
                },
            },
            "put": {
                "tags": [
                    "API Gateway (Blocking strategy)"
                ],
                "summary": "return the execution state of a task",
                "description": "If you use this endpoint, a simple HTTP (Blocking strategy) request will send to server"
                               " and after a while you'll receive the response. Based on different situation it maybe "
                               "take time to respond. if you face with this issue, "
                               "you can use Pooling strategy endpoints",
                "operationId": "getTaskStatus",
                "consumes": [
                    "application/json",
                ],
                "produces": [
                    "application/json",
                ],
                "parameters": [
                    {
                        "in": "body",
                        "name": "payload",
                        "description": "rely on resources requirements such as (sales, accounting and etc) "
                                       "which is mentioned in their own documents",
                    }
                ],
                "responses": {
                    "A Json Response": {
                        "description": "Rely on each resource requirement"
                    }
                },
            },
            "patch": {
                "tags": [
                    "API Gateway (Blocking strategy)"
                ],
                "summary": "return the execution state of a task",
                "description": "If you use this endpoint, a simple HTTP (Blocking strategy) request will send to server"
                               " and after a while you'll receive the response. Based on different situation it maybe "
                               "take time to respond. if you face with this issue, "
                               "you can use Pooling strategy endpoints",
                "operationId": "getTaskStatus",
                "consumes": [
                    "application/json",
                ],
                "produces": [
                    "application/json",
                ],
                "parameters": [
                    {
                        "in": "body",
                        "name": "payload",
                        "description": "rely on resources requirements such as (sales, accounting and etc) "
                                       "which is mentioned in their own documents",
                    }
                ],
                "responses": {
                    "A Json Response": {
                        "description": "Rely on each resource requirement"
                    }
                },
            },
            "delete": {
                "tags": [
                    "API Gateway (Blocking strategy)"
                ],
                "summary": "return the execution state of a task",
                "description": "If you use this endpoint, a simple HTTP (Blocking strategy) request will send to server"
                               " and after a while you'll receive the response. Based on different situation it maybe "
                               "take time to respond. if you face with this issue, "
                               "you can use Pooling strategy endpoints",
                "operationId": "getTaskStatus",
                "consumes": [
                    "application/json",
                ],
                "produces": [
                    "application/json",
                ],
                "parameters": [
                    {
                        "in": "body",
                        "name": "payload",
                        "description": "rely on resources requirements such as (sales, accounting and etc) "
                                       "which is mentioned in their own documents",
                    }
                ],
                "responses": {
                    "A Json Response": {
                        "description": "Rely on each resource requirement"
                    }
                },
            }
        }
    }
