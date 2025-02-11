import random

def play(): 
    r_score =[] # Saves the score of every round
    round = 0
    while True:
        try:
            level = input("Enter level (1-easy 2- medium 3-hard) ->\t")
            if level in ['1','2','3']:
                break
            else:
                raise  ValueError
        except ValueError:
            print("Invalid level. Please enter 1, 2, or 3")

    while True:
        word = gword(level)   
        final = ["0"] * len(word) #list to append the correct letters
        n = len(word)
        chances = 6
        round +=1

        print(f"Round -> {round}")

        while (n>0):
            try:
                inp = input("Enter the letter -> ").lower()

                if not inp.isalpha() or len(inp) != 1:
                    raise ValueError("Invalid input. Please enter a single letter from a to z.")
                if (chances>0 and n>0):
                    if inp in word:
                        final[word.index(inp)] = inp 
                        print(final)
                        word[word.index(inp)] = 0
                        print(f"Correct!! chances -> {chances}")
                        n-=1

                    else:
                        chances -=1
                        print(f"Incorrect!! chances -> {chances}") 
                else:
                    break
                
            except ValueError as e:
                print(e)
                continue
            print(n)
            
        if chances > 0:
            print("you won")
            r_score.append(chances)

        else:
            print("you lost")
            break 
        
        choice   = input("e - exit || any to continue next")
        if choice == 'e':
            break 
    
    gscore(r_score)

def gword(level):
    words = {
        '1': ["cat", "dog", "rat", "pig"],
        '2': ["apple", "plane", "train", "house"],
        '3': ["elephant", "computer", "building", "mountain"]
    }
    return list(random.choice(words.get(str(level), words['1'])))

def gscore(r_score):
    sc_list = {1:5000,2:10000,3:15000,4:20000,5:25000,6:30000}
    score = 0
    for i in r_score:
        score += sc_list[i]
    print(f"Your Score is {score}")

def seescore():
    pass

def main():
    print("\n\t\t\t\t\tWelcome to Hangman Game")
    while True:
        try:
            choose = input("Enter P - Play | S - See Score -> \t").upper()

            if choose == "P" or choose == "S":
                break

            else:
                raise ValueError
        except:
            print("Invalid input!!! Enter P or S")


    if choose =='P':
        play()
    else:
        seescore()


if __name__ == "__main__":
    main()