
import pymongo
import tkinter as tk
from tkinter import *



class Application(Frame):
    def _init_(self,master):
        super(Application,self)._init_(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.Label(self,text="CHOOSE A MONGO CMD. FROM BELOW").grid(row=0,column=0,sticky=W)
        self.Label(self,text="CREATE DB").grid(row=1,column=0,sticky=W)
        self.Button(self,text="Click to COnnect DB",command=self.b_conn).grid(row=2,column=0,sticky=W)
    def b_conn(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["customers"]
        mydict = { "name": "John", "address": "Highway 37" }
        x = mycol.insert_one(mydict)
        print(x.inserted_id)



#main()
root=Tk()
root.title("SIMPLE_GUI")
root.geometry("200x100")
root.mainloop()




lbl=Label(root,text="MONGO DB")
lbl.grid(row=0,column=0)
bt1=Button(root,text="CREATE")
bt1.grid(row=2,column=1)
bt1=Button(root,text="READ")
bt1.grid(row=4,column=1)
bt1=Button(root,text="UPDATE")
bt1.grid(row=6,column=1)
bt1=Button(root,text="DELETE")
bt1.grid(row=8,column=1)


bt1=Button(root,text="CREATE",command=konect,width=50)
bt1.grid(row=2,column=1)
bt1=Button(root,text="READ")
bt1.grid(row=4,column=1)
bt1=Button(root,text="UPDATE")
bt1.grid(row=6,column=1)
bt1=Button(root,text="DELETE")
bt1.grid(row=8,column=1)


