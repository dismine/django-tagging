# Copyright (c) 2008, Donovan Preston
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from os import path

from setuptools import find_packages, setup


setup(
    name='Spawning',
    description='Spawning is a wsgi server which supports multiple processes, multiple threads, green threads, non-blocking HTTP io, and automatic graceful upgrading of code.',
    long_description=file(
        path.join(
            path.dirname(__file__),
            'README.txt'
        )
    ).read(),
    author='Donovan Preston',
    author_email='dsposx@mac.com',
    include_package_data = True,
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    version='0.9.3pre',
    install_requires=['eventlet', 'simplejson', 'PasteDeploy'],
    entry_points={
        'console_scripts': [
            'spawn=spawning.spawning_controller:main',
        ],
        'paste.server_factory': [
            'main=spawning.paste_factory:server_factory'
        ]
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta"
    ]
)

