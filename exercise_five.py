#iterate over the key: value pairs in home_town and print a string for each item, for ex
#

home_town = {
  'city': 'Dallas',
  'state': 'Texas',
  'population': "1,000,000"
}

# for key in home_town:
#     print (f'{key} = {home_town[key]}')

for key, value in home_town.items():
  print(f"{key} = {value}")