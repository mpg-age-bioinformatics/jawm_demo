# jawm_demo

This is a jawm demo module.

For more information on jawm please visit [jawm's repo](https://github.com/mpg-age-bioinformatics/jawm/tree/main).

Example usage:
```
# docker
jawm demo.py demo -p ./yaml/docker.yaml

# slurm & apptainer with multiple yaml files
jawm demo.py demo -p ./yaml/vars.yaml ./yaml/hpc.yaml
```