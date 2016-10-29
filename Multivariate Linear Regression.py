import sys
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages")
import numpy as np
import pylab as pl
import functools

def setup():
    #putting the data into allData list variable
    dataset = open("x17.txt", "r")
    global y
    y = []
    global allData
    allData = []
    for line in dataset:
        l = line.strip("\n").split("\t")
        y.append(float(l[-1]))
        listLength = len(l)
        allData.append(l[:-1])
    global m
    m = len(allData)
    
    #Create the numbers of xs to store our features (depends on the numbers of features)
    for i in range(0, len(allData[0])):
        li = []
        for g in range(0, len(allData)):
            li.append(allData[g][i])
        globals()["x%s" % i] = li
    global X
    X = []
    for h in range(0, len(allData[0])):
        X.append(globals()["x%s" % h])
    X = np.array(X, dtype=np.float64)
    X = np.transpose(X) 
    
    #Now we create the same number of parameters as our xs
    for r in range(0, len(allData[0])):
        globals()["param%s" % r] = 0.0
    global theta
    theta = []
    for u in range(0, len(allData[0])):
        theta.append(globals()["param%s" %u])
    theta = np.array(theta)

    #mean normalization for the Xs to get accurate thetas and faster GD.
    b = np.transpose(X)
    for i in range(1, len(allData[0])):
        maxVal = max(b[i])
        print("Max val", maxVal)
        minVal = min(b[i])
        total = functools.reduce(lambda u, o: u + o, b[i])
        print("total", total)
        average = (functools.reduce(lambda u, o: u + o, b[i])/len(b[i]))
        print("Average", average)
        for p in range(0, len(X)):
            b[i][p] = ((b[i][p] - average)/(maxVal-minVal))
        
    global X
    X = np.transpose(b)
    print(X)
    

def hypothesis(theta, X):
    #thetaT*x or theta0*x0 + theta1*x1 + theta2*x2...
    count = 0
    sum1 = 0.0
    for i in theta:
        sum1 = sum1 + (i*X[count])
        count = count + 1
    return sum1

def costFunction(theta, X, y, m):
    #this is just the cost function implementation
    #when that one line of data is passed into here, each value of X is 
    sum1 = 0.0
    for i in range(0, m):
        sum1 = sum1 + ((hypothesis(theta, X[i]) - y[i])**2.0)
    return ((1.0/(2.0 * m))*sum1)

def GradientDescent(theta, X, y):
    #X[i] is one line of data not the whole data for a feature
    #therefore X[i] = [1, 2, 3, 4] where 1 would be part of X0, 2 part of X1 and so on
    #X[i][j] would be a value in the single line of data
    sum1 = 0.0
    alpha = 0.01573
    for j in range(0, len(theta)):
        for i in range(0, m):
            sum1 = sum1 + ((hypothesis(theta, X[i]) - y[i]) * X[i][j])
        temp = ((1.0/m) * sum1 * alpha)
        theta[j] = theta[j] - temp
    return theta

def runner():
    setup()
    global costFuncL
    costFuncL = []
    numberOfRuns = 1000
    currCost = costFunction(theta, X, y, m)
    newtheta = theta
    for i in range(numberOfRuns):
        costFuncL.append(costFunction(newtheta, X, y, m))
        newtheta = GradientDescent(newtheta, X, y)
        newCost = costFunction(newtheta, X, y, m)
        if newCost < currCost:
            currCost = newCost
            besttheta = newtheta
    return besttheta

def plotCost():
    numRuns = []
    for i in range(0, 1000):
        numRuns.append(i)
    pl.plot(numRuns, costFuncL)
    pl.show()

def run():
    latesttheta = runner()
    print(latesttheta)
   # Xtopredict = [1, 62.0, 4.0, 50.0, 1.456]
    Xtopredict = [1, 63.48, 3.46, 52, 1.48216]
    Xtopredict = np.array(Xtopredict)
    y = hypothesis(latesttheta, Xtopredict)
    print(y)
    plotCost()
run()
