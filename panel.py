class Panel(object):

    def __init__(self,canvas):

        #GLOBAL VARIABLES
        self.PANEL_WIDTH         = 150  
        self.PANEL_HEIGHT        = 250
        self.BUTTON_LENGTH       = 30
        self.PANEL_X             = 50
        self.PANEL_Y             = 300
        self.DISPLAY_HALF_HEIGHT = 50
        self.BUTTON_HALF_HEIGHT  = 200

        #HORIZONTAL PARTITION LINE VARIABLES
        self.HLINE1_X            = 50
        self.HLINE1_Y            = 400
        self.HLINE2_X            = 50
        self.HLINE2_Y            = 450
        self.HLINE3_X            = 50
        self.HLINE3_Y            = 500

        #VERTICAL PARTITION LINE VARIABLES
        self.VLINE1_X            = 100
        self.VLINE1_Y            = 350
        self.VLINE2_X            = 150
        self.VLINE2_Y            = 350

        #MAIN PANEL BODY
        self.body = canvas.create_rectangle(self.PANEL_X,self.PANEL_Y,self.PANEL_X + self.PANEL_WIDTH,self.PANEL_Y + self.PANEL_HEIGHT,fill="#fff")
        
        self.display_half   = canvas.create_rectangle(self.PANEL_X,self.PANEL_Y,self.PANEL_X + self.PANEL_WIDTH,self.PANEL_Y + self.DISPLAY_HALF_HEIGHT,fill="#444")
        #self.v_display_line = canvas.create_rectangle(150,300,150,350,fill="#444")
        self.button_half    = canvas.create_rectangle(self.PANEL_X,self.PANEL_Y + self.DISPLAY_HALF_HEIGHT,self.PANEL_X + self.PANEL_WIDTH,self.PANEL_Y + self.BUTTON_HALF_HEIGHT,fill="#fff")

        #HORIZONTAL LINES
        self.hline_1 = canvas.create_rectangle(self.HLINE1_X,self.HLINE1_Y,self.HLINE1_X + self.PANEL_WIDTH,self.HLINE1_Y,fill="#000")
        self.hline_2 = canvas.create_rectangle(self.HLINE2_X,self.HLINE2_Y,self.HLINE2_X + self.PANEL_WIDTH,self.HLINE2_Y,fill="#000")
        self.hline_3 = canvas.create_rectangle(self.HLINE3_X,self.HLINE3_Y,self.HLINE3_X + self.PANEL_WIDTH,self.HLINE3_Y,fill="#000")
        
        #VERTICAL LINES
        self.vline_1 = canvas.create_rectangle(self.VLINE1_X,self.VLINE1_Y,self.VLINE1_X,self.VLINE1_Y + self.BUTTON_HALF_HEIGHT,fill="#000")
        self.vline_2 = canvas.create_rectangle(self.VLINE2_X,self.VLINE2_Y,self.VLINE2_X,self.VLINE2_Y + self.BUTTON_HALF_HEIGHT,fill="#000")
        
        #BUTTON 1
        self.button_1   = canvas.create_rectangle(60,360,90,390,fill="#888")
        self.button_1_id = canvas.create_text(70, 370, anchor="nw")
        canvas.itemconfig(self.button_1_id, text="1")
        canvas.tag_bind(self.button_1, '<Button-1>', lambda x: self.foo(1))
        # self.button_1.bind('<Button-1>',foo)

        #BUTTON 2
        self.button_2 = canvas.create_rectangle(110,360,140,390,fill="#888")
        self.button_2_id = canvas.create_text(120, 370, anchor="nw")
        canvas.itemconfig(self.button_2_id, text="2")
        canvas.tag_bind(self.button_2, '<Button-1>', lambda x: self.foo(2))

        #BUTTON 3
        self.button_3 = canvas.create_rectangle(160,360,190,390,fill="#888")
        self.button_3_id = canvas.create_text(170, 370, anchor="nw")
        canvas.itemconfig(self.button_3_id, text="3")
        canvas.tag_bind(self.button_3, '<Button-1>', lambda x: self.foo(3))

        #BUTTON 4
        self.button_4 = canvas.create_rectangle(60,410,90,440,fill="#888")
        self.button_4_id = canvas.create_text(70, 420, anchor="nw")
        canvas.itemconfig(self.button_4_id, text="4")
        canvas.tag_bind(self.button_4, '<Button-1>', lambda x: self.foo(4))

        #BUTTON 5
        self.button_5 = canvas.create_rectangle(110,410,140,440,fill="#888")
        self.button_5_id = canvas.create_text(120, 420, anchor="nw")
        canvas.itemconfig(self.button_5_id, text="5")
        canvas.tag_bind(self.button_5, '<Button-1>', lambda x: self.foo(5))

        #BUTTON 6
        self.button_6 = canvas.create_rectangle(160,410,190,440,fill="#888")
        self.button_6_id = canvas.create_text(170, 420, anchor="nw")
        canvas.itemconfig(self.button_6_id, text="6")
        canvas.tag_bind(self.button_6, '<Button-1>', lambda x: self.foo(6))

        #BUTTON 7
        self.button_7 = canvas.create_rectangle(60,460,90,490,fill="#888")
        self.button_7_id = canvas.create_text(70, 470, anchor="nw")
        canvas.itemconfig(self.button_7_id, text="7")
        canvas.tag_bind(self.button_7, '<Button-1>', lambda x: self.foo(7))

        #BUTTON 8
        self.button_8 = canvas.create_rectangle(110,460,140,490,fill="#888")
        self.button_8_id = canvas.create_text(120, 470, anchor="nw")
        canvas.itemconfig(self.button_8_id, text="8")
        canvas.tag_bind(self.button_8, '<Button-1>', lambda x: self.foo(8))

        #BUTTON 9
        self.button_9 = canvas.create_rectangle(160,460,190,490,fill="#888")
        self.button_9_id = canvas.create_text(170, 470, anchor="nw")
        canvas.itemconfig(self.button_9_id, text="9")
        canvas.tag_bind(self.button_9, '<Button-1>', lambda x: self.foo(9))

        #BUTTON G
        self.button_10 = canvas.create_rectangle(110,510,140,540,fill="#888")
        self.button_10_id = canvas.create_text(120, 520, anchor="nw")
        canvas.itemconfig(self.button_10_id, text="G")
        canvas.tag_bind(self.button_10, '<Button-1>', lambda x: self.foo('G'))

    def foo(self,event):

        print "Button " + str(event) + " pressed!"
        

    
