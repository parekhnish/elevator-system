
class Panel(object):

	def __init__(self,canvas):

		self.body = canvas.create_rectangle(50,300,250,500,fill="#fff")
		# self.x = canvas.coords(self.body)[0]
  		# self.y = canvas.coords(self.body)[1]

        self.display_half = canvas.create_rectangle(50,300,250,350,fill="#444")
        self.button_half  = canvas.create_rectangle(50,350,250,500,fill="#033")

        self.display_half_x = canvas.coords(self.body)[0]
        self.display_half_y = canvas.coords(self.body)[1]

        self.button_half_x = canvas.coords(self.body)[0]
        self.button_half_x = canvas.coords(self.body)[1]
