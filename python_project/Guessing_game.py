the_number = 8
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

print("  => Guessing_game <=")
print("  _you have 3 chance_  ")

while guess != the_number and not out_of_guess: 
    if guess_count < guess_limit:
        guess = int(input("- Enter a number betwen 1 and 10 : "))
        guess_count += 1
    else : 
        out_of_guess = True

if out_of_guess ==True:
     print(" you lose the correct number is 8 ")
else:
    print (" ===> you win <=== ")


       
      
