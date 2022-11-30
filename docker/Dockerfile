ARG BASE_IMAGE=nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04
FROM ${BASE_IMAGE} as base

SHELL [ "/bin/bash", "-c" ]

WORKDIR /home/data

ARG PYHF_VERSION=0.6.3
ARG PYHF_BACKEND=jax
# Set PATH to pickup virtualenv when it is unpacked
ENV PATH=/usr/local/venv/bin:"${PATH}"
RUN apt-get -qq -y update && \
    apt-get -qq -y install --no-install-recommends \
        python3 \
        python3-dev \
        curl \
        git && \
    apt-get -y autoclean && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/* && \
    python3 -m venv /usr/local/venv && \
    python -m pip --no-cache-dir install --upgrade pip setuptools wheel
