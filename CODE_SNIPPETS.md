# Code Snippets

## Address Api

### Retrieve
```bash
curl https://api.lob.com/v1/addresses/adr_fa85158b26c3eb7c \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = AddressesApi(api_client)

try:
  address = api.get("adr_fa85158b26c3eb7c")
except ApiException as e:
  print(e)
```







### Delete
```bash
curl -X DELETE "https://api.lob.com/v1/addresses/adr_43769b47aed248c2" \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = AddressesApi(api_client)

try:
  deleted_resource = api.delete("adr_43769b47aed248c2")
except ApiException as e:
  print(e)
```


### Create
```bash
curl https://api.lob.com/v1/addresses \
  
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
```

```python
address_editable = AddressEditable(
  description = "Harry - Office",
  name = "Harry Zhang",
  company = "Lob",
  email = "harry@lob.com",
  phone = "5555555555",
  address_line1 = "210 King St",
  address_line2 = "# 6100",
  address_city = "San Francisco",
  address_state = "CA",
  address_zip = "94107",
  address_country = CountryExtended("US"),
)

with ApiClient(configuration) as api_client:
  api = AddressesApi(api_client)

try:
  created_address = api.create(address_editable)
except ApiException as e:
  print(e)
```





### List
```bash
curl -X GET "https://api.lob.com/v1/addresses?limit=2" \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = AddressesApi(api_client)

try:
  addresses = api.list(limit=2)
except ApiException as e:
  print(e)
```










































## Postcards Api

### Retrieve
```bash
curl https://api.lob.com/v1/postcards/psc_5c002b86ce47537a \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = PostcardsApi(api_client)

try:
  postcard = api.get("psc_5c002b86ce47537a")
except ApiException as e:
  print(e)
```







### Delete
```bash
curl -X DELETE "https://api.lob.com/v1/postcards/psc_5c002b86ce47537a" \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = PostcardsApi(api_client)

try:
  deleted_resource = api.cancel("psc_5c002b86ce47537a")
except ApiException as e:
  print(e)
```


### Create
```bash
curl https://api.lob.com/v1/postcards \
  
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
```

```python
postcard_editable = PostcardEditable(
  description = "Demo Postcard job",
  _from = "adr_210a8d4b0b76d77b",
  front = "<html style='padding: 1in; font-size: 50;'>Front HTML for {{name}}</html>",
  back = "<html style='padding: 1in; font-size: 20;'>Back HTML for {{name}}</html>",
  to = AddressEditable(
    name = "Harry Zhang",
    address_line1 = "210 King St",
    address_line2 = "# 6100",
    address_city = "San Francisco",
    address_state = "CA",
    address_zip = "94107",
  ),
  merge_variables = MergeVariables(
    name = "Harry",
  ),
)

with ApiClient(configuration) as api_client:
  api = PostcardsApi(api_client)

try:
  created_postcard = api.create(postcard_editable)
except ApiException as e:
  print(e)
```





### List
```bash
curl -X GET "https://api.lob.com/v1/postcards?limit=2" \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = PostcardsApi(api_client)

try:
  postcards = api.list(limit=2)
except ApiException as e:
  print(e)
```


## SelfMailers Api

### Retrieve
```bash
curl https://api.lob.com/v1/self_mailers/sfm_8ffbe811dea49dcf \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = SelfMailersApi(api_client)

try:
  self_mailer = api.get("sfm_8ffbe811dea49dcf")
except ApiException as e:
  print(e)
```







### Delete
```bash
curl -X DELETE "https://api.lob.com/v1/self_mailers/sfm_8ffbe811dea49dcf" \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = SelfMailersApi(api_client)

try:
  deleted_resource = api.delete("sfm_8ffbe811dea49dcf")
except ApiException as e:
  print(e)
```


### Create
```bash
curl https://api.lob.com/v1/self_mailers \
  
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
```

