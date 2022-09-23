# Lawrence Arundel
# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
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
player_location = 'Living Room'
while player_location != 'exit':
    print('You are in the ' + player_location)
    print('----------------------')
    print('Enter your move: ', end='')
    user_move = input()
    if user_move in (rooms.get(player_location)):
        player_location = rooms[player_location][user_move]
    elif user_move == 'exit':
        player_location = user_move
    else:
        print('Invalid move, try again.')
