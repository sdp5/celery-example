# celery-example

Code taken from [dev.to article](https://dev.to/dhananjayharidas/scaling-celery-based-application-in-production-jak). Rights belong to the AUTHOR.

### Scaling Celery Workers

#### Increasing the Number of Workers

Start multiple Celery worker processes:
```
celery -A celery_config worker --loglevel=info --concurrency=4
```
To scale further, start more workers:
```
celery -A celery_config worker --loglevel=info --concurrency=4
celery -A celery_config worker --loglevel=info --concurrency=4
```

### Distributed Workers

Run workers on different machines by pointing them to the same message broker:

```
celery -A celery_config worker --loglevel=info --concurrency=4 -Q fetch_queue
celery -A celery_config worker --loglevel=info --concurrency=8 -Q extract_queue
celery -A celery_config worker --loglevel=info --concurrency=2 -Q compare
```

### Autoscaling

Enable autoscaling to dynamically adjust the number of worker processes:

```
celery -A celery_config worker --loglevel=info --autoscale=10,3
```

`--autoscale=10,3`: Scales between 3 and 10 worker processes based on load.

### Distributed Task Execution

#### Machine 1 (Message Broker and Backend):

Run Redis as your broker and backend.

#### Machine 2 (Worker Node):

Start Celery workers:
```
celery -A celery_config worker --loglevel=info --concurrency=4 -Q fetch_queue
```

#### Machine 3 (Worker Node):

Start Celery workers:
```
celery -A celery_config worker --loglevel=info --concurrency=8 -Q extract_queue
```

#### Machine 4 (Worker Node):

Start Celery workers:
```
celery -A celery_config worker --loglevel=info --concurrency=2 -Q compare_queue
```

### Monitoring and Management

Use monitoring tools like Flower, Prometheus, and Grafana to monitor Celery tasks:

#### Flower

Start Flower to monitor Celery workers:
```
celery -A celery_config flower
```

### Load Balancing and High Availability 

Implement load balancing for high availability and fault tolerance:

#### Example Load Balancer Setup

Use HAProxy or another load balancer to distribute requests across multiple Redis instances.


### Summary

    Scale Workers: Increase the number of Celery workers to handle more tasks concurrently.
    Dedicated Queues: Use different queues for different types of tasks and scale them independently.
    Autoscaling: Enable autoscaling to dynamically adjust the number of worker processes based on load.
    Distributed Execution: Distribute workers across multiple machines to improve scalability and fault tolerance.
    Monitoring: Use monitoring tools to keep track of the performance and health of your Celery workers.
    Load Balancing: Implement load balancing for high availability and fault tolerance.
