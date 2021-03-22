#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import copy
import imutils

start_x = int(input("Enter starting x-coordinate (between 6 and 394): "))       #user inputs the starting and finishing coordinates
start_y = int(input("Enter starting y-coordinate (between 6 and 294): "))
goal_x = int(input("Enter finishing x-coordinate (between 6 and 394): "))
goal_y = int(input("Enter finishing y-coordinate (between 6 and 294): "))
print()

image = np.ones((401,301,1),np.uint8)*255       #creates blank image

if start_x// 10 < 1:        #lists location as a string with 6 integers (x and y coords) (000000 to 403300)
    stringx = '00'
elif start_x // 10 < 10:
    stringx = '0'
else:
    stringx = ''     
if start_y // 10 < 1:
    stringy = '00'
elif start_y // 10 < 10:
    stringy = '0'
else:
    stringy = '' 

location = str(stringx+str(start_x)+stringy+str(start_y))

new_loc = copy.deepcopy(location)

def check_inputs(start_x,start_y,goal_x,goal_y):        #checks that the inputs are valid
    i = 0
    if start_x >= 403 or start_x <= 0:
        print('Starting x-coord outside range.')
        i = 1
        return i
    else:
        pass
    if start_y >= 300 or start_y <= 0:
        print('Starting y-coord outside range.')
        i = 1
        return i
    else:
        pass
    if goal_x >= 403 or goal_y <= 0:
        print('Goal x-coord outside range.')
        i = 1
        return i
    else:
        pass
    if goal_y >= 300 or goal_y <= 0:
        print('Goal y-coord outside range.')
        i = 1
        return i
    else:
        pass

def moveUp(x,y,cost,p):     #move up function returns the coordinates and path taken to get to coordinates above the current parent coordinate
    p = p + 'A'
    y += 1
    cost += 1
    if x // 10 < 1:
        stringx = '00'
    elif x // 10 < 10:
        stringx = '0'
    else:
        stringx = ''     
    if y // 10 < 1:
        stringy = '00'
    elif y // 10 < 10:
        stringy = '0'
    else:
        stringy = '' 
    location = str(stringx+str(int(x))+stringy+str(int(y)))
    return x,y,location,cost,p

def moveRight(x,y,cost,p):      #next few functions are same as moveUp but for each of the 8 directions
    p = p + 'C'
    x += 1
    cost += 1
    if x // 10 < 1:
        stringx = '00'
    elif x // 10 < 10:
        stringx = '0'
    else:
        stringx = ''      
    if y // 10 < 1:
        stringy = '00'
    elif y // 10 < 10:
        stringy = '0'
    else:
        stringy = '' 
    location = str(stringx+str(int(x))+stringy+str(int(y)))
    return x,y,location,cost,p

def moveDown(x,y,cost,p):
    p = p + 'E'
    y -= 1
    cost += 1
    if x // 10 < 1:
        stringx = '00'
    elif x // 10 < 10:
        stringx = '0'
    else:
        stringx = ''     
    if y // 10 < 1:
        stringy = '00'
    elif y // 10 < 10:
        stringy = '0'
    else:
        stringy = '' 
    location = str(stringx+str(int(x))+stringy+str(int(y)))
    return x,y,location,cost,p

def moveLeft(x,y,cost,p):
    p = p + 'G'
    x -= 1
    cost += 1
    if x // 10 < 1:
        stringx = '00'
    elif x // 10 < 10:
        stringx = '0'
    else:
        stringx = ''     
    if y // 10 < 1:
        stringy = '00'
    elif y // 10 < 10:
        stringy = '0'
    else:
        stringy = '' 
    location = str(stringx+str(int(x))+stringy+str(int(y)))
    return x,y,location,cost,p

def moveUpRight(x,y,cost,p):
    p = p + 'B'
    y += 1
    x += 1
    cost += np.sqrt(2)
    if x // 10 < 1:
        stringx = '00'
    elif x // 10 < 10:
        stringx = '0'
    else:
        stringx = ''    
    if y // 10 < 1:
        stringy = '00'
    elif y // 10 < 10:
        stringy = '0'
    else:
        stringy = '' 
    location = str(stringx+str(int(x))+stringy+str(int(y)))
    return x,y,location,cost,p

