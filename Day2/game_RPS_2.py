# Game plan A is rock, B is paper, C is Scissor
# rock can beat scissor ,scissor can beat paper and paper can beat rock
# A =1 B = 2 c=3 if we win 6 points loose 0 points
# X is Rock, Y is Paper, Z is Scissor 

# what is maximum points combination
# X can beat C points 1 +6
# Y can beat A points 2 + 6
# Z can beat B points 3 +6
# A X B Y C Z draw 3
# C X A Y B Z  win
# B X C Y A Z loose
# draw_list  = [] it gives the list of combintion for draw, keeping draw points inside 
# array so that when it happen then only points got added
draw=0
#drawList = [['A', 'X'], ['B', 'Y'], ['C', 'Z'],3]
drawList = [['A', 'Y'], ['B', 'Y'], ['C', 'Y'],3]
#win combination
win=0
#winList = [['C', 'X'], ['A', 'Y'], ['B', 'Z'],6]

winList = [['B', 'Z'],6]
# search each line in three list
loose=0
#looseList = [['B', 'X'], ['C', 'Y'], ['A', 'Z'],0]
looseList = [['A', 'X'], ['B', 'X'], ['C', 'X'],0]
f = open("game_input.txt","r")
game_input=f.read()
#using "repr" we can check how the data is stored in file 
#print(repr(game_input)) 
whole_string = game_input.split('\n')

# for line in whole_string:
#     comb = line.split()
#     #print(comb)
#     #print(line)
#     #print(comb)
#     if (comb in drawList ):
#         draw=draw + drawList[3] + (drawList.index(comb)+1)
#         print(draw,comb)
#     elif (comb in winList ):
#         win=win + winList[3] + (winList.index(comb)+1)
#         print(win,comb)
#     elif (comb in looseList ):
#         loose=loose + looseList[3] + (looseList.index(comb)+1)
#         print(loose,comb)
#     else:
#         print("Not a valid input")
# print('draw',draw)
# print('win',win)
# print('loose',loose)
# print(draw+win+loose)
combination = ['A','B','C']
for line in whole_string:
    comb = line.split()
    print(comb[0],comb[1])
    if(comb[1] == 'X'):
        if comb[0] == 'A':
            loose = loose + 3
        elif comb[0] == 'B':
            loose = loose + 1
        else:
            loose = loose + 2
          
        print('loose',loose)
    elif(comb[1] == 'Y'):
        if comb[0] == 'A':
            draw = draw + 1 + 3
        elif comb[0] == 'B':
            draw = draw + 2 + 3
        else:
            draw = draw + 3 + 3
        print('draw',draw)
    else:
        if comb[0] == 'A':
            win = win + 2 + 6
        elif comb[0] == 'B':
            win = win + 3 + 6
        else:
            win = win + 1 + 6

        print('win',win)

print('draw',draw)
print('win',win)
print('loose',loose)
print(draw+win+loose)