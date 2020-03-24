questionsEZ =[('how long is a fortnite in days\n:','14 days','Fortnite'),
('what is used to unclog a toilet\n:','a plunger','plunger'),
('whats the key ingredient in disinfectent\n:','alcohol','Alcohol'),
('what does cpu stand for \n:','central processing unit','Central Processing unit'),
('is water a molecule or compound \n:','a compound','Compound'),
('what is the italian word for pie? \n:','pizza','Pizza'),
(' Which Australian marsupial enjoy eating eucalyptus leaves\n:','koala','Koala'),
('Which Russian town suffered an infamous nuclear disaster in 1986?\n:','chernobyl','Chernobyl'),
('Which planet shares its name with a famous disney dog?\n:','pluto','Pluto'),
('Which sea creature has three hearts?\n:','octopus','an Octopus')]

questionsNM=[('What is the capital of Australia \n:','canberra','Canberra'),
('how is the color yellow made, ~hint: write as a equation \n:','blue + green','green + blue'),
('define the acronym USB \n:','Universal Serial Bus','universal serial bus'),
('what is currently the hottest chillie pepper on the scovile scale\n:','the carolina reaper','Carolina Reaper'),
("what is the main ingredint used to make barbecue sauce's flavour\n:","tomatoes","Tomatoes"),
('what is the atomic symbol for gold \n:', 'au','Au'),
('what country is below england','france','France'),
('what company founded the "Android" os for smartphones','google','Google')]

questionsHD = [('who was the original founder of the famous "Harvard College ~be sure to use capitals~\n: ','John Harvard','john harvard'),
('what is the top line of a Dvorak keyboard \n:','pyfgcrl','PYFGCRL'),
("what is saturns largest moon's name \n:","titan","Titan"),
('what is the adress limit of 8-bit CPUs\n:','16','16 adress'),
('what was the first computer virus in the DOS system\n:','the brain virus','brain virus'),
('what company had its GUI interface concept from Steve Jobs\n:','Xerox','xerox'),
('Which company doesnt have thier headquaters in the Silicon Valley\n:','IBM','ibm'),
('what is the first system that boots up when s pc is turned on\n:','bios','rom bios'),
('what is the difference between HTTP & HTTPS\n:','HTTPS is secure whereas HTTP is not','HTTP is unsecured while HTTPS is secured.'),
('what does mbp/s \n:','Million bits per second','million bits per second'),]


    
def run_quizE():
    skip_power=2 
    answered={}
    lives=3
    power=0
        
        
        # this loops through list, but each element of list is actually
        # a question+answer as u can see above, as a tuple. (1,2,3) that is tuple.
        #( question , answer ) = ('how much is 1+1?','2')
    introduction = print("this is a quiz game. get 2 questions right in a row and you can skip a question or 2 depending on how many you got correct \n")

    player1 = input("\nWhat is your name player?\n:")
    for question,answer,oranswer in questionsEZ:
        answered[question]=False #Dictionary of answers right/wrong/skipped, key to False


            
        print('Power:',power,'Lives:',lives,'player:',player1)
            
            #Check if power is equal or more than 'skip_power' - required to skip number
            #And then just print to notify that ability to skip is there.
        if power>=skip_power:print('Press "Y" to skip following question and pay '+str(skip_power)+' power.\n')
            
        ans=input(question)
        if ans==answer:
            power+=1
            answered[question]=True #Dictionary key that was set to false, is now True.
            print('Correct answer, power + 1.\n')
            
            #elif - if answer was not right, but it was 'Y', and power is enough to skip, we just skip.
            #In a way, this is like a step before life lose, if two conditions are met:
            #'Y' and enough power.
        elif ans=='Y' and power>=skip_power: 
            print('\nSkipped question using '+str(skip_power)+' power (You currently have '+str(power)+' power).\n')
                #and so we dont take from lives, just from power, and for loop goes next.
            power-=skip_power
            answered[question]='Skipped'
            
        else:
            lives-=1
            print('Wrong answer, lives -1.\n')
            if lives==0:
                restart=input('Game over, restart? (Y\\N)')
                if restart=='Y':run_quiz()
                break
            
    print('Answers summary:\n','\n'.join(a+':'+str(answered[a]) for a in answered))
    restart=input('Finished, restart? (Y\\N)')
    if restart=='Y':
        run_quizE()

