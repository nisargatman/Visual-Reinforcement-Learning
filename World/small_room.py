import MalmoPython
import os
import sys
import time

def set_rewards(my_mission):
    pass
'''Reward function is defined in bands: the closest blocks to the door have a higher reward compared to blocks further away
            
            (0,5) (1,5) (2,5) (3,5) (4,5) (5,5)
            
            (0,4)  ****  ***    **    *    -
            
            (0,3)  ****  ***    **    *   (5,3)
            
            (0,2)  ****  ***    **   **   (5,2)
            
            (0,1)  ****  ***   ***   ***  (5,1)
            
            (0,0) (1,0) (2,0) (3,0) (4,0) (5,0)'''
    

def build_world(my_mission):
    for i in xrange(3): # Walls --> rectangle around points 0,0 0,5 5,0 and 5,5. Height = 3
        my_mission.drawLine(0,227+i,0,5,227+i,0,"cobblestone")
        my_mission.drawLine(0,227+i,0,0,227+i,5,"cobblestone")
        
        # door location is at 5,4
        if i == 2: # place for door
            my_mission.drawLine(5,227+i,0,5,227+i,5,"cobblestone")
        else:
            my_mission.drawLine(5,227+i,0,5,227+i,3,"cobblestone")
        my_mission.drawLine(0,227+i,5,5,227+i,5,"cobblestone")
    
    set_rewards(my_mission)

def main():
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately
    agent_host = MalmoPython.AgentHost()
    
    mission_file = './xmls/mission_xml3.xml'
    with open(mission_file, 'r') as f:
        print "Loading mission from %s" % mission_file
        mission_xml = f.read()
    
    my_mission = MalmoPython.MissionSpec(mission_xml,True)
    my_mission.forceWorldReset()
    length, breadth = 460, 380
    my_mission.requestVideo(length, breadth)
    my_mission_record = MalmoPython.MissionRecordSpec()
    
    build_world(my_mission)
    
    max_retries = 3
    for retry in range(max_retries):
        try:
            agent_host.startMission( my_mission, my_mission_record)
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

    while world_state.is_mission_running:
        # agent_host.sendCommand(cmds[n])
        time.sleep(0.5)
        world_state = agent_host.getWorldState()
        for frame in world_state.video_frames:
            print "Frame:",frame.width,'x',frame.height,':',frame.channels,'channels'
            #image = Image.frombytes('RGB', (frame.width, frame.height), str(frame.pixels) ) # to convert to a PIL image
    print "Mission has stopped."

if __name__ == '__main__':
    main()