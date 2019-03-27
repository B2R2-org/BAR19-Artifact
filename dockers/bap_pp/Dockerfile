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

RUN opam init --comp=4.05.0+flambda
RUN git clone https://github.com/BinaryAnalysisPlatform/bap.git
WORKDIR /bap
RUN git checkout v1.5.0
RUN eval `opam config env`
RUN opam pin add bap .

ADD bench.ml.patch /bench.ml.patch
WORKDIR /root
RUN git clone https://github.com/BinaryAnalysisPlatform/bap-plugins.git
WORKDIR /root/bap-plugins
RUN patch -p0 < /bench.ml.patch
WORKDIR /root/bap-plugins/lifting-benchmark
RUN eval `opam config env` && ocamlbuild -package bap -package findlib.dynload  bench.native

ADD ./run.sh /run.sh
WORKDIR /
