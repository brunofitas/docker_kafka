#! /usr/bin/env python

import os
import sys
import time


if 'ADVERTISED_HOSTNAME' in os.environ:
    ADVERTISED_HOSTNAME = os.environ['ADVERTISED_HOSTNAME']
else:
    ADVERTISED_HOSTNAME = sys.argv[1]


if 'ADVERTISED_PORT' in os.environ:
    ADVERTISED_PORT = os.environ['ADVERTISED_PORT']
else:
    ADVERTISED_PORT = "9092"


ZOOKEEPER_ADDRESS = os.environ['ZOOKEEPER_ADDRESS']

if 'ZOOKEEPER_PORT' in os.environ:
    ZOOKEEPER_PORT = os.environ['ZOOKEEPER_PORT']
else:
    ZOOKEEPER_PORT = "2181"


KAFKA_HOME = os.environ['KAFKA_HOME']

template = open(KAFKA_HOME + "/config/server.template", "r")

file_data = template.read()

template.close()

new_data = file_data.replace("ZOOKEEPER_ADDRESS", ZOOKEEPER_ADDRESS)\
                    .replace("ZOOKEEPER_PORT", ZOOKEEPER_PORT)\
                    .replace("ADVERTISED_HOSTNAME", ADVERTISED_HOSTNAME)\
                    .replace("ADVERTISED_PORT", ADVERTISED_PORT)

properties = open(KAFKA_HOME + "/config/server.properties", "w")

properties.write(new_data)

properties.close()