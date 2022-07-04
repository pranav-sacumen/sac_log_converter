"""Setup file for Log converter module."""
from setuptools import setup

PACKAGE_NAME = "sac_log_converter"
py_typed = ["py.typed"]

setup(
    packages={
        f"{PACKAGE_NAME}": py_typed,
        f"{PACKAGE_NAME}.constants": py_typed,
        # f"{PACKAGE_NAME}.": py_typed,
        # f"{PACKAGE_NAME}.get_config.py": py_typed,
        # f"{PACKAGE_NAME}.leef_to_json.oy": py_typed,
        # f"{PACKAGE_NAME}.utils.py": py_typed
    },
    setup_requires=["pytest-runner"]
)
