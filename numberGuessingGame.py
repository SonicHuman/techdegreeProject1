import random

def start_game():
    print("""
                     (
                    ( )
                   (   )
         _________________________              
         \     |           |     /
          | THE CAULDRON OF DOOM |
          |    |           |     |
          |    |           |     |
          \____| |       | |____/
               |_|       |_|
                 | |   | |  
                 |_|| ||_|
                    | |
                    |_|




    PREDICT THE DIVINE NUMBER IN THE CAULDRON AND ASCEND.........
    
    ELSE..
    
    THOU SHALT DESCEND INTO THE DEPTHS OF DESPAIR...MUAHAHAHAHAHA!!!!

    BE FOREWARNED, YOU MAY ONLY GUESS THRICE TIMES!
    """)
    print("\nHARK!!! WHICH NUMBERRR HAVE I CONJURRRED IN THE CAULDRON??!!")
    answer = random.randrange(1000)


start_game()
