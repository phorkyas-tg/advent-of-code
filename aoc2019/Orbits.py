from anytree import Node
from anytree.exporter import JsonExporter
from anytree.importer import JsonImporter
from aoc2019.AocInput import d6Input


def GetNode(entry):
    nodes = entry.split(")")
    return Node(nodes[0]), Node(nodes[1])


def ReadTree(input, fileName=None, readFromJson=False, writeToJson=False):
    if readFromJson:
        importer = JsonImporter()
        inputFile = open(fileName, 'r')
        orbit = importer.read(inputFile)
        inputFile.close()
        return orbit

    nodes = {}
    for entry in input:
        parent, child = GetNode(entry)

        child.parent = parent
        if parent.name in nodes:
            child.parent = nodes[parent.name]
        else:
            nodes[parent.name] = parent

    while len(nodes) != 1:
        for key, value in nodes.items():
            for parent in value.descendants:

                if parent.name in nodes:
                    subnode = nodes.pop(parent.name)
                    for child in subnode.children:
                        child.parent = parent
                    break

            else:
                continue
            break

    orbit = nodes.popitem()[1]

    if writeToJson:
        exporter = JsonExporter(indent=4, sort_keys=False)
        outputFile = open(fileName, 'w')
        exporter.write(orbit, outputFile)
        outputFile.close()

    return orbit


def GetOrbitDepth(input):
    orbit = ReadTree(input.copy(), "aoc2019/orbits.json", True, False)

    depth = 0
    for descendant in orbit.descendants:
        depth += descendant.depth

    return depth


