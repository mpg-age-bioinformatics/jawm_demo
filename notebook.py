# ---
# jupyter:
#   jupytext:
#     cell_markers: '{{{,}}}'
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.17.0
#   kernelspec:
#     display_name: Python 3.12.6
#     language: python
#     name: py3.12.6
# ---

# # jawm notebook example
#
# This notebook demonstrates how to use jawm from inside a notebook.

# ### 0. Packages import

import jawm

# ### 1. Locally
#
# A simple example running your command locally.

# {{{
# definde the process
demo_p1=jawm.Process( 
    name="demo_p1",
    script="""#!/bin/bash
echo "{{extra_args}} {{my_demo_argument}}" 2>&1 | tee {{mk.output}}/demo.txt
""",
    var={
        "extra_args": "",
        "my_demo_argument":"This is just a demo.", 
        "mk.output":"./test/test-output/", # the prefix "mk." leads to the creation of this folder and volume mapping if you are using containers
    }
)

# excute the process
demo_p1.execute()

# wait for all above processes to complete
jawm.Process.wait()

# capture the output
print(demo_p1.get_output())
# }}}

# ### 2. Docker
#
# With jawm you can also run processes with docker from inside a notebook.

# {{{
# definde the process
demo_p2=jawm.Process( 
    name="demo_p2",
    script="""#!/usr/bin/env python3
with open("{{map.file}}", "r") as src, open("{{mk.output}}/demo.txt", "a") as dst:
    dst.write(src.read())
""",
    var={
        "mk.output":"<output_folder>", # the prefix "mk." leads to the creation of this folder and volume mapping if you are using containers
        "map.file":"<some_file>"# the prefix "map." leads to the mapping of this file if you are using containers
    },
    container="python:3.13-slim",
    environmnent="docker",
    
    # other docker parameters

    # docker_run_as_user=True,
    # environment_docker={ "-v": ["/nexus:/nexus"] }
    # in this example you do not need to do volume mapping as the prefixes `mk.`` in the `mk.output`` variable
    # and `map.` in the `map.file` variable will instruct jawm to do this volume mappings for you. 
    # Unless you deactivate automated mapping with:
    # automated_mount=False,

    # other general paramaters

    # parallel: False # do not run jobs in parallel

)

# excute the process
demo_p2.execute()

# wait for all above processes to complete
jawm.Process.wait()

# capture the output
print(demo_p2.get_output())
# }}}

# ### 3. slurm and apptainer
#
# Also slurm and apptainer can be used with jawm.

# {{{
demo_p3=jawm.Process( 
    name="demo_p3",
    script="""#!/usr/bin/env Rscript
write( "Demo completed", file = "{{mk.output}}/demo.txt", append = TRUE)
""",    
    var={
        "mk.output":"<output_folder>", # the prefix "mk." leads to the creation of this folder and volume mapping if you are using containers
    },
    manager="slurm",
    manager_slurm={ "-p":"cluster,dedicated", "--mem":"20GB", "-t":"1:00:00", "-c":"8" }, # your slum parameters here
    environment="apptainer",
    container="docker://r-base:4.5.1", 
    # environment_apptainer={"-B": [input_file, output_folder] } # your apptainer parameters here.
    # in this example you do not need to do volume mapping as the prefixes `mk.`` in the `mk.output`` variable
)

# excute the process
demo_p3.execute()

# wait for all above processes to complete
jawm.Process.wait()

# capture the output
print(demo_p3.get_output())
# }}}

# ### 4. Establishing dependencies
#
# So far we have used `jawm.Process.wait()` to avoid dependent jobs to start without it's parent process finishing.
#
# We can also do this by setting dependencies in a process and we can also set `wait` on specific processes.

# {{{
demo_p1.execute()

# set dependency for demo_p2
demo_p2.depends_on=[demo_p1.hash]

# execute demo_p2
demo_p2.execute()

# wait for a specific process to finish
jawm.Process.wait(process_list=[ demo_p2.hash ]) # use tail="both" if you want stdout and stderr to be print live for you

# execute demo_p3
demo_p3.execute()

# wait for all above processes to complete
jawm.Process.wait()

# }}}

# ### 5. From notebook to the command line
#
# Having developed your code on a notebook, you can now run the associated script from a command line.
#
# ```
# $ jupyter nbconvert --to python notebook.ipynb
#
# $ python3 notebook.py
# ```
#
# Please notice that unless you have docker, apptainer and slurm in your path and the 
# respective slurm and apptainer paramters set this example will not work for you.
#
#
# ### 6. Using `yaml` to store arguments.
#
# You can now define new parameters for your workflow which you can store in `yaml` files 
# and overwrite the paramaters set here at run time:
#
# ```
# $ jawm notebook.py -p ./yaml/docker.yaml
# ```
#
# Check out the examples on the `yaml` folder.
#
# Additionaly, you can load those parameters into the process when running your 
# workflow on a notebook:

demo_p1.param_file="yaml/docker.yaml"
demo_p1.execute()

# or

demo_p1.param_file=["yaml/vars.yaml", "yaml/hpc.yaml"]
demo_p1.execute()
