FROM ubuntu:22.04

MAINTAINER strongpapazola <strongpapazola@gmail.com>

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      openjdk-8-jdk \
      net-tools \
      curl \
      netcat \
      gnupg \
      libsnappy-dev \
      nano \
    && rm -rf /var/lib/apt/lists/*


ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/

RUN curl -O https://dist.apache.org/repos/dist/release/hadoop/common/KEYS

RUN gpg --import KEYS

# ENV HADOOP_VERSION 2.10.2
ENV HADOOP_VERSION 3.2.1
# ENV HADOOP_VERSION 3.3.4
# ENV HADOOP_VERSION 3.0.3
# ENV HADOOP_URL https://dlcdn.apache.org/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz
ENV HADOOP_URL https://archive.apache.org/dist/hadoop/core/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz

# # ENV HADOOP_URL https://dlcdn.apache.org/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz
# # ENV HADOOP_URL https://dlcdn.apache.org/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz.asc

RUN set -x \
    && curl -fSL "$HADOOP_URL" -o /tmp/hadoop.tar.gz \
    && curl -fSL "$HADOOP_URL.asc" -o /tmp/hadoop.tar.gz.asc \
    && gpg --verify /tmp/hadoop.tar.gz.asc \
    && tar -xvf /tmp/hadoop.tar.gz -C /opt/ \
    && rm /tmp/hadoop.tar.gz*

RUN ln -s /opt/hadoop-$HADOOP_VERSION/etc/hadoop /etc/hadoop

# Hadoop 2.10.2
# RUN mv /etc/hadoop/mapred-site.xml.template /etc/hadoop/mapred-site.xml
# RUN mv /etc/hadoop/mapred-queues.xml.template /etc/hadoop/mapred-queues.xml

RUN mkdir /opt/hadoop-$HADOOP_VERSION/logs

RUN mkdir /hadoop-data

ENV HADOOP_HOME=/opt/hadoop-$HADOOP_VERSION
ENV HADOOP_CONF_DIR=/etc/hadoop
ENV MULTIHOMED_NETWORK=1
ENV USER=root
ENV PATH $HADOOP_HOME/bin/:$PATH

ADD entrypoint.sh /entrypoint.sh

RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
