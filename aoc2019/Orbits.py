from anytree import Node, RenderTree
from aoc2019.AocInput import d6Input

def GetNode(entry):
    nodes = entry.split(")")
    return Node(nodes[0]), Node(nodes[1])


# temp = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"]

nodes = {}
for entry in d6Input:
# for entry in temp:
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

depth = 0
for descendant in orbit.descendants:
    depth += descendant.depth

print(depth)
# Answer 322508


