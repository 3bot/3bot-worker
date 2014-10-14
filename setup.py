# -*- encoding: utf-8 -*-

from setuptools import setup
import threebot_worker as app

setup(
    name="threebot-worker",
    author_email="admin@arteria.ch",
    maintainer_email="renner@arteria.ch",
    version=app.__version__,

    install_requires=[
        "pyzmq",
        "threebot-crypto",
    ],
)
