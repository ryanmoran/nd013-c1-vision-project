ARG UBUNTU_VERSION=20.04

ARG ARCH=
ARG CUDA=11.2
FROM nvidia/cuda${ARCH:+-$ARCH}:${CUDA}.1-base-ubuntu${UBUNTU_VERSION} as base
# ARCH and CUDA are specified again because the FROM directive resets ARGs
# (but their default value is retained if set previously)
ARG ARCH
ARG CUDA
ARG CUDNN=8.1.0.77-1
ARG CUDNN_MAJOR_VERSION=8
ARG LIB_DIR_PREFIX=x86_64
ARG LIBNVINFER=8.0.0-1
ARG LIBNVINFER_MAJOR_VERSION=8

# Let us install tzdata painlessly
ENV DEBIAN_FRONTEND=noninteractive

# Needed for string substitution
SHELL ["/bin/bash", "-c"]

RUN apt-get -qqy update \
  && echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
  && apt-get -qqy install \
    apt-transport-https \
    build-essential \
    ca-certificates \
    cuda-command-line-tools-${CUDA/./-} \
    cuda-nvrtc-${CUDA/./-} \
    curl \
    ffmpeg \
    g++ \
    git \
    git-core \
    gnupg \
    libcublas-${CUDA/./-} \
    libcudnn8=${CUDNN}+cuda${CUDA} \
    libcufft-${CUDA/./-} \
    libcurand-${CUDA/./-} \
    libcusolver-${CUDA/./-} \
    libcusparse-${CUDA/./-} \
    libfreetype6-dev \
    libhdf5-serial-dev \
    libzmq3-dev \
    pkg-config \
    software-properties-common \
    unzip \
    wget \
    zip \
    zlib1g-dev \
  && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add - \
  && apt-get -qqy update \
  && apt-get -qqy install \
    google-cloud-sdk

ENV LANG C.UTF-8

RUN [[ "${ARCH}" = "ppc64le" ]] || { \
  apt-get update \
    && apt-get install -y --no-install-recommends libnvinfer${LIBNVINFER_MAJOR_VERSION}=${LIBNVINFER}+cuda11.0 \
  libnvinfer-plugin${LIBNVINFER_MAJOR_VERSION}=${LIBNVINFER}+cuda11.0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*; \
  }

ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:/usr/local/cuda/lib64:$LD_LIBRARY_PATH

RUN ln -s /usr/local/cuda/lib64/stubs/libcuda.so /usr/local/cuda/lib64/stubs/libcuda.so.1 \
  && echo "/usr/local/cuda/lib64/stubs" > /etc/ld.so.conf.d/z-cuda-stubs.conf \
  && ldconfig

RUN apt-get update -qqy \
  && add-apt-repository ppa:deadsnakes/ppa -y \
  && apt-get install -qqy python3.8-dev python3.8-distutils

RUN ln -s $(which python3.8) /usr/local/bin/python3
RUN ln -s $(which python3) /usr/local/bin/python
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
  && python get-pip.py \
  && rm get-pip.py

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install -r requirements.txt
RUN python -m pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI

ENV TF_CPP_MIN_LOG_LEVEL=2

RUN wget https://github.com/protocolbuffers/protobuf/releases/download/v3.13.0/protoc-3.13.0-linux-x86_64.zip && \
    unzip protoc-3.13.0-linux-x86_64.zip -d /app/protobuf/

ENV PATH "$PATH:/app/protobuf/bin"

RUN git clone https://github.com/tensorflow/models.git && \
    cd /app/models/research/ && \
    protoc object_detection/protos/*.proto --python_out=. && \
    cp object_detection/packages/tf2/setup.py . && \
    python -m pip install .

WORKDIR /app/project
