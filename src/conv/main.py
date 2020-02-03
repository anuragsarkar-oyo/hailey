

'''

Convolutional neural network implementation

'''

class ConvNet:

    def __init__(self, inputSize, strideSize, filterSize, zeroPaddingSize):
        self.inputSize = inputSize[0]
        self.strideSize = strideSize
        self.filterSize = filterSize
        self.zeroPaddingSize = zeroPaddingSize
        self.neuronSize = (inputSize - filterSize + 2 * zeroPaddingSize) / strideSize + 1

    def convolute(self):
        if self.neuronSize != int(self.neuronSize):
            raise ValueError("value mismatch !")




x = ConvNet([5, 5, 3], 1, 3, 1).convolute()
