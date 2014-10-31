#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.



from Tkinter import *
import random
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")

class enemy:
    def __init__(self,parent,color,x,y,speed):
        global drawpad
        self.circle = drawpad.create_oval(10, 10, 50, 50, fill=color)
        drawpad.move(self.circle,x,y)
        self.origdirection = speed
        self.direction = self.origdirection
    
    def animate(self):
        global drawpad
        x1, y1, x2, y2 = drawpad.coords(self.circle)
        if x2 > drawpad.winfo_width(): 
            self.direction = -self.origdirection
        elif x1 < 0:
            self.direction = self.origdirection
        
        drawpad.move(self.circle,self.direction,0)
	drawpad.after(1, self.animate)
# Create your "enemies" here, before the class


class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.objects = []
       	    
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=0)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down", background= "green")
       	    self.down.grid(row=0,column=1)
       	    self.down.bind("<Button-1>", self.downClicked)
       	    
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background= "green")
       	    self.left.grid(row=0,column=2)
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background= "green")
       	    self.right.grid(row=0,column=3)
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    
       	    drawpad.pack(side=BOTTOM)
	   
	
	def regObj(self,obj):
	    self.objects.append(obj)
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	  
        def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)
	   
	def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
	   
	def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,20,0)
	  
	       	    #spawn 3 enemies on different y positions

		
		
app = MyApp(root)
for i in range(random.randint(5,10)):
    app.regObj(enemy(app,"red",40 * i + random.randint(5,25),60 * i + random.randint(5,25),random.randint(1,3)).animate())
root.mainloop()