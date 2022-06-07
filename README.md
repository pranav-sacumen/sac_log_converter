# Sac Request


sac_request is a Python wrapper of python requests module which can be
used to perform the http/https requests.

Supported Authentication methods in Sac request module.
1. Open urls
2. Basic Authentication
3. Token based authentication

## Requirements
python 3.6

## Installation

*Install from source*
- Pull the latest code from the source.

    > https://github.com/nitesh-sacumen/sac_requests

- Enable a virtual environment
- Use the below command to install required packages in the virtual environment

    > pip install -r requirements.txt

## Usage
### General HttpRequest Configuration.

python
from context.config import HttpConfig
from context.headers import HttpHeaders
from context.request import HttpRequest
from context.url import HttpURL

http_config = HttpConfig(
    time_out=5,
    retry_interval=1,
    status_force_list=[429, 500, 502, 503, 504],
    max_retry=3,
    auth_type="NO_AUTH",
)
http_url = HttpURL(host="www.google.com", protocol="https", port=3306)

headers = HttpHeaders({
    "content_type" : "application/json"
})
http_request = HttpRequest(headers=headers, url=http_url,
                           config=http_config)

* `HttpConfig()` keep the settings related to request Session like timeout, max-retries etc.
* `HttpURL()` create the base url which contains the host, port and protocol.
* `HttpHeaders()` keep the default headers that needs to be used for all request.
* `HttpRequest()` creates thea request handler to perform the http/https requests.

### Configure Basic Authentication
To use the basic authentication auth_type need to be set as BASIC_AUTH.
Also, We need to pass the auth params in the request method.
python
from context.config import HttpConfig

http_config = HttpConfig(
    auth_type="BASIC_AUTH",
)

* `auth_type="BASIC_AUTH"` Indicates that the request will use the basic authentication. To use the basic authentication we have to pass the auth params in every request.

### Configure Token Bases Authentication
To use the basic authentication auth_type need to be set as BASIC_AUTH.
Also, We need to pass the auth params in the request method.
python
from context.config import HttpConfig

http_config = HttpConfig(
    auth_type="BEARER_TOKEN",
)

* `auth_type="BEARER_TOKEN"` Indicates that the request will use the token based authentication. To use the token authentication we have to pass the auth "Authorization" in request headers.

## Example

### Get request
It demonstrates the use the sac_request module to fetch the
public repository of bitbucket.

python
from constants.general import HTTPS
from context.config import HttpConfig
from context.headers import HttpHeaders
from context.request import HttpRequest
from context.url import HttpURL


config = HttpConfig() #Loads Default Configuration
http_url = HttpURL(
    host="api.bitbucket.org",
    protocol=HTTPS,
)
headers = HttpHeaders({})
endpoint = "/2.0/repositories"
http_request = HttpRequest(headers=headers, url=http_url, config=config)

response = http_request.get(endpoint=endpoint)


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
