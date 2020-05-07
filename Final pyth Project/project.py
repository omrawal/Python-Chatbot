from tkinter import *
from tkinter import messagebox
from gtts import gTTS
from PIL import ImageTk, Image
import os
import re
import playsound
import random
# import datetime


def rock():             #if user selects rock than select random input for computer
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'rock'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


def paper():            #if user selects paper than select random input for computer
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'paper'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


def scissor():          #if user selects scissor than select random input for computer
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'scissor'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


def reset():            #make score of both user and computer as zero and restart game
        global USER_SCORE
        global COMP_SCORE
        USER_SCORE = 0
        COMP_SCORE = 0
        result("rock", "rock")


def choice_to_number(choice):                       #conversion of choice to number for easy of programing
        rps = {'rock': 0, 'paper': 1, 'scissor': 2}
        return rps[choice]

def number_to_choice(number):                       #conversion of number to choice for easy of programing
    rps = {0: 'rock', 1: 'paper', 2: 'scissor'}
    return rps[number]

def random_computer_choice():                       #function to select random choice
    return random.choice(['rock', 'paper', 'scissor'])

def result(human_choice, comp_choice):              #mainframe of rockpaperscissor game
    global USER_SCORE
    global COMP_SCORE
    global window1
    user = choice_to_number(human_choice)
    comp = choice_to_number(comp_choice)
    if(user == comp):
        pass
        # print("Tie")
    elif((user-comp) % 3 == 1):
        # print("You win")
        USER_SCORE += 1
    else:
        # print("Comp wins")
        COMP_SCORE += 1
    text_area = Text(window1, height=6, width=30, bg="#FFFF99")
    text_area.grid(column=0, row=4)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(
            uc=USER_CHOICE, cc=COMP_CHOICE, u=USER_SCORE, c=COMP_SCORE)
    text_area.insert(END, answer)
    text_area.place(x=140, y=400)
    if(USER_SCORE == 10 and COMP_SCORE == 10):
        flag = messagebox.askyesno(
                "Game Tie", "Tough Fight!!!! GAME TIED!!!!\n Do You Wish to Play Again?")
        if(flag == 1):
            reset()
        else:
            window1.destroy()
            run()
    elif(USER_SCORE == 10):
        flag = messagebox.askyesno(
                "User Wins", "CONGRATULATIONS!!!! YOU WON!!!!\n Do You Wish to Play Again?")
        if(flag == 1):
            reset()
            run()
        else:
            window1.destroy()
            run()
    elif(COMP_SCORE == 10):
        flag = messagebox.askyesno(
                "Computer Wins", "SORRY!!!! YOU LOST!!!!\n Do You Wish to Retry?")
        if(flag == 1):
            reset()
        else:
            window1.destroy()
            run()


def createframe(s):                     #frame creation
    window = Tk()
    window.title(s)
    window.geometry("500x700")
    return window




