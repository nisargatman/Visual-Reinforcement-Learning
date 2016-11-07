import MalmoPython
import os
import sys
import time
import random

config = {
    'length':50,
    'breadth':50,
    'height':20,
    'ceiling':"yes",
    'num_torches':5,
    'torch_pos':(1,2,3,4,5),
    'num_chairs':1,
    'chair_pos':(1),
    'height_bookcase':10,
    'bookcase_pos':8,
    'num_lamps':1,
    'lamp_pos':(2),
    'nun_sofas':1,
    'sofa_pos':(2),
    'num_tables':1,
    'table_pos':(1),
    'cakes':"yes",
    'cake_pos':(1)

} # dictionary that contains configuraiton for setting up world

def build_world(my_mission):
    pass

def main():
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately
    agent_host = MalmoPython.AgentHost()

    mission_file = './xmls/mission_xml.xml'
    with open(mission_file, 'r') as f:
        print "Loading mission from %s" % mission_file
        mission_xml = f.read()
    my_mission = MalmoPython.MissionSpec(mission_xml,True)

    build_world(my_mission)

    my_mission.requestVideo( 640, 480 )

    my_mission_record = MalmoPython.MissionRecordSpec()

    max_retries = 3
    for retry in range(max_retries):
        try:
            agent_host.startMission( my_mission, my_mission_record )
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

    # main loop:
    while world_state.is_mission_running:
        agent_host.sendCommand( "move 1" )
        agent_host.sendCommand( "turn " + str(random.random()*2-1) )
        agent_host.sendCommand("move 1")
        time.sleep(0.5)
        world_state = agent_host.getWorldState()
        print "video,observations,rewards received:",world_state.number_of_video_frames_since_last_state,world_state.number_of_observations_since_last_state,world_state.number_of_rewards_since_last_state
        for reward in world_state.rewards:
            print "Summed reward:",reward.getValue()
        for error in world_state.errors:
            print "Error:",error.text
        for frame in world_state.video_frames:
            print "Frame:",frame.width,'x',frame.height,':',frame.channels,'channels'
            print type(frame.pixels)
            #image = Image.frombytes('RGB', (frame.width, frame.height), str(frame.pixels) ) # to convert to a PIL image
    print "Mission has stopped."

if __name__ == "__main__":
    main()