def GetFieldDict(notes):
    # read dict of keys with the specific ranges
    fieldDict = {}
    for line in notes.splitlines():
        ticketField, values = line.split(":")
        values = values.split()

        range1 = list(map(int, values[0].split("-")))
        range2 = list(map(int, values[2].split("-")))

        fieldDict[ticketField] = [range1, range2]
    return fieldDict


def SepaparateTickets(nearbyTickets, fieldDict):
    # separate nearby tickets into invalid numbers and valid tickets
    invalidNumbers = []
    validTickets = []
    for ticket in nearbyTickets.splitlines():
        if "nearby tickets:" in ticket:
            continue
        numbers = list(map(int, ticket.split(",")))

        for number in numbers:
            for range1, range2 in fieldDict.values():
                if range1[0] <= number <= range1[1] or range2[0] <= number <= range2[1]:
                    break
            else:
                invalidNumbers.append(number)
                break
        else:
            validTickets.append(numbers)
    return validTickets, invalidNumbers


def GetInvalidTickets(puzzleInput):
    notes, yourTicket, nearbyTickets = puzzleInput.split("\n\n")
    fieldDict = GetFieldDict(notes)
    validTickets, invalidNumbers = SepaparateTickets(nearbyTickets, fieldDict)

    return sum(invalidNumbers)


def GetValidTickets(puzzleInput, keyWord="departure"):
    notes, yourTicket, nearbyTickets = puzzleInput.split("\n\n")
    fieldDict = GetFieldDict(notes)
    validTickets, invalidNumbers = SepaparateTickets(nearbyTickets, fieldDict)

    # for each index in every valid ticket check if the values are in the range of a note dict key
    possibleFields = {}
    for ticketField, ranges in fieldDict.items():
        range1, range2 = ranges

        for i in range(len(validTickets[0])):
            for validTicket in validTickets:
                if not range1[0] <= validTicket[i] <= range1[1] and \
                        not range2[0] <= validTicket[i] <= range2[1]:
                    break
            else:
                possibleFields.setdefault(i, [])
                possibleFields[i].append(ticketField)

    # reduce the possible solutions
    correctFields = {}
    while True:
        for i, ticketField in possibleFields.items():
            if len(ticketField) == 1:
                correctKey = ticketField[0]
                correctFields[i] = correctKey
                for keys in possibleFields.values():
                    try:
                        keys.remove(correctKey)
                    except ValueError:
                        pass
                break
        else:
            break

    # multiply the values of your ticket that start with the given keyword
    yourTicket = list(map(int, yourTicket.splitlines()[1].split(",")))
    result = 1
    for i, ticketField in correctFields.items():
        if ticketField.startswith(keyWord):
            result *= yourTicket[i]

    return result
