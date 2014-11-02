class Floor(object):

    def __init__(self,canvas,app,name):

        self.app = app
        self.name = name
        self.canvas = canvas
        self.up_button = canvas.create_polygon( 100,(10-name)*60 + 10 , 83,60*(10-name) + 30 , 117,60*(10-name) + 30 , fill="#000")
        self.down_button = canvas.create_polygon( 133,(10-name)*60 + 10, 167,(10-name)*60 + 10 , 150,60*(10-name) + 30, fill="#000")
        self.up_status = "off"
        self.down_status = "off"

        canvas.tag_bind(self.up_button, '<Button-1>', lambda x: self.upCall(1))
        canvas.tag_bind(self.down_button, '<Button-1>', lambda x: self.downCall(1))


    def upCall(self,event):

        self.canvas.itemconfigure(self.up_button, fill = "#f00")
        self.up_status = "on"
        self.app.floorRequest(self.name,"up")

    def downCall(self,event):

        self.canvas.itemconfigure(self.down_button, fill = "#f00")
        self.down_status = "on"
        self.app.floorRequest(self.name,"down")

    def upTurnOff(self):
        self.canvas.itemconfigure(self.up_button, fill = "#000")
        self.up_status = "off"

    def downTurnOff(self):
        self.canvas.itemconfigure(self.down_button, fill = "#000")
        self.down_status = "off"

