def number_guessing_ai():    
    print("Pick a number in range of 1 to 1000 and I will guess it in maximum of 10 moves.")
    max = 1000
    min = 0
    for i in range(10):
        guess = int((max - min)/2) + min
        print(f"My guess is {guess}.")
        print("Was I correct?")
        print("(a) No, too big!")
        print("(b) No, too small!")
        print("(c) Yes! You won!")
        clue = input("Answer (a,b or c): ")
        if clue == "a":
            max = guess
        elif clue == "b":
            min = guess
        elif clue == "c":
            print("Yey, I guessed! That was fun!")
            return None
            
    print("You must have cheated!!!")


number_guessing_ai()