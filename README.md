# Sac Log Converter


Sac Log converter is a re-usable module which is developed to convert any log datas from LEEF format into Json format
and also Json format into LEEF format .


By using this module one can easily convert the data from one format to another format in a minimum amount of time.

## Requirements
python 3.6

## Installation

*Install from source*
- Pull the latest code from the source.

    > https://github.com/pranav-sacumen/sac_log_converter

- Enable a virtual environment
- Use the below command to install required packages in the virtual environment

    > pip install -r requirements.txt

## Usage

"""Utility functions to be used by logger module."""
import os
from configparser import ConfigParser
from pathlib import Path
from typing import Any, Dict, List


def to_dict(config: ConfigParser) -> Dict[str, Any]:
    """Convert a ConfigParser object into a dictionary.

    The resulting dictionary has sections as keys which point to a dict of the
    sections options as key => value pairs.
    """
    config_dict: Dict[str, Any] = {}
    for section in config.sections():
        config_dict[section] = {}
        for key, val in config.items(section):
            config_dict[section][key] = val
    return config_dict


## Generate code documentations

To generate code documentation, `sphinx` is required.

To generate documentation for Sac Requests, perform following steps:

1. Create a virtual environment
2. Enable virtual environment
3. Install required libraries from `requirements.txt`.
4. Install required doc generator modules from `docs_requirements.txt`.
5. Provide configurations in `documentation.cfg` file present within `config` directory.
6. Run `doc_generator.py` file.
shell
python doc_generator.py


This will create code documentation in html format at `docs/_build/html` directory.
