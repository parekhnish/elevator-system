from floor import *
from elevator import *
from Tkinter import *
from panel import *

class Application:    
    
    def __init__(self, master):

        global building

        self.master = master
        self.building = Canvas(master, width = 800, height = 700)
        self.building.pack(side=LEFT)

        self.panel = Canvas(master, width = 500, height = 700)
        self.panel.pack(side=LEFT)

        self.make_floors(self.building)
        self.make_elevators(self.building)
        self.make_panels(self.panel)

    def make_panels(self, arena):
        self.panel_list = []
        
        for i in range(0,4):
            p = Panel(arena,i+1,self.elevator_list[i])
            self.panel_list.append(p)
        
        #print "Called make_panels"        
    
    def make_elevators(self,canvas):

        self.elevator_list = []
        for i in range(0,4):
            e = Elevator(canvas, i)
            self.elevator_list.append(e)
        #print "Called make_elevators!"

    def make_floors(self,canvas):
        
        canvas.create_rectangle(200,50,700,50, fill = "#000")

        for i in range(1,11):
            canvas.create_rectangle(200,50+(i*60),700,50+(i*60))

        canvas.create_rectangle(200,50,200,650, fill = "#000")
        canvas.create_rectangle(700,50,700,650, fill = "#000")

        self.floor_list = []
        for i in range(0,10):
            f = Floor(canvas, self, i)
            self.floor_list.append(f)

        #print "Called make_floors!"

    def simulate(self):

        for e in self.elevator_list:
            e.update(self.building)

        self.master.after(40,self.simulate)

        #print "Called simulate!"

    def floorRequest(self,floor,dir):
        
        for e in self.elevator_list:
            if (e.move_status=="idle"):
                e.addFloor(floor)
                break

        #print "Called floorRequest!"
        
master = Tk()
app = Application(master)
app.simulate()
master.mainloop()






