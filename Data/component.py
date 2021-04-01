class Component(object):
    def __init__(self, stateLabel:str, funcDo) -> None:
        self.stateLabel = stateLabel
        self.__do = funcDo
        self.__degree = 1
        self.__prev = None
    
    def getLabel(self):
        return self.stateLabel
        
    def setPrev(self, prevObj):
        self.__prev = prevObj

    def calc(self):
        if self.__do == None:
            raise Exception("Fungsi do harus diset terlebih dahulu")

        return self.__do(self.__prev.calc())

class Parallel(Component):
    def __init__(self, stateLabel: str, funcDo, degree:int) -> None:        
        super().__init__(stateLabel, funcDo)
        self.__degree = degree
    
    def setPrev(self, *prevObjs):
        return super().setPrev(prevObjs)

    def calc(self, input=None):
        if self.__do == None:
            raise Exception("Fungsi do harus diset terlebih dahulu")

        result = None

        for i in self.__prev:
            result = self.__do(self.i.calc())
        
        return result

class Delay(Component):
    def __init__(self, stateLabel: str, prevObj, defaultValue) -> None:
        def delay(self, x):
            pop = self.__delay
            self.__delay = x

            return pop

        super().__init__(stateLabel, delay)
        self.__delay = defaultValue

class InputObject(object):
    def __init__(self) -> None:
        super().__init__()
        self.__value = None
    
    def setValue(self, value):
        self.__value = value
    
    def getValue(self):
        return self.__value


class Input(Component):
    def __init__(self, stateLabel: str, input:InputObject) -> None:
        self.__ref = input
        super().__init__(stateLabel, lambda x : x)
    
    def calc(self):
        return self.__ref.getValue()