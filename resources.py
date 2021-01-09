import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'pytest-shutil'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'pillow'])