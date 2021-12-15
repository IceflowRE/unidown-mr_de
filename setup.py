#!/usr/bin/env python
from pathlib import Path

from setuptools import find_packages, setup

from unidown_mr_de import meta

# get long description
with Path('README.rst').open(mode='r', encoding='UTF-8') as reader:
    LONG_DESCRIPTION = reader.read()

setup(
    name=meta.NAME,
    version=meta.VERSION,
    description=meta.DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/x-rst',
    author=meta.AUTHOR,
    author_email=meta.AUTHOR_EMAIL,
    license=meta.LICENSE,
    url=meta.PROJECT_URL,
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Natural Language :: German',
        'Environment :: Console',
    ],
    keywords='plugin unidown',
    packages=find_packages(include=['unidown_mr_de', 'unidown_mr_de.*']),
    python_requires='>=3.8',
    install_requires=[
        'unidown==2.0.2',
        'urllib3[secure]>=1.26.7',
        'tqdm>=4.62.3',
        'beautifulsoup4==4.10.0',
        'lxml==4.7.1',
        'certifi',
    ],
    extras_require={
        'dev': [
            'flake8==4.0.1',
            'pylint==2.12.2',
            'pyroma==3.2',
            'twine==3.7.1',
            'setuptools==59.6.0',
            'wheel==0.37.0',
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
