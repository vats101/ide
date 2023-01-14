import uuid   #needed to generate unique filenames
import subprocess
import os
def create_source_file(code,language):
    file_name=str(uuid.uuid4())+ "."+language
    with open("code/" + file_name,"w") as f:
        f.write(code)
    return file_name

def execute_file(file_name,language):
    if(language=="cpp"):
        #g++ xyz.cpp
        # subprocess.run(["g++","code/" + file_name])    #this only compiles the code

        # subprocess.run(["./a.exe"])          #this executes the compiled file.
        result= subprocess.run(["g++","C:/Users/DELL/PycharmProjects/miniproject/code/"+file_name],stdout=subprocess.PIPE)
        print(result.stdout,result.returncode)
        if(result.returncode!=0):
            #logic for compilation error hence  failure
            return
        result = subprocess.run(["./a.exe"], stdout=subprocess.PIPE)   #we are capturing the output
        if(result.returncode!=0):
            #logic for runtime error haenc failure
            return
        return result.stdout.decode("utf-8")

