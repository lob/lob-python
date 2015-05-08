# lob-python

[![Build Status](https://travis-ci.org/lob/lob-python.svg?branch=master)](https://travis-ci.org/lob/lob-python)
[![PyPI version](https://badge.fury.io/py/lob.svg)](http://badge.fury.io/py/lob) [![Downloads](https://pypip.in/download/lob/badge.svg)](https://pypi.python.org/pypi/lob/)
[![Coverage Status](https://coveralls.io/repos/lob/lob-python/badge.svg?branch=master)](https://coveralls.io/r/lob/lob-python?branch=master)
[![Dependency Status](https://gemnasium.com/lob/lob-python.svg)](https://gemnasium.com/lob/lob-python)

This is the python wrapper for the Lob.com API. See full Lob.com documentation [here](https://lob.com/docs/python).

This wrapper works in the object oriented style, that is, to make calls you have to call the method on a class and the
return types are python objects. To get a `dict` on any object, you can call the `to_dict()` method of the object.

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

- [Simple Postcard Service](https://lob.com/services/postcards)
- [Simple Letter Service](https://lob.com/services/letters)
- [Simple Check Service](https://lob.com/services/checks)
- [Simple Print Service](https://lob.com/services/sps)
- [Simple Area Mail](https://lob.com/services/sam)
- [Address Verification](https://lob.com/verification/address)

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

- [Verifying Addresses in a CSV](https://github.com/lob/lob-python/tree/master/examples/csv_address_verification)
- [Creating Dynamic Postcards with HTML and Data](https://github.com/lob/lob-python/tree/master/examples/csv_postcards)

## API Documentation

- [Introduction](https://lob.com/docs/python#introduction)
- [Versioning](https://lob.com/docs/python#version)
- [Image Prepping](https://lob.com/docs/python#prepping)
- **Addresses**
  - [Address Book](https://lob.com/docs/python#addresses)
    - [Create an Address](https://lob.com/docs/python#addresses_create)
    - [Retrieve an Address](https://lob.com/docs/python#addresses_retrieve)
    - [Delete an Address](https://lob.com/docs/python#addresses_delete)
    - [List all Addresses](https://lob.com/docs/python#addresses_list)
  - [Simple Address Verification](https://lob.com/docs/python#verify)
    - [Verify an Address](https://lob.com/docs/python#verify_create)
- **Simple Postcard Service**
  - [Postcards](https://lob.com/docs/python#postcards)
    - [Create a Postcard](https://lob.com/docs/python#postcards_create)
    - [Retrieve a Postcard](https://lob.com/docs/python#postcards_retrieve)
    - [List all Postcards](https://lob.com/docs/python#postcards_list)
- **Simple Letter Service**
  - [Letters](https://lob.com/docs/python#letters)
    - [Create a Letter](https://lob.com/docs/python#letters_create)
    - [Retrieve a Letter](https://lob.com/docs/python#letters_retrieve)
    - [List all Letters](https://lob.com/docs/python#letters_list)
- **Simple Check Service**
  - [Checks](https://lob.com/docs/python#checks)
    - [Create a Check](https://lob.com/docs/python#checks_create)
    - [Retrieve a Check](https://lob.com/docs/python#checks_retrieve)
    - [List all Checks](https://lob.com/docs/python#checks_list)
  - [Bank Accounts](https://lob.com/docs/python#bank-accounts)
    - [Create a Bank Account](https://lob.com/docs/python#bankaccounts_create)
    - [Retrieve a Bank Account](https://lob.com/docs/python#bankaccounts_retrieve)
    - [List all Bank Accounts](https://lob.com/docs/python#bankaccounts_list)
    - [Verify a Bank Account](https://lob.com/docs/python#bankaccounts_verify)
    - [Delete a Bank Account](https://lob.com/docs/python#bankaccounts_delete)
- **Simple Print Service**
  - [Jobs](https://lob.com/docs/python#jobs)
    - [Create a Job](https://lob.com/docs/python#jobs_create)
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
- **Simple Area Mail**
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
  - [SPS Templates](https://lob.com/docs/python#sps-templates)
  - [Custom Fonts with HTML](https://lob.com/docs/python#html-fonts)
  - [Postcard HTML Examples](https://lob.com/docs/python#postcard-examples)
  - [Area HTML Examples](https://lob.com/docs/python#area-examples)
  - [Letter HTML Examples](https://lob.com/docs/python#letter-examples)

## Testing

Install all requirements with `pip install -r requirements.txt`.

You can run all tests with the command `nosetests` in the main directory.

=======================

Copyright &copy; 2013 Lob.com

Released under the MIT License, which can be found in the repository in `LICENSE.txt`.
