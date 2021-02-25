import time
import random
import sys
sys.path.append('../')

from Common_Libraries.p3b_lib import *

import os
from Common_Libraries.repeating_timer_lib import repeating_timer

def update_sim():
    try:
        my_table.ping()
    except Exception as error_update_sim:
        print (error_update_sim)

### Constants
speed = 0.2 #Qbot's speed

### Initialize the QuanserSim Environment
my_table = servo_table()
arm = qarm()
arm.home()
bot = qbot(speed)

def disp_cont():


    #asks user which container they would want to dispense
    print("\nFor a random container, input 0\nFor a clean plastic container input 1")
    print("For a clean metal container input 2\nFor a clean paper container input 3")
    print("For a dirty plastic container input 4\nFor a dirty metal container input 5")
    print("For a dirty paper container input 6\n")
    num =int(input("Dispense container : "))

    
    if num == 0:
        
        #dispenses a container randomly
        bottle = random.randrange(1,6)
        x = my_table.container_properties(bottle)
        my_table.dispense_container()

        #collects container properties(bin location, weight in grams, and its material)
        location= x[2]
        weight = x[1]
        material = x[0]
        properties = [location, weight, material]

        return properties
    
    else:

        #dispenses a container of their choice
        bottle = num
        x = my_table.container_properties(bottle)
        my_table.dispense_container()

        location= x[2]
        weight = x[1]
        material = x[0]
        properties = [location, weight, material]

        return properties


def move_arm(counter):

    #coordinates to pick up container
    grab_cont = [0.6915, 0.0, 0.2604] 

    #coordinate after grabing the container
    position_1 = [0.5022, 0.0, 0.2461] 
    position_2 = [0.3819, -0.0, 0.6216]
    position_4 = [0.0, -0.3005, 0.5757]

    #coordinates to drop off containers onto the qbot
    dropoff_1 = [0.0, -0.5264, 0.4257]
    dropoff_2 = [0.0, -0.4374, 0.4812]
    dropoff_3 = [0.0, -0.3447, 0.4772]

    #extra coordinate for 3rd container so it does not intefere with other containers
    position_5 = [0.0, -0.3447, 0.4772]

    #gathers the drop off coordinates
    dropoff_hopper = [dropoff_1,dropoff_2,dropoff_3]

    #counts the amount the amount of time the container has been dispensed
    location = dropoff_hopper[counter]


    #calls arm to move to its respected coordinates
    arm.home()
    arm.move_arm(grab_cont[0],grab_cont[1],grab_cont[2])
    arm.control_gripper(45)
    arm.move_arm(position_1[0],position_1[1],position_1[2])
    arm.move_arm(position_2[0],position_2[1],position_2[2])
    arm.move_arm(position_5[0],position_5[1],position_5[2])


    arm.move_arm(location[0],location[1],location[2])
    arm.control_gripper(-45)
    arm.move_arm(position_4[0],position_4[1],position_4[2])
    
    

def load_cont(counter,location_1, weight_1, material_1):
#this function is to load the containers onto the hopper

    #using the while loop continously dispenses and loads hopper until counter reaches a certain amount
    #this set of the while function is to drop the first container onto a certain part of the hopper
    while counter < 1:
        properties = disp_cont()
        location_1 = properties[0]
        weight_1 = properties[1]
        material_1 = properties[2]

        move_arm(counter)

        #this is to let the user know the first container's properties                       
        if location_1 == "Bin01":
            
            print("")
            print("Container is",material_1,"that weighs",weight_1,
                "and will be transported to",location_1)
            print("")
            
        elif location_1 == "Bin02":

            print("")
            print("Container is",material_1,"that weighs",weight_1,
                "and will be transported to",location_1)
            print("")
            
        elif location_1 == "Bin03":

            print("")
            print("Container is",material_1,"that weighs",weight_1,
                "and will be transported to",location_1)
            print("")
            
        elif location_1 == "Bin04":

            print("")
            print("Container is",material_1,"that weighs",weight_1,
                "and will be transported to",location_1)
            print("")

        #stops the loop   
        counter += 1

    #this drops off the second container to its given location onto the hopper   
    while counter >= 1:
        properties2 = disp_cont()
        location_2 = properties2[0]
        weight_2 = properties2[1]
        material_2 = properties2[2]

        #lets user know the next container's properties
        if location_2 == "Bin01":
            
            print("Container is",material_2,"that weighs",weight_2,
                "and will be transported to",location_2)
            print("")
            
        elif location_2 == "Bin02":
            
            print("Container is",material_2,"that weighs",weight_2,
                "and will be transported to",location_2)
            print("")
            
        elif location_2 == "Bin03":
            
            print("Container is",material_2,"that weighs",weight_2,
                "and will be transported to",location_2)
            print("")
            
        elif location_2 == "Bin04":
            
            print("Container is",material_2,"that weighs",weight_2,
                "and will be transported to",location_2)
            print("")
            

        #arm will transfer container onto hopper if it meets these restrictions, otherwise, will transfer once qbot is back from unloading 
        if (counter < 3) and (location_1 == location_2) and (weight_1 + weight_2 < 90):    

            move_arm(counter)
            
            weight_1 += weight_2

            print("Total mass in box:", weight_1, "g \n")
            print("")

            #stops the loop
            counter += 1

        #this informs user that it has not met the requirements in order to be transferred 
        else:
            print("This hopper has exceeded the amount of weight capacity of 90g or\nhas 3 containers on the hopper or\nhas a different bin location as the loaded container/s\n")      
            print("")
            
            location = [location_1, location_2]

            return location, weight_2



