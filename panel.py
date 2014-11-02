class Panel(object):

    def __init__(self,canvas,number,elevator):

        self.canvas   = canvas
        self.elevator = elevator
        self.number   = number
        
        #GLOBAL VARIABLES
        self.PANEL_WIDTH         = 150  
        self.PANEL_HEIGHT        = 250
        self.BUTTON_LENGTH       = 30
        self.PANEL_GAP           = 70 
        self.DISPLAY_HALF_HEIGHT = 50
        self.BUTTON_HALF_HEIGHT  = 200
        self.OFFSET              = 10
        self.TEXT_OFFSET         = 10
        #--------------------------------------------------
        if(self.number == 1):
            self.PANEL_X             = 20 
            self.PANEL_Y             = 70 
        #--------------------------------------------------
        elif self.number == 2:        
            self.PANEL_X             = 20 + (self.PANEL_WIDTH + self.PANEL_GAP)
            self.PANEL_Y             = 70         
        #--------------------------------------------------
        elif self.number == 3:
            self.PANEL_X             = 20 
            self.PANEL_Y             = 70 + (self.PANEL_HEIGHT + self.PANEL_GAP)        
        #--------------------------------------------------
        else:
            self.PANEL_X             = 20 + (self.PANEL_WIDTH + self.PANEL_GAP)
            self.PANEL_Y             = 70 + (self.PANEL_HEIGHT + self.PANEL_GAP)        
        #--------------------------------------------------

        self.label = self.canvas.create_text(self.PANEL_X + self.PANEL_WIDTH/2,self.PANEL_Y - 10,font="Arial 20 bold", text = "Elevator " + str(self.number))

        #HORIZONTAL PARTITION LINE VARIABLES
        self.HLINE1_X            = self.PANEL_X
        self.HLINE1_Y            = self.PANEL_Y + 2*self.DISPLAY_HALF_HEIGHT
        self.HLINE2_X            = self.PANEL_X
        self.HLINE2_Y            = self.PANEL_Y + 3*self.DISPLAY_HALF_HEIGHT
        self.HLINE3_X            = self.PANEL_X
        self.HLINE3_Y            = self.PANEL_Y + 4*self.DISPLAY_HALF_HEIGHT

        #VERTICAL PARTITION LINE VARIABLES
        self.VLINE1_X            = self.PANEL_X + self.DISPLAY_HALF_HEIGHT
        self.VLINE1_Y            = self.PANEL_Y + self.DISPLAY_HALF_HEIGHT
        self.VLINE2_X            = self.PANEL_X + 2*self.DISPLAY_HALF_HEIGHT
        self.VLINE2_Y            = self.PANEL_Y + self.DISPLAY_HALF_HEIGHT

        #BUTTON VARIABLES
        self.BUTTON_START_X      = self.PANEL_X + self.OFFSET
        self.BUTTON_START_Y      = self.PANEL_Y + self.DISPLAY_HALF_HEIGHT + self.OFFSET
        self.BUTTON_GAP_X        = self.VLINE2_X - self.VLINE1_X
        self.BUTTON_GAP_Y        = self.HLINE2_Y - self.HLINE1_Y

        #MAIN PANEL BODY
        self.body = canvas.create_rectangle(self.PANEL_X,self.PANEL_Y,self.PANEL_X + self.PANEL_WIDTH,self.PANEL_Y + self.PANEL_HEIGHT,fill="#fff")
        
        self.display_half   = canvas.create_rectangle(self.PANEL_X,self.PANEL_Y,self.PANEL_X + self.PANEL_WIDTH,self.PANEL_Y + self.DISPLAY_HALF_HEIGHT,fill="#444")
        self.button_half    = canvas.create_rectangle(self.PANEL_X,self.PANEL_Y + self.DISPLAY_HALF_HEIGHT,self.PANEL_X + self.PANEL_WIDTH,self.PANEL_Y + self.BUTTON_HALF_HEIGHT,fill="#fff")

        #HORIZONTAL LINES
        self.hline_1 = canvas.create_rectangle(self.HLINE1_X,self.HLINE1_Y,self.HLINE1_X + self.PANEL_WIDTH,self.HLINE1_Y,fill="#000")
        self.hline_2 = canvas.create_rectangle(self.HLINE2_X,self.HLINE2_Y,self.HLINE2_X + self.PANEL_WIDTH,self.HLINE2_Y,fill="#000")
        self.hline_3 = canvas.create_rectangle(self.HLINE3_X,self.HLINE3_Y,self.HLINE3_X + self.PANEL_WIDTH,self.HLINE3_Y,fill="#000")
        
        #VERTICAL LINES
        self.vline_1 = canvas.create_rectangle(self.VLINE1_X,self.VLINE1_Y,self.VLINE1_X,self.VLINE1_Y + self.BUTTON_HALF_HEIGHT,fill="#000")
        self.vline_2 = canvas.create_rectangle(self.VLINE2_X,self.VLINE2_Y,self.VLINE2_X,self.VLINE2_Y + self.BUTTON_HALF_HEIGHT,fill="#000")
        
        #BUTTON LIST AND BUTTON STATUS FLAGS
        self.button_list = []
        self.flag_list   = []

        for i in range(0,12):
            self.flag_list.append(False)
