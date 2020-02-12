# Create a rock paper scissors game in Python

# Player should be able to type r, p, or s
# Computer will pick r, p, or s

# Game will print out the results and keep track of wins, losses, and ties

# Type q to quit



def eval_moves(player_move, cpu_move):
    winning_moves = {'r': 's', 's': 'p', 'p': 'r'}
    if player_move == cpu_move:
        print('You tie')
        return 0
    elif winning_moves[player_move] == cpu_move:
        print('You won!')
        return 1
    else:
        print('You came close, try again!')
        return -1


choices = ['r', 'p', 's']
win = 0
losses = 0
ties = 0

# LOOP
while True:
    # READ
    cmd = input('~~>')
    # EVAL
    # Computer picks r/p/s
    cpu_move = random.choice(choices)
    if cmd == 'r':
        if cpu_move == 'r':
            #tie
            tie += 1
        elif cpu_move == 'p':
            losses += 1
        elif cpu_move == 's':
            win += 1
    elif cmd = 'p':
        if cpu_move == 'p':
            #tie
            tie += 1
        elif cpu_move == 's':
            losses += 1
        elif cpu_move == 'r':
            win += 1
        pass
    elif cmd = 's':
        if cpu_move == 's':
            #tie
            tie += 1
        elif cpu_move == 'r':
            losses += 1
        elif cpu_move == 'p':
            win += 1
        pass
    elif cmd =='q':
        print('Goodbye')
        break
    else: 
        print("I did not understand that command. Please pick r, p, s, or q.")
    # Compare player command to cpu command
    # Update results based on win/loss/tie
    # Print results and score
    print(f'CPU picks {cpu_move}')
    print(f'Wins: {wins}, Losses: {losses}, Ties: {ties}')
    print(f'COMMAND IS {cmd}')



