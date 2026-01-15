import tkinter as tk
import random


windo = tk.Tk()
windo.title("Guessing Game")
windo.geometry("350x350")
windo.config(bg="black")



#FUN FOR CHECK THE UMBER IS RIGHT OR WRONGE
def check_number():
    Ai_number = random.randint(1,5)

    num = userInput.get()


    if not num.isdigit:
        outputBox.config(text="only enter number")
    elif num== None:
        outputBox.config(text="enter number")



    num = int (num)

    if num == Ai_number:
        outputBox.config(text="correct! you win this game",fg="green")
        userInput.delete(0,tk.END)
    elif num > Ai_number:
        outputBox.config(text="too high ! number you guess",fg="red")
        userInput.delete(0,tk.END)


    else :
        outputBox.config(text="too low ! number you guess",fg="red")
        userInput.delete(0,tk.END)









#Tittal lable
lableBox = tk.Label(windo,text="WELCOM TO GUESS GAME...",font=("Arial",14),bg="black",fg="white")
lableBox.pack(pady=10)

#input instruction
instBox = tk.Label(windo,text="guess (1 to 5) number....",font=("Arial",10),bg="black",fg="white")
instBox.pack(pady=5)

#input box
userInput = tk.Entry(windo,font=("Arial",20),bg="black",fg="white",justify="center",insertbackground="white")
userInput.pack(pady=5)


#check btn
submit = tk.Button(windo,text="PLAY",font=("Arial",12),width=10,command=check_number,bg="green",fg="white")
submit.pack(pady=5)

#out box
outputBox = tk.Label(windo,text="",font=("Arial",13),bg="black")
outputBox.pack(pady=5)

windo.mainloop()



