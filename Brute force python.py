import random
import pyautogui
character="0123456789"
character_list=list(character)
c=0
password=pyautogui.password("Enter password here: ")
guess_password=''
while(guess_password!=password):
    guess_password=random.choices(character_list,k=len(password))

    print("<"+str(guess_password)+">")
    c+=1
    
    if(guess_password==list(password)):
        print("Your Password is:"+"".join(guess_password))
        print("Loop count:",c)
        break