def moveDownRight(x,y,cost,p):
    p = p + 'D'
    y -= 1
    x += 1
    cost += np.sqrt(2)
    if x // 10 < 1:
        stringx = '00'
    elif x // 10 < 10:
        stringx = '0'
    else:
        stringx = ''    
    if y // 10 < 1:
        stringy = '00'
    elif y // 10 < 10:
        stringy = '0'
    else:
        stringy = '' 
    location = str(stringx+str(int(x))+stringy+str(int(y)))
    return x,y,location,cost,p

def moveDownLeft(x,y,cost,p):
    p = p + 'F'
    y -= 1
    x -= 1
    cost += np.sqrt(2)
    if x // 10 < 1:
        stringx = '00'
    elif x // 10 < 10:
        stringx = '0'
    else:
        stringx = ''     
    if y // 10 < 1:
        stringy = '00'
    elif y // 10 < 10:
        stringy = '0'
    else:
        stringy = '' 
    location = str(stringx+str(int(x))+stringy+str(int(y)))
    return x,y,location,cost,p

def moveUpLeft(x,y,cost,p):
    p = p + 'H'
    y += 1
    x -= 1
    cost += np.sqrt(2)
    if x // 10 < 1:
        stringx = '00'
    elif x // 10 < 10:
        stringx = '0'
    else:
        stringx = ''     
    if y // 10 < 1:
        stringy = '00'
    elif y // 10 < 10:
        stringy = '0'
    else:
        stringy = '' 
    location = str(stringx+str(int(x))+stringy+str(int(y)))
    return x,y,location,cost,p

def moveAround(x,y,cost,p):         #combines all the movement actions to easily find relevant values are parent coordinates
    x_up, y_up, loc_up, cost_up, p_up = moveUp(x,y,cost,p)
    x_down, y_down, loc_down, cost_down, p_down = moveDown(x,y,cost,p)
    x_right, y_right, loc_right, cost_right, p_right = moveRight(x,y,cost,p)
    x_left, y_left, loc_left, cost_left, p_left = moveLeft(x,y,cost,p)
    x_upright, y_upright, loc_upright, cost_upright, p_upright = moveUpRight(x,y,cost,p)
    x_downright, y_downright, loc_downright, cost_downright, p_downright = moveDownRight(x,y,cost,p)
    x_downleft, y_downleft, loc_downleft, cost_downleft, p_downleft = moveDownLeft(x,y,cost,p)
    x_upleft, y_upleft, loc_upleft, cost_upleft, p_upleft = moveUpLeft(x,y,cost,p)
    return x_up, y_up, loc_up, cost_up, p_up, x_down, y_down, loc_down, cost_down, p_down, x_right, y_right, loc_right, cost_right, p_right, x_left, y_left, loc_left, cost_left, p_left, x_upright, y_upright, loc_upright, cost_upright, p_upright, x_downright, y_downright, loc_downright, cost_downright, p_downright, x_downleft, y_downleft, loc_downleft, cost_downleft, p_downleft, x_upleft, y_upleft, loc_upleft, cost_upleft, p_upleft 
    
travelled = {location : [0,'I']}    #creates  of points that have been travelled to, as well as the cost to get there

current_x = copy.deepcopy(start_x)
current_y = copy.deepcopy(start_y)
current_p = travelled[location][1]
current_cost = travelled[location][0]

locations = [location]

obstacles = []      #lists obstacle points that cannot be traversed

for i in range(0,301):      #left boundary
    x = 0
    y = i
    if y // 10 < 1:
        stringy = '00'
    elif y // 10 < 10:
        stringy = '0'
    else:
        stringy = '' 
    stringx = '00'
    location = str(stringx+str(int(x))+stringy+str(int(y)))
    obstacles.append(location)
    
for i in range(0,401):      #bottom boundary
    x = i
    y = 0
    if x // 10 < 1:
        stringx = '00'
    elif x // 10 < 10:
        stringx = '0'
    else:
        stringx = '' 
    stringy = '00'
    location = str(stringx+str(int(x))+stringy+str(int(y)))
    obstacles.append(location)
    
