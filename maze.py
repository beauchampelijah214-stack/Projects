import math,tkinter as tk, random, time
#canvas setup
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
sky_backdrop=canvas.create_rectangle(0,0,401,200, fill="light blue")
canvas.pack()

#helpful functions

#splits move distance pixels in angle direction into x and y
def split_move(angle, distance):
    x=round((distance*math.cos(math.radians(angle))),2)
    y=round((distance*math.sin(math.radians(angle))),2)
    return(x,y)


#uses math to find the center of objects
def get_center(what):
    coords=canvas.coords(what)
    xcenter=0
    ycenter=0
    for i in range(len(coords)):
        if i%2==0:
            xcenter+=coords[i]
        else:
            ycenter+=coords[i]
    xcenter/=(len(coords)/2)
    ycenter/=(len(coords)/2)
    return[xcenter, ycenter]

#uses math to find the angle between two points and returns them
def angleTo(x1,y1, x2,y2):
    absAngle = math.degrees(math.atan2(y2 - y1, x2 - x1))
    angle = ((absAngle-180) + 360) % 360
    return (angle)

#uses math to return the coords to rotate the player degrees degrees around its center
def rotateCoords(degrees):
    center=get_center(player)
    m,n = center[0], center[1]
    coords=canvas.coords(player)
    a,b,c,d,e,f=coords[0],coords[1],coords[2],coords[3],coords[4],coords[5]
    deg = degrees
    r = -deg * (math.pi) / 180
    x1 = math.cos(r) * (a - m) - (b - n) * math.sin(r) + m
    y1 = math.sin(r) * (a - m) + (b - n) * math.cos(r) + n
    x2 = math.cos(r) * (c - m) - (d - n) * math.sin(r) + m
    y2 = math.sin(r) * (c - m) + (d - n) * math.cos(r) + n
    x3 = math.cos(r) * (e - m) - (f - n) * math.sin(r) + m
    y3 = math.sin(r) * (e - m) + (f - n) * math.cos(r) + n
    return (round(x1, 2), round(y1, 2), round(x2, 2), round(y2, 2), round(x3, 2), round(y3, 2))

#returns true if the coordinates provided hit the coordinates of any of the walls. it also sets hitX to True for the di-color effect if it hits the horizontal side of any wall. 
hitX=False
def coordsHit(x,y,what='player'):
    global hitX
    hitX=False
    if not ((5<x<395) and (5<y<395)): #boundary
        if (5==y or y==395):
            hitX=True
        #maze exit
        if y>=395 and 175<x<225:
            if what=='player':
                game_end()
            else:
                return False
        elif y>396:
            return False
        else:
            return True
    
    elif  (-1<x<51) and (49<y<56): 
        if (50==y or y==55):
            hitX=True
        return True
    
    elif  (49<x<101) and (99<y<106): 
        if (100==y or y==105):
            hitX=True
        return True
    
    elif  (-1<x<51) and (149<y<156): 
        if (150==y or y==155):
            hitX=True
        return True
    
    elif  (49<x<201) and (199<y<206): 
        if (200==y or y==205):
            hitX=True
        return True
    
    elif  (49<x<101) and (249<y<256): 
        if (250==y or y==255):
            hitX=True
        return True
    
    elif  (49<x<151) and (349<y<356): 
        if (350==y or y==355):
            hitX=True
        return True
    
    elif  (49<x<56) and (249<y<351): 
        if (250==y or y==350):
            hitX=True
        return True
    
    elif  (99<x<106) and (49<y<151): 
        if (50==y or y==150):
            hitX=True
        return True
    
    elif  (99<x<106) and (199<y<256): 
        if (200==y or y==255):
            hitX=True
        return True
    
    elif  (149<x<156) and (349<y<401): 
        if (350==y or y==400):
            hitX=True
        return True
    
    elif  (99<x<201) and (149<y<156): 
        if (150==y or y==155):
            hitX=True
        return True
    
    elif  (99<x<301) and (299<y<306): 
        if (300==y or y==305):
            hitX=True
        return True
    
    elif  (149<x<156) and (-1<y<101): 
        if (0==y or y==100):
            hitX=True
        return True
    
    elif  (149<x<251) and (49<y<56): 
        if (50==y or y==55):
            hitX=True
        return True
    
    elif  (299<x<306) and (-1<y<51): 
        if (0==y or y==50):
            hitX=True
        return True
    
    elif  (199<x<401) and (99<y<106): 
        if (100==y or y==105):
            hitX=True
        return True
    
    elif  (349<x<356) and (49<y<101): 
        if (50==y or y==100):
            hitX=True
        return True
    
    elif  (299<x<306) and (99<y<151): 
        if (100==y or y==150):
            hitX=True
        return True
    
    elif  (349<x<401) and (299<y<306): 
        if (300==y or y==305):
            hitX=True
        return True
    
    elif  (349<x<356) and (249<y<301): 
        if (250==y or y==300):
            hitX=True
        return True
    
    elif  (349<x<356) and (149<y<201): 
        if (150==y or y==200):
            hitX=True
        return True
    
    elif  (249<x<256) and (149<y<201): 
        if (150==y or y==200):
            hitX=True
        return True
    
    elif  (249<x<356) and (199<y<206): 
        if (200==y or y==205):
            hitX=True
        return True
    
    elif  (299<x<306) and (199<y<251): 
        if (200==y or y==250):
            hitX=True
        return True
    
    elif  (199<x<206) and (199<y<251): 
        if (200==y or y==250):
            hitX=True
        return True
    
    elif  (199<x<306) and (249<y<256): 
        if (250==y or y==255):
            hitX=True
        return True
    
    elif  (299<x<306) and (299<y<351): 
        if (300==y or y==350):
            hitX=True
        return True
    
    elif  (299<x<351) and (349<y<356): 
        if (350==y or y==355):
            hitX=True
        return True
    
    elif  (199<x<206) and (299<y<351): 
        if (300==y or y==350):
            hitX=True
        return True
    
    elif  (199<x<251) and (349<y<356): 
        if (350==y or y==355):
            hitX=True
        return True
    
    elif  (249<x<256) and (349<y<401): 
        if (350==y or y==400):
            hitX=True
        return True
    
    elif  (149<x<156) and (249<y<301): 
        if (250==y or y==300):
            hitX=True
        return True
    
    else:
        return False

