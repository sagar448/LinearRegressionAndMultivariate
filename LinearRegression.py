import sys
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages")
import pylab as pl
"""So basically the cost function calculates the error from each point by a given
line. The gradient descent basically minimizes this cost function.
It does this by moving towards the minima of the cost function.
Based on the slope of the point of a certain value of given thetas.
Then alpha is how far down it should move down to get to the next legit theta
Then once again the gradient descent calculates the slope at that given theta
and moves towards the minima. This is done until convergence is reached"""
m = 7.0
x = [150, 200, 250, 300, 350, 400, 500, 600, 700] #Square_feet
y = [6450, 7450, 8450, 9450, 11450, 15450, 16950, 18450, 20450] #Price
numberOfRuns = 1000

def hTheta(theta0, theta1, x):
    return theta0 + (theta1*x)

def GradientDescent(theta0, theta1, x, y, alpha):
    sum1 =0.0
    sum2 = 0.0
    for i in range(0, len(x)):
        sum1 = sum1 + (hTheta(theta0, theta1, x[i]) - y[i])
        sum2 = sum2 + ((hTheta(theta0, theta1, x[i]) - y[i]) * x[i])
    temp0 = theta0 - (alpha*(1.0/m)*sum1)
    temp1 = theta1 - (alpha*(1.0/m)*sum2)
    theta0 = temp0
    theta1 = temp1
    return [theta0, theta1]

def costFunction(theta0, theta1, x, y):
    sum1 = 0.0
    for i in range(0, len(x)):
        sum1 = sum1 + ((hTheta(theta0, theta1, x[i]) - y[i])**2.0)
    return ((1.0/(2.0 * m))*sum1)

def runner(x, y, alpha):
    global costFuncL
    costFuncL = []
    theta0 = 0.0
    theta1 = 0.0
    currCost = costFunction(theta0, theta1, x, y)
    for i in range(numberOfRuns):
        costFuncL.append(costFunction(theta0, theta1, x, y))
        theta0, theta1 = GradientDescent(theta0, theta1, x, y, alpha)
        newCost = costFunction(theta0, theta1, x, y)
        if newCost < currCost:
            currCost = newCost
            bestTheta0 = theta0
            bestTheta1 = theta1
    return [bestTheta0, bestTheta1]

def plotCost():
    numRuns = []
    for i in range(0, 1000):
        numRuns.append(i)
    pl.plot(numRuns, costFuncL)
    pl.show()

def plotResult(theta0, theta1, x, y):
    pl.plot(x, y, "ro")
    yvals = []
    for i in x:
        yvals.append(hTheta(theta0, theta1, i))
    pl.plot(x, yvals)
    pl.show()
        

def run(valueToPredict, alpha):
    thetas = [0, 0]
    thetas[0], thetas[1] = runner(x, y, alpha)
    print("Values of Thetas are "+str(thetas[0])+" and "+str(thetas[1]))
    print("House of square feet "+str(valueToPredict)+" is rougly "+str(hTheta(thetas[0], thetas[1], valueToPredict)))
    plotCost()
    plotResult(thetas[0], thetas[1], x, y)
    #ideal alpha is 0.00000005


