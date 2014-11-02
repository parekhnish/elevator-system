class Elevator(object):

    def __init__(self,building,canvas,name):

        self.ELEVATOR_WIDTH = 50
        self.ELEVATOR_HEIGHT = 60
        self.ELEVATOR_SEPARATION = 120
        self.ELEVATOR_START_X = 250
        self.ELEVATOR_START_Y = 50
        self.ELEVATOR_VELOCITY = 5
        self.ELEVATOR_COLOR = "#222"
        self.DOOR_COLOR = "#FE8"

        self.building = building
        self.name = name
        self.body = canvas.create_rectangle(self.ELEVATOR_START_X+(self.name*self.ELEVATOR_SEPARATION),self.ELEVATOR_START_Y,self.ELEVATOR_START_X+self.ELEVATOR_WIDTH+(self.name*self.ELEVATOR_SEPARATION),self.ELEVATOR_START_Y+self.ELEVATOR_HEIGHT,fill=self.ELEVATOR_COLOR)
        self.door = canvas.create_rectangle(self.ELEVATOR_START_X+(self.name*self.ELEVATOR_SEPARATION),self.ELEVATOR_START_Y,self.ELEVATOR_START_X+        1          +(self.name*self.ELEVATOR_SEPARATION),self.ELEVATOR_START_Y+self.ELEVATOR_HEIGHT,fill=self.DOOR_COLOR)
        self.x = canvas.coords(self.body)[0]
        self.y = canvas.coords(self.body)[1]
        self.dest = None

        self.floor_list = []
        for i in range(0,10):
            self.floor_list.append(False)

        self.call_queue = []

        self.door_status = 0
        self.open_status = 0
        self.move_status = "idle"
        self.status = "idle"
        self.current_floor = 9
        self.vel = 0

    def addFloor(self,floor):

        self.call_queue.append(floor)
        #print "Called addFloor!"
        print self.call_queue

    def update(self,canvas):

        if self.status == "idle":
            self.checkQueue()

        elif self.status == "moving":
            self.checkQueue()
            self.checkDest()
            self.moveElevator(canvas)

        elif self.status == "opening":
            self.openDoor(canvas)

        elif self.status == "open":
            self.keepDoorOpen()

        elif self.status == "closing":
            self.closeDoor(canvas)
        
        # canvas.move(self.body,0,self.vel)
        # self.x = canvas.coords(self.body)[0]
        # self.y = canvas.coords(self.body)[1]
        # if self.y >= 590:
        #     self.vel = 0
        #     canvas.itemconfigure(self.body,fill="#ff4")

        canvas.update()

    def checkMoveStatus(self):

        if(self.vel>0):
            self.move_status = "down"
        elif(self.vel<0):
            self.move_status = "up"
        else:
            self.move_status = "idle"

        if self.move_status=="idle" and len(self.call_queue)!=0:
            self.dest = self.call_queue[0]
            if(self.current_floor < self.dest):
                self.vel = -self.ELEVATOR_VELOCITY
                self.move_status = "down"
            else:
                self.vel = self.ELEVATOR_VELOCITY
                self.move_status = "up"

    def checkQueue(self):

        if not(len(self.call_queue)==0):
            self.dest = self.call_queue[0]
            if self.status == "idle":
                if self.current_floor < self.dest:
                    self.vel = -self.ELEVATOR_VELOCITY
                elif self.current_floor > self.dest:
                    self.vel = self.ELEVATOR_VELOCITY
                else:
                    self.vel = 0

            self.status = "moving"

    def checkDest(self):

        if((self.y+10)%60==0):
            self.current_floor = 10 - (self.y+10)/60
        else:
            self.current_floor = None

        if self.dest == self.current_floor:

            if self.dest in self.call_queue:
                self.building.floor_list[self.dest].upTurnOff()
                self.building.floor_list[self.dest].downTurnOff()

                panel = self.building.panel_list[self.name]
                if self.dest==0:
                    panel.canvas.itemconfig(panel.button_list[9], fill="#888")
                    panel.flag_list[9] = False
                else:
                    panel.canvas.itemconfig(panel.button_list[self.dest-1], fill="#888")
                    panel.flag_list[self.dest-1] = False

                self.call_queue.remove(self.dest)

            self.status = "opening"
            self.vel = 0

    def openDoor(self,canvas):
        if self.door_status == 50:
            self.status = "open"
        else:
            self.door_status += 2
            canvas.coords(self.door,self.x,self.y,self.x+self.door_status,self.y+self.ELEVATOR_HEIGHT)

    def keepDoorOpen(self):
        if self.open_status == 100:
            self.status = "closing"
            self.open_status = 0

        else:
            self.open_status += 5

    def closeDoor(self,canvas):
        if self.door_status == 0:
            self.status = "idle"

        else:
            self.door_status -= 2
            canvas.coords(self.door,self.x,self.y,self.x+self.door_status,self.y+self.ELEVATOR_HEIGHT)


    def moveElevator(self,canvas):

        if self.vel>0:
            self.move_status = "down"
        elif self.vel<0:
            self.move_status = "up"
        else:
            self.move_status = "idle"

        canvas.move(self.body,0,self.vel)
        canvas.move(self.door,0,self.vel)
        self.x = canvas.coords(self.body)[0]
        self.y = canvas.coords(self.body)[1]