def rpsclicked(win_to_dest):            #executed chen RockPaperScissor button is clicked
    win_to_dest.destroy()
    global window1
    window1 = createframe("Rock Paper Scissors Game")

    rock_im = Image.open("rock.jpg")
    rock_img = ImageTk.PhotoImage(rock_im)

    paper_im = Image.open("paper.jpg")
    paper_img = ImageTk.PhotoImage(paper_im)

    scissor_im = Image.open("scissor.jpg")
    scissor_img = ImageTk.PhotoImage(scissor_im)

    load = Image.open("sps.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(window1, image=render)
    img.image = render
    img.config(height=370, width=440)
    img.place(x=20, y=20)
    bt_rock = Button(window1, image=rock_img, command=rock)
    bt_rock.place(x=80, y=500)
    bt_rock.config(height=110, width=110)

    bt_paper = Button(window1, image=paper_img, command=paper)
    bt_paper.place(x=200, y=500)
    bt_paper.config(height=110, width=110)

    bt_scissor = Button(window1, image=scissor_img, command=scissor)
    bt_scissor.place(x=320, y=500)
    bt_scissor.config(height=110, width=110)

    bt_reset = Button(window1, text="Reset", command=reset)
    bt_reset.place(x=250, y=650)
    bt_reset.config(height=1, width=5)

    bt_home = Button(window1, text="Home", command=lambda:homeclicked(window1))
    bt_home.place(x=100, y=650)
    bt_home.config(height=1, width=5)

    window1.mainloop()

def hclicked(txt, TXT):                     # executed when listen is clicked no chatbot only text to speech
    language = "en"
    output = gTTS(text=txt, lang=language, slow=False)
    output.save("v1.mp3")
    playsound.playsound("v1.mp3", True)
    os.remove("v1.mp3")
    TXT.delete(0, END)
    pass


def hclickedchat(txt, TXT):                 # real chatbot code 
    language = "en"
    q = open("questions.txt", 'r')
    a = open("answers.txt", 'r')
    ql = q.readlines()
    al = a.readlines()
    s = txt
    s = s.lower()
    flag = 0
    for i in range(0, len(ql)):
        ql[i] = ql[i][:-1]
        k = re.search(ql[i], s)
        if(k != None):
            flag = 1
            answer = al[i]
            break
    if(flag != 1):                          # if no match than say default of command not recognized
        answer = al[-1]
    outp = gTTS(text=answer, lang=language, slow=False)
    outp.save("v2.mp3")
    playsound.playsound("v2.mp3", True)
    os.remove("v2.mp3")
    # os.system("start v1.mp3")
    TXT.delete(0, END)
    pass

def homeclicked(win_to_dest):               # toggle effect
    win_to_dest.destroy()
    run()


def gttsclicked(win_to_dest):               # mainframe of chatbot
    win_to_dest.destroy()
    window = createframe("Hermione")
    wq = Label(window, bg="ivory", fg="darkgreen", text="Enter the note: ")
    wq.place(x=10, y=30)
    txt = Entry(window, width=40)
    txt.place(x=110, y=30)
    bth = Button(window, text="Listen!!",
                 command=lambda: hclicked(txt.get(), txt))
    bth.place(x=200, y=60)
    w = Label(window, bg="ivory", fg="darkgreen",
              text="Talk to Hermoine (Chatbot) <BETA> ")
    w.place(x=100, y=150)
    wq = Label(window, bg="ivory", fg="darkgreen", text="Enter your part: ")
    wq.place(x=10, y=190)
    txtc = Entry(window, width=40)
    txtc.place(x=110, y=190)
    btc = Button(window, text="Let me hear you!!",
                 command=lambda: hclickedchat(txtc.get(), txtc))
    btc.place(x=110, y=240)

    bt_home = Button(window, text="Home", command=lambda:homeclicked(window))
    bt_home.place(x=250, y=650)
    bt_home.config(height=1, width=5)

    pass


def run():                                          # function called to start the application so as to aid toggle effect
    Start_window = createframe("Tkinter Mobile")
    wq = Label(Start_window)

    bt = Button(Start_window, text="Hear Hermione Speak", command=lambda:gttsclicked(Start_window))
    bt.grid(column=0, row=0)
    bt.place(x=250, y=70)
    bt.config(height=3, width=18)

    # ,command=rpsclicked
    cbt = Button(Start_window, text="Play Rock Paper Scizzor", command=lambda:rpsclicked(Start_window))
    cbt.grid(column=0, row=0)
    cbt.place(x=250, y=300)
    cbt.config(height=3, width=18)

    load = Image.open("hermione1.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(Start_window, image=render)
    img.image = render
    img.config(height=150, width=150)
    img.place(x=20, y=20)

    load = Image.open("rps.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(Start_window, image=render)
    img.image = render
    img.config(height=150, width=150)
    img.place(x=20, y=250)

    Start_window.mainloop()

USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""
window1=None
run()