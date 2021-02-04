from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
while True:
    hits = mc.events.pollProjectileHits()
    if len(hits) > 0 :
        hit = hits[0]
        
        mc.player.setPos(x,y,z)
        #mc.setBlocks(x+1,y+1,z+1,x-1,y-1,z-1,46)
        #mc.setBlock(x,y+2,z,152)
        mc.createExplosion(x,y,z,1000)