ARG BASE_IMAGE=nvidia/cuda:11.6.0-cudnn8-devel-ubuntu20.04
FROM ${BASE_IMAGE} as base

SHELL [ "/bin/bash", "-c" ]

WORKDIR /home/data

ARG PYHF_VERSION=0.7.2
ARG PYHF_BACKEND=jax
# Set PATH to pickup virtualenv when it is unpacked
ENV PATH=/usr/local/venv/bin:"${PATH}"
RUN apt-get -qq update && \
    apt-get -qq -y install --no-install-recommends \
        python3 \
        python3-dev \
        python3-venv \
        curl \
        git && \
    apt-get -y autoclean && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/* && \
    python3 -m venv /usr/local/venv && \
    . /usr/local/venv/bin/activate && \
    python -m pip --no-cache-dir install --upgrade pip setuptools wheel && \
    python -m pip --no-cache-dir install "pyhf[xmlio,contrib]==${PYHF_VERSION}" && \
    python -m pip --no-cache-dir install \
    --find-links https://storage.googleapis.com/jax-releases/jax_cuda_releases.html \
    "jax[cuda]==0.3.25" && \
    mkdir -p -v /docker && \
    curl -sL https://raw.githubusercontent.com/matthewfeickert/nvidia-gpu-ml-library-test/main/jax_detect_GPU.py \
        -o /docker/jax_detect_GPU.py && \
    mkdir -p -v \
        /.local \
        /.config \
        /.cache \
        /.jupyter \
        /work && \
    chmod --recursive 777 \
        /usr/local/venv \
        /.local \
        /.config \
        /.cache \
        /.jupyter \
        /work

# Creation of a /.cache dir and chmod to universal write is to allow for pip installs
# into the virtual environment by non-root users

# CONTROL FOR MANUAL BUILD
# # N.B. variable CUDA_VERSION already exists in the image
# ARG CUDA_VERSION_MAJOR=cuda11
# # ARG CUDA_VERSION_MAJOR=cuda111
# # ARG CUDNN_VERSION=cudnn805
# ARG CUDNN_VERSION=cudnn82
# ARG JAX_VERSION=0.3.1
# ARG JAXLIB_VERSION=0.1.76

# RUN python -m pip --no-cache-dir install \
#     --find-links https://storage.googleapis.com/jax-releases/jax_cuda_releases.html \
#     "jax[${CUDA_VERSION_MAJOR}_${CUDNN_VERSION}]==0.3.25"
# RUN python -m pip --no-cache-dir install \
#     --find-links https://storage.googleapis.com/jax-releases/jax_cuda_releases.html \
#     "jax==${JAX_VERSION}" \
#     "jaxlib==${JAXLIB_VERSION}+${CUDA_VERSION_MAJOR}.${CUDNN_VERSION}"

WORKDIR /work
