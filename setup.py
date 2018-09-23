#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    author="Simone Marzola",
    author_email='marzolasimone@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="MongoDB connector for BI SQLAlchemy Dialect",
    install_requires=[
        'sqlalchemy',
    ],
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='sqlalchemy mongodb',
    name='sqlalchemy_mongobi',
    packages=find_packages(include=['sqlalchemy_mongobi']),
    test_suite='tests',
    url='https://github.com/smarzola/sqlalchemy-mongobi',
    version='0.2.1',
    zip_safe=False,
    entry_points={
        'sqlalchemy.dialects': [
            'mongobi = sqlalchemy_mongobi.dialect:MongoBIDialect_mysqldb',
            'mongobi.mysqldb = sqlalchemy_mongobi.dialect:MongoBIDialect_mysqldb',
            'mongobi.pymysql = sqlalchemy_mongobi.dialect:MongoBIDialect_pymysql',
        ]
    },
)
