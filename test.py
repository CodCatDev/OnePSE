import Onepse
app = Onepse.CreateWindow(title="Test App", size=[600,300]) # Creating window
app.show() # Show window
eventer = Onepse.EventHandler()
app.setBgColor([255,100,125])
while True:
    eventer.update()
    if eventer.isClose():
        break
    app.updateRender()