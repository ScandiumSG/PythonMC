import random as rd
import numpy as np
from tqdm import tqdm


class generateValues():
    def generateNValues(numberOfValues, minVal, maxVal):
        # Generate X and Y values as python lists
        print("Generating...")
        generatedX = []
        generatedY = []
        for n in tqdm(range(0,numberOfValues)):
            newValue = rd.uniform(minVal, maxVal)
            generatedX.append(newValue)

            newValue = rd.uniform(minVal, maxVal)
            generatedY.append(newValue)

        # Convert from python list to numpy array
        python2D = [generatedX, generatedY]
        generatedData = np.array(python2D)
        print("Generation complete!")
        return generatedData


    if __name__ == '__main__':
        print("Starting.")
        genData = generateNValues(4, 0, 2)
        print("Values printed: ", len(genData[0]))
        for i in range(1,len(genData[0])+1):
            print("X: ", genData[0][i-1],"\t\t","Y: ", genData[1][i-1])
