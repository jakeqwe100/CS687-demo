import glob
import os
import sys
import time
import random
import time
import numpy as np
import cv2	
try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass
 
import carla
 
actor_list =  []
try:
	#create client
	client = carla.Client('localhost', 2000)
	client.set_timeout(2.0)
	#world connection
	world = client.get_world() 
	#get blueprint libarary
	blueprint_library = world.get_blueprint_library()
	#Choose a vehicle blueprint which name is model3 and select the first one
	bp = blueprint_library.filter("model3")[0]
	print(bp)
	#Returns a list of recommended spawning points and random choice one from it
	spawn_point = random.choice(world.get_map().get_spawn_points())
	#spawn vehicle to the world by spawn_actor method
	vehicle = world.spawn_actor(bp,spawn_point)
	#control the vehicle
	vehicle.set_autopilot(enabled=True)
	# vehicle.apply_control(carla.VehicleControl(throttle=0.1,steer=0.0))
	#add vehicle to the actor list
	actor_list.append(vehicle)
	time.sleep(25)
finally:
	for actor in actor_list:
		actor.destroy()
	print("All cleaned up!")