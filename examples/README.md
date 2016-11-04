# Python Examples

Here we have put together a hand full of python examples to help get you started. As always feel free to [contact us](https://lob.com/support) directly if you have any questions on implementation.

## Getting started
Before running these examples make sure you are in the `examples/` directory.
```
cd examples/
```

## Examples

### Create letters from CSV

An example showing how to dynamically create sample billing letters with variable data using Lob's [Letter API](https://lob.com/services/letters).

In order to run the program, enter:

```
cd create_letters_from_csv/
python letters.py input.csv
```

### Create postcards from CSV

An example showing how to dynamically create postcards from a CSV using HTML, a custom font, variable data, and Lob's [Postcard API](https://lob.com/services/postcards).

In order to run the program enter:

```
cd create_postcards_from_csv/
python create_postcards_from_csv.py input.csv
```

### Create checks from CSV

An example showing how to dynamically create checks from a CSV with variable data using Lob's [Check API](https://lob.com/services/checks).

In order to run the program enter:

```
cd create_check_from_csv/
python check.py input.csv
```

### Verify addresses from CSV

An example showing how to validate and cleanse a CSV spreadsheet full of shipping addresses using Lob's [Address Verification API](https://lob.com/verification/address).

```
cd verify_addresses_from_csv/
python verify.py input.csv
```

### Create a check
```
python check.py
```

### Create a job
```
python job.py
```

### Create a letter
```
python letter.py
```

### Create a postcard
```
python postcard.py
```
