import jawm

simple_p1=jawm.Process( 
    name="simple_process",
    script="""#!/bin/bash
echo "{{my_simple_argument}}" 2>&1 | tee {{output}}/simple.txt
""",    
    var={
        "my_simple_argument":"This is just a simple example.", 
        "mk.output":"./test/test-output", # the prefix "mk." leads to the creation of this folder and volume mapping when using containers
    },
    container="ubuntu:24.04",
    environment="docker",
)

simple_p1.execute()
jawm.Process.wait( simple_p1.hash)
print("Your file can be found under: ./test/test-output/simple.txt")