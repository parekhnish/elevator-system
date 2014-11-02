class Elevator(object):

    def __init__(self,canvas,name):

        self.ELEVATOR_WIDTH = 50
        self.ELEVATOR_HEIGHT = 60
        self.ELEVATOR_SEPARATION = 120
        self.ELEVATOR_START_X = 250
        self.ELEVATOR_START_Y = 50
        self.ELEVATOR_VELOCITY = 5
        self.ELEVATOR_COLOR = "#060"

        self.name = name
        self.body = canvas.create_rectangle(self.ELEVATOR_START_X+(self.name*self.ELEVATOR_SEPARATION),self.ELEVATOR_START_Y,self.ELEVATOR_START_X+self.ELEVATOR_WIDTH+(self.name*self.ELEVATOR_SEPARATION),self.ELEVATOR_START_Y+self.ELEVATOR_HEIGHT,fill=self.ELEVATOR_COLOR)
        #self.middle_line = canvas.create_rectangle(1.5*self.ELEVATOR_START_X+(self.name*self.ELEVATOR_SEPARATION),self.ELEVATOR_START_Y,1.5*self.ELEVATOR_START_X+(self.name*self.ELEVATOR_SEPARATION),self.ELEVATOR_START_Y+self.ELEVATOR_HEIGHT,fill= "#000")
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
            self.openDoor()

        elif self.status == "open":
            self.keepDoorOpen()

        elif self.status == "closing":
            self.closeDoor()
        
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
                self.call_queue.remove(self.dest)
            self.status = "opening"
            self.vel = 0

    def openDoor(self):
        if self.door_status == 500:
            self.status = "open"
        else:
            self.door_status += 5

    def keepDoorOpen(self):
        if self.open_status == 1000:
            self.status = "closing"
            self.open_status = 0

        else:
            self.open_status += 5

    def closeDoor(self):
        if self.door_status == 0:
            self.status = "idle"

        else:
            self.door_status -= 5


    def moveElevator(self,canvas):

        if self.vel>0:
            self.move_status = "down"
        elif self.vel<0:
            self.move_status = "up"
        else:
            self.move_status = "idle"

        canvas.move(self.body,0,self.vel)
        self.x = canvas.coords(self.body)[0]
        self.y = canvas.coords(self.body)[1]
