import re


def BuildLayers(puzzleInput, width=25, height=6):
    layerSize = width * height

    layers = []
    i = 0
    while i < len(puzzleInput):
        layers.append(puzzleInput[i:i+layerSize])
        i += layerSize

    return layers


def PrintImage(image, printToConsole=False, width=25):
    i = 0
    img = []
    while i < len(image):
        row = image[i:i + width]
        img.append(row)
        if printToConsole:
            print(row)
        i += width
    return img


def GetFewestZeros(puzzleInput):
    fewestZeros = 1e8
    result = 0

    for l in BuildLayers(puzzleInput):
        zeros = len(re.findall("0", l))
        if zeros < fewestZeros:
            fewestZeros = zeros
            ones = len(re.findall("1", l))
            twos = len(re.findall("2", l))
            result = ones * twos

    return result


def DecodeImage(puzzleInput, width=25, height=6):
    layers = BuildLayers(puzzleInput, width, height)

    decodedImage = ""
    for pixel in range(len(layers[0])):
        for layer in range(len(layers)):
            currentPixel = layers[layer][pixel]
            if currentPixel != "2":
                if currentPixel == "0":
                    decodedImage += " "
                elif currentPixel == "1":
                    decodedImage += "#"
                else:
                    decodedImage += currentPixel
                break

    return PrintImage(decodedImage, False, width)
