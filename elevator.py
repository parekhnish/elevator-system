class Elevator(object):

    def __init__(self,canvas,name):

        self.ELEVATOR_WIDTH = 30
        self.ELEVATOR_HEIGHT = 60
        self.ELEVATOR_SEPARATION = 120
        self.ELEVATOR_START_X = 250
        self.ELEVATOR_START_Y = 50
        self.ELEVATOR_VELOCITY = 5
        self.ELEVATOR_COLOR = "#060"

        self.name = name
        self.body = canvas.create_rectangle(self.ELEVATOR_START_X+(self.name*self.ELEVATOR_SEPARATION),self.ELEVATOR_START_Y,self.ELEVATOR_START_X+self.ELEVATOR_WIDTH+(self.name*self.ELEVATOR_SEPARATION),self.ELEVATOR_START_Y+self.ELEVATOR_HEIGHT,fill=self.ELEVATOR_COLOR)
        self.x = canvas.coords(self.body)[0]
        self.y = canvas.coords(self.body)[1]

        self.floor_list = []
        for i in range(0,10):
            self.floor_list.append(False)

        self.call_queue = []

        self.door_status = "closed"
        self.move_status = "idle"
        self.current_floor = 0
        self.vel = self.ELEVATOR_VELOCITY

    def update(self,canvas):

        self.checkCurrentFloor()

        canvas.move(self.body,0,self.vel)
        self.x = canvas.coords(self.body)[0]
        self.y = canvas.coords(self.body)[1]
        if self.y >= 230:
            self.vel = 0
            canvas.itemconfigure(self.body,fill="#ff4")

        canvas.update()

    def checkCurrentFloor(self):

        if((self.y+10)%60==0):
            self.current_floor = 10 - (self.y+10)/60
