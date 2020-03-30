FROM ubuntu:16.04
MAINTAINER Artur Piliuk

RUN apt-get update && apt-get upgrade -y
RUN apt-get install nginx -y
EXPOSE 80


RUN sed -i 's/listen 80/listen 0.0.0.0:80/g' /etc/nginx/sites-available/default
CMD /etc/init.d/nginx restart && tail -f /dev/null