from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext 
import cx_Oracle
import socket
import requests
from matplotlib import pyplot as plt
import numpy as np


#splash screen

splash=Tk()
splash.overrideredirect(True)
splash.geometry("800x500+300+100")
splash.configure(background='salmon')
lbl= Label(splash,text="Welcome to Student Management System !!!",font=("Helvetica",20,'bold'))
lbl.pack(pady=10)
image_file = "F:\python\GUI practice\\image12.png"
image = PhotoImage(file=image_file, format="png")
canvas = Canvas(splash, height=400, width=1000)
canvas.create_image(403, 227, image=image)
canvas.pack()

try:
	city="Mumbai"
	socket.create_connection(("www.goggle.com",80))
	print("connected")
	a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2="&q="+city
	a3="&appid=b8fe7aff02134720530f81ffccf5569b"
	api_address=a1+a2+a3
	
	res=requests.get(api_address)
	print(res)

	data=res.json()
	print(data)
	
	main=data["main"]
	print(main)
	
	temp=main['temp']
	print(temp)
	
	var1 = StringVar()
	var2 = StringVar()
	label1 = Message(splash, textvariable=var1,width=200,font=('arial',11,'bold'))
	label2 = Message(splash, textvariable=var2,width=200,font=('arial',11,'bold'))

	msg1="Temperature(Celsius):"+str(temp)
	var2.set(msg1)
	label2.pack(side=LEFT,padx=150)
	
	msg2="City:"+city
	var1.set(msg2)
	label1.pack(side=LEFT)

except OSError as e:
	print(e)
	print("check network")
def f00():
	splash.withdraw()
	root.deiconify()

root=Toplevel(splash)
root.title("Student Management System")
root.geometry("800x500+300+100")
#root.configure(background="cadet blue")

