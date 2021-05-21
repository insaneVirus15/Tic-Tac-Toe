from tkinter import *
from tkinter import messagebox
win = Tk()

win.geometry("300x350+535+170")
win.minsize(300, 350)
win.maxsize(300, 350)
win.title("TIC TAC TOE")
win.configure(background="black")


x = 1
def show(b):
    global x
    x = x + 1
    if (x % 2 == 0):
        if (b["text"] == ""):
            b["text"] = "0"

    else:
        if (b["text"] == ""):
            b["text"] = "X"


    if (b1["text"] == "0" and b2["text"] == "0" and b3["text"] == "0"):
        screen = Label(win, text="PLAYER 1 IS WINNER", font=("Arial", 14), bg="black", fg="white")
        screen.grid(row=0, column=0, columnspan=3)
        b1["bg"] = "light grey"
        b2["bg"] = "light grey"
        b3["bg"] = "light grey"

        ans = messagebox.askquestion("GAME END", "Do you want to play again?")
        if (ans == "no"):
            win.quit()
        if (ans == "yes"):
            b1["text"] = ""
            b1["bg"] = "white"
            b2["text"] = ""
            b2["bg"] = "white"
            b3["text"] = ""
            b3["bg"] = "white"
            b4["text"] = ""
            b4["bg"] = "white"
            b5["text"] = ""
            b5["bg"] = "white"
            b6["text"] = ""
            b6["bg"] = "white"
            b7["text"] = ""
            b7["bg"] = "white"
            b8["text"] = ""
            b8["bg"] = "white"
            b9["text"] = ""
            b9["bg"] = "white"

            screen = Label(win, text="START", font=("Arial", 14), height=2, width=20, background="black", fg="white")
            screen.grid(row=0, column=0, columnspan=3)

    elif (b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X"):
        screen = Label(win, text="PLAYER 2 IS WINNER", font=("Arial", 14), bg="black", fg="white")
        screen.grid(row=0, column=0, columnspan=3)
        b1["bg"] = "light grey"
        b2["bg"] = "light grey"
        b3["bg"] = "light grey"

        ans = messagebox.askquestion("GAME END", "Do you want to play again?")
        if (ans == "no"):
            win.quit()
        if (ans == "yes"):
            b1["text"] = ""
            b1["bg"] = "white"
            b2["text"] = ""
            b2["bg"] = "white"
            b3["text"] = ""
            b3["bg"] = "white"
            b4["text"] = ""
            b4["bg"] = "white"
            b5["text"] = ""
            b5["bg"] = "white"
            b6["text"] = ""
            b6["bg"] = "white"
            b7["text"] = ""
            b7["bg"] = "white"
            b8["text"] = ""
            b8["bg"] = "white"
            b9["text"] = ""
            b9["bg"] = "white"

            screen = Label(win, text="START", font=("Arial", 14), height=2, width=20, background="black", fg="white")
            screen.grid(row=0, column=0, columnspan=3)

    elif (b4["text"] == "0" and b5["text"] == "0" and b6["text"] == "0"):
        screen = Label(win, text="PLAYER 1 IS WINNER", font=("Arial", 14), bg="black", fg="white")
        screen.grid(row=0, column=0, columnspan=3)
        b4["bg"] = "light grey"
        b5["bg"] = "light grey"
        b6["bg"] = "light grey"

        ans = messagebox.askquestion("GAME END", "Do you want to play again?")
        if (ans == "no"):
            win.quit()
        if (ans == "yes"):
            b1["text"] = ""
            b1["bg"] = "white"
            b2["text"] = ""
            b2["bg"] = "white"
            b3["text"] = ""
            b3["bg"] = "white"
            b4["text"] = ""
            b4["bg"] = "white"
            b5["text"] = ""
            b5["bg"] = "white"
            b6["text"] = ""
            b6["bg"] = "white"
            b7["text"] = ""
            b7["bg"] = "white"
            b8["text"] = ""
            b8["bg"] = "white"
            b9["text"] = ""
            b9["bg"] = "white"

            screen = Label(win, text="START", font=("Arial", 14), height=2, width=20, background="black", fg="white")
            screen.grid(row=0, column=0, columnspan=3)

    elif (b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X"):
        screen = Label(win, text="PLAYER 2 IS WINNER", font=("Arial", 14), bg="black", fg="white")
        screen.grid(row=0, column=0, columnspan=3)
        b4["bg"] = "light grey"
        b5["bg"] = "light grey"
        b6["bg"] = "light grey"

        ans = messagebox.askquestion("GAME END", "Do you want to play again?")
        if (ans == "no"):
            win.quit()
        if (ans == "yes"):
            b1["text"] = ""
            b1["bg"] = "white"
            b2["text"] = ""
            b2["bg"] = "white"
            b3["text"] = ""
            b3["bg"] = "white"
            b4["text"] = ""
            b4["bg"] = "white"
            b5["text"] = ""
            b5["bg"] = "white"
            b6["text"] = ""
            b6["bg"] = "white"
            b7["text"] = ""
            b7["bg"] = "white"
            b8["text"] = ""
            b8["bg"] = "white"
            b9["text"] = ""
            b9["bg"] = "white"

            screen = Label(win, text="START", font=("Arial", 14), height=2, width=20, background="black", fg="white")
            screen.grid(row=0, column=0, columnspan=3)

    elif (b7["text"] == "0" and b8["text"] == "0" and b9["text"] == "0"):
        screen = Label(win, text="PLAYER 1 IS WINNER", font=("Arial", 14), bg="black", fg="white")
        screen.grid(row=0, column=0, columnspan=3)
        b7["bg"] = "light grey"
        b8["bg"] = "light grey"
        b9["bg"] = "light grey"

        ans = messagebox.askquestion("GAME END", "Do you want to play again?")
        if (ans == "no"):
            win.quit()
        if (ans == "yes"):
            b1["text"] = ""
            b1["bg"] = "white"
            b2["text"] = ""
            b2["bg"] = "white"
            b3["text"] = ""
            b3["bg"] = "white"
            b4["text"] = ""
            b4["bg"] = "white"
            b5["text"] = ""
            b5["bg"] = "white"
            b6["text"] = ""
            b6["bg"] = "white"
            b7["text"] = ""
            b7["bg"] = "white"
            b8["text"] = ""
            b8["bg"] = "white"
            b9["text"] = ""
            b9["bg"] = "white"

            screen = Label(win, text="START", font=("Arial", 14), height=2, width=20, background="black", fg="white")
            screen.grid(row=0, column=0, columnspan=3)

    elif (b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X"):
        screen = Label(win, text="PLAYER 2 IS WINNER", font=("Arial", 14), bg="black", fg="white")
        screen.grid(row=0, column=0, columnspan=3)
        b7["bg"] = "light grey"
        b8["bg"] = "light grey"
        b9["bg"] = "light grey"

        ans = messagebox.askquestion("GAME END", "Do you want to play again?")
        if (ans == "no"):
            win.quit()
        if (ans == "yes"):
            b1["text"] = ""
            b1["bg"] = "white"
            b2["text"] = ""
            b2["bg"] = "white"
            b3["text"] = ""
            b3["bg"] = "white"
            b4["text"] = ""
            b4["bg"] = "white"
            b5["text"] = ""
            b5["bg"] = "white"
            b6["text"] = ""
            b6["bg"] = "white"
            b7["text"] = ""
            b7["bg"] = "white"
            b8["text"] = ""
            b8["bg"] = "white"
            b9["text"] = ""
            b9["bg"] = "white"

            screen = Label(win, text="START", font=("Arial", 14), height=2, width=20, background="black", fg="white")
            screen.grid(row=0, column=0, columnspan=3)

    elif (b1["text"] == "0" and b4["text"] == "0" and b7["text"] == "0"):
        screen = Label(win, text="PLAYER 1 IS WINNER", font=("Arial", 14), bg="black", fg="white")
        screen.grid(row=0, column=0, columnspan=3)
        b1["bg"] = "light grey"
        b4["bg"] = "light grey"
        b7["bg"] = "light grey"

        ans = messagebox.askquestion("GAME END", "Do you want to play again?")
        if (ans == "no"):
            win.quit()
        if (ans == "yes"):
            b1["text"] = ""
            b1["bg"] = "white"
            b2["text"] = ""
            b2["bg"] = "white"
            b3["text"] = ""
            b3["bg"] = "white"
            b4["text"] = ""
            b4["bg"] = "white"
            b5["text"] = ""
            b5["bg"] = "white"
            b6["text"] = ""
            b6["bg"] = "white"
            b7["text"] = ""
            b7["bg"] = "white"
            b8["text"] = ""
            b8["bg"] = "white"
            b9["text"] = ""
            b9["bg"] = "white"

            screen = Label(win, text="START", font=("Arial", 14), height=2, width=20, background="black", fg="white")
            screen.grid(row=0, column=0, columnspan=3)

    elif (b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X"):
        screen = Label(win, text="PLAYER 2 IS WINNER", font=("Arial", 14), bg="black", fg="white")
        screen.grid(row=0, column=0, columnspan=3)
        b1["bg"] = "light grey"
        b4["bg"] = "light grey"
        b7["bg"] = "light grey"

        ans = messagebox.askquestion("GAME END", "Do you want to play again?")
        if (ans == "no"):
            win.quit()
        if (ans == "yes"):
            b1["text"] = ""
            b1["bg"] = "white"
            b2["text"] = ""
            b2["bg"] = "white"
            b3["text"] = ""
            b3["bg"] = "white"
            b4["text"] = ""
            b4["bg"] = "white"
            b5["text"] = ""
            b5["bg"] = "white"
            b6["text"] = ""
            b6["bg"] = "white"
            b7["text"] = ""
            b7["bg"] = "white"
            b8["text"] = ""
            b8["bg"] = "white"
            b9["text"] = ""
            b9["bg"] = "white"

            screen = Label(win, text="START", font=("Arial", 14), height=2, width=20, background="black", fg="white")
            screen.grid(row=0, column=0, columnspan=3)

    elif (b2["text"] == "0" and b5["text"] == "0" and b8["text"] == "0"):
        screen = Label(win, text="PLAYER 1 IS WINNER", font=("Arial", 14), bg="black", fg="white")
        screen.grid(row=0, column=0, columnspan=3)
        b2["bg"] = "light grey"
        b5["bg"] = "light grey"
        b8["bg"] = "light grey"

        ans = messagebox.askquestion("GAME END", "Do you want to play again?")
        if (ans == "no"):
            win.quit()
        if (ans == "yes"):
            b1["text"] = ""
            b1["bg"] = "white"
            b2["text"] = ""
            b2["bg"] = "white"
            b3["text"] = ""
            b3["bg"] = "white"
            b4["text"] = ""
            b4["bg"] = "white"
            b5["text"] = ""
            b5["bg"] = "white"
            b6["text"] = ""
            b6["bg"] = "white"
            b7["text"] = ""
            b7["bg"] = "white"
            b8["text"] = ""
            b8["bg"] = "white"
            b9["text"] = ""
            b9["bg"] = "white"

            screen = Label(win, text="START", font=("Arial", 14), height=2, width=20, background="black", fg="white")
            screen.grid(row=0, column=0, columnspan=3)

    elif (b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X"):
        screen = Label(win, text="PLAYER 2 IS WINNER", font=("Arial", 14), bg="black", fg="white")
        screen.grid(row=0, column=0, columnspan=3)
        b2["bg"] = "light grey"
        b5["bg"] = "light grey"
        b8["bg"] = "light grey"

        ans = messagebox.askquestion("GAME END", "Do you want to play again?")
        if (ans == "no"):
            win.quit()
        if (ans == "yes"):
            b1["text"] = ""
            b1["bg"] = "white"
            b2["text"] = ""
            b2["bg"] = "white"
            b3["text"] = ""
            b3["bg"] = "white"
            b4["text"] = ""
            b4["bg"] = "white"
            b5["text"] = ""
            b5["bg"] = "white"
            b6["text"] = ""
            b6["bg"] = "white"
            b7["text"] = ""
            b7["bg"] = "white"
            b8["text"] = ""
            b8["bg"] = "white"
            b9["text"] = ""
            b9["bg"] = "white"

            screen = Label(win, text="START", font=("Arial", 14), height=2, width=20, background="black", fg="white")
            screen.grid(row=0, column=0, columnspan=3)

    elif (b3["text"] == "0" and b6["text"] == "0" and b9["text"] == "0"):
        screen = Label(win, text="PLAYER 1 IS WINNER", font=("Arial", 14), bg="black", fg="white")
        screen.grid(row=0, column=0, columnspan=3)
        b3["bg"] = "light grey"
        b6["bg"] = "light grey"
        b9["bg"] = "light grey"

        ans = messagebox.askquestion("GAME END", "Do you want to play again?")
        if (ans == "no"):
            win.quit()
        if (ans == "yes"):
            b1["text"] = ""
            b1["bg"] = "white"
            b2["text"] = ""
            b2["bg"] = "white"
            b3["text"] = ""
            b3["bg"] = "white"
            b4["text"] = ""
            b4["bg"] = "white"
            b5["text"] = ""
            b5["bg"] = "white"
            b6["text"] = ""
            b6["bg"] = "white"
            b7["text"] = ""
            b7["bg"] = "white"
            b8["text"] = ""
            b8["bg"] = "white"
            b9["text"] = ""
            b9["bg"] = "white"

            screen = Label(win, text="START", font=("Arial", 14), height=2, width=20, background="black", fg="white")
            screen.grid(row=0, column=0, columnspan=3)

    elif (b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X"):
        screen = Label(win, text="PLAYER 2 IS WINNER", font=("Arial", 14), bg="black", fg="white")
        screen.grid(row=0, column=0, columnspan=3)
        b3["bg"] = "light grey"
        b6["bg"] = "light grey"
        b9["bg"] = "light grey"

        ans = messagebox.askquestion("GAME END", "Do you want to play again?")
        if (ans == "no"):
            win.quit()
        if (ans == "yes"):
            b1["text"] = ""
            b1["bg"] = "white"
            b2["text"] = ""
            b2["bg"] = "white"
            b3["text"] = ""
            b3["bg"] = "white"
            b4["text"] = ""
            b4["bg"] = "white"
            b5["text"] = ""
            b5["bg"] = "white"
            b6["text"] = ""
            b6["bg"] = "white"
            b7["text"] = ""
            b7["bg"] = "white"
            b8["text"] = ""
            b8["bg"] = "white"
            b9["text"] = ""
            b9["bg"] = "white"

            screen = Label(win, text="START", font=("Arial", 14), height=2, width=20, background="black", fg="white")
            screen.grid(row=0, column=0, columnspan=3)

    elif (b1["text"] == "0" and b5["text"] == "0" and b9["text"] == "0"):
        screen = Label(win, text="PLAYER 1 IS WINNER", font=("Arial", 14), bg="black", fg="white")
        screen.grid(row=0, column=0, columnspan=3)
        b1["bg"] = "light grey"
        b5["bg"] = "light grey"
        b9["bg"] = "light grey"

        ans = messagebox.askquestion("GAME END", "Do you want to play again?")
        if (ans == "no"):
            win.quit()
        if (ans == "yes"):
            b1["text"] = ""
            b1["bg"] = "white"
            b2["text"] = ""
            b2["bg"] = "white"
            b3["text"] = ""
            b3["bg"] = "white"
            b4["text"] = ""
            b4["bg"] = "white"
            b5["text"] = ""
            b5["bg"] = "white"
            b6["text"] = ""
            b6["bg"] = "white"
            b7["text"] = ""
            b7["bg"] = "white"
            b8["text"] = ""
            b8["bg"] = "white"
            b9["text"] = ""
            b9["bg"] = "white"

            screen = Label(win, text="START", font=("Arial", 14), height=2, width=20, background="black", fg="white")
            screen.grid(row=0, column=0, columnspan=3)

    elif (b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X"):
        screen = Label(win, text="PLAYER 2 IS WINNER", font=("Arial", 14), bg="black", fg="white")
        screen.grid(row=0, column=0, columnspan=3)
        b1["bg"] = "light grey"
        b5["bg"] = "light grey"
        b9["bg"] = "light grey"

        ans = messagebox.askquestion("GAME END", "Do you want to play again?")
        if (ans == "no"):
            win.quit()
        if (ans == "yes"):
            b1["text"] = ""
            b1["bg"] = "white"
            b2["text"] = ""
            b2["bg"] = "white"
            b3["text"] = ""
            b3["bg"] = "white"
            b4["text"] = ""
            b4["bg"] = "white"
            b5["text"] = ""
            b5["bg"] = "white"
            b6["text"] = ""
            b6["bg"] = "white"
            b7["text"] = ""
            b7["bg"] = "white"
            b8["text"] = ""
            b8["bg"] = "white"
            b9["text"] = ""
            b9["bg"] = "white"

            screen = Label(win, text="START", font=("Arial", 14), height=2, width=20, background="black", fg="white")
            screen.grid(row=0, column=0, columnspan=3)

    elif (b3["text"] == "0" and b5["text"] == "0" and b7["text"] == "0"):
        screen = Label(win, text="PLAYER 1 IS WINNER", font=("Arial", 14), bg="black", fg="white")
        screen.grid(row=0, column=0, columnspan=3)
        b3["bg"] = "light grey"
        b5["bg"] = "light grey"
        b7["bg"] = "light grey"

        ans = messagebox.askquestion("GAME END", "Do you want to play again?")
        if (ans == "no"):
            win.quit()
        if (ans == "yes"):
            b1["text"] = ""
            b1["bg"] = "white"
            b2["text"] = ""
            b2["bg"] = "white"
            b3["text"] = ""
            b3["bg"] = "white"
            b4["text"] = ""
            b4["bg"] = "white"
            b5["text"] = ""
            b5["bg"] = "white"
            b6["text"] = ""
            b6["bg"] = "white"
            b7["text"] = ""
            b7["bg"] = "white"
            b8["text"] = ""
            b8["bg"] = "white"
            b9["text"] = ""
            b9["bg"] = "white"

            screen = Label(win, text="START", font=("Arial", 14), height=2, width=20, background="black", fg="white")
            screen.grid(row=0, column=0, columnspan=3)

    elif (b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X"):
        screen = Label(win, text="PLAYER 2 IS WINNER", font=("Arial", 14), bg="black", fg="white")
        screen.grid(row=0, column=0, columnspan=3)
        b3["bg"] = "light grey"
        b5["bg"] = "light grey"
        b7["bg"] = "light grey"

        ans = messagebox.askquestion("GAME END", "Do you want to play again?")
        if (ans == "no"):
            win.quit()
        if (ans == "yes"):
            b1["text"] = ""
            b1["bg"] = "white"
            b2["text"] = ""
            b2["bg"] = "white"
            b3["text"] = ""
            b3["bg"] = "white"
            b4["text"] = ""
            b4["bg"] = "white"
            b5["text"] = ""
            b5["bg"] = "white"
            b6["text"] = ""
            b6["bg"] = "white"
            b7["text"] = ""
            b7["bg"] = "white"
            b8["text"] = ""
            b8["bg"] = "white"
            b9["text"] = ""
            b9["bg"] = "white"

            screen = Label(win, text="START", font=("Arial", 14), height=2, width=20, background="black", fg="white")
            screen.grid(row=0, column=0, columnspan=3)

    else:
        screen = Label(win, text="BEST OF LUCK", font=("Arial", 14), bg="black", fg="white")
        screen.grid(row=0, column=0, columnspan=3)

    if( b1["text"] != "" and b2["text"] != "" and b3["text"] != "" and b4["text"] != "" and b5["text"] != "" and b6["text"] != "" and b7["text"] != "" and b8["text"] != "" and b9["text"] != ""):

        screen = Label(win, text="IT'S A TIE", font=("Arial", 14), bg="black", fg="white",width=20)
        screen.grid(row=0, column=0, columnspan=3)

        ans = messagebox.askquestion("GAME END", "Do you want to play again?")
        if (ans == "no"):
            win.quit()
        if (ans == "yes"):
            b1["text"] = ""
            b1["bg"] = "white"
            b2["text"] = ""
            b2["bg"] = "white"
            b3["text"] = ""
            b3["bg"] = "white"
            b4["text"] = ""
            b4["bg"] = "white"
            b5["text"] = ""
            b5["bg"] = "white"
            b6["text"] = ""
            b6["bg"] = "white"
            b7["text"] = ""
            b7["bg"] = "white"
            b8["text"] = ""
            b8["bg"] = "white"
            b9["text"] = ""
            b9["bg"] = "white"

            screen = Label(win, text="START", font=("Arial", 14), height=2,width=20, background="black", fg="white")
            screen.grid(row=0, column=0, columnspan=3)

screen = Label(win, text="START", font=("Arial", 14), height=2, background="black", fg="white")
screen.grid(row=0, column=0, columnspan=3)

b1 = Button(win, text="",font=("",9,"bold"), width=13, height=6,bg="white", command=lambda: show(b1))
b1.grid(row=1, column=0)

b2 = Button(win, text="",font=("",9,"bold"), width=13, height=6,bg="white", command=lambda: show(b2))
b2.grid(row=1, column=1)

b3 = Button(win, text="",font=("",9,"bold"), width=13, height=6,bg="white", command=lambda: show(b3))
b3.grid(row=1, column=2)

b4 = Button(win, text="",font=("",9,"bold"), width=13, height=6,bg="white", command=lambda: show(b4))
b4.grid(row=2, column=0)

b5 = Button(win, text="",font=("",9,"bold"), width=13, height=6,bg="white", command=lambda: show(b5))
b5.grid(row=2, column=1)

b6 = Button(win, text="",font=("",9,"bold"), width=13, height=6,bg="white", command=lambda: show(b6))
b6.grid(row=2, column=2)

b7 = Button(win, text="",font=("",9,"bold"), width=13, height=6,bg="white", command=lambda: show(b7))
b7.grid(row=3, column=0)

b8 = Button(win, text="",font=("",9,"bold"), width=13, height=6,bg="white", command=lambda: show(b8))
b8.grid(row=3, column=1)

b9 = Button(win, text="",font=("",9,"bold"), width=13, height=6,bg="white", command=lambda: show(b9))
b9.grid(row=3, column=2)

win.mainloop()