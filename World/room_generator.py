import MalmoPython
import os
import sys
import time

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

}

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately

agent_host = MalmoPython.agent_host()
mission_xml = ""
my_mission = MalmoPython.MissionSpec(missionXML, True)
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

print "Waiting for the mission to start ",
world_state = agent_host.getWorldState()
while not world_state.has_mission_begun:
    sys.stdout.write(".")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print "Error:",error.text

print
print "Mission running "