```python
self_mailer_editable = SelfMailerEditable(
  description = "Demo Self Mailer job",
  _from = "adr_210a8d4b0b76d77b",
  inside = "<html style='padding: 1in; font-size: 50;'>Inside HTML for {{name}}</html>",
  outside = "<html style='padding: 1in; font-size: 20;'>Outside HTML for {{name}}</html>",
  to = AddressEditable(
    name = "Harry Zhang",
    address_line1 = "210 King St",
    address_line2 = "# 6100",
    address_city = "San Francisco",
    address_state = "CA",
    address_zip = "94107",
  ),
  merge_variables = MergeVariables(
    name = "Harry",
  ),
)

with ApiClient(configuration) as api_client:
  api = SelfMailersApi(api_client)

try:
  created_self_mailer = api.create(self_mailer_editable)
except ApiException as e:
  print(e)
```





### List
```bash
curl -X GET "https://api.lob.com/v1/self_mailers?limit=2" \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = SelfMailersApi(api_client)

try:
  self_mailers = api.list(limit=2)
except ApiException as e:
  print(e)
```


## Letters Api

### Retrieve
```bash
curl https://api.lob.com/v1/letters/ltr_4868c3b754655f90 \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = LettersApi(api_client)

try:
  letter = api.get("ltr_4868c3b754655f90")
except ApiException as e:
  print(e)
```







### Delete
```bash
curl -X DELETE "https://api.lob.com/v1/letters/ltr_4868c3b754655f90" \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = LettersApi(api_client)

try:
  deleted_resource = api.cancel("ltr_4868c3b754655f90")
except ApiException as e:
  print(e)
```


### Create
```bash
curl https://api.lob.com/v1/letters \
  
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
```

```python
letter_editable = LetterEditable(
  description = "Demo Letter",
  _from = "adr_210a8d4b0b76d77b",
  file = "<html style='padding-top: 3in; margin: .5in;'>HTML Letter for {{name}}</html>",
  color = True,
  to = AddressEditable(
    name = "Harry Zhang",
    address_line1 = "210 King St",
    address_line2 = "# 6100",
    address_city = "San Francisco",
    address_state = "CA",
    address_zip = "94107",
  ),
  merge_variables = MergeVariables(
    name = "Harry",
  ),
  cards = [
    "card_c51ae96f5cebf3e",
  ],
)

with ApiClient(configuration) as api_client:
  api = LettersApi(api_client)

try:
  created_letter = api.create(letter_editable)
except ApiException as e:
  print(e)
```





### List
```bash
curl -X GET "https://api.lob.com/v1/letters?limit=2" \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = LettersApi(api_client)

try:
  letters = api.list(limit=2)
except ApiException as e:
  print(e)
```


## Checks Api

### Retrieve
```bash
curl https://api.lob.com/v1/checks/chk_534f10783683daa0 \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = ChecksApi(api_client)

try:
  check = api.get("chk_534f10783683daa0")
except ApiException as e:
  print(e)
```







### Delete
```bash
curl -X DELETE "https://api.lob.com/v1/checks/chk_534f10783683daa0" \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = ChecksApi(api_client)

try:
  deleted_resource = api.cancel("chk_534f10783683daa0")
except ApiException as e:
  print(e)
```


### Create
```bash
curl https://api.lob.com/v1/checks \
  
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
```

```python
check_editable = CheckEditable(
  description = "Demo Check",
  bank_account = "bank_8cad8df5354d33f",
  amount = 22.5,
  memo = "rent",
  logo = "https://s3-us-west-2.amazonaws.com/public.lob.com/assets/check_logo.png",
  check_bottom = "<h1 style='padding-top:4in;'>Demo Check for {{name}}</h1>",
  _from = "adr_210a8d4b0b76d77b",
  to = AddressDomestic(
    name = "Harry Zhang",
    address_line1 = "210 King St",
    address_line2 = "# 6100",
    address_city = "San Francisco",
    address_state = "CA",
    address_zip = "94107",
  ),
  merge_variables = MergeVariables(
    name = "Harry",
  ),
)

with ApiClient(configuration) as api_client:
  api = ChecksApi(api_client)

try:
  created_check = api.create(check_editable)
except ApiException as e:
  print(e)
```





