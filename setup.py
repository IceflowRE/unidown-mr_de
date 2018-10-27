#!/usr/bin/env python
from pathlib import Path

from setuptools import find_packages, setup

# get long description
with Path('README.rst').open(mode='r', encoding='UTF-8') as reader:
    long_description = reader.read()

setup(
    name='unidown-mr_de',
    version='1.0.0.dev1',
    description='MR german books plugin for unidown.',
    long_description=long_description,
    author='Iceflower S',
    author_email='iceflower@gmx.de',
    license='GPLv3',
    url='https://github.com/IceflowRE/unidown-mr_de',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Natural Language :: German',
        'Environment :: Console',
    ],
    keywords='plugin unidown',
    packages=find_packages(include=['unidown_mr_de', 'unidown_mr_de.*']),
    python_requires='>=3.7',
    install_requires=[
        'unidown==2.0.0.dev6',
        'urllib3[secure]==1.24',
        'tqdm==4.28.1',
    ],
    extras_require={
        'dev': [
            'prospector[with_everything]==1.1.4',
            'nose2[coverage_plugin]==0.8.0',
            'twine==1.12.1',
            'setuptools==40.4.3',
            'wheel==0.32.1',
            'pygments==2.2.0'
        ]
    },
    package_data={

    },
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'unidown.plugin': "mr_de = unidown_mr_de.plugin:Plugin"
    },
)
