def oneDensonaldiff(h,deltTime,MiddleTemp,XNumber,NextTemp):
    X=0.32
    deltX=X/XNumber
    temperatureWater=30
    rouS=7800
    rouL=7200
    specificHeatS=660
    specificHeatL=830
    TconductivityS=31
    TconductivityL=35
    liqTemp=1514
    SodTemp=1453
    emissivity=0.8
    Boltzman = 0.000000056684
    m=1.34
    for i in range(XNumber):
        if MiddleTemp[i]>=liqTemp:
            rou=rouL
            specificHeat=specificHeatL
            Tconductivity=TconductivityL
        if  MiddleTemp[i]<=SodTemp:
            rou=rouS
            specificHeat=specificHeatS
            Tconductivity=TconductivityS
        if  (SodTemp<MiddleTemp[i]) & (liqTemp>MiddleTemp[i]):
            rou=(rouS-rouL)*(liqTemp-MiddleTemp[i])/(liqTemp-SodTemp)+rouL
            Tconductivity=(TconductivityS)*(liqTemp-MiddleTemp[i])/(liqTemp-SodTemp)+m*(1-(liqTemp-MiddleTemp[i])/(liqTemp-SodTemp))*TconductivityL
            specificHeat=(specificHeatS-specificHeatL)*(liqTemp-MiddleTemp[i])/(liqTemp-SodTemp)+specificHeatL+274950/(liqTemp-SodTemp)
        a1=Tconductivity/(rou*specificHeat)
        a= (Tconductivity*deltTime)/(rou*specificHeat*deltX*deltX)
        if i==0:
            NextTemp[i]=(1-2*deltTime*h/(rou*specificHeat*deltX)-2*deltTime*a1/(deltX*deltX))*MiddleTemp[i]+2*deltTime*a1*MiddleTemp[i+1]/(deltX*deltX)+2*deltTime*h*temperatureWater/(rou*specificHeat*deltX)
        if i==XNumber-1:
            NextTemp[i]=(1-2*deltTime*h/(rou*specificHeat*deltX)-2*deltTime*a1/(deltX*deltX))*MiddleTemp[i]+2*deltTime*a1*MiddleTemp[i-1]/(deltX*deltX)+2*deltTime*h*temperatureWater/(rou*specificHeat*deltX)
        if 0<i<XNumber-1:
            NextTemp[i]=a*MiddleTemp[i+1]+a*MiddleTemp[i-1]+(1-2*a)*MiddleTemp[i]
    return NextTemp
        
