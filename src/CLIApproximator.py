import random as rd
import math
from tqdm import tqdm


class MCcalc():

    circleDot = 0
    boxDot = 0

    iterations = int(input("Set number of iterations: "))

    reportIntervall = (input("How many iterations between status update? "))
    if (reportIntervall != '' and reportIntervall != ' ' and reportIntervall != 'none'):
        reportIntervall = int(reportIntervall)
    else:
        reportIntervall = int(iterations) + 1

    def withinCircle(xVal, yVal, radius):
        distance = math.sqrt((abs(xVal-radius)**2)+(abs(yVal-radius)**2))
        if (distance <= radius):
            return True
        else:
            return False

    def calcPi(pointsInside, pointsOutside):
        if (pointsInside is not None and pointsOutside is not None):
            ratio = pointsInside / (pointsOutside + pointsInside)
            piVal = ratio * 4
            return piVal
        else:
            return 0

    if __name__ == '__main__':
        minVal = 0
        maxVal = 2
        for i in tqdm(range(0,iterations)):
            xData = rd.uniform(minVal, maxVal)
            yData = rd.uniform(minVal, maxVal)
            if (withinCircle(xData, yData,1)):
                circleDot += 1
            else: 
                boxDot += 1
            if ((i % reportIntervall) == 0 and i != 0): 
                print("Current value after ", i, " iterations: ", str(calcPi(circleDot, boxDot)))
        print("Finished\n", "Estimated PI value: ", str(calcPi(circleDot, boxDot)))

    def __main__(self):
        pass

    def __init__(self):
        pass