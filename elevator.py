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
        self.PEOPLE_MAX = 10

        self.building = building
        self.name = name
        self.body = canvas.create_rectangle(self.ELEVATOR_START_X+(self.name*self.ELEVATOR_SEPARATION),self.ELEVATOR_START_Y + 9*self.ELEVATOR_HEIGHT,self.ELEVATOR_START_X+self.ELEVATOR_WIDTH+(self.name*self.ELEVATOR_SEPARATION),self.ELEVATOR_START_Y + 10*self.ELEVATOR_HEIGHT,fill=self.ELEVATOR_COLOR)
        self.door = canvas.create_rectangle(self.ELEVATOR_START_X+(self.name*self.ELEVATOR_SEPARATION),self.ELEVATOR_START_Y + 9*self.ELEVATOR_HEIGHT,self.ELEVATOR_START_X+        1          +(self.name*self.ELEVATOR_SEPARATION),self.ELEVATOR_START_Y + 10*self.ELEVATOR_HEIGHT,fill=self.DOOR_COLOR)
        self.x = canvas.coords(self.body)[0]
        self.y = canvas.coords(self.body)[1]
        self.dest = None
        self.people = 0
        
        self.floor_list = []
        for i in range(0,10):
            self.floor_list.append(False)

        self.call_queue = []

        self.door_status = 0
        self.open_status = 0
        self.move_status = "idle"
        self.status = "idle"
        self.current_floor = 0
        self.vel = 0

    def addFloor(self,floor,direction,type):


        if floor == self.current_floor:
            # if len(self.call_queue)==0:
            #     self.call_queue.append([floor,direction])
            # else:
            #     self.call_queue.insert(0,[floor,direction])

            if direction == "up":
                self.building.floor_list[int(self.current_floor)].upTurnOff()
            else:
                self.building.floor_list[int(self.current_floor)].downTurnOff()

            panel = self.building.panel_list[self.name]
            if int(self.current_floor)==0:
                panel.canvas.itemconfig(panel.button_list[9], fill="#888")
                panel.flag_list[9] = False
            else:
                panel.canvas.itemconfig(panel.button_list[int(self.current_floor)-1], fill="#888")
                panel.flag_list[self.dest-1] = False

            if self.status == "idle":
                self.status = "opening"
            elif self.status == "closing":
                self.status = "opening"
            elif self.status == "open":
                self.open_status -= 50


        elif self.status == "moving":
            if (self.current_floor < floor and self.dest >= floor and direction=="up") or (self.current_floor > floor and self.dest <= floor and direction=="down"):
                if self.dest==floor:
                    self.setElevator(type,floor,direction)
                    return
                self.call_queue.insert(0,[floor,direction])
            else:
                flag = 0
                for i in range(1,len(self.call_queue)):
                    previous = self.call_queue[i-1][0]
                    next = self.call_queue[i][0]
                    if (previous < floor and next >= floor and direction=="up") or (previous > floor and next <= floor and direction=="down"):
                        if next==floor:
                            self.setElevator(type,floor,direction)
                            return
                        flag = 1
                        self.call_queue.insert(i,[floor,direction])
                        break

                if flag == 0:
                    self.call_queue.append([floor,direction])


        elif self.status == "idle" or "opening" or "open" or "closing" and not(floor==self.current_floor):
            if (len(self.call_queue)==0):
                self.call_queue.append([floor,direction])
            else:
                if (self.current_floor < floor and self.call_queue[0][0] >= floor and direction=="up") or (self.current_floor > floor and self.call_queue[0][0] <= floor and direction=="down"):
                    if self.call_queue[0][0]==floor:
                        self.setElevator(type,floor,direction)
                        return                    
                    self.call_queue.insert(0,[floor,direction])
                else:
                    flag = 0
                    for i in range(1,len(self.call_queue)):
                        previous = self.call_queue[i-1][0]
                        next = self.call_queue[i][0]
                        if (previous < floor and next >= floor and direction=="up") or (previous > floor and next <= floor and direction=="down"):
                            if next==floor:
                                self.setElevator(type,floor,direction)
                                return
                            flag = 1
                            self.call_queue.insert(i,[floor,direction])
                            break

                    if flag == 0:
                        self.call_queue.append([floor,direction])


        self.setElevator(type,floor,direction)


    def setElevator(self,type,floor,direction):
        if type=="floor_call" and not(floor==self.current_floor):
            if direction=="up":
                self.building.floor_list[floor].elevator_up = self
            else:
                self.building.floor_list[floor].elevator_down = self

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
        

        canvas.update()

    
    def checkQueue(self):

        if not(len(self.call_queue)==0):
            self.dest = self.call_queue[0][0]
            if self.status == "idle":
                if self.current_floor < self.dest:
                    self.vel = -self.ELEVATOR_VELOCITY
                elif self.current_floor > self.dest:
                    self.vel = self.ELEVATOR_VELOCITY
                else:
                    self.vel = 0

            self.status = "moving"

    def checkDest(self):


        self.current_floor = float(10 - float((self.y+10)/60))

        if self.dest == self.current_floor:

            if (([self.dest,"up"] in self.call_queue) or ([self.dest,"down"] in self.call_queue)):
                if [self.dest,"up"] in self.call_queue:
                    self.building.floor_list[self.dest].upTurnOff()
                    self.building.floor_list[self.dest].elevator_up = None

                elif [self.dest,"down"] in self.call_queue:
                    self.building.floor_list[self.dest].downTurnOff()
                    self.building.floor_list[self.dest].elevator_down = None


                panel = self.building.panel_list[self.name]
                if self.dest==0:
                    panel.canvas.itemconfig(panel.button_list[9], fill="#888")
                    panel.flag_list[9] = False
                else:
                    panel.canvas.itemconfig(panel.button_list[self.dest-1], fill="#888")
                    panel.flag_list[self.dest-1] = False

                if [self.dest,"up"] in self.call_queue:
                    self.call_queue.remove([self.dest,"up"])
                elif [self.dest,"down"] in self.call_queue:
                    self.call_queue.remove([self.dest,"down"])


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
