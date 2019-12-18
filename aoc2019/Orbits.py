from anytree import Node
from anytree.exporter import JsonExporter
from anytree.importer import JsonImporter
from anytree.search import find


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


def GetOrbitMinimalDistance(input, nodeName1, nodeName2):
    orbit = ReadTree(input.copy(), "aoc2019/orbits.json", True, False)

    node1 = find(orbit, filter_=lambda node: node.name == nodeName1)

    distance = 0
    parent = node1.parent
    while True:
        node2 = find(parent, filter_=lambda node: node.name == nodeName2)
        if node2 is not None:
            start = 0
            for i in range(len(node1.path)):
                if node1.path[i].name == parent.name:
                    start = i
                if node1.path[i].name == nodeName1:
                    distance += i - start
                    break

            start = 0
            for i in range(len(node2.path)):
                if node2.path[i].name == parent.name:
                    start = i
                if node2.path[i].name == nodeName2:
                    distance += i - start
                    return distance - 2

        parent = parent.parent
