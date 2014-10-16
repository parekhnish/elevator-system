from Tkinter import *

class Application:    
    
    def __init__(self, master):

        global building

        self.building = Canvas(master, width = 1000, height = 700)
        self.building.pack(side=LEFT)

        self.panel = Canvas(master, width = 300, height = 700)
        self.panel.pack(side=LEFT)        
        
        
master = Tk()
app = Application(master)
master.mainloop()





