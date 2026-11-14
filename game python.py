s=8
i=0
while i<3:
    g=int(input("GUESS the number : "))
    i+=1
    if g==s:
        print("YOU WON!!!!!! ˘⌣˘ʃ")
        break
    else:
        print("You lost! Better luck next time")
