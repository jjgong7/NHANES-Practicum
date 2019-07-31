# ! python
# coding: utf-8
# Credit: https://gist.github.com/tommyogden/ec79f2ebe2baf45655445b575dc7f540

import os
import argparse
import glob

#Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import re
from collections import defaultdict

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors.execute import CellExecutionError

# Parse args
parser = argparse.ArgumentParser(description="Runs a set of Jupyter \
                                              notebooks.")
file_text = """ Notebook file(s) to be run, e.g. '*.ipynb' (default),
'my_nb1.ipynb', 'my_nb1.ipynb my_nb2.ipynb', 'my_dir/*.ipynb'
"""
parser.add_argument('file_list', metavar='F', type=str, nargs='*', 
    help=file_text)
parser.add_argument('-t', '--timeout', help='Length of time (in secs) a cell \
    can run before raising TimeoutError (default 600).', default=600, 
    required=False)
parser.add_argument('-p', '--run-path', help='The path the notebook will be \
    run from (default pwd).', default='.', required=False)
args = parser.parse_args()
print('Args:', args)
if not args.file_list: # Default file_list
    args.file_list = glob.glob('*.ipynb')

# Check list of notebooks
notebooks = []
print('Notebooks to run:')
for f in args.file_list:
    # Find notebooks but not notebooks previously output from this script
    if f.endswith('.ipynb') and not f.endswith('_out.ipynb'):
        print(f[:-6])
        notebooks.append(f[:-6]) # Want the filename without '.ipynb'

# Execute notebooks and output
num_notebooks = len(notebooks)
print('*****')
for i, n in enumerate(notebooks):
    #split up file path to include out folder
    n_split = n.rsplit('/', 1)
    output_path = n_split[0] + '/output' 
    n_out = output_path + '/' + n_split[1] + '_out'
    with open(n + '.ipynb') as f:
        nb = nbformat.read(f, as_version=4)
        ep = ExecutePreprocessor(timeout=int(args.timeout), kernel_name='python3')
        try:
            print('Running', n, ':', i, '/', num_notebooks)
            out = ep.preprocess(nb, {'metadata': {'path': args.run_path}})
        except CellExecutionError:
            out = None
            msg = 'Error executing the notebook "%s".\n' % n
            msg += 'See notebook "%s" for the traceback.' % n_out
            print(msg)
        except TimeoutError:
            msg = 'Timeout executing the notebook "%s".\n' % n
            print(msg)
        finally:
            # Write output file
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            with open (n_out + '.ipynb', mode='wt') as f:
                nbformat.write(nb, f)