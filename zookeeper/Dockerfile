FROM strongpapazola/hadoop-base:3.3.4-java8

MAINTAINER strongpapazola <strongpapazola@gmail.com>

# HEALTHCHECK CMD curl -f http://localhost:9864/ || exit 1

# ENV ZOOKEEPER_URL https://dlcdn.apache.org/zookeeper/zookeeper-3.9.0/apache-zookeeper-3.9.0-bin.tar.gz
ENV ZOOKEEPER_URL http://bigdata.bisa.ai/apache-zookeeper-3.9.0-bin.tar.gz
RUN set -x \
    && curl -fSL "$ZOOKEEPER_URL" -o /tmp/zookeeper.tar.gz \
    && tar -xvf /tmp/zookeeper.tar.gz -C /opt/ \
    && rm /tmp/zookeeper.tar.gz* \
    && mv /opt/apache-zookeeper-3.9.0-bin/ /opt/zookeeper

ENV PATH /opt/zookeeper/bin/:$PATH

RUN cp /opt/zookeeper/conf/zoo_sample.cfg /opt/zookeeper/conf/zoo.cfg
RUN echo "bindAddr=0.0.0.0" >> /opt/zookeeper/conf/zoo.cfg
# RUN echo "admin.serverPort=8080" >> /opt/zookeeper/conf/zoo.cfg
RUN echo "admin.enableServer=false" >> /opt/zookeeper/conf/zoo.cfg

EXPOSE 2181
# EXPOSE 2181 8080 45235  

# CMD ["zkServer.sh","start"]
CMD ["zkServer.sh", "start-foreground"]


# ENV FLUME_HOME /opt/flume
# ENV PATH /opt/flume:$PATH

# COPY data.log /
# COPY zookeeper.conf /opt/flume/conf

# bin/flume-ng agent -conf ./conf/ -f conf/zookeeper.conf -n agent1 -Dzookeeper.root.logger=DEBUG




# RUN cp $SQOOP_HOME/conf/sqoop-env-template.sh $SQOOP_HOME/conf/sqoop-env.sh
# RUN echo "export HADOOP_COMMON_HOME=/opt/hadoop-3.2.1/" >> $SQOOP_HOME/conf/sqoop-env.sh
# RUN echo "export HADOOP_MAPRED_HOME=/opt/hadoop-3.2.1/share/hadoop/mapreduce/" >> $SQOOP_HOME/conf/sqoop-env.sh
# RUN $SQOOP_HOME/conf/sqoop-env.sh

# # RUN cp /opt/hadoop-3.3.4/share/hadoop/yarn/timelineservice/lib/commons-lang-2.6.jar /opt/sqoop/
# RUN cp /opt/hadoop-3.2.1/share/hadoop/yarn/timelineservice/lib/commons-lang-2.6.jar /opt/sqoop/
# RUN cp /opt/hadoop-3.2.1/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.2.1-tests.jar /opt/sqoop/
# RUN cp /opt/hadoop-3.2.1/share/hadoop/mapreduce/hadoop-mapreduce-client-core-3.2.1.jar /opt/sqoop/
# RUN cp /opt/hadoop-3.2.1/share/hadoop/mapreduce/hadoop-mapreduce-client-common-3.2.1.jar /opt/sqoop/

# #Set path to where bin/hadoop is available
# export HADOOP_COMMON_HOME=/opt/hadoop-3.3.4
# #Set path to where hadoop-*-core.jar is available
# export HADOOP_MAPRED_HOME=/opt/hadoop-3.3.4/share/hadoop/mapreduce/


# ENV HDFS_CONF_dfs_datanode_data_dir=file:///hadoop/dfs/data
# RUN mkdir -p /hadoop/dfs/data
# VOLUME /hadoop/dfs/data

# ADD run.sh /run.sh
# RUN chmod a+x /run.sh

# EXPOSE 9864

# CMD ["/run.sh"]
