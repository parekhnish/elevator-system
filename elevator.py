class Elevator(object):

	def __init__(self,canvas,name):

		self.name = name
		self.body = canvas.create_rectangle(200,200,200,200,fill="#000")
		self.x = canvas.coords(self.body)[0]
		self.y = canvas.coords(self.body)[1]

		self.floor_list = []
		for i in range(0,11):
			floor_list[i] = False

		print len(floor_list)

		self.call_queue = []

		self.door_status = "closed"
		self.move_status = "idle"
		self.current_floor = 0

		self.vel = 0
