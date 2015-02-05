import sdl


#Frame delta vars.
currTime = 0
prevTime = 0
prevFpsUpdate = 0

#Updated with a certain frequency.
fps = 0
averageDelta = 0

#The frequency by which to update the FPS.
fpsUpdateFrequency = 1

#Frames since last FPS update.
frames = 0

#The current timestep.
dt = 0

#The timer period (reciprocal of the frequency.)
#timerPeriod = getTimerPeriod()


def init():
    global currTime, prevFpsUpdate
    
#Init the SDL timer system (needed for SDL_Delay.)
    if sdl.InitSubSystem(sdl.INIT_TIMER) < 0:
        print (sdl.GetError())
        
    currTime = getTime()
    prevFpsUpdate = currTime


def getAverageDelta():
    pass

def getDelta():
    pass

def getFPS():
    pass

def getMicroTime():
    pass

def getTime():
    pass

def sleep():
    pass

def step():
    global currTime, prevTime, dt
    #Frames rendered

    #"Current" time is previous time by now.
    prevTime = currTime;

    #Get time from system.
    currTime = getTime();

    #Convert to number of seconds.
    dt = currTime - prevTime;

    timeSinceLast = currTime - prevFpsUpdate;
    #Update FPS?
    if timeSinceLast > fpsUpdateFrequency:
        fps = int((frames/timeSinceLast) + 0.5);
        averageDelta = timeSinceLast/frames;
        prevFpsUpdate = currTime;
        frames = 0;


