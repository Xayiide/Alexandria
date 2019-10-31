


def readToken():
    with open('../token.txt', 'r') as token:
        return token.readline().strip("\n");
