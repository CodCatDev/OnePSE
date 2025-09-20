import Onepse
app = Onepse.CreateWindow(title="Key print in console", size=[600,300]) # Create a window
app.show()
eventer = Onepse.EventHandler() # Create a EventHandler object
while True: # App while
    eventer.update() # update data of keys or events
    if eventer.isClose():
        break # stop app when its closed
    keys = eventer.getKeys() # get all pressed keys
    for key in keys: # get all keys
        print(key.key) # Print a key