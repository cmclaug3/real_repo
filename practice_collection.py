#
#
# BLACK JACK
# create from scratch
#
#

def black_jack():
        
        import random
        import time

        deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,
                7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,
                10,10,10,10,10,10,10,10,10,10,10,11,11,
                11,11]

        cHand = random.choice(deck)
        pHand = random.choice(deck) + random.choice(deck)

        print('your hand: ' + str(pHand))
        print('computer hand: showing ' + str(cHand))

        while pHand <= 21:               

                firstHit = input('h or s? then ENTER ')
                
                if firstHit == 'h':
                        pHand += random.choice(deck)
                        print(pHand)                               
                elif firstHit == 's':
                        print('you stay at ' + str(pHand))
                        break
                else:
                        print('you messed up')

        if pHand > 21:
                print('you lose')

        print(' ')
        time.sleep(1.00)
        print('dealer playing...')
        time.sleep(1.00)
        print(' ')

        while cHand < 16:
                print(cHand)
                cHand += random.choice(deck)
                time.sleep(1.00)

        if cHand >= 16 and cHand <= 21:
                print('computer stays at ' + str(cHand))
                
        if cHand > 21:
                print(cHand)
                print('computer busts')

        print(' ')

        if pHand == cHand:
                print('tie')

        elif pHand > 21:
                print('you lose')
 #               cScore = cScore + 1
 #               print(pScore +' - '+ cScore)
        elif cHand > 21:
                print('you win')
 #               pScore = pScore + 1
 #               print(pScore +' - '+ cScore)
        elif pHand > cHand:
                print('you win')
 #               pScore = pScore + 1
 #               print(pScore +' - '+ cScore)
        elif pHand < cHand:
                print('you lose')
 #               cScore = cScore + 1
 #               print(pScore +' - '+ cScore)
        
        playAgain = input('SPACEBAR then ENTER to play again ')

        if playAgain == ' ':
                print(' ')
                black_jack()
black_jack()
 ########STILL NEED
        #deal with the 11/1 Ace rule
        #keep score




                

                

                

        
                

        

        

                

                


                

                
        

        






                        
                        
                        

                
	
		 
