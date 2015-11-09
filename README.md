# lob-python

[![Build Status](https://travis-ci.org/lob/lob-python.svg?branch=master)](https://travis-ci.org/lob/lob-python)
[![PyPI version](https://badge.fury.io/py/lob.svg)](http://badge.fury.io/py/lob) [![Downloads](https://pypip.in/download/lob/badge.svg)](https://pypi.python.org/pypi/lob/)
[![Coverage Status](https://coveralls.io/repos/lob/lob-python/badge.svg?branch=master)](https://coveralls.io/r/lob/lob-python?branch=master)
[![Dependency Status](https://gemnasium.com/lob/lob-python.svg)](https://gemnasium.com/lob/lob-python)

This is the python wrapper for the Lob.com API. See full Lob.com documentation [here](https://lob.com/docs/python). For best results, be sure that you're using [the latest version](https://lob.com/docs/python#version) of the Lob API and the latest version of the python wrapper.

This wrapper supports Python 2.6, 2.7, 3.2, 3.3, and 3.4 and works in the object oriented style. That is, to make calls you have to call the method on a class and the return types are python objects. To get a `dict` on any object, you can call the `to_dict()` method of the object.

## Table of Contents

- [Getting Started](#getting-started)
  - [Registration](#registration)
  - [Installation](#installation)
  - [Usage](#usage)
- [Examples](#examples)
- [API Documentation](#api-documentation)
- [Testing](#testing)

## Getting Started

Here's a general overview of the Lob services available, click through to read more.

- [Postcards API](https://lob.com/services/postcards)
- [Letters API](https://lob.com/services/letters)
- [Checks API](https://lob.com/services/checks)
- [Prints API](https://lob.com/services/sps)
- [Area Mail API](https://lob.com/services/sam)
- [Address Verification API](https://lob.com/verification/address)

### Registration

First, you will need to first create an account at [Lob.com](https://dashboard.lob.com/#/register) and obtain your Test and Live API Keys.

Once you have created an account, you can access your API Keys from the [Settings Panel](https://dashboard.lob.com/#/settings).

### Installation

You can use `pip` or `easy_install` for installing the package.

```
pip install lob
easy_install lob
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

There are simple scripts to demonstrate how to create all the core Lob objects (checks, letters, postcards. etc.) As well as more complex examples that utilize other libraries and external files:

- [Verifying and Creating Letters from CSV](https://github.com/lob/lob-python/blob/master/examples/verify_and_create_letters_from_csv/letter.py)
- [Verifying Addresses in a CSV](https://github.com/lob/lob-python/blob/master/examples/verify_addresses_from_csv/verify_addresses_from_csv.py)
- [Creating Dynamic Postcards with HTML and Data](https://github.com/lob/lob-python/blob/master/examples/create_postcards_from_csv/create_postcards_from_csv.py)

## API Documentation

- [Introduction](https://lob.com/docs/python#introduction)
- [Authentication](https://lob.com/docs/python#auth)
- [Versioning](https://lob.com/docs/python#version)
- [Errors](https://lob.com/docs/python#errors)
- [Rate Limiting](https://lob.com/docs/python#rate-limits)
- [Metadata](https://lob.com/docs/python#metadata)
- **Addresses**
  - [Address Book](https://lob.com/docs/python#addresses)
    - [Create an Address](https://lob.com/docs/python#addresses_create)
    - [Retrieve an Address](https://lob.com/docs/python#addresses_retrieve)
    - [Delete an Address](https://lob.com/docs/python#addresses_delete)
    - [List all Addresses](https://lob.com/docs/python#addresses_list)
  - [Address Verification API](https://lob.com/docs/python#verify)
    - [Verify an Address](https://lob.com/docs/python#verify_create)
- **Postcards API**
  - [Postcards](https://lob.com/docs/python#postcards)
    - [Create a Postcard](https://lob.com/docs/python#postcards_create)
    - [Retrieve a Postcard](https://lob.com/docs/python#postcards_retrieve)
    - [List all Postcards](https://lob.com/docs/python#postcards_list)
- **Letters API**
  - [Letters](https://lob.com/docs/python#letters)
    - [Create a Letter](https://lob.com/docs/python#letters_create)
    - [Retrieve a Letter](https://lob.com/docs/python#letters_retrieve)
    - [List all Letters](https://lob.com/docs/python#letters_list)
- **Checks API**
  - [Checks](https://lob.com/docs/python#checks)
    - [Create a Check](https://lob.com/docs/python#checks_create)
    - [Retrieve a Check](https://lob.com/docs/python#checks_retrieve)
    - [List all Checks](https://lob.com/docs/python#checks_list)
  - [Bank Accounts](https://lob.com/docs/python#bank-accounts)
    - [Create a Bank Account](https://lob.com/docs/python#bankaccounts_create)
    - [Retrieve a Bank Account](https://lob.com/docs/python#bankaccounts_retrieve)
    - [Delete a Bank Account](https://lob.com/docs/python#bankaccounts_delete)
    - [Verify a Bank Account](https://lob.com/docs/python#bankaccounts_verify)
    - [List all Bank Accounts](https://lob.com/docs/python#bankaccounts_list)
- **Prints API**
  - [Jobs](https://lob.com/docs/python#jobs)
    - [Create a Job](https://lob.com/docs/python#jobs_create)
    - [Create a MultiObject Job](https://lob.com/docs/python#jobs_multi)
    - [Retrieve a Job](https://lob.com/docs/python#jobs_retrieve)
    - [List all Jobs](https://lob.com/docs/python#jobs_list)
  - [Objects](https://lob.com/docs/python#objects)
    - [Create an Object](https://lob.com/docs/python#objects_create)
    - [Retrieve an Object](https://lob.com/docs/python#objects_retrieve)
    - [Delete an Object](https://lob.com/docs/python#objects_delete)
    - [List all Objects](https://lob.com/docs/python#objects_list)
  - [Settings](https://lob.com/docs/python#settings)
    - [Retrieve a Setting](https://lob.com/docs/python#settings_retrieve)
    - [List all Settings](https://lob.com/docs/python#settings_list)
- **Area Mail API**
  - [Areas](https://lob.com/docs/python#areas)
    - [Create an Area Mailing](https://lob.com/docs/python#areas_create)
    - [Retrieve an Area Mailing](https://lob.com/docs/python#areas_retrieve)
    - [List all Area Mailings](https://lob.com/docs/python#areas_list)
  - [Routes](https://lob.com/docs/python#routes)
    - [Retrieve a Zip Code](https://lob.com/docs/python#routes_retrieve)
    - [List all Zip Codes](https://lob.com/docs/python#routes_list)
- **Resources**
  - [Countries](https://lob.com/docs/python#countries)
    - [List all Countries](https://lob.com/docs/python#countries_list)
  - [States](https://lob.com/docs/python#states)
    - [List all States](https://lob.com/docs/python#states_list)
- **Appendix**
  - [API Changelog](https://lob.com/docs/python#changelog)
  - [HTML Examples](https://lob.com/docs/python#html-examples)
  - [Image Prepping](https://lob.com/docs/python#prepping)
  - [Prints API Templates](https://lob.com/docs/python#prints-templates)

## Testing

Install all requirements with `pip install -r requirements.txt`.

You can run all tests with the command `nosetests` in the main directory.

=======================

Copyright &copy; 2013 Lob.com

Released under the MIT License, which can be found in the repository in `LICENSE.txt`.
