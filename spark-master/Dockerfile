# FROM bde2020/spark-base:3.3.0-hadoop3.3
FROM strongpapazola/hadoop-base:3.3.4-java8

LABEL maintainer="Gezim Sejdiu <g.sejdiu@gmail.com>, Giannis Mouchakis <gmouchakis@gmail.com>"

COPY master.sh /

ENV SPARK_MASTER_PORT 7077
ENV SPARK_MASTER_WEBUI_PORT 8080
ENV SPARK_MASTER_LOG /spark/logs

EXPOSE 8080 7077 6066

RUN cp /spark/conf/spark-env.sh.template /spark/conf/spark-env.sh
RUN echo "HADOOP_CONF_DIR=/etc/hadoop" >> /spark/conf/spark-env.sh
RUN echo "export HADOOP_CONF_DIR=/etc/hadoop" >> /spark/conf/spark-env.sh
RUN /spark/conf/spark-env.sh


CMD ["/bin/bash", "/master.sh"]
