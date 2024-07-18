from drawingpanel import *
height = 1000
width = 1500
panel = DrawingPanel(width, height)
panel.set_background("lightgrey")
canvas = panel.canvas

class missile():
    def __init__(self,color,px,py,vx,vy,ay):
        self.color = color
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy
        self.ay = ay
        
    def draw(self):
        canvas.create_oval(self.px - 40, self.py - 15
         , self.px + 40, self.py + 15, fill= self.color)

    def update(self):
        self.px += self.vx
        # accel due to gravity is 5 pixel per "sec" squared
        self.vy += self.ay
        self.py += self.vy

def draw_Bazooka(canvas):

    canvas.create_rectangle(50, 450, 250, 490, fill='green', outline='black')
    canvas.create_rectangle(0, 460, 50, 480, fill='darkgreen', outline='black')
    canvas.create_rectangle(100, 490, 120, 530, fill='brown', outline='black')
    canvas.create_oval(225, 430, 245, 450, fill='black', outline='grey')

class circle():

    def __init__(self, x, y, radius, color):
        circle = canvas.create_oval(x-radius, y-radius, x+radius, y+radius, outline="red", width=15, fill=color)
        self.px = x
        self.py = y
def main():
    missile1 = missile("black",250, 470, 60, -74, 7.4)
    missile2 = missile("red",250, 470, 60, 0, 7.4)
    missile3 = missile("lightblue",250, 470, 115, -74, 7.4)
    missile4 = missile("yellow",250, 470, 115, 0, 7.4)
    missile5 = missile("violet",250, 470, 90, 0, 0)
    missile_list = [missile1, missile2, missile3, missile4, missile5]

    while True:
        if missile1.px >= 950:
            panel.clear()
            break
        else:
            for m in missile_list:
                m.draw()
            panel.sleep(140)
            panel.clear()
            for m in missile_list:
                m.update()
            circles = []
            circles.append(circle(850, 100, 50, "white"))
            circles.append(circle(850, 900, 50, "white"))
            circles.append(circle(1400, 100, 50, "white"))
            circles.append(circle(1400, 900, 50, "white"))
            circles.append(circle(1150, 470, 50, "white"))
            draw_Bazooka(canvas)
    draw_Bazooka(canvas)
    canvas.create_text(850,100,text="BOOM!!!",font=("Arial",30),fill="red",angle=45)
    panel.sleep(200)
    canvas.create_text(850, 900, text="BOOM!!!", font=("Arial", 30), fill="orange",angle=135)
    panel.sleep(190)
    canvas.create_text(1400, 100, text="BOOM!!!", font=("Arial", 30), fill="orange",angle=135)
    panel.sleep(180)
    canvas.create_text(1400, 900, text="BOOM!!!", font=("Arial", 30), fill="red",angle=45)
    panel.sleep(170)
    canvas.create_text(1150, 470, text="BOOM!!!", font=("Arial", 50), fill="blue")
    panel.sleep(160)
    panel.clear()
    canvas.create_text(1150, 470, text="BOOM!!!", font=("Arial", 55), fill="blue",angle=60)
    panel.sleep(150)
    panel.clear()
    canvas.create_text(1150, 470, text="BOOM!!!", font=("Arial", 60), fill="red", angle=120)
    panel.sleep(140)
    panel.clear()
    canvas.create_text(1150, 470, text="BOOM!!!", font=("Arial", 65), fill="orange", angle=180)
    panel.sleep(130)
    panel.clear()
    canvas.create_text(1150, 470, text="BOOM!!!", font=("Arial", 70), fill="yellow", angle=240)
    panel.sleep(120)
    panel.clear()
    canvas.create_text(1150, 470, text="BOOM!!!", font=("Arial", 75), fill="green", angle=300)
    panel.sleep(110)
    panel.clear()
    canvas.create_text(1150, 470, text="BOOM!!!", font=("Arial", 80), fill="blue", angle=360)
    panel.sleep(100)
    panel.clear()
    canvas.create_text(1150, 470, text="BOOM!!!", font=("Arial", 85), fill="pink", angle=60)
    panel.sleep(90)
    panel.clear()
    canvas.create_text(1150, 470, text="BOOM!!!", font=("Arial", 90), fill="purple", angle=120)
    panel.sleep(80)
    panel.clear()
    canvas.create_text(1150, 470, text="BOOM!!!", font=("Arial", 95), fill="red", angle=180)
    panel.sleep(70)
    panel.clear()
    canvas.create_text(1150, 470, text="BOOM!!!", font=("Arial", 100), fill="orange", angle=240)
    panel.sleep(60)
    panel.clear()
    canvas.create_text(1150, 470, text="BOOM!!!", font=("Arial", 105), fill="yellow", angle=300)
    panel.sleep(50)
    panel.clear()
    canvas.create_text(1150, 470, text="BOOM!!!", font=("Arial", 110), fill="green", angle=360)
main()