import math

class Floor(object):

    def __init__(self,canvas,app,name,display_up,display_down):

        self.app = app
        self.name = name
        self.canvas = canvas

        self.display_up = display_up
        self.display_down = display_down
        self.display_up_text = canvas.create_text(35 , 60+((9-self.name)*60) , anchor="nw")
        self.display_down_text = canvas.create_text(175, 60+((9-self.name)*60) , anchor="nw")
        self.display_up_value = '***'
        self.display_down_value = '***'

        self.elevator_up = None
        self.elevator_down = None

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

    def updateDisplay(self):

        if self.elevator_up==None:
            self.display_up_value = '***'
        else:
            if self.elevator_up.status == "moving":
                if self.elevator_up.move_status == "down":
                    self.display_up_value = str(int(math.ceil(self.elevator_up.current_floor)))
                else:
                    self.display_up_value = str(int(math.floor(self.elevator_up.current_floor)))
            else:
                self.display_up_value = str(int(self.elevator_up.current_floor))
                
            

        if self.elevator_down==None:
            self.display_down_value = '***'
        else:
            if self.elevator_down.status == "moving":
                if self.elevator_down.move_status == "down":
                    self.display_down_value = str(int(math.ceil(self.elevator_down.current_floor)))
                else:
                    self.display_down_value = str(int(math.floor(self.elevator_down.current_floor)))
            else:
                self.display_down_value = str(int(self.elevator_down.current_floor))
                

        self.canvas.itemconfigure(self.display_up_text, text=self.display_up_value)
        self.canvas.itemconfigure(self.display_down_text, text=self.display_down_value)

