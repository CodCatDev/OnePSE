import Onepse
#import time
App = Onepse.CreateWindow()
App.show()
run = True
Eventer = Onepse.EventHandler()
while run:
    Eventer.update()
    #time.sleep(1)
    if Eventer.isClose():
        run = False
        break
    keys = Eventer.getKeys()
    if keys:
        print(keys[0].key)