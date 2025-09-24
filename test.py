import Onepse
app = Onepse.CreateWindow(title="Test App", size=[600,400]) # Creating window
app.show() # Show window
eventer = Onepse.EventHandler()
color = Onepse.Color()
app.Render.setBgColor([0,0,0])
rect1 = Onepse.Objects.Rect(30,40)
rect2 = Onepse.Objects.Rect(80,60)
rect2.setColor(color.rgb(1,1,1))
rect1.setColor(color.hex("#AAFF00"))
app.Render.addObject(rect1)
while True:
    eventer.update()
    app.Render.clear()
    if eventer.isClose():
        break
    for key in eventer.getKeys():
        if key.key == "W":
            app.Render.setBgColor([255,255,255])
            app.Render.addObject(rect2)
        elif key.key == "B":
            app.Render.setBgColor([0,0,0])
            app.Render.removeObject(rect2)
    app.Render.update()