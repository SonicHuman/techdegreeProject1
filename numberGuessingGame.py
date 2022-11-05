import random
count = 0

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
    OF MADNESS, MISERY, AND LIFE IMMORTAL.
    THINE CUNNING AND WIT CAN GUIDE THEE OUT..
    OR LEAD YE TO CERTAIN DESPAIR AND DOUBT.

    NUMBERED 1 TO 20, THE CRYPTS PORTEND.. 
    NAME THE DIVINE NUMBER IN THE CAULDRON AND ASCEND!

    NAME IT NOT AFTER THRICE GUESSES, YE MUST BEGIN AGAIN..
    THIS RIDDLE AND THY WIT ARE YOUR ONLY FRIENDS!  

    IF 6 CONJURINGS COME TO PASS THOU HAST SEALED THINE OWN FATE..
    666 YEARS OF SOLITUDE IN THE CRYPT AWAIT.......
    
    AAAAAAAAAHAHAHAAAAA!!!!

    """)
    
    #generate random number and store the answer
    answer = random.randrange(20)
    #print(answer)

    # #continuously prompt player for guess until they guess correctly
    # while guess != answer and count < 3:
    # #     #handle non-numeric input
    #      try:
    #          guess = int(input("\nHARK!!! WHICH NUMBERRR HAVE I CONJURRRED IN THE CAULDRONNNN??!!"))
    #      except ValueError:
    #          print("BLASPHEMY!!  THOU SHALT CHOOSE A NUMBER, KNAVE..")
    #          continue
        
    #     #handle guesses out of range
    #     if guess > 20 or guess < 1:
    #         #easter egg
    #         if guess == 666:
    #             print("""
    #           IMPOSTER!!!!  
    #           IT CANNOT BE!!! 
    #           HOW HAS YE DIVINED THE MASTER CRYPT KEY TO ASCENSION???!!! 
              
    #           NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    #              OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    #                   OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!!

    #            YOU HAVE ASCENDED OUT OF THE PORTAL THROUGH A SECRET CRYPT!  WELL DONE!


    #            YOU SEE TREES, SUNSHINE, AND HEAR BIRDS CHIRPING :)
    #               """)
    #         break

    #         else:
    #             print("FIEND!!  THOU SHALT CHOOSE BUT ONE OF THE CRYPT NUMBERS..")
    #             continue
        
    #     #keep count of their legit guess
    #     count +=1

    #     #check their legit guess with the answer
    #     if guess > answer:
    #         print("A FALSEHOOD!  THY NUMBER IS TOO LARGE...CHOOSE AGAIN!")
    #         continue
    #     elif guess < answer:
    #         print("A FALSEHOOD!  THY NUMBER IS TOO SMALL...CHOOSE AGAIN!")
    #         continue



start_game()
