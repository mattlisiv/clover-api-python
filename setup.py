#!/usr/bin/env python

from setuptools import setup, find_packages

install_requires = [
    'requests>=2.20.0'
]

tests_require = [
    'pytest',
    ]

setup(
    name='cloverapi-python',
    version='0.0.3',
    author='Matt Lisivick',
    author_email='lisivickmatt@gmail.com',
    license='MIT',
    url='https://github.com/mattlisiv/clover-api-python',
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=tests_require,
    description='An unofficial Python client for the Clover API v3',
    download_url='https://github.com/mattlisiv/clover-api-python/archive/master.zip',
    keywords=['clover','api'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Information Technology',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
