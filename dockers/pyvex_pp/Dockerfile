FROM ubuntu:16.04

RUN sed -i 's/archive.ubuntu.com/ftp.daumkakao.com/g' /etc/apt/sources.list && \
    echo "deb-src http://ftp.daumkakao.com/ubuntu/ bionic main restricted" >> /etc/apt/sources.list && \
    apt update && \
    apt -y install \
    python3-dev \
    libffi-dev \
    build-essential \
    python3-pip \
    git

RUN git clone https://github.com/angr/pyvex.git /root/pyvex
ADD ./main_main.c.patch /root/pyvex/patch
WORKDIR /root/pyvex
RUN pip3 install cffi
RUN python3 setup.py install
RUN patch -p0 < /root/pyvex/patch
RUN python3 setup.py install

ADD ./lift.py /root/pyvex/lift.py
ADD ./run.sh /run.sh
