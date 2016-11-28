#!/bin/bash

CONTAINER_IP=$(hostname -I)


python /app/set_server_properties.py $CONTAINER_IP


$KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server.properties & KAFKA_SERVER_PID=$!

wait $KAFKA_SERVER_PID
