import setuptools

with open("README.md", 'r', encoding='utf-8') as file:
    decription = file.read()
    

__version__ = '0.0.0'

REPO_NAME = 'TextSummarization'
AUTHOR_USER_NAME = 'Prasad-2003'
AUTHOR_EMAIL = 'nagasaikayithi@gmail.com'
SRC_REPO = 'textSummarizer'


setuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='NLP+Python+Package',
    long_description=decription,
    long_description_content_type="text/markdown",
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls={
        'Bug Tracker': f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues',
    },
    package_dir = {"": "src"}, 
    packages=setuptools.find_packages(where='src'),
)