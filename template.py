import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')


project_name = 'textSummarizer'

files = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/.__init__.py',
    f'src/{project_name}/config/.__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/.__init__.py',
    f'src/{project_name}/entity/.__init__.py',
    f'src/{project_name}/constants/.__init__.py',
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb'
]

for path in files:
    path = Path(path)
    dir, f = os.path.split(path)
    
    if dir != '':
        os.makedirs(dir, exist_ok=True)
        logging.info(f'Creating directory: {dir} for the file {f}')
        
        
    if ((not os.path.exists(path)) or (os.path.getsize(path) == 0)):
        with open(path, 'w') as file:
            pass
        logging.info(f'Creating empty file: {path}')
    
    else:
        logging.info(f'{f} already exists')