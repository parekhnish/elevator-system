from floor import *
from elevator import *
from Tkinter import *
from panel import *

class Application:    
    
    def __init__(self, master):

        global building

        self.TIME_DOOR = 5
        self.TIME_FLOOR = 12
        self.TIME_WAIT = 20

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
        self.color_list = ["#f00","#ff0","#f0f","#0ff","#faf","#aaf","#afa","#4ff","#f44"]
        for i in range(0,10):
            display_up   = canvas.create_rectangle(35,60+(i*60),75,100+(i*60))    
            display_down = canvas.create_rectangle(175,60+(i*60),215,100+(i*60))
            #canvas.create_rectangle(240,50+(i*60),660,110+(i*60))
            
            if i == 9:
                #canvas.create_rectangle(292,50+(i*60),379,110+(i*60),fill = "#fff")
                #canvas.create_rectangle(412,50+(i*60),499,110+(i*60),fill = "#fff")
                #canvas.create_rectangle(532,50+(i*60),619,110+(i*60),fill = "#fff")
                
                #Floor Color
                #canvas.create_rectangle(670,50+(i*60),770,110+(i*60),fill = "#fff")
                
                #Floor Name
                canvas.create_text(720,80 + (i*60),font="Arial 20 bold", text = "Floor G")
            else:
                #canvas.create_rectangle(292,50+(i*60),379,110+(i*60),fill = self.color_list[8-i])
                #canvas.create_rectangle(412,50+(i*60),499,110+(i*60),fill = self.color_list[8-i])
                #canvas.create_rectangle(532,50+(i*60),619,110+(i*60),fill = self.color_list[8-i])
                
                #Floor Color
                #canvas.create_rectangle(670,50+(i*60),770,110+(i*60),fill = self.color_list[8-i])
                
                #Floor Name
                canvas.create_text(720,80 + (i*60),font="Arial 20 bold", text = "Floor " + str(10-i-1))
            
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
                e.addFloor(floor,direction,"floor_call")
                print "SAME_FLOOR_ELEVATOR" + str(e.name)
                return

        score_list = []
        i=0
        for e in self.elevator_list:
            score_list.append([self.calculateScore(e,floor,direction),i])
            i += 1

        score_list.sort(key=lambda x:x[0])

        flag = 0
        for score in score_list:
            if not(self.elevator_list[score[1]].people>=10):
                self.elevator_list[score[1]].addFloor(floor,direction,"floor_call")
                flag = 1
                break

        # score_list = []
        # for e in self.elevator_list:
        #     score_list.append(self.calculateScore(e,floor,direction))

        # minScore = 1000000
        # selected_elevator = None
        # i=0
        # for score in score_list:
        #     if score<minScore:
        #         selected_elevator = self.elevator_list[i]
        #         minScore = score

        #     i += 1

        # selected_elevator.addFloor(floor,direction,"floor_call")


        if flag==0:
            if direction=="up":
                self.floor_list[floor].upTurnOff()
            else:
                self.floor_list[floor].downTurnOff()


        

    def calculateScore(self,e,floor,direction):

        score = 0

        if e.status=="closing":
            score += float(e.door_status/50)*self.TIME_DOOR

        elif e.status=="open":
            score += float((100-e.open_status)/100)*self.TIME_WAIT + self.TIME_DOOR

        elif e.status=="opening":
            score += float((50 - e.door_status)/50)*self.TIME_DOOR + self.TIME_WAIT + self.TIME_DOOR

        


        if len(e.call_queue)==0:
            score += float(abs(e.current_floor - floor))*self.TIME_FLOOR

        else:
            if e.status=="opening" or e.status=="open" or e.status=="closing" or e.status=="idle":

                if (e.current_floor < floor and e.call_queue[0][0] >= floor and direction=="up") or (e.current_floor > floor and e.call_queue[0][0] <= floor and direction=="down"):
                    if not(e.call_queue[0][0]==floor):
                        score += self.TIME_WAIT + 2*self.TIME_DOOR
                
                    score += float(abs(e.current_floor - floor)*self.TIME_FLOOR)
                else:
                    score += float(abs(e.current_floor - e.call_queue[0][0])*self.TIME_FLOOR) + self.TIME_WAIT + 2*self.TIME_DOOR

                    flag = 0
                    for i in range(1,len(e.call_queue)):
                        previous = e.call_queue[i-1][0]
                        next = e.call_queue[i][0]

                        if (previous < floor and next >= floor and direction=="up") or (e.current_floor > floor and next <= floor and direction=="down"):
                            if not(floor==next):
                                score += self.TIME_WAIT + 2*self.TIME_DOOR
                            score += float(abs(previous - floor)*self.TIME_FLOOR)
                            flag = 1
                            break
                        else:
                            score += float(abs(previous - next)*self.TIME_FLOOR) + self.TIME_WAIT + 2*self.TIME_DOOR

                    if flag==0:
                        score += float(abs(e.call_queue[len(e.call_queue)-1][0] - floor)*self.TIME_FLOOR)

            else:
                if (e.current_floor < floor and e.dest >= floor and direction=="up") or (e.current_floor > floor and e.dest <= floor and direction=="down"):
                    # if not(e.dest==floor):
                    #         score += self.TIME_WAIT + 2*self.TIME_DOOR
                            
                    score += float(abs(e.current_floor - floor)*self.TIME_FLOOR)
                else:
                    score += float(abs(e.current_floor - e.dest)*self.TIME_FLOOR) + self.TIME_WAIT + 2*self.TIME_DOOR

                    flag = 0
                    for i in range(1,len(e.call_queue)):
                        previous = e.call_queue[i-1][0]
                        next = e.call_queue[i][0]

                        if (previous < floor and next >= floor and direction=="up") or (e.current_floor > floor and next <= floor and direction=="down"):
                            if not(floor==next):
                                score += self.TIME_WAIT + 2*self.TIME_DOOR
                            score += float(abs(previous - floor)*self.TIME_FLOOR)
                            flag = 1
                            break
                        else:
                            score += float(abs(previous - next)*self.TIME_FLOOR) + self.TIME_WAIT + 2*self.TIME_DOOR

                    if flag==0:
                        score += float(abs(e.call_queue[len(e.call_queue)-1][0] - floor)*self.TIME_FLOOR)
 

        print "Elevator" + str(e.name) + ' ----- ' + str(score)
        return score
    

        
master = Tk()
app = Application(master)
app.simulate()
master.mainloop()






