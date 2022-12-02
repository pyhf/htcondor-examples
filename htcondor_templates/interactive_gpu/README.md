# Interactive jobs with GPU resources

## Problem

```console
[mfeickert@submit-1 interactive_gpu]$ pwd
/home/mfeickert/testarea/htcondor-examples/htcondor_templates/interactive_gpu
[mfeickert@submit-1 interactive_gpu]$ . ./submit.sh
Submitting job(s).
1 job(s) submitted to cluster 16761109.
Waiting for job to start...
Received disconnect from UNKNOWN port 65535:2: Too many authentication failures
Authentication failed.
```

## Answer

```
# ForwardAgent yes
# Don't forward agent to avoid ssh problems
# when trying to run interactive jobs
Host chtc CHTC
    HostName submit1.chtc.wisc.edu
    Compression yes
    ForwardX11 yes
    ForwardX11Trusted yes
    IdentityFile ~/.ssh/id_ed25519-chtc
    IdentitiesOnly yes
    ForwardAgent no
    User mfeickert
```

this is hinted at on the [Running HTC jobs using Docker containers](https://chtc.cs.wisc.edu/uw-research-computing/docker-jobs.html#3-testing) page in that in mentions connecting by ssh

> You can test a container interactively in CHTC by using a normal Docker job submit file and using the interactive flag with `condor_submit`:
>
> ```
> [alice@submit]$ condor_submit -i docker.sub
> ```
> This should start a session inside the indicated Docker container and connect you to it using ssh.
> Type `exit` to end the interactive job.

and this ssh isn't magical, and so would need to know to ignore your defaults.

## TO ADD TO THE HELLO GPU EXAMPLE

How to get information before using GPUs

https://chtc.cs.wisc.edu/uw-research-computing/gpu-jobs#d-using-condor_status-to-explore-chtc-gpus
