class swapString:
    string = ""
    numPeople = 0

    def __init__(self, numPeople):
        self.numPeople = numPeople
        for number in range(1,numPeople + 1):
            self.string += str(number)
    
    def swap(self, briberPos):
        if briberPos == 0:
            return False
        if briberPos == len(self.string):
            return False
        stringList = list(self.string)
        hold = stringList[briberPos - 1]
        stringList[briberPos - 1] = stringList[briberPos]
        stringList[briberPos] = hold
        self.string = ''.join(stringList)
        return True
    
    def minSwaps(self):
        q = self.string
        bribes = 0
        maxOff = 2
        lineLength = len(q)
        for index,person in enumerate(q):
            linePos = index + 1
            if (int(person) - index - 1) > maxOff:
                print("Too chaotic")
                return
            # Person has been bribed
            if linePos > int(person):
                inFrontOriginalPos = max(int(person) - 2, 0)
                for j in range(inFrontOriginalPos, index):
                    if int(q[j]) > int(person):
                        bribes+=1

        print(bribes)
        return bribes
        
    
# test = swapString(5) 
# print(test.string)
# print("test)")