def transfer_cont(bin_location):
#this fumction will tell where to dump the loaded container/s

    bot.activate_ultrasonic_sensor()
    bot.activate_actuator()

    #next set of if statements specifies the location to dump the containers
    if bin_location == "Bin01":

        #this while loop follows the yellow line to precisely get it to it destination
        lost_line  = 0
        while lost_line < 2:
           lost_line, velocity = bot.follow_line(0.4)
           bot.forward_velocity(velocity)

            #species which bin the qbot should approach
           data = bot.read_ultrasonic_sensor("Bin01")

            #once sensor reads the distance and if the bin is near to its readings
           if data <= 0.1: #qbot will stop once the qbot is less than or equal to 0.1m in distance
               bot.stop()

               print("The Q bot has reached ",data,"m and will now dump the container/s")
               print("")
                
               #breaks the loop
               break
            
    elif bin_location == "Bin02":
        
        lost_line  = 0
        while lost_line < 2:
           lost_line, velocity = bot.follow_line(0.4)
           bot.forward_velocity(velocity)
            
           data = bot.read_ultrasonic_sensor("Bin02")

           if data <= 0.1:
               bot.stop()

               print("The Q bot has reached ",data,"m and will now dump the container/s")
               print("")                

               break
            
    elif bin_location == "Bin03":
        
        lost_line  = 0
        while lost_line < 2:
           lost_line, velocity = bot.follow_line(0.4)
           bot.forward_velocity(velocity)
           
           data = bot.read_ultrasonic_sensor("Bin03")

           if data <= 0.1:
               bot.stop()

               print("The Q bot has reached ",data,"m and will now dump the container/s")
               print("")

               break
            
    elif bin_location == "Bin04":
        
        lost_line  = 0
        while lost_line < 2:
           lost_line, velocity = bot.follow_line(0.4)
           bot.forward_velocity(velocity)
            
           data = bot.read_ultrasonic_sensor("Bin04")

           if data <= 0.1:
               bot.stop()

               print("The Q bot has reached ",data,"m and will now dump the container/s")
               print("")

               break
            
           

def dump_cont():
#this function will just simply rotate and dump the container onto its respected bin

    #deactivates sensor
    bot.deactivate_ultrasonic_sensor()

    #rotates to bin
    bot.rotate(94)
    bot.forward_time(0.5)
    bot.rotate(-94)

    #activates actuator to dump the container
    bot.activate_actuator()

    #Q bot dumps container 
    bot.dump()
    time.sleep(1)

    #deactivates actuator
    bot.deactivate_actuator()

    #returns back to yellow line
    bot.rotate(-94)
    bot.forward_time(0.5)
    bot.rotate(94)
    
   
def home_position():
#function will follow yellow line until Q bot is back to its initial position
    
    lost_line  = 0
    while lost_line < 2:
       lost_line, velocity = bot.follow_line(0.5)
       bot.forward_velocity(velocity)

    #Q bot and Q arm will rotate to its initial position  
    bot.rotate(196)  
    arm.home()
    

def main():
    
    #declares each variable
    counter = 0
    weight_1 = 0
    location_1 = 0
    location_2 = 0
    material_1 = 0

    i=0
    while i<1:

        location, total_mass = load_cont(counter, location_1, weight_1, material_1)

        #tells qbot where to transfer the first container/s
        transfer_cont(location[0])

        dump_cont()
        home_position()

        #tells qbot where to transfer the next container/s
        location_1 = location[1]
        #print(location[1])
        weight_1 = total_mass

        move_arm(0)

        
        counter = 1
        
main()

update_thread = repeating_timer(2,update_sim)
