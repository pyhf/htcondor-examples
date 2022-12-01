#!/bin/bash
echo "Hello CHTC from Job ${1} running on $(hostname)"
echo ""
echo "Trying to see if nvidia/cuda can access the GPU...."
nvidia-smi

echo ""
echo "And if JAX can detect the GPU:"
python /docker/jax_detect_GPU.py
