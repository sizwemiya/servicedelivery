#how to create simple GUI registration form.
#importing tkinter module for GUI application
from tkinter import *

#Creating object 'root' of Tk()
root = Tk()

#Providing Geometry to the form
root.geometry("500x500")

#Providing title to the form
root.title('Registration form')

def SUBMIT():
    print("Successfully Registered")

#this creates 'Label' widget for Registration Form and uses place() method.
label_0 =Label(root,text="GOVERNMENT SERVICE DELIVERY FORM ", width=40,font=("bold",20))
#place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
label_0.place(x=90,y=60)

#this creates 'Label' widget for Fullname and uses place() method.
label_1 =Label(root,text="FullName", width=20,font=("bold",10))
label_1.place(x=45,y=130)

#this will accept the input string text from the user.
entry_1=Entry(root)
entry_1.place(x=240,y=130)

#this creates 'Label' widget for Email and uses place() method.
label_3 =Label(root,text="Email", width=20,font=("bold",10))
label_3.place(x=35,y=180)

entry_3=Entry(root)
entry_3.place(x=240,y=180)

#this creates 'Label' widget for Gender and uses place() method.
label_4 =Label(root,text="Gender", width=20,font=("bold",10))
label_4.place(x=35,y=230)



#the variable 'var' mentioned here holds Integer Value, by deault 0
var=IntVar()

#this creates 'Radio button' widget and uses place() method
Radiobutton(root,text="Male",padx= 5, variable= var, value=1).place(x=235,y=230)
Radiobutton(root,text="Female",padx= 20, variable= var, value=2).place(x=290,y=230)



##this creates 'Label' widget for country and uses place() method.
label_5=Label(root,text="Country",width=20,font=("bold",10))
label_5.place(x=40,y=280)

#this creates list of countries available in the dropdownlist.
list_of_country=[ 'Lesotho' ,'South Africa' , 'Swaziland' ,'Botswana' ,'Zimbabwe', 'Other']

#the variable 'c' mentioned here holds String Value, by default ""
c=StringVar()
droplist=OptionMenu(root,c, *list_of_country)
droplist.config(width=15)
c.set('Select Country')
droplist.place(x=240,y=280)

##this creates 'Label' widget for Employment Status and uses place() method.
label_6=Label(root,text="Employment Status",width=20,font=('bold',10))
label_6.place(x=75,y=310)


#the variable 'var1' mentioned here holds Integer Value, by default 0
var1=IntVar()
#this creates Checkbutton widget and uses place() method.
Checkbutton(root,text="Employed", variable=var1).place(x=230,y=330)


#the variable 'var2' mentioned here holds Integer Value, by default 0
var2=IntVar()
Checkbutton(root,text="Unemployed", variable=var2).place(x=230,y=310)

#the variable 'var3' mentioned here holds Integer Value, by default 0
var3=IntVar()
Checkbutton(root,text="Self Employed", variable=var3).place(x=230,y=350)

#this creates 'Label' widget for District and uses place() method.
label_7 =Label(root,text="District", width=20,font=("bold",10))
label_7.place(x=30,y=380)

#this will accept the input string text from the user.
entry_7=Entry(root)
entry_7.place(x=240,y=380)

#this creates 'Label' widget for Sub-district and uses place() method.
label_8 =Label(root,text="Sub-district", width=20,font=("bold",10))
label_8.place(x=40,y=410)

#this will accept the input string text from the user.
entry_8=Entry(root)
entry_8.place(x=240,y=410)

#this creates 'Label' widget for Rating and uses place() method.
label_9 =Label(root,text="Rating", width=20,font=("bold",10))
label_9.place(x=25,y=440)

var=IntVar()
#this creates 'Radio button' widget and uses place() method
Radiobutton(root,text="Excellent",padx= 5, variable= var, value=3).place(x=235,y=440)
Radiobutton(root,text="Standard",padx= 5, variable= var, value=4).place(x=235,y=470)
Radiobutton(root,text="Poor",padx= 5, variable= var, value=5).place(x=235,y=500)


##this creates 'Label' widget for age group and uses place() method.
label_10=Label(root,text="Age Group",width=20,font=("bold",10))
label_10.place(x=35,y=530)

#this creates list of age group available in the dropdownlist.
list_of_age=[ '15 and Below' ,'16 to 25' , '26 to 35' ,'36 to 45' ,'46 to 55', '56 and Above']

#the variable 'c' mentioned here holds String Value, by default ""
c=StringVar()
droplist=OptionMenu(root,c, *list_of_age)
droplist.config(width=15)
c.set('Select Age Group')
droplist.place(x=240,y=530)

#this creates 'Label' widget for Department and uses place() method.
label_11 =Label(root,text="Department", width=20,font=("bold",10))
label_11.place(x=40,y=570)

#this will accept the input string text from the user.
entry_11=Entry(root)
entry_11.place(x=240,y=570)

#this creates 'Label' widget for feedback and uses place() method.
label_12 =Label(root,text="Feedback", width=20, font=("bold",10))
label_12.place(x=35, y=600)


my_text = Text(root, width=20, height=5, font=("Helvetica", 10))
my_text.pack(pady=20) 
my_text.place(x=240,y=600)

#this creates button for submitting the details provides by the user
Button(root, text='SUBMIT' , width=20,bg="blue",fg='white') .place(x=180,y=700)
command=SUBMIT




#this will run the mainloop.
root.mainloop()