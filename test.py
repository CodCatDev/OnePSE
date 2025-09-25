import onepse
app = onepse.CreateWindow() # Creating window
app.show() # Show window
eventer = onepse.EventHandler()
color = onepse.Color()
app.Render.setBgColor([0,0,0])
rect1 = onepse.Objects.Rect(30,40)
rect1.setColor(color.hex("#AAFF00"))
app.Render.addObject(rect1)
speed = 5
while True:
    eventer.update()
    app.Render.clear()
    if eventer.isClose():
        break
    for key in eventer.getKeys():
        if key.key == "W":
            rect1.changePos(yto=-speed)
        if key.key == "S":
            rect1.changePos(yto=speed)
        if key.key == "A":
            rect1.changePos(xto=-speed)
        if key.key == "D":
            rect1.changePos(xto=speed)
    app.Render.update()