#----------------------------------------------------------------------------------------------------
        #BUTTON 1
        self.button_1    = canvas.create_rectangle(self.BUTTON_START_X,self.BUTTON_START_Y,self.BUTTON_START_X + self.BUTTON_LENGTH,self.BUTTON_START_Y + self.BUTTON_LENGTH,fill="#888")
        self.button_1_id = canvas.create_text(self.BUTTON_START_X + self.TEXT_OFFSET, self.BUTTON_START_Y + self.TEXT_OFFSET, anchor="nw")
        
        canvas.itemconfig(self.button_1_id, text="1")
        canvas.tag_bind(self.button_1, '<Button-1>', lambda x: self.foo(1,self.flag_list[0]))
        
        self.button_list.append(self.button_1)
#----------------------------------------------------------------------------------------------------    
        #BUTTON 2
        self.button_2    = canvas.create_rectangle(self.BUTTON_START_X + self.BUTTON_GAP_X,self.BUTTON_START_Y,self.BUTTON_START_X + self.BUTTON_LENGTH + self.BUTTON_GAP_X,self.BUTTON_START_Y + self.BUTTON_LENGTH,fill="#888")
        self.button_2_id = canvas.create_text(self.BUTTON_START_X + self.BUTTON_GAP_X + self.TEXT_OFFSET, self.BUTTON_START_Y + self.TEXT_OFFSET, anchor="nw")
        
        canvas.itemconfig(self.button_2_id, text="2")
        canvas.tag_bind(self.button_2, '<Button-1>', lambda x: self.foo(2,self.flag_list[1]))
        
        self.button_list.append(self.button_2)
#----------------------------------------------------------------------------------------------------      
        #BUTTON 3
        self.button_3    = canvas.create_rectangle(self.BUTTON_START_X + 2*self.BUTTON_GAP_X,self.BUTTON_START_Y,self.BUTTON_START_X + self.BUTTON_LENGTH + 2*self.BUTTON_GAP_X,self.BUTTON_START_Y + self.BUTTON_LENGTH,fill="#888")
        self.button_3_id = canvas.create_text(self.BUTTON_START_X + 2*self.BUTTON_GAP_X + self.TEXT_OFFSET, self.BUTTON_START_Y + self.TEXT_OFFSET, anchor="nw")
        
        canvas.itemconfig(self.button_3_id, text="3")
        canvas.tag_bind(self.button_3, '<Button-1>', lambda x: self.foo(3,self.flag_list[2]))
  
        self.button_list.append(self.button_3)
#----------------------------------------------------------------------------------------------------      
        #BUTTON 4
        self.button_4    = canvas.create_rectangle(self.BUTTON_START_X,self.BUTTON_START_Y + self.BUTTON_GAP_Y,self.BUTTON_START_X + self.BUTTON_LENGTH,self.BUTTON_START_Y + self.BUTTON_GAP_Y + self.BUTTON_LENGTH,fill="#888")
        self.button_4_id = canvas.create_text(self.BUTTON_START_X + self.TEXT_OFFSET, self.BUTTON_START_Y + self.BUTTON_GAP_Y + self.TEXT_OFFSET, anchor="nw")
        
        canvas.itemconfig(self.button_4_id, text="4")
        canvas.tag_bind(self.button_4, '<Button-1>', lambda x: self.foo(4,self.flag_list[3]))
        
        self.button_list.append(self.button_4)
#----------------------------------------------------------------------------------------------------        
        #BUTTON 5
        self.button_5    = canvas.create_rectangle(self.BUTTON_START_X + self.BUTTON_GAP_X,self.BUTTON_START_Y + self.BUTTON_GAP_Y,self.BUTTON_START_X + self.BUTTON_GAP_X + self.BUTTON_LENGTH,self.BUTTON_START_Y + self.BUTTON_GAP_Y + self.BUTTON_LENGTH,fill="#888")
        self.button_5_id = canvas.create_text(self.BUTTON_START_X + self.BUTTON_GAP_X + self.TEXT_OFFSET, self.BUTTON_START_Y + self.BUTTON_GAP_Y + self.TEXT_OFFSET, anchor="nw")

        canvas.itemconfig(self.button_5_id, text="5")
        canvas.tag_bind(self.button_5, '<Button-1>', lambda x: self.foo(5,self.flag_list[4]))

        self.button_list.append(self.button_5)
