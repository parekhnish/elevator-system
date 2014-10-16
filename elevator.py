class Elevator(object):

<<<<<<< HEAD
    def __init__(self,canvas,name):

        self.name = name
        self.body = canvas.create_rectangle(200,200,200,200,fill="#000")
        self.x = canvas.coords(self.body)[0]
        self.y = canvas.coords(self.body)[1]

        self.floor_list = []
        for i in range(0,11):
            floor_list[i] = False

        print len(floor_list)
=======

	def __init__(self,canvas,name):

		self.name = name
		self.body = canvas.create_rectangle(50+(self.name*50),50,80+(self.name*50),150,fill="#060")
		self.x = canvas.coords(self.body)[0]
		self.y = canvas.coords(self.body)[1]

		self.floor_list = []
		for i in range(0,10):
			self.floor_list.append(False)
>>>>>>> 7c2d112d06ced412244db3f39568ce3f24241f36

        self.call_queue = []

        self.door_status = "closed"
        self.move_status = "idle"
        self.current_floor = 0

<<<<<<< HEAD
        self.vel = 0
=======
		self.vel = 5

	def update(self,canvas):

		canvas.move(self.body,0,self.vel)
		canvas.update()


>>>>>>> 7c2d112d06ced412244db3f39568ce3f24241f36
