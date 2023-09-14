FROM strongpapazola/hadoop-base:3.3.4-java8

MAINTAINER strongpapazola <strongpapazola@gmail.com>

# HEALTHCHECK CMD curl -f http://localhost:9864/ || exit 1

ENV SQOOP_VERSION 1.99.7
# ENV SQOOP_URL https://archive.apache.org/dist/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz
ENV SQOOP_URL http://bigdata.bisa.ai/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz
RUN set -x \
    && curl -fSL "$SQOOP_URL" -o /tmp/sqoop.tar.gz \
    && tar -xvf /tmp/sqoop.tar.gz -C /opt/ \
    && rm /tmp/sqoop.tar.gz* \
    && mv /opt/sqoop-1.4.7.bin__hadoop-2.6.0/ /opt/sqoop

# RUN curl -fSL https://ftp.ntu.edu.tw/MySQL/Downloads/Connector-J/mysql-connector-java-8.0.29.tar.gz -o /tmp/mysql.tar.gz \
RUN curl -fSL http://bigdata.bisa.ai//mysql-connector-java-8.0.29.tar.gz -o /tmp/mysql.tar.gz \
    && tar -xvf /tmp/mysql.tar.gz -C /opt/ \
    && rm /tmp/mysql.tar.gz \
    && mv /opt/mysql-connector-java-8.0.29/mysql-connector-java-8.0.29.jar /opt/sqoop/lib 

ENV SQOOP_HOME /opt/sqoop/
# export PATH=/opt/sqoop/bin/:$PATH
ENV PATH /opt/sqoop/bin/:$PATH

RUN cp $SQOOP_HOME/conf/sqoop-env-template.sh $SQOOP_HOME/conf/sqoop-env.sh
RUN echo "export HADOOP_COMMON_HOME=/opt/hadoop-3.2.1/" >> $SQOOP_HOME/conf/sqoop-env.sh
RUN echo "export HADOOP_MAPRED_HOME=/opt/hadoop-3.2.1/share/hadoop/mapreduce/" >> $SQOOP_HOME/conf/sqoop-env.sh
RUN $SQOOP_HOME/conf/sqoop-env.sh

# RUN cp /opt/hadoop-3.3.4/share/hadoop/yarn/timelineservice/lib/commons-lang-2.6.jar /opt/sqoop/
RUN cp /opt/hadoop-3.2.1/share/hadoop/yarn/timelineservice/lib/commons-lang-2.6.jar /opt/sqoop/
RUN cp /opt/hadoop-3.2.1/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-3.2.1-tests.jar /opt/sqoop/
RUN cp /opt/hadoop-3.2.1/share/hadoop/mapreduce/hadoop-mapreduce-client-core-3.2.1.jar /opt/sqoop/
RUN cp /opt/hadoop-3.2.1/share/hadoop/mapreduce/hadoop-mapreduce-client-common-3.2.1.jar /opt/sqoop/

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
