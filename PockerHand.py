
def sublistExists(list1, list2):
    return ''.join(list2) in ''.join(list1)



def royalFlush(lst):
	suits = ['A','K','Q','J','10']
	for card in lst:
		if(card[:len(card)-1] in suits):
			suits.pop(suits.index(card[:len(card)-1]))
	if (len(suits) ==0):
		return True
	else:
	    return False	
			
def checkOrder(lst):
	suits = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
	suitsX = ['X','X','X','X','6','7','8','9','10','J','Q','K','X']
	#counter =0
	for card in lst:
		if(card[:len(card)-1] in suits):
			suits[suits.index(card[:len(card)-1])] = 'X'
			#counter +=1
	return (sublistExists(suits,['X' for x in range(5)])) or (suits == suitsX )
	
 

def checkThreeCards(lst):
	lst.sort()
	if((lst[0][:len(lst[0])-1] == lst[1][:len(lst[1])-1] == lst[2][:len(lst[2])-1] ) or (lst[1][:len(lst[1])-1] == lst[2][:len(lst[2])-1] == lst[3][:len(lst[3])-1]) or (lst[2][:len(lst[2])-1] == lst[3][:len(lst[3])-1] == lst[4][:len(lst[4])-1])):
		if ((lst[0][:len(lst[0])-1] == lst[1][:len(lst[1])-1]) and (lst[3][:len(lst[3])-1] == lst[4][:len(lst[4])-1])):
			return "FH"
		else:
		    return "TK"
	return "KeepGoing"	    	

def checkNumberOfPairs(lst):
	lst.sort()
	counter = 0

	for x in range(len(lst)-1):
		if(lst[x][:len(lst[x])-1] == lst[x+1][:len(lst[x])-1]):
			counter+=1

	if(counter == 2):
	    return "Two Pairs"
	elif(counter == 1):
	    return "Pair"
	else:
	    return "High Card"        		


lst = []
lst = input().split()
lst1 = ['10C', 'JC' ,'JK', 'KC', 'JC'] 
lst.sort()

#First check - Does the all suits same?
#print(lst[0][len(lst[0])-1:] ," ", lst[1][len(lst[1])-1:] ," ", lst[2][len(lst[2])-1:] ," ", lst[3][len(lst[3])-1:] ," ", lst[4][len(lst[4])-1:])
if(lst[0][len(lst[0])-1:] == lst[1][len(lst[1])-1:] == lst[2][len(lst[2])-1:] == lst[3][len(lst[3])-1:] == lst[4][len(lst[4])-1:]):
	#print("All  suits are same")
	#print(lst1)
	if(royalFlush(lst)):
		print("Royal Flush")
	else:
	    if(checkOrder(lst)):  # SF or FL check
	        print("Straight Flush")
	    else:
	        print("Flush")    	


#Third check - Does the all values same?
else:
	if((lst[0][len(lst[0])-2] == lst[1][len(lst[1])-2] == lst[2][len(lst[2])-2] == lst[3][len(lst[3])-2] ) or (lst[1][len(lst[1])-2] == lst[2][len(lst[2])-2] == lst[3][len(lst[3])-2] == lst[4][len(lst[4])-2])):
		print("Four of a Kind")


	else:
	    if(checkThreeCards(lst) == "FH"):
	        print("Full House")
	    elif(checkThreeCards(lst) == "TK"):
	        print("Three of a Kind")
	    else:
	        if(checkOrder(lst)):
	            print("Straight")
	        else:
	            print(checkNumberOfPairs(lst))            	
