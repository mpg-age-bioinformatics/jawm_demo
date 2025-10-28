# jawm_demo

This is a jawm demo module.

Checkout `demo.py` and `notebook.ipynb` for examples on how to develop data analysis workflows with jawm.

Installing jawm:
```
pip install git+ssh://git@github.com/mpg-age-bioinformatics/jawm.git
```
For more information on jawm please visit jawm's repo on [GitHub.com](https://github.com/mpg-age-bioinformatics/jawm/tree/main).

Example usage:
```
# clone this module
git clone git@github.com:mpg-age-bioinformatics/jawm_demo.git

# download test data
cd jawm_demo
jawm-test -r download

# docker
jawm demo.py demo -p ./yaml/docker.yaml

# slurm & apptainer with multiple yaml files
jawm demo.py demo -p ./yaml/vars.yaml ./yaml/hpc.yaml
```

Testing this module on your system's python, jawm, and docker installations:
```
jawm-test --python_versions system --jawm_versions local
```
More information on running and developing tests can be found in `./test/README.md`.
