FROM ubuntu:16.04

RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y python python-dev python-pip python-virtualenv && \
  apt-get install -y apt-utils && \
  apt-get install -y build-essential && \
  apt-get install -y libreadline-dev && \
  apt-get install -y libffi-dev && \
  apt-get install -y git && \
  apt-get install -y pkg-config && \
  rm -rf /var/lib/apt/lists/*

WORKDIR /

RUN \
  git clone --recurse-submodules https://github.com/micropython/micropython.git

WORKDIR /micropython/ports/unix

RUN \
  make axtls && \
  make

WORKDIR /

RUN \
  git clone https://github.com/micropython/micropython-lib.git

WORKDIR /micropython-lib

RUN make install

WORKDIR /root

ENTRYPOINT ["/micropython/ports/unix/micropython"]