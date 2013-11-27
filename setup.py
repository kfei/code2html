import re
import sys

pkg_file = open("code2html/__init__.py").read()
metadata = dict(re.findall("__([a-z]+)__\s*=\s*'([^']+)'", pkg_file))
description = open('README.rst').read()

from setuptools import setup, find_packages

install_requires = []
pyversion = sys.version_info[:2]
if pyversion < (2, 7) or (3, 0) <= pyversion <= (3, 1):
    install_requires.append('argparse')

setup(
    name='code2html',
    description='Convert source code repository to HTML,'
                ' with beautiful syntax highlight.',
    packages=find_packages(),
    author='Lin, Ke-fei',
    author_email='kfei@kfei.net',
    version=metadata['version'],
    url='http://github.com/kfei/code2html',
    license="MIT",
    keywords="code, syntax, highlight, convert, html",
    long_description=description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ],

    install_requires=[
        'setuptools',
        ] + install_requires,

    entry_points={
        'console_scripts': [
            'code2html = code2html.cli:main'
        ]
    }
)
