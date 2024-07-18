from drawingpanel import *
panel  = DrawingPanel(1500, 1000)
panel.set_background("white")
canvas = panel.canvas

class missile():
    def __init__(self):
        self.px = 250
        self.py = 470
    def draw(self):
        canvas.create_oval(self.px - 15, self.py - 15
         , self.px + 15, self.py + 15, fill='black')
def draw_Bazooka(canvas):
    rec=canvas.create_rectangle(50, 450, 250, 490, fill='green', outline='black')
    canvas.create_rectangle(0, 460, 50, 480, fill='darkgreen', outline='black')
    canvas.create_rectangle(100, 490, 120, 530, fill='brown', outline='black')
    canvas.create_oval(225, 430, 245, 450, fill='grey', outline='black')
class circle():
    def __init__(self,x, y, radius, color):
        circle = canvas.create_oval(x-radius, y-radius, x+radius, y+radius, outline="red", width=2, fill=color)
        self.px=x
        self.py=y
def main():
    panel.set_background("#D68910")
    canvas.create_text(850, 100, text="BOOM!!!", font=("Arial", 30), fill="red")
    circles = []
    circles.append(circle(850, 100, 50, "white"))
    circles.append(circle(850, 900, 50, "white"))
    circles.append(circle(1400, 100, 50, "white"))
    circles.append(circle(1400, 900, 50, "white"))
    circles.append(circle(1150, 470, 50, "yellow"))
    m = []
    for ii in range(5):
        m.append(missile())
    draw_Bazooka(canvas)

    i=0
    while i<5:
        x2=circles[i].px
        y2=circles[i].py
        mid = m[i].px + x2
        mid = mid/2
        gao = y2 - m[i].py
        kuan = x2 - m[i].px

        if gao!=0:
            rate = gao/kuan
        else:
            rate=0
        while (m[i].px < x2):
            m[i].draw()
            z = (mid-m[i].px) / kuan
            z = z * z*50
            m[i].px += 30
            m[i].py += 30 * rate
            if m[i].px>mid:
                m[i].py+=z
            else:
                m[i].py-=z

            panel.sleep(10)
            panel.clear()
            draw_Bazooka(canvas)
            circles = []
            if i<1:
                circles.append(circle(850, 100, 50, "white"))
            else:
                circles.append(circle(1150, 470, 50, "yellow"))
            if i<2:
                circles.append(circle(850, 900, 50, "white"))
            else:
                circles.append(circle(1150, 470, 50, "yellow"))
            if i<3:
                circles.append(circle(1400, 100, 50, "white"))
            else:
                circles.append(circle(1150, 470, 50, "yellow"))
            if i<4:
                circles.append(circle(1400, 900, 50, "white"))
            else:
                circles.append(circle(1150, 470, 50, "yellow"))
            circles.append(circle(1150, 470, 50, "yellow"))
        panel.clear()
        draw_Bazooka(canvas)
        i+=1
        circles = []
        if i < 1:
            circles.append(circle(850, 100, 50, "white"))
        else:
            circles.append(circle(1150, 470, 50, "yellow"))
        if i < 2:
            circles.append(circle(850, 900, 50, "white"))
        else:
            circles.append(circle(1150, 470, 50, "yellow"))
        if i < 3:
            circles.append(circle(1400, 100, 50, "white"))
        else:
            circles.append(circle(1150, 470, 50, "yellow"))
        if i < 4:
            circles.append(circle(1400, 900, 50, "white"))
        else:
            circles.append(circle(1150, 470, 50, "yellow"))
        circles.append(circle(1150, 470, 50, "yellow"))
        canvas.create_text(x2,y2, text="BOOM!!!", font=("Arial", 50), fill="red")
        panel.sleep(1000)

    panel.clear()
    draw_Bazooka(canvas)
    panel.sleep(1000)
    panel.clear()
    canvas.create_text(750, 500, text="There is nothing meaningful after a total war.", font=("Arial", 50), fill="red")
    panel.mainloop()
main()