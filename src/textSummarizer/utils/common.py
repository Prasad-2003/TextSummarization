import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox
    """
    try:
        with open(path, 'r') as f:
            content = yaml.safe_load(f)
            logger.info(f"yaml file: {path} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(paths: list, verbose=True):
    '''Create list of directories
        
        Args:
            paths: list of paths to directories
            verbose: print info about created directories
    '''
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"directory: {path} created successfully")
                
                
@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns the size of a file in KB
    """
    size = round(os.path.getsize(path) / 1024)
    return f"~ {size} KB"
