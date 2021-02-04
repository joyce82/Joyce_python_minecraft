from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
import time
import random
mc = mcs.create()
while True:
    x,y,z = mc.player.getPos()
    time.sleep(1)
    x = x+random.uniform(1,10)
    y = y+random.uniform(1,10)
    z = z+random.uniform(1,10)
    mc.spawnEntity(x+1,y,z,93)