from datetime import datetime
from pathlib import Path

import nox

# Default sessions to run if no session handles are passed
nox.options.sessions = ["build"]


DIR = Path(__file__).parent.resolve()


@nox.session()
def build(session):
    """
    Build image
    """

    default_image = "nvidia/cuda:11.6.0-cudnn8-devel-ubuntu20.04"
    target_images = [
        default_image,
        "nvidia/cuda:11.2.2-devel-ubuntu20.04",
        "nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04",
    ]
    pyhf_version = "0.7.0"
    pyhf_backend = "jax"
    for base_image in target_images:
        cuda_version = base_image.split(":")[-1].split("-devel")[0]

        session.run("docker", "pull", base_image, external=True)
        run_command = [
            "docker",
            "build",
            "--file",
            "docker/Dockerfile",
            "--build-arg",
            f"BASE_IMAGE={base_image}",
            "--build-arg",
            f"PYHF_VERSION={pyhf_version}",
            "--build-arg",
            f"PYHF_BACKEND={pyhf_backend}",
            "--tag",
            f"pyhf/cuda:{pyhf_version}-{pyhf_backend}-cuda-{cuda_version}",
        ]
        if base_image == default_image:
            run_command += ["--tag", f"pyhf/cuda:latest-{pyhf_backend}"]
        run_command += "."
        session.run(*run_command, external=True)


@nox.session()
def test(session):
    session.run(
        "docker",
        "run",
        "--rm",
        "-ti",
        "--gpus",
        "all",
        "pyhf/cuda:latest-jax",
        external=True,
    )
