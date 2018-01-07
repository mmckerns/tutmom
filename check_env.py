#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 2015-2016 California Institute of Technology.
# Copyright (c) 2016-2018 Mike McKerns.
# License: 3-clause BSD.
"""
check environment scipt
"""
import sys

# requirements
has = dict(
    # optimization
    scipy='0.6.0',
    mystic='0.3.1',
    # parallel computing
    pathos='0.2.1',
    # dependencies
    pox='0.2.3',
    dill='0.2.7',
    klepto='0.1.4',
    numpy='1.0',
    sympy='0.6.7',
    ppft='1.6.4.7',
    multiprocess='0.70.5',
    # examples
    matplotlib='0.91',
    jupyter='1.0',
    cvxopt='1.1.0',
    # optional
   #pyina='0.2.0.dev0',
   #pulp='1.6.0',
   #Numberjack='1.1.0',
   #python-constraints='1.2', # installs as 'constraints'
    sqlalchemy='0.8.4',
)


# executables
# list: At least one item is expected
# tuple: All items are expected
run = dict(
    # optimization
    mystic=('mystic_log_reader.py','mystic_model_plotter.py',
            'support_convergence.py','support_hypercube.py',
            'support_hypercube_measures.py','support_hypercube_scenario.py',),
    # parallel computing
    pathos=('pathos_tunnel.py','pathos_server.py','tunneled_pathos_server.py',),
    # dependencies
    ppft=('ppserver.py',),
    # examples
    ### jupyter-notebook
    # optional
   #pyina=('sync','cp','rm','ezpool.py','ezscatter.py',),
)


returns = 0

# check installed packages
for module in has.keys():
    try:
        _module = module.split('-')[-1]
        __module__ = __import__(_module, globals(), locals(), [], 0)
        exec('%s = __module__' % _module)
    except ImportError:
        print("%s:: %s" % (module, sys.exc_info()[1]))
        run.pop(module, None)
        returns += 1


# check required versions
from distutils.version import LooseVersion as V
for module,version in has.items():
    try:
        _module = module.split('-')[-1]
        assert V(eval(_module).__version__) >= V(version)
    except NameError:
        pass # failed import
    except AttributeError:
        pass # can't version-check non-standard packages...
    except AssertionError:
        print("%s:: Version >= %s is required" % (module, version))
        returns += 1


def executable_exist(module, prog):
    try:
        assert which(prog)
#           process = Popen([prog, '--help'], stderr=STDOUT, stdout=PIPE)
#           process.wait()
        return True
    except (OSError, AssertionError):
        from sys import exc_info
        print("%s:: Executable '%s' not found" % (module, prog))
        #print("%s:: %s" % (prog, exc_info()[1]))
        return False


# check required executables
try:
    from pox import which
   #from subprocess import Popen, STDOUT, PIPE#, call
except ImportError:
    sys.exit(returns)
for module,executables in run.items():
    if isinstance(executables, list):
        found = False
        for executable in executables:
            if executable_exist(module, executable):
                found = True
                break
        if not found:
            returns += 1
    else:
        for executable in executables:
             if not executable_exist(module, executable):
                 returns += 1

# final report
if not returns:
    print('-'*50)
    print('OK.  All required items installed.')

sys.exit(returns)


