FROM strongpapazola/hadoop-base:3.3.4-java8

MAINTAINER strongpapazola <strongpapazola@gmail.com>

HEALTHCHECK CMD curl -f http://localhost:8042/ || exit 1

ADD run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 8042

CMD ["/run.sh"]
