import MalmoPython
import os
import sys
import time
import random
from PIL import Image

config = {
    'length':20,
    'breadth':20,
    'height':5,
    'ceiling':"no",
    'num_torches':7,
    'torch_pos':((1,0,10),(1,0,19),(1,0,1),(10,0,1),(10,0,19),(19,0,1),(19,0,10)),
    'num_windows':6,
    'window_pos':((0,0,10),(0,0,19),(10,0,0),(10,0,20),(19,0,0),(20,0,10)),
    'height_bookcase':3,
    'bookcase_pos':2,
    'fire':"yes",
    'fire_pos':"wall"

} # dictionary that contains configuraiton for setting up world

def build_world(my_mission):
    start_x = 0
    start_y = 227
    start_z = 0
    for i in range(config['height']):
        my_mission.drawLine(start_x, start_y+i, start_z, start_x+config['length'], start_y+i, start_z, "cobblestone")
        my_mission.drawLine(start_x, start_y+i, start_z, start_x, start_y+i, start_z+config['breadth'], "cobblestone")
        if i>1:
            my_mission.drawLine(start_x+config['length'], start_y+i, start_z, start_x+config['length'], start_y+i, start_z+config['breadth'],"cobblestone")
        else:
            my_mission.drawLine(start_x+config['length'], start_y+i, start_z, start_x+config['length'], start_y+i, start_z+config['breadth']-2,"cobblestone")
        my_mission.drawLine(start_x, start_y+i, start_z+config['breadth'], start_x+config['length'], start_y+i, start_z+config['breadth'], "cobblestone")
    if config['ceiling'] == "yes":
        for i in range(config['length']):
            my_mission.drawLine(start_x+i, start_y+config['height'], start_z, start_x+i, start_y+config['height'], start_z+config['breadth'], "cobblestone")
    torches = config['torch_pos']
    for i in range(config['num_torches']):    
        rand = torches[i]
        tx = rand[0]
        ty = rand[1]
        tz = rand[2]
        my_mission.drawBlock(tx,ty+start_y,tz,"torch")
    windows = config['window_pos']
    for i in range(config['num_windows']):    
        rand = windows[i]
        tx = rand[0]
        ty = rand[1]
        tz = rand[2]
        my_mission.drawBlock(tx,ty+start_y+2,tz,"glass")
    for i in range(config['height_bookcase']):
        my_mission.drawLine(config['bookcase_pos'],start_y+i,1,config['bookcase_pos']+7,start_y+i,1,'bookshelf')
    my_mission.drawBlock(config['length'],start_y,config['breadth']-1,'cobblestone') # change to birch_door
    for i in range(config['length']/2):
        my_mission.drawLine(config['length']/4+i,start_y,config['length']/4,config['length']/4+i,start_y,config['length']*3/4,'carpet')
    my_mission.drawLine(14,start_y,8,14,start_y,13,"iron_block")
    my_mission.drawLine(14,start_y+1,8,14,start_y+1,13,"double_stone_slab")
    for i in range(5):
        my_mission.drawLine(13-i,start_y,8,13-i,start_y,13,"wool")
    my_mission.drawLine(config['length']*3/4,start_y,config['length']/4,config['length']*3/4,start_y,config['breadth']*3/4,'birch_stairs')
    if config['fire'] == "yes":
        my_mission.drawBlock(config['length']/2,start_y,config['breadth']-1,'fire')
        my_mission.drawBlock(config['length']/2,start_y+1,config['breadth']-1,'brick_block')
        my_mission.drawBlock(config['length']/2-1,start_y,config['breadth']-1,'brick_block')
        my_mission.drawBlock(config['length']/2-2,start_y,config['breadth']-1,'red_flower')
        my_mission.drawBlock(config['length']/2+1,start_y,config['breadth']-1,'brick_block')
        my_mission.drawBlock(config['length']/2+2,start_y,config['breadth']-1,'red_flower')
    my_mission.drawBlock(1,start_y,config['breadth']/2,'double_wooden_slab')
    my_mission.drawBlock(1,start_y,config['breadth']/2-1,'double_wooden_slab')
    my_mission.drawBlock(1,start_y,config['breadth']/2-2,'double_wooden_slab')
    my_mission.drawBlock(1,start_y,config['breadth']/2-3,'bookshelf')
    my_mission.drawBlock(1,start_y,config['breadth']/2+1,'double_wooden_slab')
    my_mission.drawBlock(1,start_y,config['breadth']/2+2,'double_wooden_slab')
    my_mission.drawBlock(1,start_y,config['breadth']/2+3,'bookshelf')
    my_mission.drawBlock(1,start_y+1,config['breadth']/2,'wooden_slab')
    my_mission.drawBlock(1,start_y+1,config['breadth']/2-1,'wooden_slab')
    my_mission.drawBlock(1,start_y+1,config['breadth']/2-2,'wooden_slab')
    my_mission.drawBlock(1,start_y+1,config['breadth']/2+1,'wooden_slab')
    my_mission.drawBlock(1,start_y+1,config['breadth']/2+2,'wooden_slab')
    my_mission.drawBlock(1,start_y+1,config['breadth']/2,'iron_block')
    my_mission.drawLine(12,start_y,2,16,start_y,2,'nether_brick_fence')
    my_mission.drawLine(12,start_y,3,16,start_y,3,'nether_brick_fence')
    my_mission.drawLine(12,start_y+1,2,16,start_y+1,2,'wooden_pressure_plate')
    my_mission.drawLine(12,start_y+1,3,16,start_y+1,3,'wooden_pressure_plate')
    my_mission.drawBlock(config['length']/4,start_y,config['length']/4,"oak_stairs")
    for i in range(4):
        my_mission.drawLine(3,start_y+i,19,5,start_y+i,19,'noteblock')
    my_mission.drawBlock(config['length']-1,start_y,config['breadth']/2,"chest")
    my_mission.drawBlock(3,start_y,config['breadth']/2,"stonebrick")


