import oneDTemperatureCal
import numpy.linalg as nlg
import numpy as np
dis=[0.0,0.9,3.86,5.679,7.574,11.363,17.457,23.402,29.022,31.332]
measuredTemp=[1010,985,942,941,915,860,812]
disMeasure=[3.9,5.8,11.3,13.5,17.9,23.5,31]
numberofMeasuredPoint=7
SCZ_num=8
no_MeasuredPoint=SCZ_num-numberofMeasuredPoint
h_initial=[545.4,381.4,246.4,182.5,158.3,147.9,147.8,146.9]
h_new=[0]*SCZ_num
dh=[0]*numberofMeasuredPoint
VcastOriginal=0.6/60
deltTime=0.1
measuredStepPoint=[0]*numberofMeasuredPoint
for i in range(numberofMeasuredPoint):
    measuredStepPoint[i]=int((disMeasure[i]/VcastOriginal)/deltTime)
#print(measuredStepPoint)
XNumber=30
calTemp=[0]*numberofMeasuredPoint
calTemp_sensive=[0]*numberofMeasuredPoint
errorTemp=[0]*numberofMeasuredPoint
oneDTemperatureCal.oneDTempCal(dis,VcastOriginal,deltTime,XNumber,measuredStepPoint,numberofMeasuredPoint,calTemp,h_initial)
iter_max=10;
J=[0]*iter_max
eye=[([0]*numberofMeasuredPoint) for i in range(numberofMeasuredPoint)]
delth=1
dudh_1=[([0]*numberofMeasuredPoint) for i in range(numberofMeasuredPoint)]
dudh_2=[([0]*numberofMeasuredPoint) for i in range(numberofMeasuredPoint)]
dudh=[([0]*numberofMeasuredPoint) for i in range(numberofMeasuredPoint)]
dudh_transport=[([0]*numberofMeasuredPoint) for i in range(numberofMeasuredPoint)]
h_delt_all=[([0]*SCZ_num) for i in range(SCZ_num)]
eps=0.1
for i in range(numberofMeasuredPoint):
    for j in range(numberofMeasuredPoint):
        if i==j:
            eye[i][j]=1.0
for iter_num in range(iter_max):
    for i in range(numberofMeasuredPoint):
        J[iter_num]=J[iter_num]+(calTemp[i]-measuredTemp[i])*(calTemp[i]-measuredTemp[i])
    print(J[iter_num])
    J[iter_num]=0
    for i in range(numberofMeasuredPoint):
        for j in range(numberofMeasuredPoint):
            dudh_1[i][j]=calTemp[j]
  #  print(calTemp)
    for i in range(SCZ_num):
        for j in range(SCZ_num):
            if i==j:
                h_delt_all[i][j]=h_initial[j]+delth
            else:
                h_delt_all[i][j]=h_initial[j]
    for i in range(no_MeasuredPoint):
        h_delt_all[i][i]=h_delt_all[i][i]-delth
    for i in range(no_MeasuredPoint,SCZ_num):
        for j in range(SCZ_num):
            h_new[j]=h_delt_all[i][j]
        oneDTemperatureCal.oneDTempCal(dis,VcastOriginal,deltTime,XNumber,measuredStepPoint,numberofMeasuredPoint,calTemp_sensive,h_new)
        for k in range(numberofMeasuredPoint):
            dudh_2[i-no_MeasuredPoint][k]=calTemp_sensive[k]
    for i in range(numberofMeasuredPoint):
        for j in range(numberofMeasuredPoint):
            dudh[i][j]=(dudh_1[i][j]-dudh_2[i][j])/delth
    for i in range(numberofMeasuredPoint):
        errorTemp[i]=(calTemp[i]-measuredTemp[i])
    dudh_transport=nlg.inv(eye+np.transpose(dudh)*dudh)*dudh
    for i in range(numberofMeasuredPoint):
        dh[i]=0
        for j in range(numberofMeasuredPoint):
            dh[i]=dh[i]+dudh_transport[i][j]*errorTemp[j]
    for r in range(no_MeasuredPoint,SCZ_num):
        h_initial[r]=h_initial[r]+dh[r-no_MeasuredPoint]
    oneDTemperatureCal.oneDTempCal(dis,VcastOriginal,deltTime,XNumber,measuredStepPoint,numberofMeasuredPoint,calTemp,h_initial)

