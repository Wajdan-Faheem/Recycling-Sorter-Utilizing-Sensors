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

def user():
    
    global  num1,num2,num3
    #dispenses a bottle within the range 1-6
    print("For a random container, input 0\nFor a clean plastic container input 1")
    print("For a clean metal container input 2\nFor a clean paper container input 3")
    print("For a dirty plastic container input 4\nFor a dirty metal container input 5")
    print("For a dirty paper container input 6")
    num1 =int(input("Dispense container 1: "))
    num2 =int(input("Dispense container 2: "))
    num3 =int(input("Dispense container 3: "))

def random


##---------------------------------------------------------------------------------------
def location_1():
#def disp_cont1():
    global location_1,weight_1,material_1,bottle_1

    if num1 == 0:
    
        
        bottle_1 = random.randrange(1,6)
        x = my_table.container_properties(bottle_1)
        #my_table.dispense_container()
        print(bottle_1)
        location_1= x[2]
        weight_1 = x[1]
        material_1 = x[0]

    else:
        bottle_1 = num1
        x = my_table.container_properties(bottle_1)
        #my_table.dispense_container()
        location_1= x[2]
        weight_1 = x[1]
        material_1 = x[0]
    print("Container 1 is",material_1,"that weighs",weight_1,
          "and will be transported to",location_1)




def disp_cont1():


    if num1 == 0:
    
        my_table.dispense_container()


    else:

        my_table.dispense_container()


def load_cont1():
    
    #time.sleep(1)
    arm.move_arm(0.6915, 0.0, 0.2604)
    arm.control_gripper(45)

    #time.sleep(1)
    arm.move_arm(0.5022, 0.0, 0.2461)
    arm.move_arm(0.3819, -0.0, 0.6216)
    arm.rotate_base(-90)
  
    #time.sleep(1)
    arm.move_arm(0.0, -0.5264, 0.4257)
    arm.control_gripper(-45)
    arm.move_arm(-0.0, -0.0359, 0.6658)

    




##---------------------------------------------------------------------------------------

def location_2():

#def disp_cont2():

    global location_2,material_2,weight_2,bottle_2

    if num2 == 0:

        
        bottle_2 = random.randrange(1,6)
        x2 = my_table.container_properties(bottle_2)
        print(bottle_2)
        #my_table.dispense_container()
        location_2= x2[2]
        weight_2 = x2[1]
        material_2 = x2[0]

    else:
        bottle_2 = num2
        x2 = my_table.container_properties(bottle_2)
        #my_table.dispense_container()
        location_2= x2[2]
        weight_2 = x2[1]
        material_2 = x2[0]

    
    print("Container 2 is",material_2,"that weighs",weight_2,
            "and will be transported to",location_2)


def disp_cont2():
    
    
    if num2 == 0:

        my_table.dispense_container()
        

    else:

        my_table.dispense_container()


def load_cont2():
    
    arm.home()
    time.sleep(1)
    arm.move_arm(0.6915, 0.0, 0.2604)
    arm.control_gripper(45)

    time.sleep(1)
    arm.move_arm(0.5022, 0.0, 0.2461)
    arm.move_arm(0.3819, -0.0, 0.6216)
    arm.rotate_base(-90)
      
    time.sleep(1)
    #arm.move_arm(0.0, -0.4002, 0.412)
    arm.move_arm(0.0, -0.4374, 0.4812)
    arm.control_gripper(-45)
    arm.move_arm(-0.0, -0.0359, 0.6658)
    


##---------------------------------------------------------------------------------------
def location_3():

#def disp_cont3():

    global location_3,weight_3,material_3,bottle_3
    
    if num3 == 0:
        
        bottle_3 = random.randrange(1,6)
        x3 = my_table.container_properties(bottle_3)

        #my_table.dispense_container()
        location_3= x3[2]
        weight_3 = x3[1]
        material_3 = x3[0]
     

    else:
        bottle_3 = num3
        x3 = my_table.container_properties(bottle_3)

        #my_table.dispense_container()
        location_3 = x3[2]
        weight_3 = x3[1]
        material_3 = x3[0]
        
    print("Container 3 is",material_3,"that weighs",weight_3,
        "and will be transported to",location_3)

    
def disp_cont3():


    if num3 == 0:
        
        my_table.dispense_container()


    else:

        my_table.dispense_container()


    
