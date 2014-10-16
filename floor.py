class Floor(object):

	def __init__(self,canvas,name):

		self.name = name
		self.upButton = canvas.create_polygon( 100,(10-name)*60 + 10 , 83,60*(10-name) + 30 , 117,60*(10-name) + 30 , fill="#f00")
		self.downButton = canvas.create_polygon( 133,(10-name)*60 + 10, 167,(10-name)*60 + 10 , 150,60*(10-name) + 30, fill="#f00")