from elevator import *
from Tkinter import *
from panel.py import *

class Application:    
    
    def __init__(self, master):

        global building

        self.master = master
        self.building = Canvas(master, width = 1000, height = 700)
        self.building.pack(side=LEFT)

        self.panel = Canvas(master, width = 300, height = 700)
        self.panel.pack(side=LEFT)        
        
        self.make_elevators(self.building)
        self.draw_panel(self.panel)

    def draw_panel(self, arena):

        p = Panel(arena)        

    def make_elevators(self,canvas):

        self.elevator_list = []
        for i in range(0,4):
            e = Elevator(canvas, i)
            self.elevator_list.append(e)

    def simulate(self):

        for e in self.elevator_list:
            e.update(self.building)

        self.master.after(40,self.simulate)
        
master = Tk()
app = Application(master)
app.simulate()
master.mainloop()






