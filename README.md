# HTCondor examples for pyhf workflows

Example configurations for using pyhf with HTCondor inspired by the [Center for High Throughput Computing examples](https://github.com/CHTC/templates-GPUs).

## CUDA enabled Docker images

These examples assume that you want to use GPU resources to take advantage of hardware acceleration and so focus on using the [`pyhf`](https://pyhf.readthedocs.io/) Docker base images built on the [NVIDIA CUDA enabled images](https://github.com/NVIDIA/nvidia-docker) for runtime use with the the NVIDIA Container Toolkit.

### Local installation

- Make sure that you have the [`nvidia-container-toolkit`](https://github.com/NVIDIA/nvidia-docker) installed on the host machine
- Check the [list of available tags on Docker Hub](https://hub.docker.com/r/pyhf/cuda/tags?page=1) to find the tag you want
- Use `docker pull` to pull down the image corresponding to the tag

Example:

```
docker pull pyhf/cuda:0.7.0-jax-cuda-11.6.0-cudnn8
```

### Local use

To check that NVIDIA GPUS are being properly detected run

```
docker run --rm --gpus all pyhf/cuda:0.7.0-jax-cuda-11.6.0-cudnn8 'nvidia-smi'
```

and check if the [`nvidia-smi`](https://developer.nvidia.com/nvidia-system-management-interface) output appears correctly.

To run (interactively) using GPUs on the host machine:

```
docker run --rm -ti --gpus all pyhf/cuda:0.7.0-jax-cuda-11.6.0-cudnn8
```
