# jawm_demo

This is a jawm demo module.

Checkout `simple.py`, `advanced.py` and `notebook.ipynb` for examples on how to develop data analysis workflows with jawm.

Installing jawm:
```
pip install git+ssh://git@github.com/mpg-age-bioinformatics/jawm.git
```
For more information on jawm please visit jawm's repo on [GitHub.com](https://github.com/mpg-age-bioinformatics/jawm/tree/main).

Example usage:
```
# clone this module
git clone git@github.com:mpg-age-bioinformatics/jawm_demo.git

# simple
cd jawm_demo
python simple.py

# simple with jawm
jawm simple.py

# download test data
jawm-test -r download

# docker
jawm advanced.py demo -p ./yaml/docker.yaml

# slurm & apptainer with multiple yaml files
jawm advanced.py demo -p ./yaml/vars.yaml ./yaml/hpc.yaml
```

Additional jawm workflows are available [here (GitHub.com)](https://github.com/mpg-age-bioinformatics?q=jawm_&type=all&language=&sort=).
