def countdown():
    global timeleft
    if timeleft>0:
        timeleft -= 1
        timeLabel.config(text="Time left: "+ str(timeleft))
        timeLabel.after(1000,countdown)
