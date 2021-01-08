def nextColour():
    global score
    global timeleft
    
    if timeleft>0:
        e.focus_set()
        if e.get().lower()==colours[1].lower():
            score += 1
        e.delete(0,tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]),text=str(colours[0]))
        scoreLabel.config(text="Score: "+str(score))
