from pynput.keyboard import Key, Listener
a=[]
pressedkeys=[]
def on_release(key):
    a.append(str(key))
    #print str("{} released".format(key))
    
    if key==Key.ctrl_l:
        for i in a:
            #print i[0]
            if "u'" in i and i[0]=="u":
                keypressed = i.split("u'")[1]
                keypressed = keypressed.split("'")[0]
                
                pressedkeys.append(keypressed)
            elif "Key.space" in i:
                pressedkeys.append(" ")

            elif "Key.tab" in i:
                pressedkeys.append("    ")
                

        string = "".join(pressedkeys)
        print ("----"*10)
        print (string)
        print ("a9aaaaaaaaaaaa")
        # I print aaaaa here


with Listener(on_release=on_release) as listener:
    listener.join()