#-----------------------------------------------------------------------------------------------------        
        #BUTTON 6
        self.button_6    = canvas.create_rectangle(self.BUTTON_START_X + 2*self.BUTTON_GAP_X,self.BUTTON_START_Y + self.BUTTON_GAP_Y,self.BUTTON_START_X + 2*self.BUTTON_GAP_X + self.BUTTON_LENGTH,self.BUTTON_START_Y + self.BUTTON_GAP_Y + self.BUTTON_LENGTH,fill="#888")
        self.button_6_id = canvas.create_text(self.BUTTON_START_X + 2*self.BUTTON_GAP_X + self.TEXT_OFFSET, self.BUTTON_START_Y + self.BUTTON_GAP_Y + self.TEXT_OFFSET, anchor="nw")
        
        canvas.itemconfig(self.button_6_id, text="6")
        canvas.tag_bind(self.button_6, '<Button-1>', lambda x: self.foo(6,self.flag_list[5]))
        
        self.button_list.append(self.button_6)
#-----------------------------------------------------------------------------------------------------        
        #BUTTON 7
        self.button_7    = canvas.create_rectangle(self.BUTTON_START_X,self.BUTTON_START_Y + 2*self.BUTTON_GAP_Y,self.BUTTON_START_X + self.BUTTON_LENGTH,self.BUTTON_START_Y + 2*self.BUTTON_GAP_Y + self.BUTTON_LENGTH,fill="#888")
        self.button_7_id = canvas.create_text(self.BUTTON_START_X + self.TEXT_OFFSET, self.BUTTON_START_Y + 2*self.BUTTON_GAP_Y + self.TEXT_OFFSET, anchor="nw")
        
        canvas.itemconfig(self.button_7_id, text="7")
        canvas.tag_bind(self.button_7, '<Button-1>', lambda x: self.foo(7,self.flag_list[6]))
        
        self.button_list.append(self.button_7)
#------------------------------------------------------------------------------------------------------        
        #BUTTON 8
        self.button_8    = canvas.create_rectangle(self.BUTTON_START_X + self.BUTTON_GAP_X,self.BUTTON_START_Y + 2*self.BUTTON_GAP_Y,self.BUTTON_START_X + self.BUTTON_GAP_X + self.BUTTON_LENGTH,self.BUTTON_START_Y + 2*self.BUTTON_GAP_Y + self.BUTTON_LENGTH,fill="#888")
        self.button_8_id = canvas.create_text(self.BUTTON_START_X + self.BUTTON_GAP_X + self.TEXT_OFFSET, self.BUTTON_START_Y + 2*self.BUTTON_GAP_Y + self.TEXT_OFFSET, anchor="nw")
        
        canvas.itemconfig(self.button_8_id, text="8")
        canvas.tag_bind(self.button_8, '<Button-1>', lambda x: self.foo(8,self.flag_list[7]))
        
        self.button_list.append(self.button_8)
#--------------------------------------------------------------------------------------------------------        
        #BUTTON 9
        self.button_9    = canvas.create_rectangle(self.BUTTON_START_X + 2*self.BUTTON_GAP_X,self.BUTTON_START_Y + 2*self.BUTTON_GAP_Y,self.BUTTON_START_X + 2*self.BUTTON_GAP_X + self.BUTTON_LENGTH,self.BUTTON_START_Y + 2*self.BUTTON_GAP_Y + self.BUTTON_LENGTH,fill="#888")
        self.button_9_id = canvas.create_text(self.BUTTON_START_X + 2*self.BUTTON_GAP_X + self.TEXT_OFFSET, self.BUTTON_START_Y + 2*self.BUTTON_GAP_Y + self.TEXT_OFFSET, anchor="nw")
        
        canvas.itemconfig(self.button_9_id, text="9")
        canvas.tag_bind(self.button_9, '<Button-1>', lambda x: self.foo(9,self.flag_list[8]))
        self.button_list.append(self.button_9)
