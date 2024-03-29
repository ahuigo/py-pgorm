#!/usr/bin/env python
from os import path as op
from setuptools import setup

# example: https://github.com/pypa/sampleproject
def _read(fname='readme.md', line=None):
    try:
        if line is None:
            return open(op.join(op.dirname(__file__), fname)).read()
        return open(op.join(op.dirname(__file__), fname)).readlines()[line].strip()
    except IOError:
        return ''

name = 'py-pgorm'
setup(
    name=name,
    version=open('version').read().strip(),
    author="ahuigo",
    author_email="ahui132@qq.com",
    license="MIT",
    url=f"http://github.com/ahuigo/{name}",

    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, package_dir={'': 'src'},  # Optional
    package_dir={"": "."},
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #   from setuptools import setup, find_packages
    #   packages=find_packages(where='src'),  # Required
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=[],
    py_modules=['pgorm'],

    #scripts=['pgorm'], # 命令pgorm 指向pgorm 中的main

    # dependencies
    python_requires='>=3.6.1',
    install_requires=['psycopg2-binary>=2.9.9'],


    description="simple postgres orm for python",
    long_description=_read(),
    long_description_content_type="text/markdown",
    keywords='orm, python, postgres',  # Optional

    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    #
    #   extras_require={  # Optional
    #       'dev': ['check-manifest'],
    #       'test': ['coverage'],
    #   },

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    #   package_data={  # Optional 
    #       'sample': ['package_data.dat'], # root/src/sample/package_data.dat
    #   },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # 
    #   data_files=[('my_data', ['data/data_file'])],  # Optional


)
