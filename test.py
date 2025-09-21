import Onepse
app = Onepse.CreateWindow(title="Test App", size=[600,300]) # Creating window
app.show() # Show window
eventer = Onepse.EventHandler()
app.setBgColor([255,100,125])
while True:
    eventer.update()
    if eventer.isClose():
        break
    for key in eventer.getKeys():
        if key.key == "W":
            app.setBgColor([255,255,255])
        elif key.key == "B":
            app.setBgColor([0,0,0])
    app.updateRender()