### List
```bash
curl -X GET "https://api.lob.com/v1/checks?limit=2" \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = ChecksApi(api_client)

try:
  checks = api.list(limit=2)
except ApiException as e:
  print(e)
```


## BankAccounts Api

### Retrieve
```bash
curl https://api.lob.com/v1/bank_accounts/bank_8cad8df5354d33f \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = BankAccountsApi(api_client)

try:
  bank_account = api.get("bank_8cad8df5354d33f")
except ApiException as e:
  print(e)
```







### Delete
```bash
curl -X DELETE "https://api.lob.com/v1/bank_accounts/bank_3e64d9904356b20" \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = BankAccountsApi(api_client)

try:
  deleted_resource = api.delete("bank_3e64d9904356b20")
except ApiException as e:
  print(e)
```



### List
```bash
curl -X GET "https://api.lob.com/v1/bank_accounts?limit=2" \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = BankAccountsApi(api_client)

try:
  bank_accounts = api.list(limit=2)
except ApiException as e:
  print(e)
```


### Verify
```bash
curl https://api.lob.com/v1/bank_accounts/bank_dfceb4a2a05b57e/verify \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \ 
  -d "amounts[]=25" \ 
  -d "amounts[]=63" \ 
```

```python
verification_data = BankAccountVerify(
  amounts = [ 
    25, 
    63, 
  ],
)

with ApiClient(configuration) as api_client:
  api = BankAccountsApi(api_client)

try:
  verified_account = api.verify("bank_dfceb4a2a05b57e", verification_data)
except ApiException as e:
  print(e)
```






### Create
```bash
curl https://api.lob.com/v1/bank_accounts \
  
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
```

```python
bank_account_writable = BankAccountWritable(
  description = "Test Bank Account",
  routing_number = "322271627",
  account_number = "123456789",
  signatory = "John Doe",
  account_type = BankTypeEnum("company"),
)

with ApiClient(configuration) as api_client:
  api = BankAccountsApi(api_client)

try:
  created_bank_account = api.create(bank_account_writable)
except ApiException as e:
  print(e)
```



## Templates Api

### Retrieve
```bash
curl https://api.lob.com/v1/templates/tmpl_c94e83ca2cd5121 \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = TemplatesApi(api_client)

try:
  template = api.get("tmpl_c94e83ca2cd5121")
except ApiException as e:
  print(e)
```







### Delete
```bash
curl -X DELETE "https://api.lob.com/v1/templates/tmpl_df934eeda694203" \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = TemplatesApi(api_client)

try:
  deleted_resource = api.delete("tmpl_df934eeda694203")
except ApiException as e:
  print(e)
```



### List
```bash
curl -X GET "https://api.lob.com/v1/templates?limit=2" \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = TemplatesApi(api_client)

try:
  templates = api.list(limit=2)
except ApiException as e:
  print(e)
```




### Update
```bash
curl https://api.lob.com/v1/templates/tmpl_c94e83ca2cd5121 \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
  -d "description=Updated description" \
  -d "published_version=vrsn_362184d96d9b0c9"
```

```python
with ApiClient(configuration) as api_client:
  api = TemplatesApi(api_client)

update_data = TemplateUpdate(
  description = "updated template",
  published_version = "vrsn_362184d96d9b0c9"
)

try:
  update_template = api.update("tmpl_c94e83ca2cd5121", update_data)
except ApiException as e:
  print(e)
```




### Create
```bash
curl https://api.lob.com/v1/templates \
  
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
```

