from mcpi.minecraft import Minecraft as mcs
import time
mc = mcs.create()
t = 0
import time
    time.sleep(0.5)
    mc.postToChat("t ="+str(t))
    t = t+1