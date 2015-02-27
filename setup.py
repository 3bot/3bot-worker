# -*- encoding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages
from os.path import join, dirname
import threebot_worker as app


def long_description():
    try:
        return open(join(dirname(__file__), 'README.md')).read()
    except IOError:
        return "LONG_DESCRIPTION Error"

setup(
    name="threebot-worker",
    version=app.__version__,
    description="Worker scripts for the 3bot plattform",
    long_description=long_description(),
    author='arteria GmbH',
    author_email="admin@arteria.ch",
    maintainer_email="renner@arteria.ch",
    url="https://github.com/3bot/3bot-worker",
    packages=find_packages(),
    include_package_data=True,
    install_requires=open('requirements.txt').read().split('\n'),
    scripts=['threebot_worker/threebot-worker'],
)
