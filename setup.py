"""Setup file for Log converter module.
"""
from setuptools import setup

PACKAGE_NAME = "sac_log_converter"
py_typed = ["py.typed"]
setup(
    packages={
        f"{PACKAGE_NAME}.Getconfig": py_typed,
        f"{PACKAGE_NAME}.main": py_typed,
        f"{PACKAGE_NAME}.sample": py_typed,
        },
    install_requires=["httpx==0.22.0"],
    setup_requires=["pytest-runner"],
)

 

