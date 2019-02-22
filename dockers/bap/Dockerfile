FROM ubuntu:16.04

RUN sed -i 's/archive.ubuntu.com/ftp.daumkakao.com/g' /etc/apt/sources.list && \
    echo "deb-src http://ftp.daumkakao.com/ubuntu/ bionic main restricted" >> /etc/apt/sources.list && \
    apt update && \
    apt -y install \
    git \
    binutils-multiarch \
    clang \
    debianutils \
    libgmp-dev \
    libzip-dev \
    llvm-dev \
    m4 \
    ncurses-dev \
    perl \
    pkg-config \
    zlib1g-dev \
    time \
    libcurl4-gnutls-dev \
    opam

RUN git clone https://github.com/BinaryAnalysisPlatform/bap.git /root/bap
ADD ./bap.patch /root/bap/patch
WORKDIR /root/bap
RUN git checkout 25fe085e46c071e3553298558b7c95265f87bec9
RUN patch -p0 < /root/bap/patch

RUN opam init --comp=4.05.0
RUN eval `opam config env` && opam pin add bap /root/bap
ADD ./run.sh /run.sh
WORKDIR /
