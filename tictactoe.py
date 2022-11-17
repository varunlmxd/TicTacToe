#TicTacToe
def print_l(list):
    print("""
                         |       |
                     {0}   |   {1}   |   {2}
                         |       |
                 ------------------------              
                         |       |
                     {3}   |   {4}   |   {5}
                         |       |
                 ------------------------
                         |       |
                     {6}   |   {7}   |   {8}
                         |       |
  """.format(list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8]))

def check_l(list):
    c=0
    if(list[0]==list[1]==list[2]):
        c=winner_l(list[1])
    elif(list[3]==list[4]==list[5]):
        c=winner_l(list[4])
    elif(list[6]==list[7]==list[8]):
        c=winner_l(list[7])
    elif(list[0]==list[3]==list[6]):
        c=winner_l(list[3])
    elif(list[1]==list[4]==list[7]):
        c=winner_l(list[4])
    elif(list[2]==list[5]==list[8]):
        c=winner_l(list[5])
    elif(list[0]==list[4]==list[8]):
        c=winner_l(list[4])
    elif(list[2]==list[4]==list[6]):
        c=winner_l(list[4])
    return c

def winner_l(result):
    if(player_1==result):
        print("Player 1 is the winner")
        return 1
    elif(player_2==result):
        print("Player 2 is the winner")
        return 1

list=['1','2','3','4','5','6','7','8','9']
print("Choose either from X or O")
player_1=input("Enter Player 1 choice: ")
player_2=None
if(player_1=='X'):
    player_2='O'
    print(f"Player 1 is {player_1}\nPlayer 2 is {player_2}:")
elif(player_1=='O'):
    player_2='X'
    print(f"Player 1 is {player_1}\nPlayer 2 is {player_2}:")
count=0
print_l(list)
while(count<9):
    if(count%2==0):
        index=input(f"Player 1 choose the index position for {player_1} to be placed: ")
        print(index)
        if index not in list:
            print("Invalid index!!!\nEnter again")
            continue    
        list[int(index)-1]=player_1
    else:
        index=input(f"Player 2 choose the index position for {player_2} to be placed: ")
        if index not in list:
            print("Invalid index!!!\nEnter again")
            continue
        list[int(index)-1]=player_2
    print_l(list)
    check=check_l(list)
    count=count+1
    if(check!=0):
        break
if(count==9):
    print("Game is Draw")
