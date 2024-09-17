import importlib as il
from typing import Dict
from types import ModuleType
from bot import utils
import sys


# Add the plugins directory to the path
sys.path.extend(['src/plugins'])
# Execution file for the project
plugin:Dict[str,ModuleType] = {}
# Get list of folder in src/plugins
plugins = utils.get_directory('src/plugins')
# Load the plugins
for pname in plugins:
    try:
        module = il.import_module(pname)
        plugin[pname] = module
    except ImportError as e:
        print(f"Error importing {pname}: {e}")