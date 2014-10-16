from Tkinter import *

class Application(Frame):
    
    def start_simulation(self):
        print "Starting elevator simulation"

    def create_widgets(self):
        #EXIT BUTTON
        self.EXIT = Button(self)
        self.EXIT["text"]    = "EXIT"
        self.EXIT["fg"]      = "red"
        self.EXIT["command"] =  self.quit
        self.EXIT.pack({"side": "left"})

        #START SIMULATION BUTTON
        self.START = Button(self)
        self.START["text"]    = "START SIMULATION"
        self.START["command"] = self.start_simulation
        self.START.pack({"side": "right"})

        #TO BE CONTINUED :p
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
