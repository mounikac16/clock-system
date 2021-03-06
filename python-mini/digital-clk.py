import tkinter as tk
import time
digital = tk.Tk()
time1 = ''
clock = tk.Label(digital, font=('times', 100, 'bold'), bg='white')
clock.pack(fill=tk.BOTH, expand=1)
def scroll():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    digital.title('Digital clock')
    clock.after(200, scroll)
scroll()
digital.mainloop(  )
