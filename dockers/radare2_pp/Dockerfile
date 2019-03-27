FROM ubuntu:16.04

RUN sed -i 's/archive.ubuntu.com/ftp.daumkakao.com/g' /etc/apt/sources.list && \
    echo "deb-src http://ftp.daumkakao.com/ubuntu/ bionic main restricted" >> /etc/apt/sources.list && \
    apt update && \
    apt -y install \
    git \
    make \
    wget \
    gcc

RUN git clone https://github.com/radare/radare2.git /root/radare2
WORKDIR /root/radare2
RUN git checkout 8fb9275f2aed24fe046b1c1ee79b4ea2be709033
ADD ./radare2.patch /root/radare2/radare2.patch

RUN /root/radare2/sys/install.sh
RUN patch -p0 --ignore-whitespace < /root/radare2/radare2.patch
RUN /root/radare2/sys/install.sh

ADD ./run.sh /run.sh
WORKDIR /