#uncollides by pulling back 1 step if moving forward and if rotating, rotates until not hitting    
def uncollide(angle):
    global directionMoving, dx, rotateAngle
    collide_point=get_center(indicator)
    offset=split_move(angle, 20)
    if directionMoving==-1:
        collide_point[0]+=offset[0]
        collide_point[1]+=offset[1]
    if coordsHit(collide_point[0],collide_point[1]):
        if dx!=0:
            minus1=split_move(angle, 4)
            x=minus1[0]*directionMoving
            y=minus1[1]*directionMoving
            canvas.move(player, x,y)
            canvas.move(indicator, x, y)
        if rotateAngle!=0:
            while True:
                canvas.coords(player, *rotateCoords(-rotateAngle))
                updatedCoords=canvas.coords(player)
                canvas.coords(indicator, updatedCoords[0]-2.5, updatedCoords[1]-2.5, updatedCoords[0]+2.5, updatedCoords[1]+2.5)
                collide_point=get_center(indicator)
                collide_point=[collide_point[0], collide_point[1]]#changes it to a list
                if not coordsHit(collide_point[0],collide_point[1]):
                    break

# raycasting 

#setup
projectiles=[]
rays=[]
FOV=50
acrossScreen=0
distanceTravelled=0
distance=0

#projectile and line setup
for i in range(FOV):
    rays.append(canvas.create_line(0,0,0,0, width=8, fill="white"))
    projectiles.append(canvas.create_rectangle(20,20,36,36))

for object in projectiles:
    canvas.itemconfig(object, state="hidden")

#sends the projectile to the wall, creating a "flashlight", then uses the distance travelled to 3d render the walls
DV=200/math.tan((math.radians(25)))
def raycast():
    global rays, FOV, projectile, acrossScreen, distanceTravelled,distance, hitX,DV
    projectileCenters=[]
    acrossScreen=5
    for index, object in enumerate(projectiles):    
        player_center=get_center(player)
        indicatorCenter=get_center(indicator)
        canvas.coords(object,player_center[0]-7,player_center[1]-7, player_center[0]+7, player_center[1]+7)
        angle=angleTo(player_center[0],player_center[1], indicatorCenter[0], indicatorCenter[1])
        angle=angle-(FOV/2)+index
        
        #linear ray distribution
        angleChanged=math.degrees(math.atan((acrossScreen-200)/DV))
        angle+=angleChanged
        finalMoveCoords=[5,5]
        distance=0
        
        #collision detection
        for i in range(400):
            center = get_center(object)
            moveCoords = split_move((angle-180)%360, i+1)
            updatedCoords=[round(center[0]+moveCoords[0]),round(center[1]+moveCoords[1])]
            distance+=1
            if coordsHit(updatedCoords[0],updatedCoords[1], "projectile"):
                finalMoveCoords=moveCoords
                break
        if len(finalMoveCoords)==0:
            finalMoveCoords=(0,0)
            #if the projectile doesn't hit a wall in 400 steps, i.e, if it found the exit, sets finalMoveCoords to 0,0 to avoid an error and to indicate that the line shouldn't be visible
        canvas.move(object, finalMoveCoords[0],finalMoveCoords[1])
        
        #lines
        indicatorCenter=get_center(indicator)
        projectileCenters.append(get_center(object))
        
        #fix fisheye
        angle2=angleTo(player_center[0],player_center[1], indicatorCenter[0], indicatorCenter[1])
        r=(angle-angle2)* (math.pi) / 180
        distance=math.cos(r)*distance
        height=3000/distance
        center=get_center(rays[index])
        canvas.coords(rays[index], acrossScreen,200+height, acrossScreen,200-height)
        
        #x/y coloring
        if hitX==True:
            blueChange=50
        else:
            blueChange=10
        hexCode=str(hex(200-round((distance/1.5)))[2:])+str(hex(200-round((distance/1.5)))[2:])+str(hex(blueChange+200-round((distance/1.5)))[2:])
        if len(hexCode)<6:
            hexCode="000000"
        if 'x' in hexCode:
            hexCode="000000"
        if finalMoveCoords==(0,0):
            canvas.itemconfig(rays[index], state='hidden')
        else:
            canvas.itemconfig(rays[index], state='normal')
            canvas.itemconfig(rays[index], fill='#'+hexCode)
        acrossScreen+=400/FOV 