for i in range(0,301):      #right boundary
    x = 400
    y = i
    if y // 10 < 1:
        stringy = '00'
    elif x // 10 < 10:
        stringy = '0'
    else:
        stringy = '' 
    stringx = ''
    location = str(stringx+str(int(x))+stringy+str(int(y)))
    obstacles.append(location)
    
for i in range(0,401):      #top boundary
    x = i
    y = 300
    if x // 10 < 1:
        stringx = '00'
    elif x // 10 < 10:
        stringx = '0'
    else:
        stringx = '' 
    stringy = ''
    location = str(stringx+str(int(x))+stringy+str(int(y)))
    obstacles.append(location)
    
for i in range(55,126):     #obstacle 1: circle
    for j in range(35,106):
        if ((i-90)**2 + (j-70)**2 < 35**2):
            x = i
            y = j
            if x // 10 < 1:
                stringx = '00'
            elif x // 10 < 10:
                stringx = '0'
            else:
                stringx = ''
            if y // 10 < 1:
                stringy = '00'
            elif y // 10 < 10:
                stringy = '0'
            else:
                stringy = '' 
            location = str(stringx+str(int(x))+stringy+str(int(y)))
            obstacles.append(location)
        else:
            pass
    
for i in range(35,135):     #obstacle 2: slanted rectangle
    for j in range(108,186):
        if (j > (0.7*i) + (372/5)) and (j < (0.7*i) + (499/5)) and (j > ((-357/250)*i) + (22051/125)) and (j < ((-357/250)*i) + (45044/125)):
            x = i
            y = j
            if x // 10 < 1:
                stringx = '00'
            elif x // 10 < 10:
                stringx = '0'
            else:
                stringx = ''
            if y // 10 < 1:
                stringy = '00'
            elif y // 10 < 10:
                stringy = '0'
            else:
                stringy = '' 
            location = str(stringx+str(int(x))+stringy+str(int(y)))
            obstacles.append(location)
        else:
            pass

for i in range(200,231):        #obstacle 3: part 1 of U-shape
    for j in range(230,241):
        if (i > 200) and (i < 231) and (j > 230) and (j < 241):
            x = i
            y = j
            if x // 10 < 1:
                stringx = '00'
            elif x // 10 < 10:
                stringx = '0'
            else:
                stringx = ''
            if y // 10 < 1:
                stringy = '00'
            elif y // 10 < 10:
                stringy = '0'
            else:
                stringy = '' 
            location = str(stringx+str(int(x))+stringy+str(int(y)))
            obstacles.append(location)
        else:
            pass

for i in range(200,211):        #obstacle 4: part 2 of U-shape
    for j in range(240,271):
        if (i > 200) and (i < 211) and (j > 240) and (j < 271):
            x = i
            y = j
            if x // 10 < 1:
                stringx = '00'
            elif x // 10 < 10:
                stringx = '0'
            else:
                stringx = ''
            if y // 10 < 1:
                stringy = '00'
            elif y // 10 < 10:
                stringy = '0'
            else:
                stringy = '' 
            location = str(stringx+str(int(x))+stringy+str(int(y)))
            obstacles.append(location)
        else:
            pass

for i in range(200,231):        #obstalce 5: part 3 of U-shape
    for j in range(270,281):
        if (i > 200) and (i < 231) and (j > 270) and (j < 281):
            x = i
            y = j
            if x // 10 < 1:
                stringx = '00'
            elif x // 10 < 10:
                stringx = '0'
            else:
                stringx = ''
            if y // 10 < 1:
                stringy = '00'
            elif y // 10 < 10:
                stringy = '0'
            else:
                stringy = '' 
            location = str(stringx+str(int(x))+stringy+str(int(y)))
            obstacles.append(location)
        else:
            pass
        
for i in range(186,307):        #obstacle 6: ellipse
    for j in range(115,176):
        if ((((i-246)**2)/3600) + (((j-145)**2)/900) < 1):
            x = i
            y = j
            if x // 10 < 1:
                stringx = '00'
            elif x // 10 < 10:
                stringx = '0'
            else:
                stringx = ''
            if y // 10 < 1:
                stringy = '00'
            elif y // 10 < 10:
                stringy = '0'
            else:
                stringy = '' 
            location = str(stringx+str(int(x))+stringy+str(int(y)))
            obstacles.append(location)
        else:
            pass
        
