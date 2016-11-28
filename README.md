# docker_kafka
A docker image for kafka


<h4>build:</h4>

```
docker build -t kafka .
```

<h4>run:</h4>

```
docker run -d -p 9092:9092 --name=kafka_1 \
    -e "ZOOKEEPER_ADDRESS=[ZOOKEEPER_ADDRESS]" \
    -e "ZOOKEEPER_PORT=[ZOOKEEPER_PORT]" \
    -e "ADVERTISED_HOSTNAME=[ADVERTISED_HOSTNAME]" \
    -e "ADVERTISED_PORT=[ADVERTISED_PORT]" \
    kafka
```
<b>Required:</b>
`ZOOKEEPER_ADDRESS`

<b>Default:</b>
`ZOOKEEPER_PORT = 2181`
`ADVERTISED_HOSTNAME = [Container IP]`
`ADVERTISED_PORT = 9092`
