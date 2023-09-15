FROM strongpapazola/hadoop-base:3.3.4-java8

MAINTAINER strongpapazola <strongpapazola@gmail.com>

# HEALTHCHECK CMD curl -f http://localhost:9864/ || exit 1

# ENV FLUME_URL https://archive.apache.org/dist/flume/1.9.0/apache-flume-1.9.0-bin.tar.gz
ENV FLUME_URL http://bigdata.bisa.ai/apache-flume-1.9.0-bin.tar.gz
RUN set -x \
    && curl -fSL "$FLUME_URL" -o /tmp/flume.tar.gz \
    && tar -xvf /tmp/flume.tar.gz -C /opt/ \
    && rm /tmp/flume.tar.gz* \
    && mv /opt/apache-flume-1.9.0-bin/ /opt/flume

ENV FLUME_HOME /opt/flume
ENV PATH /opt/flume:$PATH

COPY data.log /
COPY flume.conf /opt/flume/conf

#CMD /opt/flume/bin/flume-ng agent --conf /opt/flume/conf/ -f /opt/flume/conf/flume.conf -n agent1 -Dflume.root.logger=DEBUG




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
