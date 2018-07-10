"""This test covers 'pip install' issue #155"""
import os
import sys
import subprocess

def read_version():
    # Determine the version number by reading it from the file
    # 'comtypes\__init__.py'.  We cannot import this file (with py3,
    # at least) because it is in py2.x syntax.
    for line in open("comtypes/__init__.py"):
        if line.startswith("__version__ = "):
            var, value = line.split('=')
            return value.strip().strip('"').strip("'")
    raise NotImplementedError("__version__ is not found in __init__.py")

# prepare the same package that is usually uploaded to PyPI
subprocess.check_call([sys.executable, 'setup.py', 'sdist', '--format=zip'])

filename_for_upload = 'comtypes-%s.zip' % read_version()
target_package = os.path.join(os.getcwd(), 'dist', filename_for_upload)

# run "pip install comtypes-x.y.z.zip"
pip_exe = os.path.join(os.path.dirname(sys.executable), 'Scripts', 'pip.exe')
subprocess.check_call([pip_exe, 'install', target_package])
