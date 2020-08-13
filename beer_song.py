word="bottles"                                                              #asgns the str "bottles" to the variable word
for beer_num in range (99,0,-1):                                           #sets the range between 99 and 0, decreasing 1 on the for loop

    print (beer_num, word, "of beer in the wall")                           #shows on the screen the value of beer_num, adding the str "of beer in the wall"
    print(beer_num, word, "of beer. ")                                      
    print("Take one down")
    print("Pass it arround")    
    if beer_num==1:                                                         #the loop finds the condition that will only be true when the loop iteration gets to 1

        print("No more bottles of beer in the wall")                        #the end of the loop and the song
    else:                                                                   #tge condition that meet everytime excepto when beer_num gets to 1

        new_num=beer_num-1
        if new_num==1:
            word="bottle"                                                   #when the varibale beer_num gets to 1, the song need to change from plural to singular
        print(new_num, word, "of beer in the wall")                          
    