---
title: "Installing Z3 in an environment on a Windows 10x64 system"
date: 2021-04-27
tags: [solvers, windows installation]
excerpt: "UPDATED x 2. Z3 is an open-sourced software commonly described as a 'theorem prover'. It is also a problem solver..."
---

# What is Z3?

As per Microsoft Research [in this tutorial](https://rise4fun.com/z3/tutorial):  
>Z3 is a state-of-the art theorem prover from Microsoft Research. It can be used to check the satisfiability of logical formulas over one or more theories. Z3 offers a compelling match for software analysis and verification tools, since several common software constructs map directly into supported theories. 

Z3 is also a problem solver as shown in numerous examples in Dennis Yurichev's [SAT/SMT by example booklet](https://yurichev.com/writings/SAT_SMT_by_example.pdf). Added bonus: __Z3 has a python wrapper__ called [z3-solver](https://github.com/Z3Prover/z3/blob/master/README.md#python), which can be installed with `pip` from the [Python package index](https://pypi.org/project/z3-solver/). 

# Overview
The purpose of this post is to show how the Z3 library can be added to any compatible virtual environment on a Windows 10x64 machine.  
I followed the steps listed in __Workflow__ towards a successful installation of Z3 on my current system, Windows 10x64 with the help of these two sources: the [Z3 README file [RM]](https://github.com/Z3Prover/z3) and the additional instructions from [issue [916]](https://github.com/Z3Prover/z3/issues/916).  
As the Z3 solver is written in C++, it first needs compiling or building. The build step yields an executable file `z3.exe` and its accompanying library `libz3.dll`, along with a `python/z3` folder.  Note that as per [Dependencies in [RM]](https://github.com/Z3Prover/z3#dependencies), Python3 is required to build Z3 as well as Visual Studio.  
In order to use Z3 within python, you need to install its wrapper `z3_solver`, typically in a virtual environment &mdash; or in multiple environments: this is detailed in __Step 2__.  

# Workflow
 1. Build Z3 with python on Windows 10x64  
    1.0 Install Visual Studio  
    1.1 Create a local repo for Z3 by cloning the public __latest stable release__  
    1.2 Create the Makefile into the local Z3 repo  
    1.3 Open a Visual Studio Command Prompt  
    1.4 Build Z3 with the created Makefile from the Visual Studio Command Prompt  
 2. Install the Python wrapper for Z3, `z3_solver` in an environment    
    2.1 Activate the environment  
    2.2 Install `z3_solver`, the Python wrapper for Z3  
    2.3 Locate the environment site-packages folder  
    2.4: Copy the Z3 folder from the `<project>/z3/build/python/` directory into the <env1> environment site-packages/z3 directory  
 3. Test  

# Detailed Workflow
## 1. Build Z3 with python on Windows 10x64

My steps differ somewhat from those given in [[RM] for python](https://github.com/Z3Prover/z3#python):  
I build the python bindings in the local repo of the cloned, latest release to have a single Z3 version on my system. As documented in [916], I can then copy the necessary files into any python environment I choose.

### 1.0 Install Visual Studio (if you don't already have it)
Many other software installations also rely on it, so go ahead: [download it](https://visualstudio.microsoft.com/downloads/?utm_medium=microsoft&utm_source=docs.microsoft.com&utm_campaign=navigation+cta&utm_content=download+vs2019) and install it: you won't regret it!

### 1.1 Create a local repo for Z3 by cloning the public __latest stable release__ into some local <project> folder.
As of my installation, the release number was `z3-4.8.10`. This information is not stated in [RM], but an installation using the cloned main Z3 repo will fail if the `git clone` command lacks a branch option referencing the latest release. 
```
cd <project>
git clone --depth 1 -b z3-4.8.10 https://github.com/Z3Prover/z3.git
```
__Outcome:__ The new folder `<project>\z3` contains the latest release of Z3.  


### 1.2 Create the makefile into the local Z3 repo [RM]:  
```
cd z3
python scripts/mk_make.py -x --python
```
__Outcome:__ This step creates a build folder containing a Makefile and ends with clear instructions:
```
Makefile was successfully generated.
  compilation mode: Release
  platform: x64

To build Z3, open a [Visual Studio x64 Command Prompt], then
type 'cd C:\<path\to\project>\z3\build && nmake'

Remark: to open a Visual Studio Command Prompt, go to: "Start > All Programs > Visual Studio > Visual Studio Tools"
```
### 1.3 Open a [Visual Studio Command Prompt](https://docs.microsoft.com/en-us/visualstudio/ide/reference/command-prompt-powershell?view=vs-2019):
On my system (Windows 10x64, VS 2019):
 1. Click on the Windows Start key [Windows logo key on the keyboard] and scroll to the letter V on the menu.
 2. Expand the Visual Studio 2019 folder
 3. Select & launch: 'x64 Native Tools Command prompt for VS 2019'

### 1.4 Build Z3 with the created Makefile from the VS command prompt:
```
cd C:\<path\to\project>\z3\build && nmake   & REM use the command given at end of Step 1.2.
```  
__Outcome:__ The output lists all the C++ modules generated (in around 10 minutes on my system). A successful build ends with these lines:
```
Z3 was successfully built.
"Z3Py scripts can already be executed in the 'build\python' directory."
"Z3Py scripts stored in arbitrary directories can be executed if the 'build\python' directory is added to the PYTHONPATH environment variable and the 'build' directory is added to the PATH environment variable."
```

After a successful build, the `<project>/z3/build/` folder contains the z3 executable file `z3.exe`, the library `libz3.dll` and a `python/z3` folder.    
As noted in [[RM] for python](https://github.com/Z3Prover/z3#python):
> Note that the build/python/z3 directory should be accessible from where python is used with Z3 and it depends on libz3.dll to be in the path.
Decoded, "from where python is used" means a Python environment.

### 1.5 Add the path to `libz3.dll` to the `Z3_LIBRARY_PATH` environment variable.
    1. Click on the Windows Start key and type "environment" in the search box.  
    2. Select "Edit the system environment variables" (from Control panel), which should be the Best Match, to launch the "System Properties" window.
    3. Click on the "Environment Variables..." button on the "Advanced" tab to the "System Properties" window.
    4. Decide whether to create the new variable for the current user or for the system, then click on the corresponding section's "New..." button.  
    5. Type _Z3_LIBRARY_PATH_ in the variable name box and the _path to libz3.dll_ (i.e.: C:\Users\<u>\<project>\z3\build), in the value box and click the "OK" button in all the windows opened in this step.
    

## 2. Install the Python wrapper for Z3, `z3_solver` in an enviroment, e.g. <env1>:
### 2.1 Activate the environment (I'm using [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)):
```
conda activate env1
```
### 2.2 Install the Python wrapper for Z3:
```
(env1)> pip install z3-solver
```
### 2.3 Locate the environment site-packages folder:
Typically, in a default Anaconda installation, the path to the environment site-packages folder is: `C:\\Users\\<u>\\Anaconda3\\lib\\site-packages`   
and the corresponding path for a specific environment is: `C:\\Users\\<u>\\Anaconda3\\envs\\<env1>\\lib\\site-packages`.    
    
The following command yields the actual path on your system:  
```
(env1)> python -c "import site; print(site.getsitepackages())"  # [916]
```

### 2.4: Copy the Z3 folder from the `<project>/z3/build/python/` directory into the <env1> environment site-packages/z3 directory.  
This is what the quoted note at the end of Step 1.4 meant.

## 3 Test
```
(env1)> python
>>> import z3
>>> z3.Int('x')
x
>>> exit()
```
If you pass the test, you're all set with Z3!  

Repeat steps 2 & 3 in all the python environments you would want to have Z3 available.  
