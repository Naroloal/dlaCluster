"""
This function finds the fractal dimensionality of the cluster 
"""
 
import numpy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from Walker import Walker,randomAtRadius,DLA_Cluster


radiusArray=numpy.arange(10,80,5)
mass=[]

for i in radiusArray:
    massValue,matrix=DLA_Cluster(i,False) #import radius and True/False for GIF
    mass.append(massValue)

#------- Find fit for mass and radius of the cluster:
# Find log radius and log mass
# Should be a linear function a+bx, with the slope b equal to the power of t and 'a'=scaling

#Find Log of all the arrays
logRadius=numpy.log(radiusArray)
logMass=numpy.log(mass)

#Fit a log function using numpy polyfit
fitLog=numpy.polyfit(logRadius, logMass,1,cov = True)
fitLogFunc=numpy.poly1d(fitLog[0])

#print out the results
print("Parametros para el ajuste log-fit: slope = ",fitLog[0][0],"shift: ",fitLog[0][1])
print("Parametros para el ajuste log-fit: la forma es e^",fitLog[0][1],"*r^",fitLog[0][0])
num=str(numpy.round(fitLog[0][0],3))

# ------------------------------------------------------------------------------

################################################################################
### Create Plots
################################################################################

# ------------------------------------------------------------------------------

#--------------- Plot log
fig = plt.subplot()
plt.scatter(logRadius,logMass, color='blue', edgecolors='blue', s=30)
plt.plot(logRadius, fitLogFunc(logRadius),color='green', lw=3)
plt.title("Log-log , area vs radio",fontsize=20)
plt.xlabel("Log radio",fontsize=15)
plt.ylabel("Log area",fontsize=15)
plt.grid(True)
fig.text(2.6,4.3,'Dimension Fractal:'+num)
fig.spines["top"].set_visible(False)  
fig.spines["right"].set_visible(False)  
plt.savefig('logRadiusMass2.png')
plt.show()



        
             
        

    
    