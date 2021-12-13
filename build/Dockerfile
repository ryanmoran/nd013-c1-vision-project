FROM nvidia/cuda:11.4.2-runtime-ubuntu18.04

ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64/:/usr/local/cuda-11.4/compat

RUN apt-get -qqy update \
  && echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
  && apt-get -qqy install \
    apt-transport-https \
    ca-certificates \
    curl \
    git \
    gnupg \
    pkg-config \
    wget \
    unzip \
  && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add - \
  && apt-get -qqy update \
  && apt-get -qqy install \
    google-cloud-sdk

ENV LANG C.UTF-8

RUN apt -qqy install software-properties-common
RUN apt update -qqy && \
    add-apt-repository ppa:deadsnakes/ppa -y && \
    apt install -qqy python3.8-dev python3.8-distutils

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
