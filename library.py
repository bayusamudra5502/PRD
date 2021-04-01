# Pustaka StateMachine
# Oleh Bayu Samudra - 16520420

class StateMachine(object):
    def __init__(self, stateName) -> None:
        super().__init__()
        self.stateName = stateName
        self.lastObject = None
    
    def setLastObject(self,object):
        self.lastObject = object
    
    def evaluate(self, value):
        return self.lastObject.evaluate(value)

class Input(StateMachine):
    def __init__(self, stateName) -> None:
        super().__init__(stateName)
        self.value = None
    
    def evaluate(self, value):
        return value

class Delay(StateMachine):
    def __init__(self, initValue, stateName) -> None:
        super().__init__(stateName)
        self.value = initValue
    
    def evaluate(self, value):
        delayedValue = self.value
        self.value = self.lastObject.evaluate(value)

        return delayedValue

class Cascade(StateMachine):
    def __init__(self, stateName) -> None:
        super().__init__(stateName)
        self.feedbackCasecade = []
        self.topSM = None
    
    def setTopSM(self, SM:StateMachine):
        self.topSM = SM

    def evaluate(self, value):
        result = self.topSM.evaluate(value)
        for i in self.feedbackCasecade:
            i.setFeedbackVal(result)
        
        return result
    
    def getTopSM(self):
        return self.topSM
    
    def appendFeedback(self, *cascade):
        for i in cascade:
            self.feedbackCasecade.append(i)
    
class FeedbackCascade(Cascade):
    def __init__(self, defaultValue, stateName) -> None:
        super().__init__(stateName)
        self.value = defaultValue
    
    def setFeedbackVal(self, value):
        self.value = value
    
    def evaluate(self, value):
        return super().evaluate(self.value)

class Gain(StateMachine):
    def __init__(self, gainValue, stateName) -> None:
        super().__init__(stateName)
        self.gainValue = gainValue
    
    def evaluate(self, value):
        return self.gainValue * self.lastObject.evaluate(value)

class Transduser(object):
    def __init__(self, mainCascade:Cascade) -> None:
        super().__init__()
        self.mainCascade = mainCascade
    
    def run(self, inputs):
        result = []

        for i in inputs:
            result.append(self.mainCascade.evaluate(i))
        
        return result

class Parallel(StateMachine):
    def __init__(self, funcOperator, stateName) -> None:
        super().__init__(stateName)
        self.funcOperator = funcOperator
        self.lastObject = []
    
    def appendLast(self, *SM:StateMachine):
        for i in SM:
            self.lastObject.append(i)
    
    def evaluate(self, value):
        result = None
        for i in self.lastObject:
            result = self.funcOperator(result, i.evaluate(value))
        
        return result

class Constant(StateMachine):
    def __init__(self, constant, stateName) -> None:
        super().__init__(stateName)
        self.const = constant
    
    def evaluate(self, value):
        return self.const