def main():
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately
    agent_host = MalmoPython.AgentHost()

    mission_file = './xmls/mission_xml2.xml'
    with open(mission_file, 'r') as f:
        print "Loading mission from %s" % mission_file
        mission_xml = f.read()
    my_mission = MalmoPython.MissionSpec(mission_xml,True)
    my_mission.forceWorldReset()
    build_world(my_mission)

    length = 640
    breadth = 480
    my_mission.requestVideo(length, breadth)
    my_mission_record = MalmoPython.MissionRecordSpec()
    client_pool = MalmoPython.ClientPool()
    client_pool.add( MalmoPython.ClientInfo( "127.0.0.1", 10001 ) )

    max_retries = 3
    for retry in range(max_retries):
        try:
            agent_host.startMission( my_mission, client_pool, my_mission_record, 0, "" )
            break
        except RuntimeError as e:
            if retry == max_retries - 1:
                print "Error starting mission:",e
                exit(1)
            else:
                time.sleep(2)

    print "Waiting for the mission to start",
    world_state = agent_host.getWorldState()
    while not world_state.has_mission_begun:
        sys.stdout.write(".")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print "Error:",error.text
    print

    with open('commands_write.txt','r') as f:
        cmds = f.readlines()
    
    print len(cmds)
    raw_input()
        
    # main loop:
    n = 0
    while world_state.is_mission_running:
        agent_host.sendCommand(cmds[n])
        time.sleep(0.5)
        world_state = agent_host.getWorldState()
        for frame in world_state.video_frames:
            print "Frame:",frame.width,'x',frame.height,':',frame.channels,'channels'
            image = Image.frombytes('RGB', (frame.width, frame.height), str(frame.pixels) ) # to convert to a PIL image
            os.chdir("../SegNet/Images_label")
            image.save('Label%d.jpeg'%(n+9852))
            os.chdir("../../World")
            n = n+1
    print "Mission has stopped."

if __name__ == "__main__":
    main()