```python
template_writable = TemplateWritable(
  description = "Test Template",
  html = "<html>HTML for {{name}}</html>",
)

with ApiClient(configuration) as api_client:
  api = TemplatesApi(api_client)

try:
  created_template = api.create(template_writable)
except ApiException as e:
  print(e)
```



## TemplateVersions Api

### Retrieve
```bash
curl https://api.lob.com/v1/templates/tmpl_c94e83ca2cd5121/versions/vrsn_534e339882d2282 \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = TemplateVersionsApi(api_client)

try:
  template_version = api.get("tmpl_c94e83ca2cd5121", "vrsn_534e339882d2282")
except ApiException as e:
  print(e)
```







### Delete
```bash
curl -X DELETE "https://api.lob.com/v1/templates/tmpl_4aa14648113e45b/versions/vrsn_534e339882d2282" \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = TemplateVersionsApi(api_client)

try:
  deleted_resource = api.delete("tmpl_4aa14648113e45b", "vrsn_534e339882d2282")
except ApiException as e:
  print(e)
```



### List
```bash
curl -X GET "https://api.lob.com/v1/templates/tmpl_dadaaf7b76c9f25/versions?limit=2" \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = TemplateVersionsApi(api_client)

try:
  template_versions = api.list("tmpl_dadaaf7b76c9f25", limit=2)
except ApiException as e:
  print(e)
```




### Update
```bash
curl https://api.lob.com/v1/templates/tmpl_c94e83ca2cd5121/versions/vrsn_534e339882d2282 \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
  -d "description=Updated description"
```

```python
with ApiClient(configuration) as api_client:
  api = TemplateVersionsApi(api_client)

update_data = TemplateVersionUpdatable(
  description = "updated template"
)

try:
  update_template_version = api.update("tmpl_c94e83ca2cd5121", "vrsn_534e339882d2282", update_data)
except ApiException as e:
  print(e)
```




### Create
```bash
curl https://api.lob.com/v1/templates/tmpl_4aa14648113e45b/versions \
  
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
```

```python
template_version_writable = TemplateVersionWritable(
  description = "Second Version",
  html = "<html>Second HTML for {{name}}</html>",
)

with ApiClient(configuration) as api_client:
  api = TemplateVersionsApi(api_client)

try:
  created_template_version = api.create("tmpl_4aa14648113e45b", template_version_writable)
except ApiException as e:
  print(e)
```



## BillingGroups Api

### Retrieve
```bash
curl https://api.lob.com/v1/billing_groups/bg_4bb02b527a72667d0 \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = BillingGroupsApi(api_client)

try:
  billing_group = api.get("bg_4bb02b527a72667d0")
except ApiException as e:
  print(e)
```





### Create
```bash
curl https://api.lob.com/v1/billing_groups \
  
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
```

```python
billing_group_editable = BillingGroupEditable(
  description = "Usage group used for the Marketing Department's resource sends",
  name = "Marketing Department",
)

with ApiClient(configuration) as api_client:
  api = BillingGroupsApi(api_client)

try:
  created_bg = api.create(billing_group_editable)
except ApiException as e:
  print(e)
```

### Update
```bash
curl -X PATCH https://api.lob.com/v1/bg_759954f540a1bfdb5 \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
  -d "description=demo replacement" \
```

```python
billing_group_editable = BillingGroupEditable(
  description = "demo replacement",
)

with ApiClient(configuration) as api_client:
  api = BillingGroupsApi(api_client)

try:
  updated_bg = api.update("bg_759954f540a1bfdb5", billing_group_editable)
except ApiException as e:
  print(e)
```



### List
```bash
curl -X GET "https://api.lob.com/v1/billing_groups?limit=2" \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = BillingGroupsApi(api_client)

try:
  billing_groups = api.list(limit=2)
except ApiException as e:
  print(e)
```


## Cards Api

### Retrieve
```bash
curl https://api.lob.com/v1/cards/card_7a6d73c5c8457fc \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = CardsApi(api_client)

try:
  card = api.get("card_7a6d73c5c8457fc")
except ApiException as e:
  print(e)
```








