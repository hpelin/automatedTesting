import runpy
import subprocess
import os

def test_analysis_notebook():
    subprocess.run(['jupyter', 'nbconvert', '--to', 'script',  '--execute',  'notebooks/analyze_data.ipynb'])