filename = PhotoImage(file = "F:\python\GUI practice\\img.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


#root.iconbitmap('favicon.ico')
root.withdraw()

root.protocol("WM_DELETE_WINDOW",splash.destroy)





viewFrame=Toplevel(root)
viewFrame.title("View")
viewFrame.geometry("400x400+300+200")
viewFrame.withdraw()

filename15 = PhotoImage(file = "F:\python\GUI practice\\pen.png")
background_label = Label(viewFrame, image=filename15)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


st=scrolledtext.ScrolledText(viewFrame,width=30,height=10)
def f1():
	viewFrame.withdraw()
	st.delete('1.0',END)
	root.deiconify()
btnViewBack=Button(viewFrame,text="Back",command=f1)
st.pack()
btnViewBack.pack()



def f20(): 
	from matplotlib import pyplot as plt
	import numpy as np
	con=None
	cursor=None
	try:
		subjects = ['Physics','Chemistry','Maths','Biology']
		con=cx_Oracle.connect("system/sagar123")
		cursor=con.cursor()
		sql="select * from marks"
		cursor.execute(sql)
		data=cursor.fetchall()
		info=""
		x_marks = []
		stud=[]
		for row in data:
			sum = row[2]+row[3]+row[4]+row[5]
			x_marks.append(sum)
			stud.append(row[1])
		print(x_marks)
		print(stud)
		plt.bar(stud,x_marks)
		plt.title('Students Exam Score')
		plt.xlabel('Students',fontsize=10)
		plt.ylabel('Marks',fontsize=10)
		plt.legend()
		plt.grid()
		plt.show()
	except cx_Oracle.DatabaseError as e:
		print("issue")
		messagebox.showerror("Failure",str(e))
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()


addFrame=Toplevel(root)
addFrame.title("Add")
addFrame.geometry("400x400+300+200")
addFrame.withdraw()

filename123 = PhotoImage(file = "F:\python\GUI practice\\pen.png")
background_label = Label(addFrame, image=filename123)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



lblAddRno=Label(addFrame,text="Roll no")
entAddRno=Entry(addFrame,bd=5)

lblAddName=Label(addFrame,text="Name")
entAddName=Entry(addFrame,bd=5)

lblAddphys=Label(addFrame,text="Physics Marks")
lblAddphys.place(x=50,y=130)
entAddphys=Entry(addFrame,bd=5)
entAddphys.place(x=50,y=150)
lblAddchem=Label(addFrame,text="Chemistry Marks")
entAddchem=Entry(addFrame,bd=5)
lblAddchem.place(x=200,y=130)
entAddchem.place(x=200,y=150)

lblAddmath=Label(addFrame,text="Maths Marks")
entAddmath=Entry(addFrame,bd=5)
lblAddmath.place(x=50,y=190)
entAddmath.place(x=50,y=210)

lblAddbio=Label(addFrame,text="Biology Marks")
entAddbio=Entry(addFrame,bd=5)
lblAddbio.place(x=200,y=190)
entAddbio.place(x=200,y=210)

def f3():
	
	con=None
	cursor=None
	try:
		con = cx_Oracle.connect("system/sagar123")
		cursor=con.cursor()
		sql="insert into marks values ('%d','%s','%d','%d','%d','%d')"
		rno=entAddRno.get()
		if len(rno)==0:
			messagebox.showerror("incomplete","rollnumber is empty")
			entAddRno.focus()
			return
		if not rno.isdigit() or int(rno)<1:
			messagebox.showerror("wrong","rollnumber should be positive numbers")
			entAddRno.delete(0,END)
			entAddRno.focus()
			return
		name=entAddName.get()
		if len(name)==0:
			messagebox.showerror("incomplete","name is empty")
			entAddName.focus()
			return
		if not name.isalpha():
			messagebox.showerror("wrong","name should be alphabet")
			entAddName.delete(0,END)
			entAddName.focus()
			return
		
		phys=entAddphys.get()
		if len(phys)==0:
			messagebox.showerror("incomplete","Physics is empty")
			entAddphys.focus()
			return
		if not phys.isdigit() or int(phys)<1 or int(phys)>50:
			messagebox.showerror("wrong","Invalid input for Physics")
			entAddphys.delete(0,END)
			entAddphys.focus()
			return

		chem=entAddchem.get()
		if len(chem)==0:
			messagebox.showerror("incomplete","Chemistry is empty")
			entAddchem.focus()
			return
		if not chem.isdigit() or int(chem)<1 or int(chem)>50:
			messagebox.showerror("wrong","Invalid input for Chemistry")
			entAddchem.delete(0,END)
			entAddchem.focus()
			return

		math=entAddmath.get()
		if len(math)==0:
			messagebox.showerror("incomplete","Maths is empty")
			entAddmath.focus()
			return
		if not math.isdigit() or int(math)<1 or int(math)>50:
			messagebox.showerror("wrong","Invalid input for Maths")
			entAddmath.delete(0,END)
			entAddmath.focus()
			return

		bio=entAddbio.get()
		if len(bio)==0:
			messagebox.showerror("incomplete","Biology is empty")
			entAddbio.focus()
			return
		if not bio.isdigit() or int(bio)<1 or int(bio)>50:
			messagebox.showerror("wrong","Invalid input for Biology")
			entAddbio.delete(0,END)
			entAddbio.focus()
			return

		
		args=(int(rno),name,int(phys),int(chem),int(math),int(bio),)
		cursor.execute(sql%args)
		con.commit()
		msg=str(cursor.rowcount)+"rows inserted"
		messagebox.showinfo("Success",msg)
	except cx_Oracle.DatabaseError as e:
		print("issue",)
		con.rollback()
		messagebox.showerror("Failure",str(e))
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
		entAddRno.delete(0,END)
		entAddName.delete(0,END)
		entAddphys.delete(0,END)
		entAddchem.delete(0,END)
		entAddmath.delete(0,END)
		entAddbio.delete(0,END)
		entAddRno.focus()
btnAddSave=Button(addFrame,text="Save",command=f3)
btnAddSave.place(x=175,y=260)

def f4():
	addFrame.withdraw()
	root.deiconify()
btnAddBack=Button(addFrame,text="Back",command=f4)
btnAddBack.place(x=175,y=300)

lblAddRno.pack()
entAddRno.pack()
lblAddName.pack()
entAddName.pack()





updateFrame=Toplevel(root)
updateFrame.title("Update")
updateFrame.geometry("400x400+300+200")
updateFrame.withdraw()

filename12 = PhotoImage(file = "F:\python\GUI practice\\pen.png")
background_label = Label(updateFrame, image=filename12)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


lblUpdateRno=Label(updateFrame,text="Roll no")
entUpdateRno=Entry(updateFrame,bd=5)

lblUpdateName=Label(updateFrame,text="Name")
entUpdateName=Entry(updateFrame,bd=5)

lblUpdatephys=Label(updateFrame,text="Physics Marks")
lblUpdatephys.place(x=50,y=130)
entUpdatephys=Entry(updateFrame,bd=5)
entUpdatephys.place(x=50,y=150)
lblUpdatechem=Label(updateFrame,text="Chemistry Marks")
entUpdatechem=Entry(updateFrame,bd=5)
lblUpdatechem.place(x=200,y=130)
entUpdatechem.place(x=200,y=150)

lblUpdatemath=Label(updateFrame,text="Maths Marks")
entUpdatemath=Entry(updateFrame,bd=5)
lblUpdatemath.place(x=50,y=190)
entUpdatemath.place(x=50,y=210)

lblUpdatebio=Label(updateFrame,text="Biology Marks")
entUpdatebio=Entry(updateFrame,bd=5)
lblUpdatebio.place(x=200,y=190)
entUpdatebio.place(x=200,y=210)

def f5():
	con=None
	cursor=None
	try:
		con = cx_Oracle.connect("system/sagar123")
		rno=entUpdateRno.get()
		name=entUpdateName.get()
		phys=entUpdatephys.get()
		chem=entUpdatechem.get()
		math=entUpdatemath.get()
		bio=entUpdatebio.get()
		
		if len(rno)==0:
			messagebox.showerror("incomplete","rollnumber is empty")
			entUpdateRno.focus()
			return
		if not rno.isdigit() or int(rno)<1:
			messagebox.showerror("wrong","rollnumber should be positive numbers")
			entUpdateRno.delete(0,END)
			entUpdateRno.focus()
			return
		name=entUpdateName.get()
		if len(name)==0:
			messagebox.showerror("incomplete","name is empty")
			entUpdateName.focus()
			return
		if not name.isalpha():
			messagebox.showerror("wrong","name should be alphabet")
			entUpdateName.delete(0,END)
			entUpdateName.focus()
			return
		
		if len(phys)==0:
			messagebox.showerror("incomplete","Physics is empty")
			entUpdatephys.focus()
			return
		if not phys.isdigit() or int(phys)<1 or int(phys)>50:
			messagebox.showerror("wrong","Invalid input for Physics")
			entUpdatephys.delete(0,END)
			entUpdatephys.focus()
			return

		if len(chem)==0:
			messagebox.showerror("incomplete","Chemistry is empty")
			entUpdatechem.focus()
			return
		if not chem.isdigit() or int(chem)<1 or int(chem)>50:
			messagebox.showerror("wrong","Invalid input for Chemistry")
			entUpdatechem.delete(0,END)
			entUpdatechem.focus()
			return

		if len(math)==0:
			messagebox.showerror("incomplete","Maths is empty")
			entUpdatemath.focus()
			return
		if not math.isdigit() or int(math)<1 or int(math)>50:
			messagebox.showerror("wrong","Invalid input for Maths")
			entUpdatemath.delete(0,END)
			entUpdatemath.focus()
			return

		
		if len(bio)==0:
			messagebox.showerror("incomplete","Biology is empty")
			entUpdatebio.focus()
			return
		if not bio.isdigit() or int(bio)<1 or int(bio)>50:
			messagebox.showerror("wrong","Invalid input for Biology")
			entUpdatebio.delete(0,END)
			entUpdatebio.focus()
			return

		cursor=con.cursor()
		'''sql="update student set name='%s',phys='%d',chem='%d',math='%d',bio='%d' where rno='%d'"
		args=(name,int(rno),int(phys),int(chem),int(math),int(bio))
		cursor.execute(sql%args)
		con.commit()
		'''
		sql="update marks set name='%s' where rno='%d'"
		args=(name,int(rno))
		cursor.execute(sql%args)
		con.commit()
		
		sql="update marks set phys='%s' where rno='%d'"
		args1=(int(phys),int(rno))
		cursor.execute(sql%args1)
		con.commit()
		
		sql="update marks set chem='%s' where rno='%d'"
		args2=(int(chem),int(rno))
		cursor.execute(sql%args2)
		con.commit()
		
		sql="update marks set bio='%s' where rno='%d'"
		args=(int(math),int(rno))
		cursor.execute(sql%args)
		con.commit()
		
		sql="update marks set bio='%s' where rno='%d'"
		args4=(int(phys),int(rno))
		cursor.execute(sql%args4)
		con.commit()
		
		msg=str(cursor.rowcount)+"rows updated"
		messagebox.showinfo("Success",msg)
	except cx_Oracle.DatabaseError as e:
		print("issue",)
		con.rollback()
		messagebox.showerror("Failure",str(e))
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
		entUpdateRno.delete(0,END)
		entUpdateName.delete(0,END)
		entUpdatephys.delete(0,END)
		entUpdatechem.delete(0,END)
		entUpdatemath.delete(0,END)
		entUpdatebio.delete(0,END)
		
		entUpdateRno.focus()
btnUpdateSave=Button(updateFrame,text="Save",command=f5)
btnUpdateSave.place(x=175,y=260)

def f6():
	updateFrame.withdraw()
	root.deiconify()
btnUpdateBack=Button(updateFrame,text="Back",command=f6)
btnUpdateBack.place(x=175,y=300)

lblUpdateRno.pack()
entUpdateRno.pack()
lblUpdateName.pack()
entUpdateName.pack()





deleteFrame=Toplevel(root)
deleteFrame.title("Delete")
deleteFrame.geometry("400x400+300+200")
deleteFrame.withdraw()

filename1234 = PhotoImage(file = "F:\python\GUI practice\\pen.png")
background_label = Label(deleteFrame, image=filename1234)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

lblDeleteRno=Label(deleteFrame,text="Roll no")
entDeleteRno=Entry(deleteFrame,bd=5)

def f7():
	con=None
	cursor=None
	try:
		con = cx_Oracle.connect("system/sagar123")
		cursor=con.cursor()
		rno=entDeleteRno.get()
		if len(rno)==0:
			messagebox.showerror("incomplete","rollnumber is empty")
			entDeleteRno.focus()
			return
		if not rno.isdigit() or int(rno)<1:
			messagebox.showerror("wrong","rollnumber should be positive numbers")
			entDeleteRno.delete(0,END)
			entDeleteRno.focus()
			return
		
		sql="delete from marks where rno='%d'"
		args=(int(rno))
		cursor.execute(sql%args)
		con.commit()
		msg=str(cursor.rowcount)+"rows deleted"
		messagebox.showinfo("Success",msg)
	except cx_Oracle.DatabaseError as e:
		print("issue",)
		con.rollback()
		messagebox.showerror("Failure",str(e))
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
		entDeleteRno.delete(0,END)
		entDeleteRno.focus()
btnDeleteSave=Button(deleteFrame,text="Save",command=f7)
btnDeleteSave.place(x=180,y=80)

def f8():
	deleteFrame.withdraw()
	root.deiconify()
btnDeleteBack=Button(deleteFrame,text="Back",command=f8)
btnDeleteBack.place(x=180,y=130)

lblDeleteRno.pack()
entDeleteRno.pack()





def f9():
	root.withdraw()
	addFrame.deiconify()
btnAdd=Button(root,text="Add",font=("arial",20,'bold'),width=10,command=f9,bg="burlywood2")
btnPerf=Button(root,text="Performance",font=("arial",20,'bold'),width=10,command=f20,bg="burlywood2")

def f10():
	root.withdraw()
	viewFrame.deiconify()
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/sagar123")
		cursor=con.cursor()
		sql="select * from marks"
		cursor.execute(sql)
		data=cursor.fetchall()
		info=""
		for i in data:
			rno=i[0]
			name=i[1]
			phys=i[2]
			chem=i[3]
			math=i[4]
			bio=i[5]
			info=info+"Roll no: "+str(rno)+"Name: "+name+"Physics: "+str(phys)+"Chemistry: "+str(chem)+"Maths: "+str(math)+"Bio: "+str(bio)+"\n"
		st.configure(state="normal")
		st.insert(INSERT,info)
		st.configure(state="disabled")
		st.yview(END)
	except cx_Oracle.DatabaseError as e:
		print("issue",)
		messagebox.showerror("Failure",str(e))
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
		
btnView=Button(root,text="View",font=("arial",20,'bold'),width=10,command=f10,bg="burlywood2")

def f11():
	root.withdraw()
	updateFrame.deiconify()
btnUpdate=Button(root,text="Update",font=("arial",20,'bold'),width=10,command=f11,bg="burlywood2")

def f12():
	root.withdraw()
	deleteFrame.deiconify()
btnDelete=Button(root,text="Delete",font=("arial",20,'bold'),width=10,command=f12,bg="burlywood2")

btnAdd.pack(pady=20)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnPerf.pack(pady=10)

def f2():
	viewFrame.withdraw()
	root.deiconify()
viewFrame.protocol("WM_DELETE_WINDOW",f2)

def f13():
	addFrame.withdraw()
	root.deiconify()
addFrame.protocol("WM_DELETE_WINDOW",f13)
def f14():
	updateFrame.withdraw()
	root.deiconify()
updateFrame.protocol("WM_DELETE_WINDOW",f14)
def f15():
	deleteFrame.withdraw()
	root.deiconify()
deleteFrame.protocol("WM_DELETE_WINDOW",f15)

def f01():
	return root
f01()
splash.after(4000, f00)

splash.mainloop()


















































































