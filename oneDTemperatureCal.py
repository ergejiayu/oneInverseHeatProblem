def oneDTempCal(dis,VcastOriginal,deltTime,XNumber,measuredStepPoint,numberofMeasuredPoint,calTemp,h_initial):
    import math
    import oneDensonaldiff
    tl=[0]*10;
    for i in range(10):
        tl[i]=dis[i]/VcastOriginal
    initialTemp=[1]*XNumber
    time_Mold = int((tl[1]-tl[0])/deltTime)
    time_SCZ = int((tl[9]-tl[1])/deltTime)
    Time_all = time_Mold+time_SCZ
    TemSur = [0]*(Time_all)
    MiddleTemp=[0]*XNumber
    NextTemp=[0]*XNumber
    for i in range(XNumber):
        initialTemp[i]=1544
    MiddleTemp=initialTemp
    NextTemp=initialTemp
    for stepTime in range(1,Time_all):
        if stepTime <= time_Mold:
            tTime = deltTime*stepTime;
            h=1000*(0.07128*math.exp(-tTime)+2.328*math.exp(-tTime/9.5)+0.698)
            oneDensonaldiff.oneDensonaldiff(h,deltTime,MiddleTemp,XNumber,NextTemp)
        else:
             disNow = dis[1]+stepTime*VcastOriginal*deltTime
             if dis[1]<=disNow<=dis[2]:
                 h=h_initial[0]          
             if dis[2]<disNow<=dis[3]:
                 h=h_initial[1]
             if dis[3]<disNow<=dis[4]:
                 h=h_initial[2]
             if dis[4]<disNow<=dis[5]:
                 h=h_initial[3]
             if dis[5]<disNow<=dis[6]:
                 h=h_initial[4]
             if dis[6]<disNow<=dis[7]:
                 h=h_initial[5]
             if dis[7]<disNow<=dis[8]:
                 h=h_initial[6]
             if dis[8]<disNow:
                 h=h_initial[7]
             oneDensonaldiff.oneDensonaldiff(h,deltTime,MiddleTemp,XNumber,NextTemp)
        MiddleTemp=NextTemp
        TemSur[stepTime-1]=MiddleTemp[0]
    for j in range(numberofMeasuredPoint):
        calTemp[j]=TemSur[measuredStepPoint[j]]
