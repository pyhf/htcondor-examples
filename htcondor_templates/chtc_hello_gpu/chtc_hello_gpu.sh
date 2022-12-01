#!/bin/bash
echo "Hello CHTC from Job ${1} running on $(hostname)"
echo ""
echo "Trying to see if nvidia/cuda can access the GPU...."
echo ""
nvidia-smi

echo ""
echo "# Check if JAX can detect the GPU:"
echo ""
python /docker/jax_detect_GPU.py

echo ""
echo "# Check that pyhf is working as expected:"
echo ""
pyhf --version
pyhf --help
python -c 'import pyhf; pyhf.set_backend("jax"); print(pyhf.get_backend())'