### Delete
```bash
curl -X DELETE "https://api.lob.com/v1/cards/card_6afffd19045076c" \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = CardsApi(api_client)

try:
  deleted_resource = api.delete("card_6afffd19045076c")
except ApiException as e:
  print(e)
```



### Create
```bash
curl https://api.lob.com/v1/cards \
  
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
```

```python
card_editable = CardEditable(
  front = "https://s3-us-west-2.amazonaws.com/public.lob.com/assets/card_horizontal.pdf",
  back = "https://s3-us-west-2.amazonaws.com/public.lob.com/assets/card_horizontal.pdf",
  size = "2.125x3.375",
  description = "Test Card",
)

with ApiClient(configuration) as api_client:
  api = CardsApi(api_client)

try:
  created_card = api.create(card_editable)
except ApiException as e:
  print(e)
```






### List
```bash
curl -X GET "https://api.lob.com/v1/cards?limit=2" \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = CardsApi(api_client)

try:
  cards = api.list(limit=2)
except ApiException as e:
  print(e)
```







### Update
```bash
curl -X PATCH https://api.lob.com/v1/card_6afffd19045076c \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
  -d "description=Awesome card" \
  -d "auto_reorder=true" \
  -d "reorder_quantity=10000" \
```

```python
card_updatable = CardUpdatable(
  description = "Awesome card",
  auto_reorder = True,
  reorder_quantity = 10000,
)

with ApiClient(configuration) as api_client:
  api = CardsApi(api_client)

try:
  updated_card = api.update("card_6afffd19045076c", card_updatable)
except ApiException as e:
  print(e)
```

## CardOrders Api

### Retrieve
```bash
curl https://api.lob.com/v1/cards/card_6afffd19045076c/orders/ \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = CardOrdersApi(api_client)

try:
  card_order = api.get("card_6afffd19045076c", limit = 2, offset = 1)
except ApiException as e:
  print(e)
```




### Create
```bash
curl https://api.lob.com/v1/cards/card_6afffd19045076c/orders \
  
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
```

```python
card_order_editable = CardOrderEditable(
  quantity = 10000,
)

with ApiClient(configuration) as api_client:
  api = CardOrdersApi(api_client)

try:
  created_card_order = api.create("card_6afffd19045076c", card_order_editable)
except ApiException as e:
  print(e)
```


## Campaigns Api

### Retrieve
```bash
curl https://api.lob.com/v1/campaigns/cmp_e05ee61ff80764b \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = CampaignsApi(api_client)

try:
  campaign = api.get("cmp_e05ee61ff80764b")
except ApiException as e:
  print(e)
```









### Update
```bash
curl -X PATCH https://api.lob.com/v1/cmp_e05ee61ff80764b \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
  -d "description=Awesome campaign" \
```

```python
campaign_updatable = CampaignUpdatable(
  description = "Awesome campaign",
)

with ApiClient(configuration) as api_client:
  api = CampaignsApi(api_client)

try:
  updated_campaign = api.update("cmp_e05ee61ff80764b", campaign_updatable)
except ApiException as e:
  print(e)
```


### Create
```bash
curl https://api.lob.com/v1/campaigns \
  
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
```

```python
campaign_writable = CampaignWritable(
  name = "My First Campaign",
  schedule_type = CmpScheduleType("immediate"),
)

with ApiClient(configuration) as api_client:
  api = CampaignsApi(api_client)

try:
  created_campaign = api.create(campaign_writable)
except ApiException as e:
  print(e)
```






### List
```bash
curl -X GET "https://api.lob.com/v1/campaigns?limit=2" \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = CampaignsApi(api_client)

try:
  campaigns = api.list(limit=2)
except ApiException as e:
  print(e)
```






