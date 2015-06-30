#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 2015 California Institute of Technology.
# License: 3-clause BSD.
"""
check environment scipt
"""
import sys

# requirements
has = dict(
    # optimization
    scipy='0.0.0',
    mystic='0.0.0',
    # parallel computing
    pathos='0.0.0',
    # dependencies
    dill='0.0.0',
    klepto='0.0.0',
    numpy='0.0.0',
    sympy='0.0.0',
    pox='0.0.0',
    ppft='0.0.0',
    multiprocess='0.0.0',
    # examples
    matplotlib='0.0.0',
    # optional
   #pyina='0.0.0',
   #pyconstraints='0.0.0',
   #pulp='0.0.0',
   #cvxopt='0.0.0', # cvxpy ???
    sqlalchemy='0.0.0',
)


# executables
run = dict(
    # optimization
    mystic=('mystic_log_reader.py','mystic_model_plotter.py',
            'support_convergence.py','support_hypercube.py',
            'support_hypercube_measures.py','support_hypercube_scenario.py',),
    # parallel computing
    # dependencies
    ppft=('ppserver.py',),
    # examples
    # optional
   #pyina=('sync','cp','rm','ezpool.py','ezscatter.py',),
)


returns = 0

# check installed packages
for module in has.keys():
    try:
        __module__ = __import__(module, globals(), locals(), [], 0)
        exec('%s = __module__' % module)
    except ImportError:
        print("%s:: %s" % (module, sys.exc_info()[1]))
        returns += 1


# check required versions
from distutils.version import LooseVersion as V
for module,version in has.items():
    try:
        assert V(eval(module).__version__) >= V(version)
    except NameError:
        pass # failed import
    except AttributeError:
        pass # can't version-check non-standard packages...
    except AssertionError:
        print("%s:: Version >= %s is required" % (module, version))
        returns += 1



# check required executables
try:
    from pox import which
   #from subprocess import Popen, STDOUT, PIPE#, call
except ImportError:
    sys.exit(returns)
for module,executables in run.items():
    for prog in reversed(executables):
        try:
            assert which(prog)
#           process = Popen([prog, '--help'], stderr=STDOUT, stdout=PIPE)
#           process.wait()
            if isinstance(executables, list): break  # just requires one
        except (OSError, AssertionError):
            if isinstance(executables, list) and \
               prog != executables[0]: pass
            from sys import exc_info
            print("%s:: Executable '%s' not found" % (module, prog))
           #print("%s:: %s" % (prog, exc_info()[1]))
            returns += 1


# final report
if not returns:
    print('OK.')

sys.exit(returns)


