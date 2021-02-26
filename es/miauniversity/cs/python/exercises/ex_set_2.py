import string


class ReversedInput:
    def __init__(self, sInput):
        self.__inputValue = sInput
        self.__result = ""

    def getInput(self) -> string:
        return self.__inputValue

    def setInputViaTerminal(self):  # pragma: no cover
        self.__inputValue = input("Give me an input: ")

    @staticmethod
    def __reverseString(sInput) -> string:
        __sResult = ""
        for i in reversed(range(len(sInput))):
            __sResult += f'{sInput[i]}'
        return __sResult

    def printResult(self):  # pragma: no cover
        while self.__inputValue == "":
            print(f'Please set a non empty value!')
            self.__inputValue = input("Give me an input: ")
        print(f'The result of the reversed string "{self.getInput()}" is "{self.__reverseString(self.__inputValue)}"')

    def __setResult(self):
        self.__result = self.__reverseString(self.__inputValue)

    def getResult(self):
        self.__setResult()
        return self.__result