for i in obstacles:     #displays obstacles as black pixels on image map
    locx = int(i[0:3])
    locy = int(i[3:])
    image[locx,locy] = 0
        
clearance = []

for i in range(0,401):        #bottom clearance
    for j in range(0,6):
        if (i > 0) and (i < 401) and (j > 0) and (j < 6):
            x = i
            y = j
            if x // 10 < 1:
                stringx = '00'
            elif x // 10 < 10:
                stringx = '0'
            else:
                stringx = ''
            if y // 10 < 1:
                stringy = '00'
            elif y // 10 < 10:
                stringy = '0'
            else:
                stringy = '' 
            location = str(stringx+str(int(x))+stringy+str(int(y)))
            clearance.append(location)
        else:
            pass
        
for i in range(0,6):        #left clearance
    for j in range(0,301):
        if (i > 0) and (i < 6) and (j > 0) and (j < 301):
            x = i
            y = j
            if x // 10 < 1:
                stringx = '00'
            elif x // 10 < 10:
                stringx = '0'
            else:
                stringx = ''
            if y // 10 < 1:
                stringy = '00'
            elif y // 10 < 10:
                stringy = '0'
            else:
                stringy = '' 
            location = str(stringx+str(int(x))+stringy+str(int(y)))
            clearance.append(location)
        else:
            pass
        
for i in range(396,401):        #right clearance
    for j in range(0,301):
        if (i > 396) and (i < 401) and (j > 0) and (j < 301):
            x = i
            y = j
            if x // 10 < 1:
                stringx = '00'
            elif x // 10 < 10:
                stringx = '0'
            else:
                stringx = ''
            if y // 10 < 1:
                stringy = '00'
            elif y // 10 < 10:
                stringy = '0'
            else:
                stringy = '' 
            location = str(stringx+str(int(x))+stringy+str(int(y)))
            clearance.append(location)
        else:
            pass
        
for i in range(0,401):        #top clearance
    for j in range(296,301):
        if (i > 0) and (i < 401) and (j > 296) and (j < 301):
            x = i
            y = j
            if x // 10 < 1:
                stringx = '00'
            elif x // 10 < 10:
                stringx = '0'
            else:
                stringx = ''
            if y // 10 < 1:
                stringy = '00'
            elif y // 10 < 10:
                stringy = '0'
            else:
                stringy = '' 
            location = str(stringx+str(int(x))+stringy+str(int(y)))
            clearance.append(location)
        else:
            pass
        
for i in range(50,131):     #clearance 1: circle
    for j in range(30,111):
        if ((i-90)**2 + (j-70)**2 < 40**2):
            x = i
            y = j
            if x // 10 < 1:
                stringx = '00'
            elif x // 10 < 10:
                stringx = '0'
            else:
                stringx = ''
            if y // 10 < 1:
                stringy = '00'
            elif y // 10 < 10:
                stringy = '0'
            else:
                stringy = '' 
            location = str(stringx+str(int(x))+stringy+str(int(y)))
            clearance.append(location)
        else:
            pass

for i in range(25,145):     #clearance 2: slanted rectangle
    for j in range(98,196):
        if (j > (0.7*i) + (347/5)) and (j < (0.7*i) + (524/5)) and (j > ((-357/250)*i) + (21426/125)) and (j < ((-357/250)*i) + (45669/125)):
            x = i
            y = j
            if x // 10 < 1:
                stringx = '00'
            elif x // 10 < 10:
                stringx = '0'
            else:
                stringx = ''
            if y // 10 < 1:
                stringy = '00'
            elif y // 10 < 10:
                stringy = '0'
            else:
                stringy = '' 
            location = str(stringx+str(int(x))+stringy+str(int(y)))
            clearance.append(location)
        else:
            pass

