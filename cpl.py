#Scan the input and store in input variable
input=input("enter input in A → Xβ format")
#splits the character with space
LHS = input.split()
input = LHS[2]
#creating and initializing variables upperCase and lowerCase
upperCase = 0
lowerCase = 0
#calculates total number of upperCase and lower in inputString
upperCase = sum(1 for c in input if c.isupper())
lowerCase = sum(1 for d in input if d.islower())
if input[0].isupper() and upperCase == 2 and len(input) == 2:
	print (LHS[0]+ ' -> '+input[0:])
elif input[0].isupper():
     #Display the string by dividing the 1st upperCase character and remaining string
	print (LHS[0]+ ' -> '+input[0:1]+'<'+input[1:]+'>')
	upperCase = upperCase - 1 #decrements upperCase
	#removes 1st character from the inputString
	input = input[1:] 
else:
	#compares the length of the string and second character with upper case for the 1st step
	if len(input) == 2 and input[1].isupper():
      		#Display the string by dividing the 1st LowerCase character and remaining string
      		print (LHS[0]+ ' -> <'+input[0:1]+'>'+input[1:])
      		#Displays lowerCase -> lowerCase
      		print ('<'+input[0:1]+'> -> '+input[0:1])
      		lowerCase = lowerCase - 1 #decrements upperCase	 
	elif len(input) > 1:
    		#Display the string by dividing the 1st LowerCase character and remaining string
    		print (LHS[0]+ ' ->  <'+input[0:1]+'><'+input[1:]+'>')
    		#Displays lowerCase -> lowerCase
    		print ('<'+input[0:1]+'> -> '+input[0:1])
    		lowerCase = lowerCase - 1 #decrements upperCase
    		input = input[1:] #removes 1st character from the inputString
	else:
    		print (LHS[0]+ ' -> '+input[0:])
    		#Display the last LowerCase character
        	print('<'+input[0:1]+'> -> '+input[0:1])
         	lowerCase = lowerCase - 1 #decrements upperCase
        	input = input[1:] #removes 1st character from the inputString
#compares upperCase and lowerCase with 2 and 0
while upperCase > 2 or lowerCase > 0:
   #compares upperCase and lowerCase with 2 and 1
   if upperCase > 2 or lowerCase >= 1:
      #checks for the upperCase character
      if input[0].isupper():
         #Display the string by dividing the 1st upperCase character and remaining string
         print ('<'+input[0:]+ '> -> '+input[0:1]+'<'+input[1:]+'>')
         upperCase = upperCase - 1 #decrements upperCase
         input = input[1:] #removes 1st character from the inputString
      #checks for the lowerCase character
      elif input[0].islower():
      	if len(input) == 2 and input[1].isupper():
      		#Display the string by dividing the 1st LowerCase character and remaining string
      		print ('<'+input[0:]+ '> ->  <'+input[0:1]+'>'+input[1:])
      		#Displays lowerCase -> lowerCase
      		print ('<'+input[0:1]+'> -> '+input[0:1])
      		lowerCase = lowerCase - 1 #decrements upperCase	 
         #compares the length of input String with 1
        elif len(input) > 1:
            #Display the string by dividing the 1st LowerCase character and remaining string
            print ('<'+input[0:]+'> -> <'+input[0:1]+'><'+input[1:]+'>')
            #Displays lowerCase -> lowerCase
            print ('<'+input[0:1]+'> -> '+input[0:1])
            lowerCase = lowerCase - 1 #decrements upperCase
            input = input[1:] #removes 1st character from the inputString
        else:
            #Display the last LowerCase character
            print('<'+input[0:1]+'> -> '+input[0:1])
            lowerCase = lowerCase - 1 #decrements upperCase
            input = input[1:] #removes 1st character from the inputString