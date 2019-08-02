---
title: "Installing Z3 in an environment on a Windows 10 (x64) system"
date: 2019-07-31
tags: [solvers, Satisfiability Modulo Theories]
excerpt: "Z3](https://github.com/Z3Prover/z3) is an open-sourced software developed at Microsoft and commonly described as a "theorem prover". It is also a problem solver..."
---

# What's Z3?

[Z3](https://github.com/Z3Prover/z3) is an open-sourced software developed at Microsoft and commonly described as a "theorem prover". It is also a problem solver as shown in numerous examples in [Dennis Yurichev's SAT/SMT by example](https://yurichev.com/writings/SAT_SMT_by_example.pdf).

# Installing Z3 for python on Windows 10

These are the steps I followed for a successful installation of Z3 on my current system, Windows 10 x64. I used two sources indicated in brackets: the [Z3 README [RM] file](https://github.com/Z3Prover/z3/blob/master/README.md) and addtional instructions from issue [#916](https://github.com/Z3Prover/z3/issues/916).  
$S_i$ refers to the sequential steps to full installation.
---

## S0. Clone the source code [RM]:
```
cd <a path>
git clone https://github.com/Z3Prover/z3.git
```
The path <build> I refer to further will then be equivalent to `<a path>\z3\build`.  

## S1. First build (to .pyc components) [#916]:

The building should take place inside the x64 Native Build Tools Prompt.
For my system, the VS Tools version (Windows 10) is "x64 Native Tools Command Prompt for VS 2017"

Open that command prompt, enter the following command and press ENTER:
```
python scripts/mk_make.py -x --python
```
> [#916]: This can build a package that works in python3 (to be tested).  

## S1.post: If sucessful, the last few lines of the stdout will be:
```
64-bit:         True
Writing build\Makefile
Copied Z3Py example 'all_interval_series.py' to 'build\python'
Copied Z3Py example 'example.py' to 'build\python'
Copied Z3Py example 'mini_ic3.py' to 'build\python'
Copied Z3Py example 'mini_quip.py' to 'build\python'
Copied Z3Py example 'parallel.py' to 'build\python'
Copied Z3Py example 'rc2.py' to 'build\python'
Copied Z3Py example 'socrates.py' to 'build\python'
Copied Z3Py example 'trafficjam.py' to 'build\python'
Copied Z3Py example 'union_sort.py' to 'build\python'
Copied Z3Py example 'visitor.py' to 'build\python'
Makefile was successfully generated.
  compilation mode: Release
  platform: x64

To build Z3, open a [VS Tools x64 Command Prompt], then type 'cd <build> && nmake'

Remark: to open a Visual Studio Command Prompt, go to:  
"Start > All Programs > Visual Studio > Visual Studio Tools"
```
## S1.2 Following instructions from S1.post above:

Typed: `cd <build> && nmake`, then pressed ENTER.
This command compiles the C++ code.  


## S2. Add Z3 exec and lib files to the PATH [#916]:
 
> The z3.exe appears to be independent and can work anywhere [...]. So you can copy both build/z3.exe and build/libz3.dll into somewhere [and add them to] the PATH.  

I created a Z3 folder in `C:\Program Files` and copied z3.exe and libz3.dll from <build>, and created the PATH variables: (z3, C:\Program Files\Z3\z3.exe) and (libz3, C:\Program Files\Z3\libz3.dll).
Note: I also created these keys in both the System and User variables paths.

## S3. Copy the build/python/z3 directory to an environment:

> [#916]: Then the build/python/z3 directory should be copied into the site-packages directory of Python. On Windows, this isn't done automatically, instead you have to find your Windows site-packages: like python3 -c 'import site; print(site.getsitepackages())', then copy the entire directory there.


### S3.1: Get the site packages path for an environment:
I activated my chosen environment (which uses py3.6.7), launched python and used the code from [#916].  

### S3.2: Copied build/python/z3 directory to <env1>\lib\\site-packages

## S4. Tests:

### S4.1 Test 1:
Using a conda prompt, I activated <env1>, launched python & imported z3:
(env1)> python
>>> import z3
Import error:
```
Could not find libz3.dll; consider adding the directory containing it to
  - your system's PATH environment variable,
  - the Z3_LIBRARY_PATH environment variable, or
  - to the custom Z3_LIBRARY_DIRS Python-builtin before importing the z3 module, e.g. via
    import builtins
    builtins.Z3_LIB_DIRS = [ '/path/to/libz3.dll' ]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\catch\Anaconda3\envs\dsml\lib\site-packages\z3\__init__.py", line 1, in <module>
    from .z3 import *
  File "C:\Users\catch\Anaconda3\envs\dsml\lib\site-packages\z3\z3.py", line 45, in <module>
    from . import z3core
  File "C:\Users\catch\Anaconda3\envs\dsml\lib\site-packages\z3\z3core.py", line 67, in <module>
    raise Z3Exception("libz3.%s not found." % _ext)
z3.z3types.Z3Exception: libz3.dll not found.
```
### S4.2 Test 2:
Fix: I copied the build/python/libz3.dll file into the <env1>\lib\\site-packages\z3 folder and repeated the import & set variable tests:
```
(base)> conda activate env1
(env1)> python
>>> import z3
>>> z3.Int('x')
x
>>> exit()
(env1)> conda deactivate
```
Done!

What I think happened can be seen using the path from the sys module:
```
>>> import sys; sys.path
['', '<env1>\\python36.zip', '<env1>\\DLLs', '<env1>\\lib', '<env1>', '<env1>\\lib\\site-packages']
```
Since env1 is the active environment, this is the default path, so until I copied libz3.dll into <env1>\lib\\site-packages\z3, it could not be found.


Now I can play with z3.py and sympy!



