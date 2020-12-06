import uuid


class Node:
    def __init__(self, frame, parent=None):
        self.nodeId = str(uuid.uuid4())
        self.parent = parent
        self.children = []

        self.header = frame[:2]
        self.payload = None
        self.trailer = None

        self.numberOfChildren = self.header[0]
        self.trailerLength = self.header[1]
        self.indexedMetaData = 0

    def GetNumberOfChildren(self):
        return self.numberOfChildren

    def GetId(self):
        return self.nodeId

    def AddChild(self, childId):
        self.children.append(childId)

    def GetChildren(self):
        return self.children

    def GetTrailerLength(self):
        return self.trailerLength

    def SetPayload(self, payload):
        self.payload = payload

    def GetPayload(self):
        return self.payload

    def SetTrailer(self, trailer):
        self.trailer = trailer

    def GetTrailer(self):
        return self.trailer

    def GetFrame(self):
        frame = self.header.copy()
        frame.extend(self.payload.copy())
        frame.extend(self.trailer.copy())
        return frame

    def GetLength(self):
        return len(self.header) + len(self.payload) + len(self.trailer)

    def SetIndexedMetaData(self, imd):
        self.indexedMetaData = imd

    def GetIndexedMetadata(self):
        return self.indexedMetaData

    def GetMetadata(self):
        return sum(self.trailer)


def ParseNodesRecursion(frame, parent=None, result=None):
    newNode = Node(frame, None if parent is None else parent.GetId())
    if result is None:
        result = {}
    result[newNode.GetId()] = newNode

    # cut the header off
    frame = frame[2:]

    # go through every child. every loop the frame will be cut by the length of the child node
    for children in range(newNode.GetNumberOfChildren()):
        frame, childId = ParseNodesRecursion(frame, newNode, result)
        newNode.AddChild(childId)

    # at this point frame is the trailer of this node + the rest of all frames
    trailerLength = newNode.GetTrailerLength()
    newNode.SetTrailer(frame[:trailerLength])

    # the payload is the sum of all child node frames
    payload = []
    for childId in newNode.GetChildren():
        payload.extend(result[childId].GetFrame().copy())
    newNode.SetPayload(payload)

    # calc the indexed meta data. Default (no children) metaData is sum of trailer
    imd = newNode.GetMetadata()
    # else the trailer entry is an index to the child-metadata (counting from 1)
    if newNode.GetNumberOfChildren() > 0:
        children = newNode.GetChildren()
        imd = sum(result[children[i-1]].GetIndexedMetadata() for i in newNode.GetTrailer()
                  if 0 < i <= len(children))
    newNode.SetIndexedMetaData(imd)

    # return the rest + the current Id
    return frame[trailerLength:], newNode.GetId()


def GetSumOfMetaData(frame):
    result = {}
    ParseNodesRecursion(frame, result=result)
    return sum(node.GetMetadata() for node in result.values())


def GetSumOfMetaDataAdvanced(frame):
    result = {}
    ParseNodesRecursion(frame, result=result)
    for node in result.values():
        # Return the metaData from the first node
        return node.GetIndexedMetadata()
