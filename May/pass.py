import random

chars1 = "abcdefghijklmnopqrstuvwxyz123456789"
chars2 = "!#€%&/=?"

def main(): #define main that takes in info ab password and eventually prints it too
    length = int(input("how long? "))
    special = input("special characters? (yes/no) ").strip().lower()
    print(password(length, special)) #print password(with desired traits)

def password(length, special): #define password generator
    pool = chars1 
    if special == "yes":
        pool = chars1 + chars2 # use both pools if user wants special chasracters
    result = "" #start off empty to loop taking (length) amount characters from the pool
    for x in range(length): #create the actual loop
        result += random.choice(pool) #continue adding characters till you have the right amount of characters
    return result #return it to main

main()
