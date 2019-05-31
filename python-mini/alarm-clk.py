#Alarm clock using Python Tkinter module by Rajkumar Selvaraj
import tkinter as tk
import time
import os
from tkinter import messagebox
import webbrowser

#def main():
def SubmitButton():

  AlarmTime= entry1.get()
  Message1()
  #label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))  #delayed in execution
  CurrentTime = time.strftime("%H:%M")
  print("the alarm time is: {}".format(AlarmTime))
  #label2.config(text="")
  while AlarmTime != CurrentTime:
    #label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))
    CurrentTime = time.strftime("%H:%M")
    time.sleep(1)
  if AlarmTime == CurrentTime:
     print("now Alarm Music Playing")
     #os.system("start voltage.mp3")
     webbrowser.open("/home/chadalavada/Desktop/python-mini/voltage.mp3")
     label2.config(text = "Alarm music playing.....")
     messagebox.showinfo(title= 'Alarm Message', message= "{}".format(entry2.get()))
def Message1():
    AlarmTimeLable= entry1.get()
    label2.config(text="the Alarm time is Counting...")
    #label2.config(text= "the Alarm will ring at {}".format(AlarmTimeLable))
    messagebox.showinfo(title = 'Alarm clock', message = 'Alarm will Ring at {}'.format(AlarmTimeLable))  
def alarm():
	global root 
	root = tk.Tk()
	root.title("Alarm clock")  
	frame1 = tk.Frame(root)
	frame1.pack()
	frame1.config(height = 100, width = 100)

	global label1
	label1= tk.Label(frame1,text = "Enter the Alarm time :")
	label1.pack()

	global entry1
	entry1 = tk.Entry(frame1, width = 30)
	entry1.pack()
	entry1.insert(3,"example - 13:15")

	labelAlarmMessage= tk.Label(frame1, text="Alarm Message:")
	labelAlarmMessage.pack()

	global entry2
	entry2= tk.Entry(frame1, width=30)
	entry2.pack()

	button1= tk.Button(frame1, text= "submit", command=SubmitButton)
	button1.pack()
	global label2
	#this Label2 will show the Last Alarm Time
	label2= tk.Label(frame1)
	label2.pack()

		
	#label2.config(text="hello")

	root.mainloop()
def main():
	no=int(input("no.of alarms u wanna set"))
	while no>0:
		alarm()
		no=no-1
main()
