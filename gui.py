import tkinter as tk
from tkinter.filedialog import askdirectory
import methods as m
import os

class Gui:
    folderpath = ""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Color sorter")
        self.root.iconbitmap("images/icon.ico")
        self.root.resizable(0, 0)

        backgroundImage = tk.PhotoImage(file="images/background.png")
        self.canvas = tk.Canvas(self.root, height=400, width=400)
        self.canvas.create_image(0,0, image = backgroundImage, anchor="nw")
        self.canvas.pack()

        #displaying directory
        self.directoryFrame = tk.Frame(self.root, bg="#eae5f7")
        self.directoryFrame.place(relwidth=0.7, relheight=0.06, relx=0.05, rely=0.07)

        #button for opening
        self.openButton = tk.Button(self.root, text="Choose folder", command = lambda: self.openFolder(), bg="#faaca8")
        self.openButton.place(relx=0.75, rely=0.07)

        #button for sorting
        self.sortButton = tk.Button(self.root, text="Sort", command = lambda: self.sortImages(), bg="#faaca8")
        self.sortButton.place(relwidth=0.16, relheight=0.08, relx=0.42, rely=0.17)

        #displaying results
        self.resultsLabel = tk.Label(self.root, text="Results", bg="#f99590")
        self.resultsLabel.place(relwidth=0.9, relx=0.05, rely=0.3)
        self.resultsListbox = tk.Listbox(self.root,  bg="#eae5f7")
        self.resultsListbox.pack()
        self.resultsScrollbar = tk.Scrollbar(self.resultsListbox)
        self.resultsScrollbar.pack(side = tk.RIGHT, fill = tk.Y)  
        self.resultsScrollbar.config(command = self.resultsListbox.yview) 
        self.resultsListbox.config(yscrollcommand = self.resultsScrollbar.set)
        self.resultsListbox.place(relwidth=0.9, relheight=0.60, relx=0.05, rely=0.35)

        self.root.mainloop()
        
    #opening folder
    def openFolder(self):
        global folderpath
        folderpath = askdirectory()
        for widget in self.directoryFrame.winfo_children():
            widget.destroy()
        displayname = m.getDisplayName(folderpath)      
        self.directoryLabel = tk.Label(self.directoryFrame, text = displayname, bg="#f6f4fc")
        self.directoryLabel.pack()

    #sorting images
    def sortImages(self):        
        self.resultsListbox.delete(0, tk.END)
        #checking if folder was chosen
        if folderpath=="":
            tk.messagebox.showerror(title="Missing folder", message="Please choose a folder to proceed")
        #sorting all image files in directory
        for filename in os.listdir(folderpath):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                filepath = os.path.join(folderpath, filename)
                domcolor = m.getDomColor(filepath)
                color = m.compareColor(domcolor)
                m.moveImage(folderpath, color, filename)
                self.resultsListbox.insert(tk.END, "File: {0} assigned to color {1}.".format(filename, color))
            else:
                continue
            
    
