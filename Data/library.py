from component import *

class Machine(object):
    def __init__(self, machineLabel:str, component:Component):
        self.__input = InputObject()

        InComponent = Input("In", self.__input)
        component.setPrev(InComponent)

        self.__collection = [InComponent, component]
        self.machineLabel = machineLabel
        self.__topComponent = component
        
    
    def appendCmp(self, component:Component, linkTo):
        if type(linkTo) == int:
            component.setPrev(self.__collection[linkTo])
        elif type(linkTo) == str:
            found = False

            for i in self.__collection:
                if i.getLabel() == linkTo:
                    component.setPrev(i)
                    found = True
                    break
            
            if not found:
                raise Exception("Nama Objek tidak ditemukan")
        else:
            raise Exception("Nama Objek tidak dikenali")
        
        self.__collection.append(component)
        self.__topComponent = component
    
    def calc(self, x):
        self.__input.setValue(x)
        return self.__topComponent.calc()

class SimpleMachine(Machine):
    def __init__(self, machineLabel: str, funcDo):
        super().__init__(machineLabel, Component("C1", funcDo))

class State(object):
    def __init__(self, stateLabel:str, machine:Machine, funcCompare):
        self.stateLabel = stateLabel
        self.__machine = machine
        self.__next = self.__fail = None
        self.__comp = funcCompare
    
    def setNext(self, objNext):
        self.__next = objNext
    
    def setFail(self, objFail):
        self.__fail = objFail
    
    def next(self, value):
        result = self.__machine.calc(value)
        if self.__comp(result):
            return (self.__next, result)
        else:
            return (self.__fail, result)
