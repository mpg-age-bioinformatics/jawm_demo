import jawm

demo_p1=jawm.Process( 
    name="demo_p1",
    script="""#!/bin/bash
echo "{{extra_args}} {{my_demo_argument}}" 2>&1 | tee {{mk.output}}/demo.txt
""",

    # arguments for the script above :
    
    # var={
    #     "extra_args": "",
    #     "my_demo_argument":"This is just a demo.", 
    #     "mk.output":"<output_folder>", # the prefix "mk." leads to the creation of this folder and volume mapping if you are using containers
    # },

    # here you can describe your variables
    desc={
        "extra_args": "use this if you want to add not preset arguments",
        "my_demo_argument":"Some text that will be printed to the screen.", 
        "output":"Folder for output", # the prefix "mk." leads to the creation of this folder and volume mapping if you are using containers
    },
    
    # example arguments for jawn

    # manager="slurm",
    # manager_slurm={
    #     "-p":"cluster,dedicated", 
    #     "--mem":"20GB", 
    #     "-t":"1:00:00", 
    #     "-c":"8" 
    # },
    
    # container="docker://mpgagebioinformatics/fastqc:0.11.9",
    # environmnent="apptainer",
    # environment_apptainer={ '-B': [input_file, output_folder] }
    
    # container="mpgagebioinformatics/fastqc:0.11.9",
    # environmnent="docker",
    # environment_docker={ '-v': [input_file, output_folder] },


    # param_file="yaml/apptainer.params.yaml" ,
    # param_file=[ "yaml/apptainer.params.yaml" , "yaml/slurm.params.yaml" ],
  
)

demo_p2=jawm.Process( 
    name="demo_p2",
    script="""#!/usr/bin/env python3
with open("{{map.file}}", "r") as src, open("{{mk.output}}/demo.txt", "a") as dst:
    dst.write(src.read())
""",

    # arguments for the script above :
    
    # var={
    #     "mk.output":"<output_folder>", # the prefix "mk." leads to the creation of this folder and volume mapping if you are using containers
    #     "map.file":"<some_file>"# the prefix "map." leads to the mapping of this file if you are using containers
    # },
  
)

demo_p3=jawm.Process( 
    name="demo_p3",
    script="""#!/usr/bin/env Rscript
write( "Demo completed", file = "{{mk.output}}/demo.txt", append = TRUE)
""",

    # arguments for the script above :
    
    # var={
    #     "mk.output":"<output_folder>", # the prefix "mk." leads to the creation of this folder and volume mapping if you are using containers
    # },
  
)


if __name__ == "__main__":
    import sys
    from jawm.utils import workflow
    from jawm.utils import load_modules

    # load modules from local folders
    load_modules("submodules")

    # load modules from online git repos
    load_modules("jawm_template")

    # it can be used in the form
    # load_modules(["modules","jawm_template@<tag/commit_hash>"])
    
    # or for latest available tag
    # load_modules("jawm_template@latest")

    workflows, var, args, unknown_args= jawm.utils.parse_arguments(["main","demo","test"],)

    # usage: 

    if workflow( ["main","demo","test"], workflows ) :

        # execute process
        demo_p1.execute()

        # execute a process with dependencies
        demo_p2.depends_on=[demo_p1.hash]
        demo_p2.execute()

        # wait for all above processes to complete
        jawm.Process.wait()

        # print the output
        print(demo_p1.get_output())
        print(demo_p2.get_output())

        demo_module.demo_module_p1.execute()
        template.template_p2.execute()

        jawm.Process.wait()
        print(demo_module.demo_module_p1.get_output())
        print(template.template_p2.get_output())

    if workflow( "test", workflows ) :

        # for the test workflow we also do something more (just for demo)
        demo_p3.execute()
        jawm.Process.wait()
        print("Test completed.")


    sys.exit(0)
