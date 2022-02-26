#Alarmclock project 25.02.2022 20:22 start

#Libraries
from tkinter import *
from tkinter import ttk
import datetime
import time


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime(r'%H:%M:%S')
        date = current_time.strftime(r'%d/%m/%Y')
        print(r'Set date is: ', date)
        print(now)
        if now == set_alarm_timer:
            print(r'Time to wake up')

        break

def actual_time():
    set_alarm_timer = f'{hour.get()}:{min.get()}:{sec.get()}'
    alarm(set_alarm_timer)

#GUI
clock = Tk()
clock.title(r'AlarmClock project')
clock.geometry(r'600x300')
time_format = Label(clock, text = r'Enter time in 24 hour format!').place(x = 10)
addTime = Label(clock, text = r'Hour Min Sec').place(x = 210)
setYourAlarm = Label(clock, text = r'When to wake you up', fg = r'blue', relief = r'solid').place(x = 90)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime = Entry(clock, textvariable = hour, bg = r'pink', width = 15).place(x = 110, y = 30)
minTime = Entry(clock, textvariable = min, bg = r'pink', width = 15).place(x = 150, y = 30)
secTime = Entry(clock, textvariable = sec, bg = r'pink', width = 10).place(x = 200, y = 30)

submit = Button(clock, text = r'Set Alarm', fg = r'red', width = 10, command = actual_time).place(x = 110, y = 70)

mainloop()