def run_quizN():
    skip_power=2 
    answered={}
    lives=3
    power=0
        
        
        # this loops through list, but each element of list is actually
        # a question+answer as u can see above, as a tuple. (1,2,3) that is tuple.
        #( question , answer ) = ('how much is 1+1?','2')
    introduction = print("this is a quiz game. get 2 questions right in a row and you can skip a question or 2 depending on how many you got correct \n")

    player1 = input("\nWhat is your name player?\n:")
    for question,answer,oranswer in questionsNM:
        answered[question]=False #Dictionary of answers right/wrong/skipped, key to False


            
        print('Power:',power,'Lives:',lives,'player:',player1)
            
            #Check if power is equal or more than 'skip_power' - required to skip number
            #And then just print to notify that ability to skip is there.
        if power>=skip_power:print('Press "Y" to skip following question and pay '+str(skip_power)+' power.\n')
            
        ans=input(question)
        if ans==answer:
            power+=1
            answered[question]=True #Dictionary key that was set to false, is now True.
            print('Correct answer, power + 1.\n')
            
            #elif - if answer was not right, but it was 'Y', and power is enough to skip, we just skip.
            #In a way, this is like a step before life lose, if two conditions are met:
            #'Y' and enough power.
        elif ans=='Y' and power>=skip_power: 
            print('\nSkipped question using '+str(skip_power)+' power (You currently have '+str(power)+' power).\n')
                #and so we dont take from lives, just from power, and for loop goes next.
            power-=skip_power
            answered[question]='Skipped'
            
        else:
            lives-=1
            print('Wrong answer, lives -1.\n')
            if lives==0:
                restart=input('Game over, restart? (Y\\N)')
                if restart=='Y':run_quiz()
                break
            
    print('Answers summary:\n','\n'.join(a+':'+str(answered[a]) for a in answered))
    restart=input('Finished, restart? (Y\\N)')
    if restart=='Y':
        run_quizN()

def run_quizH():
    skip_power=2 
    answered={}
    lives=3
    power=0
        
        
        # this loops through list, but each element of list is actually
        # a question+answer as u can see above, as a tuple. (1,2,3) that is tuple.
        #( question , answer ) = ('how much is 1+1?','2')
    introduction = print("this is a quiz game. get 2 questions right in a row and you can skip a question or 2 depending on how many you got correct \n")

    player1 = input("\nWhat is your name player?\n:")
    for question,answer,oranswer in questionsHD:
        answered[question]=False #Dictionary of answers right/wrong/skipped, key to False


            
        print('Power:',power,'Lives:',lives,'player:',player1)
            
            #Check if power is equal or more than 'skip_power' - required to skip number
            #And then just print to notify that ability to skip is there.
        if power>=skip_power:print('Press "Y" to skip following question and pay '+str(skip_power)+' power.\n')
            
        ans=input(question)
        if ans==answer:
            power+=1
            answered[question]=True #Dictionary key that was set to false, is now True.
            print('Correct answer, power + 1.\n')
            
            #elif - if answer was not right, but it was 'Y', and power is enough to skip, we just skip.
            #In a way, this is like a step before life lose, if two conditions are met:
            #'Y' and enough power.
        elif ans=='Y' and power>=skip_power: 
            print('\nSkipped question using '+str(skip_power)+' power (You currently have '+str(power)+' power).\n')
                #and so we dont take from lives, just from power, and for loop goes next.
            power-=skip_power
            answered[question]='Skipped'
            
        else:
            lives-=1
            print('Wrong answer, lives -1.\n')
            if lives==0:
                restart=input('Game over, restart? (Y\\N)')
                if restart=='Y':run_quiz()
                break
            
    print('Answers summary:\n','\n'.join(a+':'+str(answered[a]) for a in answered))
    restart=input('Finished, restart? (Y\\N)')
    if restart=='Y':
        run_quizH()
def decision():
    choice = input("what difficulty would yiou like to play on |easy|normal|hard| \n:")
    if choice =="hard":
        run_quizH()
    if choice =="normal":
        run_quizN()
    if choice == "easy":
        run_quizE()
decision()
