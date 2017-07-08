Modern Optimization Methods in Python
=======================================

Highly-constrained, large-dimensional, and non-linear optimizations are found
at the root of most of today's forefront problems in statistics,
quantitative finance, risk, operations research, materials design, and other
predictive sciences. Tools for optimization, however, have not changed much in
the past 40 years -- until very recently. The abundance of parallel computing
resources has stimulated a shift away from using reduced models to solve
statistical and predictive problems, and toward more direct methods for solving
high-dimensional nonlinear optimization problems.

This tutorial will introduce
modern tools for solving optimization problems -- beginning with traditional
methods, and extending to solving high-dimensional non-convex optimization
problems with highly nonlinear constraints. We will start by introducing the
cost function, and it's use in local and global optimization. We will then
address how to monitor and diagnose your optimization convergence and results,
tune your optimizer, and utilize compound termination conditions. This tutorial
will discuss building and applying box constraints, penalty functions, and
symbolic constraints. We will then demonstrate methods to efficiently reduce
search space through the use of robust optimization constraints. Real-world
inverse problems can be expensive, thus we will show how to enable your
optimization to seamlessly leverage parallel computing. Large-scale
optimizations also can greatly benefit from efficient solver restarts and the
saving of state. This tutorial will cover using asynchronous computing for
results caching and archiving, dynamic real-time optimization, and dimensional
reduction. Next we will discuss new optimization methods that leverage parallel
computing to perform blazingly-fast global optimizations and n-dimensional
global searches. Finally, we will close with applications of global
optimization in statistics and quantitative finance.

The audience need not be
an expert in optimization, but should have interest in solving hard real-world
optimization problems. We will begin with a walk through some introductory
optimizations, learning how to build confidence in understanding your results.
By the end of the tutorial, participants will have working knowledge of how to
use modern constrained optimization tools, how to enable their solvers to
leverage high-performance parallel computing, and how to utilize legacy data
and surrogate models in statistical and predictive risk modeling.



Content
---------

All tutorial content can be obtained from this repository either with
`git, or by downloading the repository content as a zip file.  If you use
git, you can clone this repostory with::

    $ git clone https://github.com/mmckerns/tutmom.git


or, download and unzip the zipfile.

As the day of the tutorial get nearer, it is highly recommended to update
this repository.  When tutorial content is added or modified, it is
recommended to update your copy of the tutorial.  Tutorial content may be
updated up to the day of the tutorial, during the tutorial, and beyond.
To update your copy of the tutorial content with git, change to the tutorial
directory (i.e. `tutmom`), then pull an update with::

    $ git pull


or, download and unzip a new copy of the zipfile.



Requirements
--------------

To be able to run the examples, demos, and exercises in this tutorial,
the following packages must be installed::

    numpy >= 1.0,
    scipy >= 0.6.0,
    sympy >= 0.6.7,
    matplotlib >= 0.91,
    cvxopt >= 1.1.0,
    jupyter >= 1.0,
    pox >= 0.2.3,
    dill >= 0.2.7,
    multiprocess >= 0.70.5,
    ppft >= 1.6.4.7,
    klepto >= 0.1.4,
    pathos >= 0.2.1,
    mystic >= 0.3.1


and optionally::

    sqlalchemy >= 0.8.4



Installation
--------------

All packages can be installed with `pip`::

    >$ pip install setuptools
    >$ pip install numpy
    >$ pip install sympy
    >$ pip install pathos
    >$ pip install mystic
    >$ pip install matplotlib
    >$ pip install scipy
    >$ pip install cvxopt
    >$ pip install jupyter


and optionally::

    >$ pip install sqlalchemy


The `pip` installs of `numpy`, `matplotlib`, and `scipy` often fail.
A more stable choice for installing these three packages is to use a
scientific python distribution such as `canopy` or `anaconda`.



The following steps were used by the tutorial author to test on Windows:

    # installed Visual Studio Community 2015 RC
    # installed Python Tools 2.2 RC for Visual Studio 2015
    # installed Microsoft Visual C++ Compiler for Python 2.7
    # installed Miniconda 3.10.1 (64-bit) for Python 2.7
    # installed Git for Windows 1.9.5-preview20150319 (including cmd tools)
    >$ conda install pip
    >$ conda install setuptools
    >$ conda install numpy
    >$ conda install scipy
    >$ conda install matplotlib
    >$ conda install sympy
    >$ conda install cvxopt
    >$ conda install jupyter
    >$ conda install sqlalchemy
    # get https://github.com/uqfoundation/pox/blob/master/tools/pythonstartup
    # save as ~\.python (also add as PYTHONSTARTUP to environment variables)
    # associate .py file with conda's python.exe
    # fix bug where conda doesn't respect all `sys.argv`
    #   regedit HKEY_CLASSES_ROOT\Applications\python27.exe\shell\open\command
    #   regedit HKEY_CLASSES_ROOT\py_auto_file\shell\open\command
    >$ pip install pathos
    >$ pip install mystic



Verification
--------------

To test your installation, change to the tutorial directory, and run::

    >$ python check_env.py
    OK.


If you choose not install all optional dependencies, you will see a warning::

    >$ python check_env.py 
    sqlalchemy:: No module named sqlalchemy


Feel free to ignore warnings for optional dependencies.

