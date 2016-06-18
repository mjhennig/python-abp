# This file is part of Adblock Plus <https://adblockplus.org/>,
# Copyright (C) 2006-2016 Eyeo GmbH
#
# Adblock Plus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# Adblock Plus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Adblock Plus.  If not, see <http://www.gnu.org/licenses/>.

import subprocess
from os import path
from setuptools import setup, Command


DEVENV = 'devenv'
PIP = path.join(DEVENV, 'bin', 'pip')


class DevEnvCommand(Command):
    """Set up development virtualenv."""

    description = 'set up development virtualenv'
    user_options = [('python=', 'p', 'the python interpreter to use')]

    def initialize_options(self):
        self.python = 'python'
        self.source = path.dirname(path.realpath(__file__))

    def finalize_options(self):
        self.requirements = path.join(self.source, 'requirements-dev.txt')

    def run(self):
        subprocess.check_call(['virtualenv', '-p', self.python, DEVENV])
        subprocess.check_call([PIP, 'install', '-r', self.requirements])
        subprocess.check_call([PIP, 'install', '-e', '.'])


setup(
    name='python-abp',
    version='0.0.1',
    description='ABP python tools',
    long_description='A library for working with Adblock Plus filter lists.',
    author='Eyeo GmbH',
    author_email='info@adblockplus.org',
    url='https://hg.adblockplus.org/python-abp/',
    packages=['abp', 'abp.filters'],
    cmdclass={'devenv': DevEnvCommand},
    entry_points={
        'console_scripts': ['flrender=abp.filters.render_script:main']
    },
    include_package_data=True,
    license='GPLv3',
    zip_safe=False,
    keywords='filterlist adblockplus ABP',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ]
)