### Delete
```bash
curl -X DELETE "https://api.lob.com/v1/campaigns/cmp_e05ee61ff80764b" \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = CampaignsApi(api_client)

try:
  deleted_resource = api.delete("cmp_e05ee61ff80764b")
except ApiException as e:
  print(e)
```


## Creatives Api



### Update
```bash
curl -X PATCH https://api.lob.com/v1/crv_2a3b096c409b32c \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
  -d "description=Our updated 4x6 postcard creative" \
```

```python
creative_patch = CreativePatch(
  description = "Our updated 4x6 postcard creative",
)

with ApiClient(configuration) as api_client:
  api = CreativesApi(api_client)

try:
  updated_creative = api.update("crv_2a3b096c409b32c", creative_patch)
except ApiException as e:
  print(e)
```

### Retrieve
```bash
curl https://api.lob.com/v1/creatives/crv_2a3b096c409b32c \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = CreativesApi(api_client)

try:
  creative = api.get("crv_2a3b096c409b32c")
except ApiException as e:
  print(e)
```




### Create
```bash
curl https://api.lob.com/v1/creatives \
  
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
```

```python
creative_writable = CreativeWritable(
  campaign_id = "cmp_e05ee61ff80764b",
  resource_type = "postcard",
  description = "Our 4x6 postcard creative",
  _from = "adr_210a8d4b0b76d77b",
  front = "tmpl_4aa14648113e45b",
  back = "tmpl_4aa14648113e45b",
  details = PostcardDetailsWritable(
    mail_type = MailType("usps_first_class"),
  ),
)

with ApiClient(configuration) as api_client:
  api = CreativesApi(api_client)

try:
  created_creative = api.create(creative_writable)
except ApiException as e:
  print(e)
```


## Uploads Api





### Retrieve Export
```bash
curl https://api.lob.com/v1/uploads/upl_71be866e430b11e9/exports/ex_6a94fe68fd151e0f8 \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
  -d "type=failures"
```

```python
with ApiClient(configuration) as api_client:
  api = UploadsApi(api_client)

try:
  retrieved_export = api.get_export("upl_71be866e430b11e9", "ex_6a94fe68fd151e0f8")
except ApiException as e:
  print(e)
```





### Upload File

```bash
curl -X POST https://api.lob.com/v1/uploads/upl_71be866e430b11e9/file \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
  -F file=@<YOUR_FILE_NAME_HERE>
```

```python
with ApiClient(configuration) as api_client:
  api = UploadsApi(api_client)

try:
  res = api.upload_file("upl_71be866e430b11e9", open("<PATH_TO_CSV>", "rb"))
except ApiException as e:
  print(e)
```

### Retrieve
```bash
curl https://api.lob.com/v1/uploads/upl_71be866e430b11e9 \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = UploadsApi(api_client)

try:
  upload = api.get_upload("upl_71be866e430b11e9")
except ApiException as e:
  print(e)
```








### Create Export
```bash
curl https://api.lob.com/v1/uploads/upl_71be866e430b11e9/exports \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
  -d "type=failures"
```

```python
with ApiClient(configuration) as api_client:
  api = UploadsApi(api_client)

export_model = ExportModel(
  type = "all"
)

try:
  created_export = api.create_export("upl_71be866e430b11e9", export_model)
except ApiException as e:
  print(e)
```



### List
```bash
curl -X GET "https://api.lob.com/v1/uploads?limit=2" \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = UploadsApi(api_client)

try:
  uploads = api.list_upload()
except ApiException as e:
  print(e)
```





### Update
```bash
curl -X PATCH https://api.lob.com/v1/upl_71be866e430b11e9 \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
  -d "state=Ready for Validation" \
```

```python
upload_updatable = UploadUpdatable(
  state = UploadState("Ready for Validation"),
)

with ApiClient(configuration) as api_client:
  api = UploadsApi(api_client)

try:
  updated_upload = api.update_upload("upl_71be866e430b11e9", upload_updatable)
except ApiException as e:
  print(e)
```