#---------------------------------------------------------------------------------------------------------        
        #BUTTON G
        self.button_10    = canvas.create_rectangle(self.BUTTON_START_X + self.BUTTON_GAP_X,self.BUTTON_START_Y + 3*self.BUTTON_GAP_Y,self.BUTTON_START_X + self.BUTTON_GAP_X + self.BUTTON_LENGTH,self.BUTTON_START_Y + 3*self.BUTTON_GAP_Y + self.BUTTON_LENGTH,fill="#888")
        self.button_10_id = canvas.create_text(self.BUTTON_START_X + self.BUTTON_GAP_X + self.TEXT_OFFSET, self.BUTTON_START_Y + 3*self.BUTTON_GAP_Y + self.TEXT_OFFSET, anchor="nw")
        
        canvas.itemconfig(self.button_10_id, text="G")
        canvas.tag_bind(self.button_10, '<Button-1>', lambda x: self.foo('G',self.flag_list[9]))
        
        self.button_list.append(self.button_10)
#----------------------------------------------------------------------------------------------------------               
        #BUTTON <
        self.button_11    = canvas.create_rectangle(self.BUTTON_START_X,self.BUTTON_START_Y + 3*self.BUTTON_GAP_Y,self.BUTTON_START_X + self.BUTTON_LENGTH,self.BUTTON_START_Y + 3*self.BUTTON_GAP_Y + self.BUTTON_LENGTH,fill="#888")
        self.button_11_id = canvas.create_text(self.BUTTON_START_X + self.TEXT_OFFSET, self.BUTTON_START_Y + 3*self.BUTTON_GAP_Y + self.TEXT_OFFSET, anchor="nw")
        
        canvas.itemconfig(self.button_11_id, text="<")
        canvas.tag_bind(self.button_11, '<Button-1>', lambda x: self.foo('<',self.flag_list[10]))
        
        self.button_list.append(self.button_11)
#----------------------------------------------------------------------------------------------------------
        #BUTTON 9
        self.button_12    = canvas.create_rectangle(self.BUTTON_START_X + 2*self.BUTTON_GAP_X,self.BUTTON_START_Y + 3*self.BUTTON_GAP_Y,self.BUTTON_START_X + 2*self.BUTTON_GAP_X + self.BUTTON_LENGTH,self.BUTTON_START_Y + 3*self.BUTTON_GAP_Y + self.BUTTON_LENGTH,fill="#888")
        self.button_12_id = canvas.create_text(self.BUTTON_START_X + 2*self.BUTTON_GAP_X + self.TEXT_OFFSET, self.BUTTON_START_Y + 3*self.BUTTON_GAP_Y + self.TEXT_OFFSET, anchor="nw")
        
        canvas.itemconfig(self.button_12_id, text=">")
        canvas.tag_bind(self.button_12, '<Button-1>', lambda x: self.foo('>',self.flag_list[11]))
        self.button_list.append(self.button_12)
#-----------------------------------------------------------------------------------------------------------
    def foo(self,event,flag):

        if flag == False:
            
            if event == 'G' or event == '<' or event == '>':
                if event == 'G':
                    self.elevator.addFloor(0)
                
                elif event == '>':
                    if self.elevator.status == "closing" or self.elevator.status == "idle":
                        self.elevator.status = "opening"         
                elif event == '<':
                    if self.elevator.status == "opening" or self.elevator.status == "open":
                        self.elevator.status == "closing"

            else:    
                self.elevator.addFloor(event)

            if event == 'G':
                self.canvas.itemconfig(self.button_list[9], fill="#ff0")
                self.flag_list[9] = True
           
            elif event == '<':
                self.canvas.itemconfig(self.button_list[10], fill="#ff0")
                self.flag_list[10] = True
            
            elif event == '>':
                self.canvas.itemconfig(self.button_list[11], fill="#ff0")  
                self.flag_list[11] = True

            else:    
                self.canvas.itemconfig(self.button_list[event-1], fill="#ff0")
                self.flag_list[event-1] = True

        else:

            if event == 'G' or event == '<' or event == '>':
                if event == 'G':
                    temp = 0
                    if temp in self.elevator.call_queue:
                        self.elevator.call_queue.remove(0)

            else:
                if event in self.elevator.call_queue:
                    self.elevator.call_queue.remove(event)        
            

            if event == 'G':
                self.canvas.itemconfig(self.button_list[9], fill="#888")
                self.flag_list[9] = False
           
            elif event == '<':
                self.canvas.itemconfig(self.button_list[10], fill="#888")
                self.flag_list[10] = False
            
            elif event == '>':
                self.canvas.itemconfig(self.button_list[11], fill="#888")  
                self.flag_list[11] = False

            else:    
                self.canvas.itemconfig(self.button_list[event-1], fill="#888")
                self.flag_list[event-1] = False

        
        
    


    
