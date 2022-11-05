import random

#print welcome message for game
def start_game():
    print("""
                      (
                     ( )
                    (   )
         ______   __      _________              
         \     | |  |    |        /
          | THE CAULDRON OF DOOM |
          |    | |  ||  |        |
          |    | |   | ||        |
          \____|||___| |_________/
               |||   |||
                ||    ||
                ||     |
                ||     |
                 |
                 |    
                 |

    THOU HAST ENTERED A FORSAKEN PORTAL..
    OF GAMES, MISERY, AND LIFE IMMORTAL.
    THINE CUNNING AND WIT CAN GUIDE THEE OUT..
    OR LEAD YE TO MADNESS AND DOUBT.

    NUMBERED 1 TO 20, THE CRYPTS PORTEND.. 
    DIVINE THE SACRED NUMBER IN THE CAULDRON AND ASCEND!

    DIVINE IT NOT, AND THOU MUST TRY AGAIN..
    THIS RIDDLE AND THY WIT ARE THINE ONLY FRIENDS!  

    IF YE FAIL 6 TIMES, THOU HAST SEALED THINE OWN FATE..
    AND 666 YEARS OF SOLITUDE IN THE CRYPT AWAIT!
    
    AAAAAAAAAHAHAHAAAAA!!!!


    """)

start_game()
prompt = input("SHALL WE BEGIN, THEN?   ")
if prompt.lower() == 'y' or prompt.lower() == 'yes':
    #generate random number and store the answer
    answer = random.randrange(20)
    #print(answer)
    guess = 0
    count = 0
    #continuously prompt player for a guess until they guess correctly
    while guess!=answer and count < 6:
    #handle non-numeric input
        try:
            if count == 5:
                print("\nLAST CHANCE, KNAVE..")
            guess = int(input("\nHARK KNAVE!!! WHAT NUMBER HAVE I CONJURED IN THE CAULDRON??!!  "))
        except ValueError:
            print(f"\nATTEMPTS {count} \nBLASPHEMY!!  THOU SHALT CHOOSE THE SHAPE OF A NUMBER, KNAVE..")
            continue    
        #handle guesses out of range
        if guess > 20 or guess < 1:
            #easter egg
            if guess == 666:
                print("""
                        IMPOSTER!!!!  
                        IT CANNOT BE!!! 
                        HOW HAST THEE DIVINED THE MASTER CRYPT KEY???!!! 
                    
                        NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                           OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                                OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!!

                        YOU SEE A SECRET CRYPT SUDDENLY MATERIALIZE NEXT TO THE CAULDRON..
                        YOU ARE ABLE TO BYPASS THE DEPRAVED CRYPT KEEPER WITHOUT PLAYING HIS LITTLE GUESSING GAME..
                        AND ASCEND THROUGH THE SECRET CRYPT BACK TO THE DOMAIN OF MORTALS!


                        YOU SEE TREES, SUNSHINE, AND HEAR BIRDS CHIRPING :)))........

                        ...
                        ..

                        YET SUDDENLY, IN YOUR ELATION, YOU SLIP AND FALL DOWN A CLIFF TO YOUR DOOM...
                        AND YOU HEAR THE CRYPT KEEPER'S LAUGH ECHOING IN YOUR HEAD AS EVERYTHING FADES TO BLACK..

                        AHAHAHAHAHAHAAAAA AHAHAHAHAHAHAAAAAAAA AHAHAHAHAHAAAAAAAAAAAAAAAAAAAAAAA!!!!!!!!!!!!!!
                          """)
                break
            print(f"\nATTEMPTS {count} \nFIEND!!!  THOU SHALT CHOOSE BUT ONE OF THE CRYPT NUMBERS, KNAVE..")
            continue
                
        #keep count of their legit guess
        count +=1

        #print message telling them they have failed and reached the max try limit
        if count > 5 and guess!=answer:
            print(f"""
            \n\n\nDOOMED ARE YE!!!!!!!!!  YOU HAVE ERRED AND STRAYED {count} TIMES...
            YE SHALL MAKE THINE OWN BED NOW IN CRYPT NUMBER {guess} FOR THE NEXT 666 YEARS!

            AHAHAHAHAHAHAHAHAHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!!!!!!!!!!!!!
            """)
            exit()

        #check their legit guess with the answer
        if guess > answer:
            print(f"\nTRIES {count} \nTHY NUMBER IS TOO LARGE...\n")
            continue
        elif guess < answer:
            print(f"\nTRIES {count} \nTHY NUMBER IS TOO SMALL...\n")
            continue
else:
    exit()


print(f"""
        \n\n\nYESSSSSSS KNAVE, {guess} IS THE CONJURED NUMBER....AFTER {count} ATTEMPTS, THOU MAY ASCEND..
      
        BE GONE WITH YE!
      """)
