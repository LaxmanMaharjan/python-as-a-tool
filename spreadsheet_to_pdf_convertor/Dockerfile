FROM python:3.10-buster

LABEL maintainer="laxman@example.com"

ENV DEBIAN_FRONTEND=noninteractive
ENV DEBCONF_NOWARNINGS="yes"

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get --no-install-recommends install libreoffice -y

RUN apt-get install -y default-jre libreoffice-java-common

COPY . /usr/src

WORKDIR /usr/src

RUN chmod +x /usr/src/entrypoint.sh

ENTRYPOINT ["/usr/src/entrypoint.sh"]
