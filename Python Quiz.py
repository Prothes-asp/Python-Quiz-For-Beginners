print("Are You Play a Quiz ??")
print("Note : Spelling Must be a Correct . Otherwise Wrong Answer !\n")

score = 0
Questions_no = 0

Welcome_ask = input("Are You Sure Play This Quiz ? Start For Yes/Y Otherwise No/N : ").lower()
if Welcome_ask == "yes" or Welcome_ask == "y":
    print("Welcome ! Let's Start Now this Game.... \n")

    # Questions No ---- 1
    Questions_no +=1
    Question = input(f"{Questions_no}. CPU means : ").lower()
    if Question == "central processor unit":
        score +=1
        print("   Correct Answer !\n")
    else:
        print("   Wrong Answer !")
        print("   Correct Answer is : Central Processor Unit\n")




    # Questions No---- 2
    Questions_no +=1
    Question = input(f"{Questions_no}. IP means : ").lower()
    if Question == "internet protocol":
        score+=1
        print("   Correct Answer !\n")
    else:
        print("   Wrong Answer !")
        print("   Correct Answer is : Internet Protocol\n")



    # Questions No ---- 3
    Questions_no +=1
    Question = input(f"{Questions_no}. RAM means : ").lower()
    if Question == "random access memory":
        score +=1
        print("   Correct Answer !\n")
    else:
        print("   Wrong Answer !")
        print("   Correct Answer is : Random Access Memory\n")




    # Question No --- 4
    Questions_no+=1
    Question = input(f"{Questions_no}. ROM means : ").lower()
    if Question == "read only memory":
        score+=1
        print("   Correct Answer !\n")
    else:
        print("   Wrong Answer !")
        print("   Correct Answer is : Read Only Memory\n")




    # Questions No --- 5
    Questions_no +=1
    Question = input(f"{Questions_no}. ALU means : ").lower()
    if Question == "arithemetic logic unit":
        score+=1
        print("   Correct Answer !\n")
    else:
        print("   Wrong Answer !")
        print("   Correct Answer is : Arithemetic Logic Unit\n")




    # Questions No ---- 6
    Questions_no+=1
    Question = input(f"{Questions_no}. OS means : ").lower()
    if Question == "operating system":
        score+=1
        print("   Correct Answer !\n")
    else:
        print("   Wrong Answer !")
        print("   Correct Answer is : Operating System\n")



    # Questions No ---- 7
    Questions_no+=1
    Question = input(f"{Questions_no}. WWW means : ").lower()
    if Question == "world wide web":
        score+=1
        print("   Correct Answer !\n")
    else:
        print("   Wrong Answer !")
        print("   Correct Answer is : World Wide Web\n")




    # Question No --- 8
    Questions_no+=1
    Question = input(f"{Questions_no}. VPN means : ").lower()
    if Question == "virtual private network":
        score+=1
        print("   Correct Answer !\n")
    else:
        print("   Wrong Answer !")
        print("   Correct Answer is : Virtual Private Network\n")




    # Question No --- 9
    Questions_no +=1
    Question = input(f"{Questions_no}. HTML means : ").lower()
    if Question == "hyper text markup language":
        score+=1
        print("   Correct Answer !\n")
    else:
        print("   Wrong Answer !")
        print("   Correct Answer is : Hyper Text Markup Language\n")




    # Question No ---- 10
    Questions_no+=1
    Question = input(f"{Questions_no}. CSS means : ")
    if Question == "cascading style sheet":
        score+=1
        print("   Correct Answer !\n")
    else:
        print("   Wrong Answer !")
        print("   Correct Answer is : Cascading Style Sheet\n")



    # Questions No --- 11
    Questions_no +=1
    Question = input(f"{Questions_no}. VGA means : ").lower()
    if Question == "visual graphic adaptor":
        score+=1
        print("   Correct Answer !\n")
    else:
        print("   Wrong Answer !")
        print("   Correct Answer is : Visual Graphic Adaptor\n")



    # Questions No --- 12
    Questions_no +=1
    Question = input(f"{Questions_no}. PC means : ").lower()
    if Question == "personal computer":
        score +=1
        print("   Correct Answer !\n")
    else:
        print("   Wrong Answer !")
        print("   Correct Answer is : Personal Computer\n")


    # Questions No --- 13
    Questions_no +=1
    Question = input(f"{Questions_no}. USB means : ").lower()
    if Question == "universal serial board":
        score+=1
        print("   Correct Answer !\n")
    else:
        print("   Wrong Answer !")
        print("   Correct Answer is : Universal Serial Board\n")



    # Questions ----- 14
    Questions_no += 1
    Question = input(f"{Questions_no}. BIOS means  : ").lower()
    if Question == "basic input and output system":
        score+=1
        print("   Correct Answer !\n")
    else:
        print("   Wrong Answer !")
        print("   Correct Answer is : Basic Input And Output System\n")



    # Questions ----- 15
    Questions_no +=1
    Question = input(f"{Questions_no}. IDE means : ").lower()
    if Question == "integrated drive electronics":
        score+=1
        print("   Correct Answer !\n")
    else:
        print("   Wrong Answer !")
        print("   Correct Answer is : Integrated Drive Electronics\n")





else:
    print("Ok . Thank You....... ")
    quit()


# Print Total Questions And Total Correct Answer.....
print(f"Total Questions is = {Questions_no}")
print(f"Total Correct Answer is = {score}")



# Calculation Total Your Score.........
try:
    percentage = (score*100)/Questions_no
    print(f"Your Score is  = {percentage}%")
except Exception:
    print("Your Score is =  0.0%")


