from tkinter import *
from tkinter import simpledialog
from tkinter import ttk, messagebox
import json
import os
import sys

value = []
value2=[]
try:
    fileob = open("storage.txt", "r")
    file = json.load(fileob)
    for i in file:
        value.append(i)
    firsttask = [task.get('id') for task in value ]
except:
    def note():
        print("Storage.txt must include an empty list. Before running the programme, you must type open and close square brackets in the file.")
        user=input("Do You want to make changes to a storage file? (Y/N)")
        if user == "Y" or user=="y":
            fileob = open("storage.txt", "w")
            fileob.write("[]")
            print_menu()
        else:
            print("You must open storage.txt to continue.")
            note()
        
def print_menu():
    print("Press 1 to Add Task")
    print("Press 2 to Display List of All Task")
    print("Press 3 to Delete Task")
    print("Press 4 to Load Saved Task")
    print("Press 5 to Save Task")
    print("Press 6 to Exit")
n = 0
def UniqueID():
    global n 
    n+=1
    return n

def main():
    global tit
    global desc
    global uniID
    try:
        while True:
            print_menu()
            choice = int(input("Enter your choice: "))
            if choice == 1:
                uniID = UniqueID()
                smart=1
                nothing=0
                try:
                    if not firsttask:
                        nothing=nothing+uniID
                    else:
                        for boss in firsttask:
                            if boss==uniID:
                                uniID += 1
                            elif boss!=uniID:
                                smart=smart+uniID
                except Exception as e:
                    print("Good To Go")

                root = Tk()
                tit=simpledialog.askstring("title","Enter the Title: ", parent=root)
                if not tit:
                    messagebox.showwarning("Caution","Write Something")   
                    root.withdraw()
                    continue 
                desc=simpledialog.askstring("Desc","Description of Task: ",parent=root)
                messagebox.showinfo('Success','Task Added!(^///^)Save it to see next Time')  
                root.withdraw()
                if not desc:
                    messagebox.showwarning("Caution","Write Something")
                    root.withdraw()
                    continue 
                emptybox_dict = {"title":tit,"desc":desc,"id":uniID}
                value.append(emptybox_dict)
            elif choice == 2:
                try:
                    messagebox.showinfo("Information","Only Saved Tasks Are Displayed Click OK and Add Task First if you haven't finished it yet!")
                    Display()
                except Exception as e:
                    print(f"Application Closed")

            elif choice == 3:
                try:
                    fileob = open("storage.txt", "r")
                    file = json.load(fileob)
                    id = int(input("Enter id.no to Delete Task: "))
                    xyz = [task for task in file if task.get('id')==id]
                    # First filter trash 
                    value2.append(xyz)
                    value2.clear()
                    if not xyz:
                        messagebox.showinfo('OOPS','¯\_(ツ)_/¯ Nothing Found With this ID')
                        continue
                    #Second filter load in new list 
                    value.clear()
                    for task in file :
                        if task.get('id')!=id:
                            value.append(task)
                    with open("storage.txt", "w") as fileob:
                            json.dump(value, fileob)
                    if not value:
                        messagebox.showinfo('Success','Task Deleted')
                        messagebox.showinfo('OOPS','¯\_(ツ)_/¯ Save Task First')
                        continue
                        
                    messagebox.showinfo('Success','Task Deleted')
                except Exception as e:
                    messagebox.showinfo('OOPS',f'¯\_(ツ)_/¯ To Deleted {e}')
            elif choice == 4:
                try:
                    fileob = open("storage.txt","r")
                    file = json.load(fileob)
                    if file  == []:
                        messagebox.showwarning("Caution","Nothing Saved ")
                    else:
                        print(file)
                except enumerate:
                    messagebox.showwarning("Caution",f"Error {enumerate} or No Added Task First add some task to Load")
                    pass
            elif choice == 5:
                try:
                    if value==[]:
                        messagebox.showwarning("Empty","Add Task to Save!")
                    else:
                        with open("storage.txt", "w") as file:
                            file.write('\n')
                            json.dump(value, file)
                        messagebox.showinfo('Success','Task Saved')
                        file.close()
                except Exception as e:
                    pass

            elif choice == 6:
                if choice==6:
                    break
                    
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        messagebox.showwarning('Caution',f'Press 1 to Add Task First')
        python = sys.executable
        os.system(f"{python} {sys.argv[0]}")
class Display:
    def __init__(self):
        self.asf = Tk()
        self.asf.title('MyBucket')
        self.clmns=("id", "title", "desc")
        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", fieldbackground="lightblue",background="lightblue", font=('Calibri', 11)) 
        self.style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) 
        self.style.layout("mystyle.Treeview", [("mystyle.Treeview.treearea", {"sticky": "nswe"})]) 
        self.treeview = ttk.Treeview(self.asf, style="mystyle.Treeview",columns=self.clmns, show="headings")
        for column in self.treeview["columns"]:
            self.treeview.column(column, anchor=CENTER)
        self.treeview.heading("id", text="ID", anchor=CENTER)
        self.treeview.heading("title", text="Title", anchor=CENTER)
        self.treeview.heading("desc", text="Description", anchor=CENTER)

        self.title1label = Label(self.asf, text="My Bucket", fg="green", background="yellow", font="time 15 bold",anchor=CENTER)
        self.title1label.grid(row=0, columnspan=6, column=0,pady=10)

        try :
            fileob = open("storage.txt","r")
            file = json.load(fileob)
            uni_id = [i['id'] for i in file] 
            title = [i['title'] for i in file]
            desc = [i['desc'] for i in file]
            if not (uni_id and title and desc):
                messagebox.showwarning("Caution","Nothing Saved")
                self.asf.withdraw()
                return
            for saveditems in zip(uni_id,title,desc):
                    self.treeview.insert('','end', values= saveditems)
        except enumerate:
            messagebox.showwarning("Caution","Nothing Saved")
            self.asf.withdraw()

   

        self.yscrollbar = ttk.Scrollbar(self.asf, orient='vertical', command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.yscrollbar.set)
        self.treeview.grid(row=1, columnspan=3, column=1, sticky="nsew")
        self.yscrollbar.grid(row=1, columnspan=3, column=1,sticky='nse')
        self.yscrollbar.configure(command=self.treeview.yview)
        self.nothing =Button(self.asf, text="(☞ﾟヮﾟ)☞Close Window From Here ☜(ﾟヮﾟ☜)", fg="green", background="yellow", font="time 15 bold",
                    anchor=CENTER,command=self.close)
        self.nothing.grid(row=2, columnspan=5)
        
        self.rows = 3
        self.columns = 5
        for a in range(self.rows):
            self.asf.grid_rowconfigure(a, weight=1)
        for b in range(self.columns):
            self.asf.grid_columnconfigure(b, weight=1)
        self.treeview.bind("<Double-1>",self.onDoubleClick)    
    def onDoubleClick(self,event):
        messagebox.showinfo("Congratulation","Task Completed")
        selected_item = self.treeview.selection()[0]
        self.treeview.item(selected_item,tags="selected_item")  
        self.treeview.tag_configure("selected_item",background='#87A922') 
        for i in self.treeview.selection():
            self.treeview.selection_remove(i)

        self.asf.mainloop()
    def close(self):
        self.asf.withdraw()
        python = sys.executable
        os.system(f"{python} {sys.argv[0]}")


if __name__ == "__main__":
    main()