### Create
```bash
curl --location --request POST https://api.lob.com/v1/uploads \
  --header 'Content-Type: application/json' \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
```

```python
upload_writable = UploadWritable(
  campaign_id = "cmp_e05ee61ff80764b",
  column_mapping = { "firstName": "first name" },
)

with ApiClient(configuration) as api_client:
  api = UploadsApi(api_client)

try:
  created_upload = api.create_upload(upload_writable)
except ApiException as e:
  print(e)
```




### Delete
```bash
curl -X DELETE "https://api.lob.com/v1/uploads/upl_71be866e430b11e9" \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc:
```

```python
with ApiClient(configuration) as api_client:
  api = UploadsApi(api_client)

try:
  deleted_resource = api.delete_upload("upl_71be866e430b11e9")
except ApiException as e:
  print(e)
```

## ZipLookups Api

### ZipLookup
```bash
curl https://api.lob.com/v1/us_zip_lookups \
  -u test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc: \
  -d "zip_code=94107"
```

```python
with ApiClient(configuration) as api_client:
  api = ZipLookupsApi(api_client)

zip_request = ZipEditable(
  zip_code = "94107"
)

try:
  zip_lookup = api.lookup(zip_request)
except ApiException as e:
  print(e)
```

## Reverse Geocode Lookups Api

### Reverse Geocode Lookup
```bash
curl https://api.lob.com/v1/us_reverse_geocode_lookups \
  -u <YOUR_LIVE_API_KEY>: \
```

```python
with ApiClient(configuration) as api_client:
  api = ReverseGeocodeLookupsApi(api_client)

coordinates = Location(
  latitude = 37.777456,
  longitude = -122.393039,
)

try:
  geocode = api.lookup(coordinates)
except ApiException as e:
  print(e)
```

## USAutoCompletions Api

### Autocomplete
```bash
curl https://api.lob.com/v1/us_autocompletions \
  -u <YOUR_LIVE_API_KEY>: \
  -d "address_prefix=185 B" \
  -d "city=San Francisco" \
  -d "state=CA" \
  -d "zip_code=94017" \
```

```python
with ApiClient(configuration) as api_client:
  api = UsAutocompletionsApi(api_client)

autocompletion_data = UsAutocompletionsWritable(
  address_prefix = "185 B",
  city = "San Francisco",
  state = "CA",
  zip_code = "94017",
)

try:
  autocompleted_addresses = api.autocomplete(autocompletion_data)
except ApiException as e:
  print(e)
```

## UsVerifications Api

### Bulk Verify
```bash
curl https://api.lob.com/v1/bulk/us_verifications \
  -u <YOUR LIVE API KEY>: \
  --header "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "addresses[0][primary_line]=210 King Street" \
  --data-urlencode "addresses[0][city]=San Francisco" \
  --data-urlencode "addresses[0][state]=CA" \
  --data-urlencode "addresses[0][zip_code]=94017" \
  --data-urlencode "addresses[1][primary_line]=185 BERRY ST STE 6600" \
  --data-urlencode "addresses[1][city]=SAN FRANCISCO" \
  --data-urlencode "addresses[1][state]=CA" \
  --data-urlencode "addresses[1][zip_code]=94017" \
```

```python
with ApiClient(configuration) as api_client:
  api = UsVerificationsApi(api_client)

verification_data_0 = MultipleComponents(
  primary_line = "210 King Street",
  city = "San Francisco",
  state = "CA",
  zip_code = "94017",
)

verification_data_1 = MultipleComponents(
  primary_line = "185 BERRY ST STE 6600",
  city = "SAN FRANCISCO",
  state = "CA",
  zip_code = "94017",
)


address_list = MultipleComponentsList(
  addresses = [
    verification_data_0,
    verification_data_1,
  ],
)

try:
  bulk_verified = api.verifyBulk(address_list)
except ApiException as e:
  print(e)
```

