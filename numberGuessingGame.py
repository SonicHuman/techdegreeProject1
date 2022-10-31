import random

def start_game():
    print("""
                     (
                    ( )
                   (   )    
         \                      /
          |                    |
          |THE CAULDRON OF DOOM|
          |_                 __|
            |           __  |
            | _   ___  |  | |
             U | |   | |  | |
               | |    U   | | 
               | |        | |
               | |         U 
               | |
               | |
                U
    
    PREDICT THE DIVINE NUMBER IN THE CAULDRON AND ASCEND.........
    
    ELSE..
    
    THOU SHALT DESCEND INTO THE DEPTHS OF DESPAIR...MUAHAHAHAHAHA!!!!

    BE FOREWARNED, YOU MAY ONLY GUESS THRICE TIMES!
    """)
    print("\nHARK!!! WHICH NUMBERRR HAVE I CONJURRRED IN THE CAULDRON??!!")
    answer = random.randrange(1000)


start_game()
