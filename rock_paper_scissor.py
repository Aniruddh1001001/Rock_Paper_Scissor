from tkinter import *
from PIL import Image,ImageTk
from random import randint

game= Tk()
game.title("Rock paper scissor")
game.geometry("675x550")

#background
image = Image.open("john wick.jpg")
rotated_image = image.rotate(90)

photo = ImageTk.PhotoImage(rotated_image)

label1 = Label(game, image=photo)
label1.place(x=0, y=0, relwidth=1, relheight=1)

label1.image = photo

#other images
rock_imag= ImageTk.PhotoImage(Image.open("rock.jpeg"))
paper_imag= ImageTk.PhotoImage(Image.open("paper.jpeg"))
scissor_imag= ImageTk.PhotoImage(Image.open("scissor.jpeg"))
rock_com_imag= ImageTk.PhotoImage(Image.open("rock_com.jpeg"))
paper_com_imag= ImageTk.PhotoImage(Image.open("paper_com.jpeg"))
scissor_com_imag= ImageTk.PhotoImage(Image.open("scissor_com.jpeg"))
com_indicator= Label(game,text="Computer",fg="white",bg="purple",height=2,width=8).grid(row=0,column=1)
player_indicator= Label(game,text="You",fg="white",bg="purple",height=2,width=6).grid(row=0,column=3)
#load the image
user_lable= Label(game,image=rock_imag)
com_lable= Label(game,image=rock_com_imag)
user_lable.grid(row=1, column=4)
com_lable.grid(row=1,column=0 )
#score
player= Label(game,text="0",font=100,bg="#9b59b6",fg="white")
player.grid(row=1,column=2)
com = Label(game,text="0",font=100,bg="#9b59b6",fg="white")
com.grid(row=1,column=1) 
WinorLose= Label(game,text="",font=50,bg="purple",fg="White")
Label(game,text="").grid(row=4)
WinorLose.grid(row=5,column=1)

choices = ["Rock","Paper","Scissor"]

def updatemsg(q):
    WinorLose.config(text=q)

def updateplayerscore():
    score = int(player['text'])
    score+=1
    player.config(text=str(score))

def updatecompscore():
    score = int(com['text'])
    score+=1
    com.config(text=str(score))

def checkwin(x,Y):
    if x==Y:
        updatemsg("it's a tie")
    elif x=="Rock":
        if Y== "Paper":
            updatemsg("you Loose")
            updatecompscore()
        elif Y== "Scissor":
            updatemsg("You Win")
            updateplayerscore()
    elif x=="Paper":
        if Y=="Scissor":
            updatemsg("you Loose")
            updatecompscore()
        else:
            updatemsg("you Win")
            updateplayerscore()
    elif x=="Scissor":
        if Y=="Rock":
            updatemsg("you Loose")
            updatecompscore()
        else:
            updatemsg("You Win")
            updateplayerscore()

def selection(x):
#com
    Y= choices[randint(0,2)]

    if Y=="Paper":
        com_lable.configure(image=paper_imag)
    elif Y == "Scissor":
        com_lable.configure(image=scissor_imag)
    elif Y=="Rock":
        com_lable.configure(image=rock_imag)
#player
    if x=="Paper":
        user_lable.configure(image=paper_imag)
    elif x == "Scissor":
        user_lable.configure(image=scissor_imag)
    elif x=="Rock":
        user_lable.configure(image=rock_imag)

    checkwin(x, Y)


#button
Label(game,text="").grid(row=2)
paper = Button(game, width=20, height=2, text="Paper", fg="black", bg="sky blue",activebackground="yellow",command= lambda :selection("Paper") )
paper.grid(row=3, column=1)
scissor = Button(game, width=20, height=2, text="Scissor", fg="black", bg="yellow",activebackground="red",command= lambda :selection("Scissor") )
scissor.grid(row=3, column=3)
rock = Button(game, width=20, height=2, text="Rock", fg="black", bg="red",activebackground="sky blue",command= lambda :selection("Rock"))
rock.grid(row=3, column=0)


game.mainloop()