#move/rotate setup, using root.after to allow for key holding
def key_press(event):
    global dx, dy, rotateAngle, spacing, directionMoving
    if event.keysym == "Left":
        rotateAngle=10
    elif event.keysym == "Right":
        rotateAngle=-10
    elif event.keysym == "Up":
        dx=-1
        spacing=0
        directionMoving=1
    elif event.keysym == "Down":
        dx=1
        spacing=22
        directionMoving=-1
    elif event.keysym == "e":
        canvas.coords(player, 200,400-15,190,400-35,210,400-35)

def key_release(event):
    global dx, rotateAngle, directionMoving
    if event.keysym=="Up" or event.keysym=='Down':
        dx=0
    elif event.keysym=="Left" or event.keysym=="Right":
        rotateAngle=0
canvas.bind("<KeyPress>", key_press)
canvas.bind("<KeyRelease>", key_release)

def move_player():
    global dx, indicator,spacing
    player_center=get_center(player)
    indicatorCenter=get_center(indicator)
    moveAngle=angleTo(player_center[0],player_center[1], indicatorCenter[0], indicatorCenter[1])
    if dx!=0:
        if dx==-1:
            move_coords=split_move((moveAngle-180)%360, 4)
        else:
            move_coords=split_move(moveAngle, 4)
        canvas.move(player, move_coords[0],move_coords[1])
        updatedCoords=canvas.coords(player)
        canvas.coords(indicator, updatedCoords[0]-2.5, updatedCoords[1]-2.5, updatedCoords[0]+2.5, updatedCoords[1]+2.5)
        uncollide(moveAngle)
    raycast()
    root.after(100, move_player)

#using the rotateCoords function, rotates the player, updates the indicator, then calls the uncollide function to uncollide if necessary
def rotate_player():
    global  indicator, rotateAngle
    player_center=get_center(player)
    indicatorCenter=get_center(indicator)
    moveAngle=angleTo(player_center[0],player_center[1], indicatorCenter[0], indicatorCenter[1])
    if rotateAngle!=0: #if the player is rotating, uses the function rotateCoords to find the coordinates of the rotation, then assign them to the player and the direction indicator
        rotateCoordinates=rotateCoords(rotateAngle)
        updatedCoords=[]
        for i in range(6):
            updatedCoords.append(rotateCoordinates[i])
        canvas.coords(player, *updatedCoords)
        canvas.coords(indicator, updatedCoords[0]-2.5, updatedCoords[1]-2.5, updatedCoords[0]+2.5, updatedCoords[1]+2.5)
        uncollide(moveAngle)
    root.after(100, rotate_player)

# player setup
player=canvas.create_polygon(200,15,190,35,210,35, fill="red")
indicator=canvas.create_oval(197.5,12.5,202.5,17.5, fill='red')
canvas.itemconfig(indicator, state="hidden")
canvas.itemconfig(player, state="hidden")
directionMoving=0
rotateAngle=0
dx = 0
spacing=0

# start and end of the game setup
startTime=time.time()
#instructions
print("This is a 3d maze. Use left and right arrow keys to turn and up and down keys to move forward and backwards. How fast can you find the exit?")

def game_end():
    global time
    root.quit()
    endTime=time.time()-startTime
    print("Good job! You beat the maze in %s seconds"%(round(endTime,2)))

#scene setup commands
rotate_player()
move_player()
canvas.focus_set()
root.mainloop()
'''
citations:
rotate shape: https://www.desmos.com/calculator/kohoey3j60
angle between two points: https://www.cs.cmu.edu/~tcortina/15104-f20/lectures/26-TurtleGraphics.pdf
generative AI (used only for troubleshooting/debugging): https://deepai.org/chat/text-generator
how to 3d render from a flashlight and fix lens effects: https://www.youtube.com/watch?v=Vihr-PVjWF4&t=151s
maze:https://m.media-amazon.com/images/I/51ulXlbIUSS._AC_UF1000,1000_QL80_.jpg
'''




