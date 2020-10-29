import requests
import random

# base url for MTG API
base_url = 'https://api.magicthegathering.io/v1/cards'

# create empty dictionary for API data and for used rng numbers
resp = {}
rnd_used = []

# ask if user wants to search by card name (if not perform a random search)
usr_choice = input('Would you like to search by card name? (y/n): ')

# search API using entered card name
if usr_choice == 'y':
  usr_card_name = input('Enter card name: ')
  url = base_url + '?name=' + usr_card_name
  print(f'Accessing {url}')

  r = requests.get(url)
  resp = r.json()

# search API for random card by generating random numbers until one matches card ID
elif usr_choice == 'n':
  print('Searching for a random card...')
  while (('cards' in resp) == False) and (('card' in resp) == False):
    tmp = random.randint(400000, 500000)
    if tmp in rnd_used:
      continue
    else:
      rnd_used.append(tmp)
      url = base_url + '/' + str(tmp)

      r = requests.get(url)
      resp = r.json()

  print(f'Accessing {url}')

# end program if 'y' or 'n' is not entered
else:
  print('PROGRAM TERMINATED')

# try and save card name, type, rarity, and image and print outcomes
if 'card' in resp:
  try:
    card_name = resp['card']['name']
    print(f'Card Name: {card_name}')
  except:
    card_name = "No name found"
    print(f'Card Name: {card_name}')
  
  try:
    card_type = resp['card']['type']
  except:
    card_type = "- Unknown type"
  
  try:
    card_rarity = resp['card']['rarity']
    print(f'Card Type: {card_rarity} {card_type}')
  except:
    card_rarity = "Unknown rarity"
    print(f'Card Type: {card_rarity} {card_type}')
 
  try:
    card_image = resp['card']['imageUrl']
    print(f'Card Image: {card_image}')
  except:
    card_image = "No image found"
    print(f'Card Image: {card_image}')

# if multiple cards are found, ask user to select a card
# try and save card name, type, rarity, and image and print outcomes
elif 'cards' in resp:
  num_matches = len(resp['cards'])
  print(f'Your search generated {num_matches} results.')
  usr_card_num = input(f'Which card would you like to access? (0-{num_matches-1}) ')
  usr_card_num = int(usr_card_num)
  print(f'Accessing card {usr_card_num}...')

  try:
    card_name = resp['cards'][usr_card_num]['name']
    print(f'Card Name: {card_name}')
  except:
    card_name = "No name found"
    print(f'Card Name: {card_name}')
  
  try:
    card_type = resp['cards'][usr_card_num]['type']
  except:
    card_type = "- Unknown type"
  
  try:
    card_rarity = resp['cards'][usr_card_num]['rarity']
    print(f'Card Type: {card_rarity} {card_type}')
  except:
    card_rarity = "Unknown rarity"
    print(f'Card Type: {card_rarity} {card_type}')
 
  try:
    card_image = resp['cards'][usr_card_num]['imageUrl']
    print(f'Card Image: {card_image}')
  except:
    card_image = "No image found"
    print(f'Card Image: {card_image}')