for i in range(195,236):        #clearance 3: part 1 of U-shape
    for j in range(225,246):
        if (i > 195) and (i < 236) and (j > 225) and (j < 246):
            x = i
            y = j
            if x // 10 < 1:
                stringx = '00'
            elif x // 10 < 10:
                stringx = '0'
            else:
                stringx = ''
            if y // 10 < 1:
                stringy = '00'
            elif y // 10 < 10:
                stringy = '0'
            else:
                stringy = '' 
            location = str(stringx+str(int(x))+stringy+str(int(y)))
            clearance.append(location)
        else:
            pass

for i in range(195,216):        #clearance 4: part 2 of U-shape
    for j in range(235,276):
        if (i > 195) and (i < 216) and (j > 235) and (j < 276):
            x = i
            y = j
            if x // 10 < 1:
                stringx = '00'
            elif x // 10 < 10:
                stringx = '0'
            else:
                stringx = ''
            if y // 10 < 1:
                stringy = '00'
            elif y // 10 < 10:
                stringy = '0'
            else:
                stringy = '' 
            location = str(stringx+str(int(x))+stringy+str(int(y)))
            clearance.append(location)
        else:
            pass

for i in range(195,236):        #clearance 5: part 3 of U-shape
    for j in range(265,286):
        if (i > 195) and (i < 236) and (j > 265) and (j < 286):
            x = i
            y = j
            if x // 10 < 1:
                stringx = '00'
            elif x // 10 < 10:
                stringx = '0'
            else:
                stringx = ''
            if y // 10 < 1:
                stringy = '00'
            elif y // 10 < 10:
                stringy = '0'
            else:
                stringy = '' 
            location = str(stringx+str(int(x))+stringy+str(int(y)))
            clearance.append(location)
        else:
            pass

for i in range(181,312):        #clearance 6: ellipse
    for j in range(110,181):
        if ((((i-246)**2)/4225) + (((j-145)**2)/1225) < 1):
            x = i
            y = j
            if x // 10 < 1:
                stringx = '00'
            elif x // 10 < 10:
                stringx = '0'
            else:
                stringx = ''
            if y // 10 < 1:
                stringy = '00'
            elif y // 10 < 10:
                stringy = '0'
            else:
                stringy = '' 
            location = str(stringx+str(int(x))+stringy+str(int(y)))
            clearance.append(location)
        else:
            pass
        