### Single Verify
```bash
curl https://api.lob.com/v1/us_verifications \
  -u <YOUR_LIVE_API_KEY>: \
  -d "primary_line=210 King Street" \
  -d "city=San Francisco" \
  -d "state=CA" \
  -d "zip_code=94017" \
```

```python
with ApiClient(configuration) as api_client:
  api = UsVerificationsApi(api_client)
verification_data_1 = UsVerificationsWritable(
  primary_line = "210 King Street",
  city = "San Francisco",
  state = "CA",
  zip_code = "94017",
)

try:
  single_verified = api.verifySingle(verification_data_1)
except ApiException as e:
  print(e)
```

## IntlAutocompletion Api

### IntlAutocompletion
```bash
curl https://api.lob.com/v1/intl_autocompletions \
  -u <YOUR_LIVE_API_KEY>: \
  -d "address_prefix=340 Wat" \
  -d "city=Summerside" \
  -d "state=Prince Edward Island" \
  -d "zip_code=C1N 1C4" \
  -d "country=CA" \
```

```python
with ApiClient(configuration) as api_client:
  api = IntlAutocompletionsApi(api_client)

autocompletion_data = IntlAutocompletionsWritable( 
    address_prefix = "340 Wat",
    city = "Summerside",
    state = "Prince Edward Island",
    zip_code = "C1N 1C4",
    country = CountryExtended("CA"),
)

try:
  autocompleted_addresses = api.autocomplete(autocompletion_data)
except ApiException as e:
  print(e)
```

## IntlVerifications Api

### Single Verify
```bash
curl https://api.lob.com/v1/intl_verifications \
  -u <YOUR_LIVE_API_KEY>: \
  -d "primary_line=370 Water St" \
  -d "city=Summerside" \
  -d "state=Prince Edward Island" \
  -d "postal_code=C1N 1C4" \
  -d "country=CA" \
```

```python
with ApiClient(configuration) as api_client:
  api = IntlVerificationsApi(api_client)
verification_data_1 = IntlVerificationWritable(
  primary_line = "370 Water St",
  city = "Summerside",
  state = "Prince Edward Island",
  postal_code = "C1N 1C4",
  country = CountryExtended("CA"),
)

try:
  single_verified = api.verifySingle(verification_data_1)
except ApiException as e:
  print(e)
```

### Bulk Verify
```bash
curl https://api.lob.com/v1/bulk/intl_verifications \
  -u <YOUR LIVE API KEY>: \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'addresses[0][primary_line]=35 Tower Hill' \
  --data-urlencode 'addresses[0][city]=London' \
  --data-urlencode 'addresses[0][postal_code]=EC3N 4DR' \
  --data-urlencode 'addresses[0][country]=GB' \
  --data-urlencode 'addresses[1][primary_line]=370 Water St' \
  --data-urlencode 'addresses[1][city]=Summerside' \
  --data-urlencode 'addresses[1][state]=Prince Edward Island' \
  --data-urlencode 'addresses[1][postal_code]=C1N 1C4' \
  --data-urlencode 'addresses[1][country]=CA' \
```

```python
with ApiClient(configuration) as api_client:
  api = IntlVerificationsApi(api_client)

verification_data_0 = MultipleComponentsIntl(
  primary_line = "35 Tower Hill",
  city = "London",
  postal_code = "EC3N 4DR",
  country = CountryExtended("GB"),
)

verification_data_1 = MultipleComponentsIntl(
  primary_line = "370 Water St",
  city = "Summerside",
  state = "Prince Edward Island",
  postal_code = "C1N 1C4",
  country = CountryExtended("CA"),
)


address_list = IntlVerificationsPayload(
  addresses = [
    verification_data_0,
    verification_data_1,
  ],
)

try:
  bulk_verified = api.verifyBulk(address_list)
except ApiException as e:
  print(e)
```

