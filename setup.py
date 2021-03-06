import setuptools
import sys
import os


sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'coinflip'))
from version import VERSION as __version__

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='coinflip',
    version=__version__,
    author='Christian Lang',
    author_email='me@christianlang.io',
    description='A bot for choosing between games.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/christianwlang/coinflip',
    download_url='https://pypi.org/project/coinflip/',
    project_urls={
        'Documentation': 'https://capture-the-flag.readthedocs.io/en/latest/',
        'Source': 'https://github.com/documentedai/capture-the-flag',
        'Tracker': 'https://github.com/documentedai/capture-the-flag/issues'
    },
    packages=setuptools.find_packages(),
    include_package_data=True,
    license='BSD',
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'flake8'],
        'docs': ['sphinx']
    },
    install_requires=[
        'numpy',
        'discord.py'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ]
)
