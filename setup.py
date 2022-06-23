"""Setup file for Log converter module."""
from setuptools import setup

PACKAGE_NAME = "sac_log_converter"
py_typed = ["py.typed"]

setup(
    packages={
        f"{PACKAGE_NAME}": py_typed,
        f"{PACKAGE_NAME}.converter": py_typed,
        f"{PACKAGE_NAME}.LeefToJSON": py_typed,
        f"{PACKAGE_NAME}.exceptions": py_typed,
        f"{PACKAGE_NAME}.utils": py_typed
    },
    setup_requires=["pytest-runner"]
)