def load_cont3():
    
    arm.home()
    time.sleep(1)
    arm.move_arm(0.6915, 0.0, 0.2604)
    arm.control_gripper(45)

    time.sleep(1)
    arm.move_arm(0.5022, 0.0, 0.2461)
    arm.move_arm(0.3819, -0.0, 0.6216)
    arm.rotate_base(-90)
    arm.move_arm(0.0, -0.3005, 0.5757)
          
    time.sleep(1)
    #arm.move_arm(0.0, -0.3739, 0.4458)
    arm.move_arm(0.0, -0.3447, 0.4772)
    arm.control_gripper(-45)
    arm.move_arm(-0.0, -0.0359, 0.6658)

def disp_cont(cont):

    
        





##---------------------------------------------------------------------------------------      


def transfer_cont():
    bot.activate_ultrasonic_sensor()
    bot.activate_actuator()
    print(location_1)
    
    lost_line  = 0
    while lost_line < 2:
       lost_line, velocity = bot.follow_line(0.5)
       bot.forward_velocity(velocity)
       data = bot.read_ultrasonic_sensor(location_1)

       if data <= 0.1:
           bot.stop()

           print(data)

           ##bot.forward_time(0.5)
           

           break
       
    return


def transfer_cont2():
    bot.activate_ultrasonic_sensor()
    bot.activate_actuator()
    print(location_2)
    
    lost_line  = 0
    while lost_line < 2:
       lost_line, velocity = bot.follow_line(0.5)
       bot.forward_velocity(velocity)
       data = bot.read_ultrasonic_sensor(location_2)

       if data <= 0.1:
           bot.stop()

           print(data)

           ##bot.forward_time(0.5)
           

           break

def transfer_cont3():
    bot.activate_ultrasonic_sensor()
    bot.activate_actuator()
    print(location_3)
    
    lost_line  = 0
    while lost_line < 2:
       lost_line, velocity = bot.follow_line(0.5)
       bot.forward_velocity(velocity)
       data = bot.read_ultrasonic_sensor(location_3)

       if data <= 0.1:
           bot.stop()

           print(data)

           ##bot.forward_time(0.5)
           

           break


 ##--------------------------------------------------------------------------------------- 


def dump_cont():
    
    bot.deactivate_ultrasonic_sensor()
    bot.rotate(94)
    bot.forward_time(0.5)
    bot.rotate(-94)

    
    bot.activate_actuator()

    
    bot.dump()
    #time.sleep(1)
    bot.deactivate_actuator()
    
    bot.rotate(-94)
    bot.forward_time(0.5)
    bot.rotate(94)

    

def home_position():
    lost_line  = 0
    while lost_line < 2:
       lost_line, velocity = bot.follow_line(0.5)
       bot.forward_velocity(velocity)
    bot.rotate(195)  
    arm.home()
    return



 ##--------------------------------------------------------------------------------------- 
'''
def location():
    user()
    location_1()
    location_2()
    location_3()
location()
'''

def main():
    global location_1

    i=0

    while i<1:

        user()
        
        location_1()
        disp_cont1()
        load_cont1()
        
        location_2()
        #location_3()

        if location_2 == location_1: #and location_3 == location_2:

            disp_cont2()
            load_cont2()
            location_3()

            if location_2 == location_3:
                
                disp_cont3()
                load_cont3()
                
                
            else:
                print()


            transfer_cont()
            dump_cont()
            home_position()

            

        elif location_3 != location_2 and location_2 == location_1:
            
            disp_cont2()
            load_cont2()

            transfer_cont()
            dump_cont()
            home_position()
            
        else:

            transfer_cont()
            dump_cont()
            home_position()

            if location_1 != location_2:
                
                disp_cont2()
                load_cont2()

                if location_2 == location_3:
                    disp_cont3()
                    load_cont3()
                    
                else:
                    print()
                

                transfer_cont2()
                dump_cont()
                home_position()
                
            else:
                print()

main()



##---------------------------------------------------------------------------------------
## STUDENT CODE ENDS
##---------------------------------------------------------------------------------------
update_thread = repeating_timer(2,update_sim)

'''      

            if location_3 != location_2:

                disp_cont3()
                load_cont3()
                        
            else:
                    print()

                    
            transfer_cont3()
            dump_cont()
            home_position()
                        
                
            else:

               print()
'''
'''
        if location_3 == location_2:
            disp_cont3()
            load_cont3()

            transfer_cont()
            dump_cont()
            home_position()
            
        else:
            transfer_cont()
            dump_cont()
            home_position()
'''

'''
        if location != location_2:
            #transfer_cont2()
            #dump_cont()
            #home_position()
            print()
        else:
            transfer_cont2()
            dump_cont()
            home_position()
'''            
            
        #dump_cont()
        #home_position()
