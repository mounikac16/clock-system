import tkinter as tk
import math
import datetime
import time
def update_time():
	if (anastate == True):
		t=str(datetime.datetime.now())
		time=t.split()
		var1=time[1].split(':')
		hr=int(var1[0])
		minute=int(var1[1])
		sec=math.floor(float(var1[2]))
		second=int(sec)
		#print(second)
		coord=175,160,425,410						# outer white circle
		arc=c.create_oval(coord,fill="white")
		coord1=180,165,420,405						# inner black circle
		arc=c.create_oval(coord1,fill="black")
		mainpoint=297,282,303,288					# middle point
		arc=c.create_oval(mainpoint,fill="grey")
		point1=345,200,351,206						#1
		arc=c.create_oval(point1,fill="grey")
		point2=378,233,384,239						#2
		arc=c.create_oval(point2,fill="grey")
		point3=394,282,400,288						#3
		arc=c.create_oval(point3,fill="grey")
		point4=378,331,384,337						#4
		arc=c.create_oval(point4,fill="grey")
		point5=345,364,351,370						#5
		arc=c.create_oval(point5,fill="grey")
		point6=297,379,303,385						#6		
		arc=c.create_oval(point6,fill="grey")
		point7=249,364,255,370						#7
		arc=c.create_oval(point7,fill="grey")
		point8=216,331,222,337						#8
		arc=c.create_oval(point8,fill="grey")
		point9=200,282,206,288						#9
		arc=c.create_oval(point9,fill="grey")
		point10=216,233,222,239						#10
		arc=c.create_oval(point10,fill="grey")
		point11=249,200,255,206						#11
		arc=c.create_oval(point11,fill="grey")
		point12=297,185,303,191						#12			
		arc=c.create_oval(point12,fill="grey")
		if hr>=12:
			hr=12-hr
		x3=300+50*(math.cos(math.radians(((hr*30)+(minute//10)*6)-90)))
		y3=285+50*(math.sin(math.radians(((hr*30)+(minute//10)*6)-90)))
		coord3=x3,y3,300,285
		line=c.create_line(coord3,fill="green",width=5)		# hour hand
		x2=300+75*(math.cos(math.radians((minute*6)-90)))
		y2=285+75*(math.sin(math.radians((minute*6)-90)))
		coord2=x2,y2,300,285
		line=c.create_line(coord2,fill="red",width=3)		# minute hand
		x1=300+85*(math.cos(math.radians((second*6)-90)))
		y1=285+85*(math.sin(math.radians((second*6)-90)))
		coord1=x1,y1,300,285
		line=c.create_line(coord1,fill="blue",width=1)		# seconds hand
		c.pack()
		top.after(1000,update_time)
def analog():
	global anastate
	anastate=True
	global top
	top=tk.Tk()
	global c
	c=tk.Canvas(top,bg="black",height=600,width=600)
	update_time()
	top.mainloop()
k=int(input())
if k==2:
	analog()
