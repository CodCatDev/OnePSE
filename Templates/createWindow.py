import Onepse
app = Onepse.CreateWindow(title="Template #1", size=[600,300]) # Create a window class
app.show() # Show the window
eventer = Onepse.EventHandler() # Get EventHandler
while True:
    eventer.update() # update events data
    if eventer.isClose(): # check is app close
        break