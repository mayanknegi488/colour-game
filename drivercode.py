root=tkinter.Tk()
root.title("COLOURGAME")

root.geometry("375x200")
instructions = tkinter.Label(root,text="Type in the colour of the words, and not the word text!",font=('Helvetica',12))
instructions.pack()

scoreLabel = tkinter.Label(root,text="Press enter to start",font=('Helvetica',12))
scoreLabel.pack()

timeLabel = tkinter.Label(root,text="Time left: "+str(timeleft),font=('Helvetica',12))
timeLabel.pack()

label = tkinter.Label(root,font=('Helvetica',69))
label.pack()

e = tkinter.Entry(root)

root.bind('<Return>',startGame)
e.pack()

e.focus_set()
root.mainloop()
