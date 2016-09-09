# lob-python

[![Build Status](https://travis-ci.org/lob/lob-python.svg?branch=master)](https://travis-ci.org/lob/lob-python)
[![PyPI version](https://badge.fury.io/py/lob.svg)](http://badge.fury.io/py/lob)
[![Coverage Status](https://coveralls.io/repos/lob/lob-python/badge.svg?branch=master)](https://coveralls.io/r/lob/lob-python?branch=master)
[![Dependency Status](https://gemnasium.com/lob/lob-python.svg)](https://gemnasium.com/lob/lob-python)

This is the python wrapper for the Lob.com API. See full Lob.com documentation [here](https://lob.com/docs/python). For best results, be sure that you're using [the latest version](https://lob.com/docs/python#version) of the Lob API and the latest version of the python wrapper.

This wrapper supports Python 2.6, 2.7, 3.3, 3.4, 3.5, pypy, and pypy3 and works in the object oriented style. That is, to make calls you have to call the method on a class and the return types are python objects. To get a `dict` on any object, you can call the `to_dict()` method of the object.

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
- [Area Mail API](https://lob.com/services/area)
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

- [Verifying and Creating Letters from CSV](https://github.com/lob/lob-python/tree/master/examples#create-letters-from-csv)
- [Verifying Addresses in a CSV](https://github.com/lob/lob-python/tree/master/examples#verify-addresses-from-csv)
- [Creating Dynamic Postcards with HTML and Data](https://github.com/lob/lob-python/tree/master/examples#create-postcards-from-csv)

## API Documentation

- [Introduction](https://lob.com/docs/python#introduction)
- [Versioning](https://lob.com/docs/python#version)
- [Errors](https://lob.com/docs/python#errors)
- [Rate Limiting](https://lob.com/docs/python#rate-limits)
- [Metadata](https://lob.com/docs/python#metadata)
- [Asset URLs](https://lob.com/docs/python#urls)
- **Addresses**
  - [Address Book](https://lob.com/docs/python#addresses)
    - [The Address Object](https://lob.com/docs/python#addresses_object)
    - [Create an Address](https://lob.com/docs/python#addresses_create)
    - [Retrieve an Address](https://lob.com/docs/python#addresses_retrieve)
    - [Delete an Address](https://lob.com/docs/python#addresses_delete)
    - [List all Addresses](https://lob.com/docs/python#addresses_list)
  - [Address Verification API](https://lob.com/docs/python#verify)
    - [Verify an Address](https://lob.com/docs/python#verify_create)
- **Postcards API**
  - [Postcards](https://lob.com/docs/python#postcards)
    - [The Postcard Object](https://lob.com/docs/python#postcards_object)
    - [Create a Postcard](https://lob.com/docs/python#postcards_create)
    - [Retrieve a Postcard](https://lob.com/docs/python#postcards_retrieve)
    - [List all Postcards](https://lob.com/docs/python#postcards_list)
- **Letters API**
  - [Letters](https://lob.com/docs/python#letters)
    - [The Letter Object](https://lob.com/docs/python#letters_object)
    - [Create a Letter](https://lob.com/docs/python#letters_create)
    - [Retrieve a Letter](https://lob.com/docs/python#letters_retrieve)
    - [List all Letters](https://lob.com/docs/python#letters_list)
- **Checks API**
  - [Checks](https://lob.com/docs/python#checks)
    - [The Check Object](https://lob.com/docs/python#checks_object)
    - [Create a Check](https://lob.com/docs/python#checks_create)
    - [Retrieve a Check](https://lob.com/docs/python#checks_retrieve)
    - [List all Checks](https://lob.com/docs/python#checks_list)
  - [Bank Accounts](https://lob.com/docs/python#bank-accounts)
    - [The Bank Account Object](https://lob.com/docs/python#bankaccounts_object)
    - [Create a Bank Account](https://lob.com/docs/python#bankaccounts_create)
    - [Retrieve a Bank Account](https://lob.com/docs/python#bankaccounts_retrieve)
    - [Delete a Bank Account](https://lob.com/docs/python#bankaccounts_delete)
    - [Verify a Bank Account](https://lob.com/docs/python#bankaccounts_verify)
    - [List all Bank Accounts](https://lob.com/docs/python#bankaccounts_list)
- **Area Mail API**
  - [Areas](https://lob.com/docs/python#areas)
    - [The Area Object](https://lob.com/docs/python#areas_object)
    - [Create an Area Mailing](https://lob.com/docs/python#areas_create)
    - [Retrieve an Area Mailing](https://lob.com/docs/python#areas_retrieve)
    - [List all Area Mailings](https://lob.com/docs/python#areas_list)
  - [Routes](https://lob.com/docs/python#routes)
    - [The Routes Object](https://lob.com/docs/python#routes_object)
    - [Retrieve Routes](https://lob.com/docs/python#routes_retrieve)
    - [List all Routes](https://lob.com/docs/python#routes_list)
- **Resources**
  - [Countries](https://lob.com/docs/python#countries)
    - [List all Countries](https://lob.com/docs/python#countries_list)
  - [States](https://lob.com/docs/python#states)
    - [List all States](https://lob.com/docs/python#states_list)
- **Appendix**
  - [API Changelog](https://lob.com/docs/python#changelog)
  - [The Tracking Event Object](https://lob.com/docs/python#tracking_event_object)
  - [HTML Examples](https://lob.com/docs/python#html-examples)
  - [Image Prepping](https://lob.com/docs/python#prepping)

## Testing

Install all requirements with `pip install -r requirements.txt`.

You can run all tests with the command `nosetests` in the main directory.

=======================

Copyright &copy; 2013 Lob.com

Released under the MIT License, which can be found in the repository in `LICENSE.txt`.
