FROM centos:7

MAINTAINER Bruno Fitas <brunofitas@gmail.com>

ENV KAFKA_VERSION="0.9.0.1"

ENV SCALA_VERSION="2.11"

ENV KAFKA_HOME /opt/kafka_${SCALA_VERSION}-${KAFKA_VERSION}

RUN yum install wget tar java-1.8.0-openjdk-headless -y

RUN wget -q "http://www.eu.apache.org/dist/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz" \
  -O "/tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz"

RUN tar xf /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz -C /opt

VOLUME ["/kafka"]

COPY assets/server.template $KAFKA_HOME/config/server.template

COPY app /app

CMD /app/start-kafka.sh

EXPOSE 9092
