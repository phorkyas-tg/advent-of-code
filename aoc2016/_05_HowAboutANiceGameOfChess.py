import hashlib


def GetMDF5Password(doorId):
    i = 0

    password = ""
    while len(password) < 8:
        newString = doorId + str(i)
        result = hashlib.md5(newString.encode()).hexdigest()
        if result[0:5] == "00000":
            password += result[5]

        i += 1

    return password


def GetAdvancedMDF5Password(doorId):
    i = 0

    password = "########"
    while "#" in password:
        newString = doorId + str(i)
        result = hashlib.md5(newString.encode()).hexdigest()
        if result[0:5] == "00000" and result[5].isdigit() and \
                int(result[5]) < 8 and password[int(result[5])] == "#":
            index = int(result[5])
            password = password[:index] + result[6] + password[index + 1:]
        i += 1

    return password
