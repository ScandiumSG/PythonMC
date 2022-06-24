import numberGeneratorAsArray as generator
import numpy as np
import matplotlib.pyplot as plt
import math

class makePlot():
    iteration = int(input("Select amount of iterations: "))
    def makePlot(iterations, minVal, maxVal):   
        def withinCircle(xVal, yVal, radius):
            distance = math.sqrt((abs(xVal-radius))**2 + (abs(yVal-radius))**2)
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

        radius = maxVal/2
        data = generator.generateValues.generateNValues(iterations, minVal, maxVal)
        circleDataX = []
        circleDataY = []
        circlePoints = 0
        outOfBoundsDataX = []
        outOfBoundsDataY = []
        OOBPoints = 0
        for i in range(len(data[0])):
            if (withinCircle(data[0][i], data[1][i],1)):
                circleDataX.append(data[0][i])
                circleDataY.append(data[1][i])
                circlePoints += 1
            else: 
                outOfBoundsDataX.append(data[0][i])
                outOfBoundsDataY.append(data[1][i])
                OOBPoints += 1
        #Data conversion
        circle2D = [circleDataX, circleDataY]
        circleDataArray = np.array(circle2D)
        OOB2D = [outOfBoundsDataX, outOfBoundsDataY]
        OOBDataArray = np.array(OOB2D)

        #Outline define
        outline = plt.Circle((1,1), radius, color='blue', fill=False)

        #Determine pi value
        explainationText = "Iterations: "+str(iterations)+" Approximated PI value: "+str(calcPi(circlePoints, OOBPoints))

        fig, ax = plt.subplots()
        ax.scatter(circleDataArray[0], circleDataArray[1], color='blue', s=5)
        ax.scatter(OOBDataArray[0], OOBDataArray[1], color='red', s=5)
        ax.add_patch(outline)
        ax.set(xlim=(minVal, maxVal), ylim=(minVal, maxVal))
        ax.text(0, maxVal+0.01, explainationText, fontsize=12)
        plt.show()

    if __name__ == '__main__':
        makePlot(iteration, 0, 2)