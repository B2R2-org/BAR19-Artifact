FROM ubuntu:16.04

RUN sed -i 's/archive.ubuntu.com/ftp.daumkakao.com/g' /etc/apt/sources.list && \
    echo "deb-src http://ftp.daumkakao.com/ubuntu/ bionic main restricted" >> /etc/apt/sources.list && \
    apt update && \
    apt -y install \
    git \
    m4 \
    libgmp-dev \
    libzmq3-dev \
    cmake \
    llvm-6.0-dev \
    protobuf-compiler \
    pkg-config \
    opam

RUN git clone https://github.com/binsec/binsec.git /root/binsec
WORKDIR /root/binsec
RUN git checkout 0f738968e3ca373de98d725f2a8be8e052485be0

RUN opam init --comp=4.05.0
RUN eval `opam config env` && opam install ocamlbuild menhir ocamlgraph piqilib zarith zmq llvm piqi

RUN eval `opam config env` && ./configure
ADD ./binstream.ml.patch /root/binsec/binstream.ml.patch
ADD ./binstream.mli.patch /root/binsec/binstream.mli.patch
ADD ./disasm.ml.patch /root/binsec/disasm.ml.patch
RUN patch -p0 < /root/binsec/binstream.ml.patch
RUN patch -p0 < /root/binsec/binstream.mli.patch
RUN patch -p0 < /root/binsec/disasm.ml.patch
RUN eval `opam config env` && make binsec

WORKDIR /
