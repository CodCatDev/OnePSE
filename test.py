import onepse
app = onepse.CreateWindow() # Creating window
app.show() # Show window
eventer = onepse.EventHandler()
color = onepse.Color()
app.Render.setBgColor(color.rgb(100,255,100))
rect1 = onepse.Objects.Rect(30,40)
rect1.setColor(color.hex("#0000FF"))
app.Render.addObject(rect1)
speed = 5
while True:
    eventer.updateEvents()
    app.Render.clear()
    if eventer.isClose():
        break
    keys = eventer.updateKeys()
    if keys.key("W"):
        rect1.changePos(0, -speed)
    if keys.key("S"):
        rect1.changePos(0, speed)
    if keys.key("A"):
        rect1.changePos(-speed, 0)
    if keys.key("D"):
        rect1.changePos(speed, 0)
    app.Render.update()