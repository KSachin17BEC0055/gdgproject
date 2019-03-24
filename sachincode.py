#import random module
import random


#Function to shuffle the words
def shuffle(comstring): 
	 
	jumbled = []
	words = comstring.split(' ')
	for word in words:
		random_word = random.sample(word, len(word)) 

		 
		jumbled.append(''.join(random_word))
	return ' '.join(jumbled)



# Fucntion for showing final score. 
def end(pname, pscore): 
    print(pname, 'Your score is :', pscore) 

    print('Thanks for playing.') 

#selecting random word
def select(): 
    
    words = ['the office', ' the catherine tate show', 'our friends in the north', 'little britain', 
            'the IT crowd', 'being human', 'game of thrones', 'shameless', 
            'extras', 'life on mars', '13 reasons why','friends','stranger things',
             'bodies','rome','people like us','the street','wild west','wallander',
             'dear white people','torch wood','green wing','sherlock','the lakes','top gear','cracker',
             'the punisher','Conviction','help','daredevil']
    choosen = random.choice(words) 

    return choosen

# Function for playing the game. 
def game(): 
    
    p1name = input("Enter your name :")  

     
    pp1 = 0
    
    
    crossed = []
    
     
    for z in range(0,10): 

         
        choosen_word = select() 
        
        
        if choosen_word in crossed:
            choosen_word = select()
        
                
        crossed.append(choosen_word)
        
         
        qn = shuffle(choosen_word) 
        print("jumbled word is :", qn) 

        

        ans = input("Guess the word? ") 

        
        if ans == choosen_word:
                    
                    pp1 = pp1 + 1
                    print('Your score is :', pp1) 
                
        else:
            print("Sorry. correct word is :", choosen_word)  
    end(p1name , pp1) 


if __name__ == '__main__': 
    
    
    game() 
