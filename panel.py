class Panel(object):

    def __init__(self,canvas):

        self.body = canvas.create_rectangle(50,300,250,500,fill="#fff")
        # self.x = canvas.coords(self.body)[0]
        # self.y = canvas.coords(self.body)[1]

        self.display_half = canvas.create_rectangle(50,300,250,350,fill="#444")
        self.button_half  = canvas.create_rectangle(50,350,250,500,fill="#033")

        self.floor_1 = canvas.create_rectangle(50,400,250,400,fill="#000")
        self.floor_2 = canvas.create_rectangle(50,450,250,450,fill="#000")
        self.floor_3 = canvas.create_rectangle(50,500,250,500,fill="#000")
        
        
