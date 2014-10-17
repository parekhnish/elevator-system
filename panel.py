class Panel(object):

    def __init__(self,canvas):

        #MAIN PANEL BODY
        self.body = canvas.create_rectangle(50,300,200,550,fill="#fff")
        
        self.display_half   = canvas.create_rectangle(50,300,200,350,fill="#444")
        self.v_display_line = canvas.create_rectangle(150,300,150,350,fill="#444")
        self.button_half    = canvas.create_rectangle(50,350,200,550,fill="#fff")

        #HORIZONTAL LINES
        self.hline_1 = canvas.create_rectangle(50,400,200,400,fill="#000")
        self.hline_2 = canvas.create_rectangle(50,450,200,450,fill="#000")
        self.hline_3 = canvas.create_rectangle(50,500,200,500,fill="#000")
        
        #VERTICAL LINES
        self.vline_1 = canvas.create_rectangle(100,350,100,550,fill="#000")
        self.vline_2 = canvas.create_rectangle(150,350,150,550,fill="#000")
        
        #BUTTON 1
        self.button_1   = canvas.create_rectangle(60,360,90,390,fill="#888")
        self.button_1_id = canvas.create_text(70, 370, anchor="nw")
        canvas.itemconfig(self.button_1_id, text="1")
        #canvas.tag_bind(self.button_1_id, 'ButtonPress-1', self.foo(1))

        #BUTTON 2
        self.button_2 = canvas.create_rectangle(110,360,140,390,fill="#888")
        self.button_2_id = canvas.create_text(120, 370, anchor="nw")
        canvas.itemconfig(self.button_2_id, text="2")
        
        #BUTTON 3
        self.button_3 = canvas.create_rectangle(160,360,190,390,fill="#888")
        self.button_3_id = canvas.create_text(170, 370, anchor="nw")
        canvas.itemconfig(self.button_3_id, text="3")
        
        #BUTTON 4
        self.button_4 = canvas.create_rectangle(60,410,90,440,fill="#888")
        self.button_4_id = canvas.create_text(70, 420, anchor="nw")
        canvas.itemconfig(self.button_4_id, text="4")
        
        #BUTTON 5
        self.button_5 = canvas.create_rectangle(110,410,140,440,fill="#888")
        self.button_5_id = canvas.create_text(120, 420, anchor="nw")
        canvas.itemconfig(self.button_5_id, text="5")
        
        #BUTTON 6
        self.button_6 = canvas.create_rectangle(160,410,190,440,fill="#888")
        self.button_6_id = canvas.create_text(170, 420, anchor="nw")
        canvas.itemconfig(self.button_6_id, text="6")
        
        #BUTTON 7
        self.button_7 = canvas.create_rectangle(60,460,90,490,fill="#888")
        self.button_7_id = canvas.create_text(70, 470, anchor="nw")
        canvas.itemconfig(self.button_7_id, text="7")
        
        #BUTTON 8
        self.button_8 = canvas.create_rectangle(110,460,140,490,fill="#888")
        self.button_8_id = canvas.create_text(120, 470, anchor="nw")
        canvas.itemconfig(self.button_8_id, text="8")
        
        #BUTTON 9
        self.button_9 = canvas.create_rectangle(160,460,190,490,fill="#888")
        self.button_9_id = canvas.create_text(170, 470, anchor="nw")
        canvas.itemconfig(self.button_9_id, text="9")
        
        #BUTTON G
        self.button_10 = canvas.create_rectangle(110,510,140,540,fill="#888")
        self.button_10_id = canvas.create_text(120, 520, anchor="nw")
        canvas.itemconfig(self.button_10_id, text="G")
        
    def foo(self,i):

        print "Button " + str(i) + " pressed!"    
