---
title: "Installing Z3 in an environment on a Windows 10x64 system"
date: 2021-04-27
tags: [solvers, windows installation]
excerpt: "UPDATED. Z3 is an open-sourced software commonly described as a 'theorem prover'. It is also a problem solver..."
---

# What is Z3?

As per Microsoft Research [in this tutorial](https://rise4fun.com/z3/tutorial):  
>Z3 is a state-of-the art theorem prover from Microsoft Research. It can be used to check the satisfiability of logical formulas over one or more theories. Z3 offers a compelling match for software analysis and verification tools, since several common software constructs map directly into supported theories. 

Z3 is also a problem solver as shown in numerous examples in [Dennis Yurichev's SAT/SMT by example booklet](https://yurichev.com/writings/SAT_SMT_by_example.pdf). Better yet: [Z3 has a python wrapper](https://github.com/Z3Prover/z3)!


# Installing Z3 for python on Windows 10

These are the steps I followed for a successful installation of Z3 on my current system, Windows 10x64. I used two sources: the [Z3 README file [RM]](https://github.com/Z3Prover/z3/blob/master/README.md) and the additional instructions from [issue [916]](https://github.com/Z3Prover/z3/issues/916).  

My steps differ somewhat from those given in [[RM] for python](https://github.com/Z3Prover/z3#python):  
I build the python bindings in the local repo of the cloned, latest release to have a single Z3 version on my system. I can then copy the necessary files into any python environment I choose.

### Note: This installation requires Visual Studio.
Many other software installations also rely on it, so go ahead: [download it](https://visualstudio.microsoft.com/downloads/?utm_medium=microsoft&utm_source=docs.microsoft.com&utm_campaign=navigation+cta&utm_content=download+vs2019) and install it: you won't regret it!

## Step 1: Create a local repo for Z3 by cloning the __latest stable release__ into some local <project> folder.
As of my installation, the release number was `z3-4.8.10`. This information is not stated in [RM], but an installation using the cloned main Z3 repo (without any branch option for the `git clone` command), will fail.
```
cd <project>
git clone --depth 1 -b z3-4.8.10 https://github.com/Z3Prover/z3.git
```

## Step 2: Create the makefile into the local Z3 repo [RM]:
```
cd z3
python scripts/mk_make.py -x --python
```
This step creates a build folder containing a Makefile and ends with clear instructions:
```
[...]
Makefile was successfully generated.
  compilation mode: Release
  platform: x64

To build Z3, open a [Visual Studio x64 Command Prompt], then
type 'cd C:\<path\to\project>\z3\build && nmake'

Remark: to open a Visual Studio Command Prompt, go to: "Start > All Programs > Visual Studio > Visual Studio Tools"
```
## Step 3: Open a [Visual Studio Command Prompt](https://docs.microsoft.com/en-us/visualstudio/ide/reference/command-prompt-powershell?view=vs-2019):
On my system (Windows 10x64, VS 2019):
 1. Select Start [Windows logo key on the keyboard] and scroll to the letter V.
 2. Expand the Visual Studio 2019 folder
 3. Select & launch: 'x64 Native Tools Command prompt for VS 2019'

## Step 4: Build Z3 with the created Makefile from the VS command prompt:
```
cd C:\<path\to\project>\z3\build && nmake   & REM use the command given at end of Step 2.
```
The output lists all the C++ modules generated (in around 10 minutes on my system). A successful build ends with these lines:
```
Z3 was successfully built.
"Z3Py scripts can already be executed in the 'build\python' directory."
"Z3Py scripts stored in arbitrary directories can be executed if the 'build\python' directory is added to the PYTHONPATH environment variable and the 'build' directory is added to the PATH environment variable."
```

After a successful build, the <project>/z3/build/ folder contains the z3 executable file `z3.exe`, the library `libz3.dll` and a python/z3 folder.    
As noted in [[RM] for python](https://github.com/Z3Prover/z3#python):
>Note that the build/python/z3 directory should be accessible from where python is used with Z3 and it depends on libz3.dll to be in the path.
Decoded, "from where python is used" means a Python environment.

## Step 5: Add the path to `libz3.dll` to the `Z3_LIBRARY_PATH` environment variable.

## Step 6: Add Z3 to an enviroment, e.g. <env1>:
* 6.0: Activate the environment (I'm using conda):
```
conda activate env1
```
* 6.1: Install the Python wrapper for Z3:
```
pip install z3-solver
```
* 6.2 Locate the environment site-packages folder:
In a default Anaconda installation, the path to the environment site-packages folder is: `C:\\Users\\<u>\\Anaconda3\\envs\\<env1>\\lib\\site-packages`.
```
python -c "import site; print(site.getsitepackages())"
```

* 6.3: Copy the Z3 folder from the `<project>/z3/build/python/` directory into the <env1> environment site-packages/z3 directory.


## Step 7: Test
```
(env1)> python
>>> import z3
>>> z3.Int('x')
x
>>> exit()
```
If you pass the test, you're all set with Z3!

