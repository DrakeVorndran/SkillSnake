import random
board = []
boardSize = 5
playerx=0
playery=0
score = 0
tailx = []
taily = []
baitx = 0
baity =0
play = True
def genran(frm,to):
	return int((random.random()*(to-frm))+frm+random.random())
def newBait():
	baitx = genran(0,boardSize-1)
	baity = genran(0,boardSize-1)
	while(board[baity][baitx]!=" "):
		baitx = genran(0,boardSize-1)
		baity = genran(0,boardSize-1)
	board[baity][baitx] = "B"
print "Welcome to Technical Snake"
print "the goal of Technical Snake is to get your head \"@\" to the bait \"X\""
print "be carfull not to run into the walls or your tail"
print " use \"w, a, s, d\" followed by an enter to move around the board"
print "Please wait for the board to print after every imput"
for x in range(boardSize):
	boardBuilder = []
	for y in range(boardSize):
		boardBuilder.append(" ")
	board.append(boardBuilder)
board[playery][playerx]="1"
newBait()

def printBoard():
	printMe ="["
	for x in range(boardSize*2):
		printMe+="-"
	printMe+="]"
	print printMe
	for x in board:
		printMe = "["
		for y in x:
			if y == "B":
				printMe+="X"
			elif y ==" ":
				printMe+=" "
			elif y ==str(score+1):
				printMe+="@"
			elif y =="1":
				printMe+="+"
			else:
				printMe+="#"
			printMe+=" "
		printMe+="]"
		print printMe
	printMe ="["
	for x in range(boardSize*2):
		printMe+="-"
	printMe+="]"
	print printMe

playerIn = "nan"
printBoard()
while play:
	subx = 0
	for x in range(len(tailx)):
		board[taily[x-subx]][tailx[x-subx]]=str(int(board[taily[x-subx]][tailx[x-subx]])-1)
		if board[taily[x-subx]][tailx[x-subx]]=="0":
			board[taily[x-subx]][tailx[x-subx]]=" "
			tailx.pop(x-subx)
			taily.pop(x-subx)
			subx+=1
	board[playery][playerx]=str(int(board[playery][playerx])-1)
	if board[playery][playerx]=="0":
		board[playery][playerx]=" "
	else:
		tailx.append(playerx)
		taily.append(playery)
	cont = False
	while not(cont):
		playerIn = raw_input().lower();
		if playerIn=="w":
			playery-=1
			cont = True
		elif playerIn=="a":
			playerx-=1
			cont = True
		elif playerIn=="s":
			playery+=1
			cont = True
		elif playerIn=="d":
			playerx+=1
			cont = True
		else:
			print "try again"
	if (playerx>=boardSize or playerx<0 or playery >=boardSize or playery<0):
		print "Game over"
		print "Final Score",score
		play = False
		break
	elif board[playery][playerx] == "B":
		score+=1
		newBait()
	elif board[playery][playerx] != " ":
		print "Game over"
		print "Final Score",score
		play = False
		break
	board[playery][playerx]=str(score+1)
	print "Score:",score
	printBoard()