# Python Examples

Here we have put together a hand full of python examples to help get you started. Please read through the official [API Documentation](../README.md#api-documentation) to get a complete sense of what to expect from each endpoint. As always, feel free to [contact us](https://lob.com/support) directly if you have any questions on implementation.

## Getting started
Before running these examples make sure you are in the `examples/` directory.
```
cd examples/
```

## Examples

### Create letters from CSV

An example showing how to dynamically create sample billing letters with merge variables using Lob's [Letter API](https://lob.com/services/letters).

In order to run the program, enter:

```
cd create_letters_from_csv/
python letters.py input.csv
```

### Create postcards from CSV

An example showing how to dynamically create postcards from a CSV using HTML, a custom font, merge variables, and Lob's [Postcard API](https://lob.com/services/postcards).

In order to run the program enter:

```
cd create_postcards_from_csv/
python create_postcards_from_csv.py input.csv
```

### Create checks from CSV

An example showing how to dynamically create checks from a CSV with merge variables using Lob's [Check API](https://lob.com/services/checks).

In order to run the program enter:

```
cd create_check_from_csv/
python check.py input.csv
```

### Verify US Addresses from CSV

An example showing how to validate and cleanse a CSV spreadsheet full of shipping addresses using Lob's [US Verification API](https://lob.com/services/verifications).

Please note that if you are running this with a Test API Key, the verification API will always return [a dummy address](https://lob.com/docs#us_verifications_create).

```
cd verify_addresses_from_csv/
python verify.py input.csv
```

### Create a check
```
python check.py
```

### Create a letter
```
python letter.py
```

### Create a postcard
```
python postcard.py
```

### Create a self mailer
```
python self_mailer.py
```

### Create a card
```
python create_card.py
```

### Create a card order
```
python create_card_order.py
```
