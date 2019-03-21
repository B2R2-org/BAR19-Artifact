FROM ubuntu:16.04

RUN sed -i 's/archive.ubuntu.com/ftp.daumkakao.com/g' /etc/apt/sources.list && \
    echo "deb-src http://ftp.daumkakao.com/ubuntu/ bionic main restricted" >> /etc/apt/sources.list && \
    apt update && \
    apt -y install \
    git \
    python-dev \
    python-pyparsing \
    python-pycparser \
    gcc

RUN git clone https://github.com/serpilliere/elfesteem.git /root/elfesteem
WORKDIR /root/elfesteem

RUN python setup.py build
RUN python setup.py install

RUN git clone https://github.com/cea-sec/miasm.git /root/miasm
WORKDIR /root/miasm
RUN git checkout c392534a4d51759cf8ac349ea873e25b424f7472

RUN python setup.py build
RUN python setup.py install
ADD run.py /run.py
ADD run.sh /run.sh
