# Lawrence Arundel Final Project IT 140
def show_instructions():
    print("Orge Text Adventure Game")
    print("Collect 6 items to win the game, or be eaten by the orge.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")
    print('-------------------------------')


def show_interface():
    print('You are in the ' + player_location)
    print('Inventory: ' + str(user_inventory).replace('{', "").replace('}', ""))
    if rooms_items.get(
            player_location) in user_inventory or player_location == 'Living Room' or player_location == 'Chambers':
        print('-------------------------------')
        pass
    else:
        print('You see a ' + str(rooms_items[player_location]).replace('{', "").replace('}', "").replace("'", ''))
        print('-------------------------------')


def user_movement(user_location, user_move):
    if user_move in (rooms.get(user_location)):
        user_location = rooms[user_location][user_move]
        return user_location
    else:
        print('-------------------------------')
        print('Invalid move, try again.')
        return user_location


def get_item():
    user_inventory.append(rooms_items.get(player_location))


rooms = {
    'Living Room': {'South': 'Cellar'},
    'Cellar': {'North': 'Living Room', 'West': 'Office'},
    'Office': {'North': 'Studio', 'South': 'Kitchen', 'East': 'Cellar', 'West': 'Courtyard'},
    'Bedroom': {'West': 'Kitchen'},
    'Kitchen': {'North': 'Office', 'East': 'Bedroom'},
    'Courtyard': {'East': 'Office'},
    'Studio': {'South': 'Office', 'East': 'Chambers'},
    'Chambers': {'West': 'Studio'}
}
rooms_items = {
    'Cellar': {'Knife'},
    'Office': {'Arrow'},
    'Bedroom': {'Body Armor'},
    'Kitchen': {'Potion'},
    'Courtyard': {'Helmet'},
    'Studio': {'Chain'},
}
show_instructions()
# Initialize Variables
player_location = 'Living Room'
user_inventory = []
# While loop which decides how the game functions
while player_location != 'Chambers':  # Loop until player reaches Boss
    show_interface()
    print('Enter your move: ', end='')
    user_input = input()
    if user_input == 'go North' or user_input == 'go South' or user_input == 'go East' or user_input == 'go West':
        player_location = user_movement(player_location, user_input.replace('go ', ''))
        print('-------------------------------')
    elif (rooms_items.get(player_location)) not in user_inventory and rooms_items.get(player_location) is not None \
            and user_input == 'get ' + str(rooms_items[player_location]).replace('{', "").replace('}', "").replace("'",
                                                                                                                   ''):
        get_item()
        print('-------------------------------')
    else:
        print('Invalid move, try again.')
        print('-------------------------------')

if len(str(user_inventory)) < 5 and player_location == 'Chambers':
    print('NOM NOM...GAME OVER! Thanks for playing the game. Hope you enjoyed it.')
else:
    print('Congratulations! You have collected all items and defeated the ogre! '
          'Thanks for playing the game. Hope you enjoyed it. ')
