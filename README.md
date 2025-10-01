# jawm_demo

This is a jawm demo module.

Checkout `demo.py` and `notebook.ipynb` for examples on how to develop data analysis workflows with jawm.

For more information on jawm please visit [jawm's repo](https://github.com/mpg-age-bioinformatics/jawm/tree/main).

Example usage:
```
# docker
jawm demo.py demo -p ./yaml/docker.yaml

# slurm & apptainer with multiple yaml files
jawm demo.py demo -p ./yaml/vars.yaml ./yaml/hpc.yaml
```

Running tests:
```
jawm-dev test
```
More information on running and developing tests can be found in `./test/README.md`.