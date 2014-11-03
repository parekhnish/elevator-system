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
            e = Elevator(self,canvas, i)
            self.elevator_list.append(e)
        #print "Called make_elevators!"

    def make_floors(self,canvas):
        
        #canvas.create_rectangle(200,50,700,50, fill = "#000")
        #canvas.create_rectangle(200,650,700,650)
        #for i in range(1,11):
        #   canvas.create_rectangle(200,50+(i*60),700,50+(i*60))

        for i in range(0,4):
            canvas.create_rectangle(260+(i*120),40,260+(i*120),660)    
            canvas.create_rectangle(290+(i*120),40,290+(i*120),660)
            canvas.create_rectangle(260+(i*120),40,290+(i*120),40)
            canvas.create_rectangle(260+(i*120),660,290+(i*120),660)

        #canvas.create_rectangle(200,50,200,650, fill = "#000")
        #canvas.create_rectangle(700,50,700,650, fill = "#000")

        self.floor_list = []

        for i in range(0,10):
            display_up = canvas.create_rectangle(35,60+(i*60),75,100+(i*60))    
            display_down = canvas.create_rectangle(175,60+(i*60),215,100+(i*60))    
            f = Floor(canvas, self, i, display_up,display_down)
            self.floor_list.append(f)
 

    def simulate(self):

        for e in self.elevator_list:
            e.update(self.building)

        for f in self.floor_list:
            f.updateDisplay()

        self.master.after(40,self.simulate)

        #print "Called simulate!"

    def floorRequest(self,floor,direction):

        # Elevator is on SAME FLOOR as request
        for e in self.elevator_list:
            if (e.current_floor == floor):
                e.addFloor(floor,direction)
                print "SAME_FLOOR_ELEVATOR" + str(e.name)
                return

        # Elevator is idle, and is nearest to request
        min_dist = 10
        assign_elevator = None

        for e in self.elevator_list:
            if (e.status=="idle"):
                if abs(e.current_floor - floor) < min_dist:
                    print min_dist
                    print abs(e.current_floor - floor)
                    assign_elevator = e
                    min_dist = abs(e.current_floor - floor)

        if not(assign_elevator == None):
            assign_elevator.addFloor(floor,direction)
            print "IDLE_ELEVATOR" + str(e.name)
            return

        # Elevator is open, and nearest to request
        min_dist = 10
        assign_elevator = None

        for e in self.elevator_list:
            if (e.status=="opening" or e.status=="open" or e.status=="closing"):
                if abs(e.current_floor - floor) < min_dist:
                    print min_dist
                    print abs(e.current_floor - floor)
                    assign_elevator = e
                    min_dist = abs(e.current_floor - floor)

        if not(assign_elevator == None):
            assign_elevator.addFloor(floor,direction)
            print "STATIONARY_ELEVATOR" + str(e.name)
            return

        # Elevator is moving same direction as request, and is nearest to request
        min_dist = 10
        assign_elevator = None

        for e in self.elevator_list:
            if (e.status=="moving" and e.move_status == direction):
                if abs(e.current_floor - floor) < min_dist:
                    assign_elevator = e
                    min_dist = abs(e.current_floor - floor)

        if not(assign_elevator == None):
            assign_elevator.addFloor(floor,direction)
            print "SAME_DIRECTION_ELEVATOR" + str(e.name)
            return


        # Elevator is moving in opposite direction, and its destination is nearest to request
        min_dist = 20
        assign_elevator = None
        for e in self.elevator_list:
            if (e.status=="moving"):
                if (abs(e.current_floor - e.dest) + abs(e.dest - floor)) < min_dist:
                    assign_elevator = e
                    min_dist = (abs(e.current_floor - e.dest) + abs(e.dest - floor))

        if not(assign_elevator == None):
            assign_elevator.addFloor(floor,direction)
            print "OPPOSITE_DIRECTION_ELEVATOR" + str(e.name)
            return

    

        
master = Tk()
app = Application(master)
app.simulate()
master.mainloop()






