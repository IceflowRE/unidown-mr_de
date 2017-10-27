#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='unidown-plugins-mr-de',
    version='1.0.0',
    description='MR German plugin for Universal downloader.',
    author='Iceflower S',
    author_email='iceflower@gmx.de',
    license='GPLv3',
    url='https://github.com/IceflowRE/unidown-mr_de',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Natural Language :: Deutsch',
    ],
    keywords='plugin',
    packages=find_packages(),
    install_requires=[  # TODO: use only unidown as require
        'urllib3',
        'certifi',
        'tqdm',
        'protobuf',
    ],
    extras_require={
        'dev': [
            'prospector[with_everything]',
            'cov-core',
            'codecov',
            'nose2',
            'Sphinx',
            'wheel',
        ]
    },
    package_data={

    },
    include_package_data=True,
)