while current_x != goal_x or current_y != goal_y:       #runs until goal is met
    i = check_inputs(start_x,start_y,goal_x,goal_y)
    if i == 1:      #breaks loop if inputs are not valid
        break
    else:
        x_up, y_up, loc_up, cost_up, p_up, x_down, y_down, loc_down, cost_down, p_down, x_right, y_right, loc_right, cost_right, p_right, x_left, y_left, loc_left, cost_left, p_left, x_upright, y_upright, loc_upright, cost_upright, p_upright, x_downright, y_downright, loc_downright, cost_downright, p_downright, x_downleft, y_downleft, loc_downleft, cost_downleft, p_downleft, x_upleft, y_upleft, loc_upleft, cost_upleft, p_upleft   = moveAround(current_x,current_y,current_cost,current_p)
       
        if any(obs == loc_up for obs in clearance):
            pass
        elif loc_up in locations:
            if current_cost < cost_up:
                pass
            else:
                update = {loc_up : [cost_up,p_up]}
                travelled.update(update)
                locations.append(loc_up)
        else:
            update = {loc_up : [cost_up,p_up]}
            travelled.update(update)
            locations.append(loc_up)
            
        if any(obs == loc_down for obs in clearance):
            pass
        elif loc_down in locations:
            if current_cost < cost_down:
                pass
            else:
                update = {loc_down : [cost_down,p_down]}
                travelled.update(update)
                locations.append(loc_down)
        else:
            update = {loc_down : [cost_down,p_down]}
            travelled.update(update)
            locations.append(loc_down)
        
        if any(obs == loc_right for obs in clearance):
            pass
        elif loc_right in locations:
            if current_cost < cost_right:
                pass
            else:
                update = {loc_right : [cost_right,p_right]}
                travelled.update(update)
                locations.append(loc_right)
        else:
            update = {loc_right : [cost_right,p_right]}
            travelled.update(update)
            locations.append(loc_right)
            
        if any(obs == loc_left for obs in clearance):
            pass
        elif loc_left in locations:
            if current_cost < cost_left:
                pass
            else:
                update = {loc_left : [cost_left,p_left]}
                travelled.update(update)
                locations.append(loc_left)
        else:
            update = {loc_left : [cost_left,p_left]}
            travelled.update(update)
            locations.append(loc_left)
        
        if any(obs == loc_upright for obs in clearance):
            pass
        elif loc_upright in locations:
            if current_cost < cost_upright:
                pass
            else:
                update = {loc_upright : [cost_upright,p_upright]}
                travelled.update(update)
                locations.append(loc_upright)
        else:
            update = {loc_upright : [cost_upright,p_upright]}
            travelled.update(update)
            locations.append(loc_upright)
        
        if any(obs == loc_upleft for obs in clearance):
            pass
        elif loc_upleft in locations:
            if current_cost < cost_upleft:
                pass
            else:
                update = {loc_upleft : [cost_upleft,p_upleft]}
                travelled.update(update)
                locations.append(loc_upleft)
        else:
            update = {loc_upleft : [cost_upleft,p_upleft]}
            travelled.update(update)
            locations.append(loc_upleft)
            
        if any(obs == loc_downright for obs in clearance):
            pass
        elif loc_downright in locations:
            if current_cost < cost_downright:
                pass
            else:
                update = {loc_downright : [cost_downright,p_downright]}
                travelled.update(update)
                locations.append(loc_downright)
        else:
            update = {loc_downright : [cost_downright,p_downright]}
            travelled.update(update)
            locations.append(loc_downright)
            
        if any(obs == loc_downleft for obs in clearance):
            pass
        elif loc_downleft in locations:
            if current_cost < cost_downleft:
                pass
            else:
                update = {loc_downleft : [cost_downleft,p_downleft]}
                travelled.update(update)
                locations.append(loc_downleft)
        else:
            update = {loc_downleft : [cost_downleft,p_downleft]}
            travelled.update(update)
            locations.append(loc_downleft)
            
        del travelled[new_loc]
        travelled = {k: v for k, v in sorted(travelled.items(), key=lambda item: item[1])}   
        new_loc = list(travelled.keys())[0]
        current_x = int(new_loc[0:3])
        current_y = int(new_loc[3:])
        
        current_cost = list(travelled.values())[0][0]
        current_p = list(travelled.values())[0][1]
        print(current_x,current_y,current_cost,current_p)      #prints the current parent coordinates being explored
        
for i in locations:     #displays travelled to locations as gray on image map
    locx = int(i[0:3])
    locy = int(i[3:])
    if locx > 0 and locx < 404 and locy > 0 and locy < 300:
        image[locx,locy] = 190
    else:
        pass
    
opt_x = copy.deepcopy(start_x)
opt_y = copy.deepcopy(start_y)
    
for i in current_p:         #shows optimal path by back tracking from first parent node to reach solution
    if i == 'I':
        image[opt_x,opt_y] = 50
    elif i == 'A':
        opt_y += 1
        image[opt_x,opt_y] = 50
    elif i == 'B':
        opt_x += 1
        opt_y += 1
        image[opt_x,opt_y] = 50
    elif i == 'C':
        opt_x += 1
        image[opt_x,opt_y] = 50
    elif i == 'D':
        opt_x += 1
        opt_y -= 1
        image[opt_x,opt_y] = 50
    elif i == 'E':
        opt_y -= 1
        image[opt_x,opt_y] = 50
    elif i == 'F':
        opt_x -= 1
        opt_y -= 1
        image[opt_x,opt_y] = 50
    elif i == 'G':
        opt_x -= 1
        image[opt_x,opt_y] = 50
    elif i == 'H':
        opt_x -= 1
        opt_y += 1
        image[opt_x,opt_y] = 50  
        
print('Solution Found')
print('The cost of the path: ', current_cost)       #prints cost to get to goal (total distance travelled)

rotated = imutils.rotate_bound(image,-90)       #rotates image to match rubric

cv2.imshow('image',rotated)     #displays map with obstacles, travelled to points, and most optimal path
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)  