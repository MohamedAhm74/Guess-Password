# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess --
# ----------------------------

print("\t\t\t\t" + "=" * 60)
print("\t\t\t\t===================== Password Guess =======================" )
print("\t\t\t\t" + "=" * 60)

tries = 5

mainPass = "Mohamed4"

userPass = input("Write Your Password : ")

while mainPass != userPass  :

    tries -= 1

    print (f"Worng Password ,  { 'Last ' if tries == 0 else tries} Chace left ")
    userPass = input("Write Your Exepted Password : ")

    if userPass == mainPass:
        print("=====>"+" Good Job The Password is True " +"<=====")

    if tries == 0:
        print("========>"+" Thank You For Your Tries "+"<=======")
        print("=====>"+" You don't have any tries left " +"<=====")
        break

else:
    print("===========>"+" Correct Password " +"<============")