from functools import reduce
from dataclasses import dataclass, field
from typing import List
import operator


@dataclass
class Packet:
    version: int = 0
    typeId: int = 0

    lengthType: int = 0
    length: int = 0

    payload: str = ""
    numberOfSubPackets: int = 0
    subPackets: List = field(default_factory=lambda: [])

    number: int = 0


def getPacket(bitStream, packets):
    packet = Packet()
    packet.version = int(bitStream[0:3], 2)
    packet.typeId = int(bitStream[3:6], 2)
    packet.subPackets = []

    if packet.typeId == 4:
        bitPos = 6
        while True:
            group = int(bitStream[bitPos:bitPos + 1], 2)
            packet.subPackets.append(bitStream[bitPos + 1:bitPos + 5])
            bitPos += 5
            if not group:
                packet.number = int("".join(packet.subPackets), 2)
                packets.append(packet)
                return packet, bitStream[bitPos:]

    else:
        packet.lengthType = int(bitStream[6:7], 2)

        if packet.lengthType:
            packet.numberOfSubPackets = int(bitStream[7:18], 2)
            payload = bitStream[18:]
            for i in range(packet.numberOfSubPackets):
                subPacket, payload = getPacket(payload, packets)
                packet.subPackets.append(subPacket)
            packets.append(packet)
            return packet, payload
        else:
            packet.length = int(bitStream[7:22], 2)
            packet.payload = bitStream[22:22+packet.length]

            payload = packet.payload
            while len(payload) > 0:
                subPacket, payload = getPacket(payload, packets)
                packet.subPackets.append(subPacket)

            packets.append(packet)
            payload = bitStream[22+packet.length:]

        return packet, payload


def getBitStream(line):
    hexString = line.strip()
    bitStream = bin(int(hexString, 16))[2:]
    # fill with zeros
    while len(bitStream) < 4 * len(hexString):
        bitStream = "0" + bitStream

    return bitStream


def calc(packet: Packet):
    typeId = packet.typeId
    if typeId == 0:
        packet.number = sum(p.number for p in packet.subPackets)
    if typeId == 1:
        packet.number = reduce(operator.mul, [p.number for p in packet.subPackets], 1)
    if typeId == 2:
        packet.number = min(p.number for p in packet.subPackets)
    if typeId == 3:
        packet.number = max(p.number for p in packet.subPackets)
    if typeId == 5:
        packet.number = 1 if packet.subPackets[0].number > packet.subPackets[1].number else 0
    if typeId == 6:
        packet.number = 1 if packet.subPackets[0].number < packet.subPackets[1].number else 0
    if typeId == 7:
        packet.number = 1 if packet.subPackets[0].number == packet.subPackets[1].number else 0


def puzzleA(lines):
    bitStream = getBitStream(lines[0])

    packets = []
    getPacket(bitStream, packets)

    return sum(p.version for p in packets)


def puzzleB(lines):
    bitStream = getBitStream(lines[0])

    packets = []
    packet, __ = getPacket(bitStream, packets)
    for p in packets:
        calc(p)

    return packet.number


if __name__ == '__main__':
    day = "16"
    file = open("input\\input_{0}.txt".format(day), 'r')
    # file = open("input\\input_{0}_test.txt".format(day), 'r')
    inputLines = file.readlines()
    file.close()

    a = puzzleA(inputLines)
    b = puzzleB(inputLines)
    print(a)
    print(b)
    assert a == 953
    assert b == 246225449979
