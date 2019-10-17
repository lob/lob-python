# lob-python

[![Build Status](https://travis-ci.org/lob/lob-python.svg?branch=master)](https://travis-ci.org/lob/lob-python)
[![PyPI version](https://badge.fury.io/py/lob.svg)](http://badge.fury.io/py/lob)
[![Coverage Status](https://coveralls.io/repos/lob/lob-python/badge.svg?branch=master)](https://coveralls.io/r/lob/lob-python?branch=master)

This is the python wrapper for the Lob.com API. See full Lob.com documentation [here](https://lob.com/docs/python). For best results, be sure that you're using [the latest version](https://lob.com/docs/python#version) of the Lob API and the latest version of the python wrapper.

This library supports active Python releases (i.e., versions which have not reached their end of life), as well as PyPy and PyPy 3.
The currently supported versions include:

* Python 2.7
* Python 3.5
* Python 3.6
* Python 3.7
* PyPy
* PyPy 3

## Table of Contents

- [Getting Started](#getting-started)
  - [Registration](#registration)
  - [Installation](#installation)
  - [Usage](#usage)
- [Examples](#examples)
- [API Documentation](#api-documentation)
- [Testing](#testing)

## Getting Started

Lob Python wrapper works in the object oriented style. That is, to make calls you have to call the method on a class and the return types are python objects. To get a `dict` on any object, you can call the `to_dict()` method of the object.

Here's a general overview of the Lob services available, click through to read more.

- [Postcards API](https://lob.com/products/print-mail/postcards)
- [Letters API](https://lob.com/products/print-mail/letters)
- [Checks API](https://lob.com/products/print-mail/checks)
- [Address Verification API](https://lob.com/products/address-verification)

Please read through the official [API Documentation](#api-documentation) to get a complete sense of what to expect from each endpoint.

### Registration

First, you will need to first create an account at [Lob.com](https://dashboard.lob.com/#/register) and obtain your Test and Live API Keys.

Once you have created an account, you can access your API Keys from the [Settings Panel](https://dashboard.lob.com/#/settings).

### Installation

You can use `pip` to install the package.

```
pip install lob
```

To initialize the wrapper, import `lob` and set the `api_key`

```python
import lob
lob.api_key = 'your-api-key'

// set an api version (optional)
lob.api_version = 'api-version'
```

### Usage

We've provided an example script you can run in examples/ that has examples of how to use the lob-python wrapper with some of our core endpoints.

## Examples

We've provided various examples for you to try out [here](https://github.com/lob/lob-python/tree/master/examples).

There are simple scripts to demonstrate how to create all the core Lob objects (checks, letters, postcards. etc.) as well as more complex examples that utilize other libraries and external files.

## API Documentation

- [Introduction](https://lob.com/docs/python#introduction)
- [Versioning](https://lob.com/docs/python#version)
- [Errors](https://lob.com/docs/python#errors)
- [Rate Limiting](https://lob.com/docs/python#rate-limits)
- [Webhooks](https://lob.com/docs/python#webhooks)
- [Cancellation Windows](https://lob.com/docs/python#cancellation)
- [Scheduled Mailings](https://lob.com/docs/python#scheduled)
- [Metadata](https://lob.com/docs/python#metadata)
- [HTML Templates](https://lob.com/docs/python#templates)
- [Asset URLs](https://lob.com/docs/python#urls)
- **Addresses**
  - [Address Book](https://lob.com/docs/python#addresses)
    - [The Address Object](https://lob.com/docs/python#addresses_object)
    - [Create an Address](https://lob.com/docs/python#addresses_create)
    - [Retrieve an Address](https://lob.com/docs/python#addresses_retrieve)
    - [Delete an Address](https://lob.com/docs/python#addresses_delete)
    - [List all Addresses](https://lob.com/docs/python#addresses_list)
- **US Verification API**
  - [US Verification API](https://lob.com/docs/python#us_verifications)
    - [The US Verification Object](https://lob.com/docs/python#us_verifications_object)
    - [Verify a US Address](https://lob.com/docs/python#us_verifications_create)
    - [The US ZIP Lookup Object](https://lob.com/docs/python#us_zip_lookups_object)
    - [Lookup a US ZIP Code](https://lob.com/docs/python#us_zip_lookups_create)
  - [US Autocompletion API](https://lob.com/docs/python#us_autocompletions)
    - [The US Autocompletion Object](https://lob.com/docs/python#us_autocompletions_object)
    - [Autocomplete a US Address](https://lob.com/docs/python#us_autocompletions_create)
    - [The US Autocompletion Test Environment](https://lob.com/docs/python#us-autocompletions-test-environment)
- **Int'l Verification API**
  - [International Verifications](https://lob.com/docs/python#intl_verifications)
    - [Verify an International Address](https://lob.com/docs/python#intl_verifications_create)
- **Postcards API**
  - [Postcards](https://lob.com/docs/python#postcards)
    - [The Postcard Object](https://lob.com/docs/python#postcards_object)
    - [Create a Postcard](https://lob.com/docs/python#postcards_create)
    - [Retrieve a Postcard](https://lob.com/docs/python#postcards_retrieve)
    - [Cancel a Postcard](https://lob.com/docs/python#postcards_delete)
    - [List all Postcards](https://lob.com/docs/python#postcards_list)
- **Letters API**
  - [Letters](https://lob.com/docs/python#letters)
    - [The Letter Object](https://lob.com/docs/python#letters_object)
    - [Create a Letter](https://lob.com/docs/python#letters_create)
    - [Retrieve a Letter](https://lob.com/docs/python#letters_retrieve)
    - [Cancel a Letter](https://lob.com/docs/python#letters_delete)
    - [List all Letters](https://lob.com/docs/python#letters_list)
- **Checks API**
  - [Checks](https://lob.com/docs/python#checks)
    - [The Check Object](https://lob.com/docs/python#checks_object)
    - [Create a Check](https://lob.com/docs/python#checks_create)
    - [Retrieve a Check](https://lob.com/docs/python#checks_retrieve)
    - [Cancel a Check](https://lob.com/docs/python#checks_delete)
    - [List all Checks](https://lob.com/docs/python#checks_list)
  - [Bank Accounts](https://lob.com/docs/python#bank-accounts)
    - [The Bank Account Object](https://lob.com/docs/python#bankaccounts_object)
    - [Create a Bank Account](https://lob.com/docs/python#bankaccounts_create)
    - [Retrieve a Bank Account](https://lob.com/docs/python#bankaccounts_retrieve)
    - [Delete a Bank Account](https://lob.com/docs/python#bankaccounts_delete)
    - [Verify a Bank Account](https://lob.com/docs/python#bankaccounts_verify)
    - [List all Bank Accounts](https://lob.com/docs/python#bankaccounts_list)
- **Appendix**
  - [API Changelog](https://lob.com/docs/python#changelog)
  - [The Tracking Event Object](https://lob.com/docs/python#tracking_event_object)
  - [Events](https://lob.com/docs/python#events)
  - [HTML Examples](https://lob.com/docs/python#html-examples)
  - [Image Prepping](https://lob.com/docs/python#prepping)
  - [US Verification Details](https://lob.com/docs/python#us_verification_details)

## Testing

lob-python uses [Pipenv](https://docs.pipenv.org/) to manage development environments and dependencies.

You install all the development requirements by running

```shell
$ pipenv install --dev
$ pipenv shell
```

You can run all tests with the command `LOB_API_KEY=YOUR_TEST_API_KEY nosetests` in the main directory.

```shell
$ LOB_API_KEY=YOUR_TEST_API_KEY nosetests
```

## Making Releases

lob-python includes [bumpversion](https://pypi.org/project/bumpversion/) as a development dependency. This
tool should be used when changing the version number, as it will ensure that it's updated correctly and
consistently.

Running bumpversion will increment the specified version part (`major`, `minor`, `patch`), commit the change,
and tag it.

```shell
$ bumpversion <part>
```

After the version has been bumped, you can push the change and tag.

```shell
$ git push origin head
$ git push origin --tags
```

Finally, create the distribution and push it to PyPI using [twine](https://pypi.org/project/twine/).

```shell
$ python setup.py sdist
...
Writing lob-4.0.0/setup.cfg
Creating tar archive
removing 'lob-4.0.0' (and everything under it)
$ twine upload dist/lob-4.0.0.tar.gz
```

---

Copyright &copy; 2013-2019 Lob.com

Released under the MIT License, which can be found in the repository in `LICENSE.txt`.
