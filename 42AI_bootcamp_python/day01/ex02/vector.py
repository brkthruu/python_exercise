import sys

class Vector:
    def __init__(self, elem):
        if type(elem) == list:
            for i in elem:
                if not isinstance(i, float):
                    print("Use float data.")
                    return None
            self.values = elem
        elif type(elem) == int:
            self.values = list()
            for i in range(elem):
                self.values.append(float(i))
        elif type(elem) == tuple:
            for i in elem:
                if not isinstance(i, int):
                    print("input in (int, int) format.")
                    return None
            self.values = list(range(elem[0], elem[1]))
        self.size = len(self.values)

    def __str__(self):
        output = ""
        return "(Vector " + repr(self.values) + ")"


    def __add__(self, operand):
        result = list()
        if isinstance(operand, int) or isinstance(operand, float):
            for i in self.values:
                result.append(i + operand)
            return Vector(result)
        elif isinstance(operand, Vector):
            if len(operand.values) != self.size:
                print("Can't add these two vectors.")
                return 0
            else:
                for i, data in enumerate(self.values):
                    result.append(self.values[i] + operand.values[i])
                return Vector(result)
    
    def __radd__(self, operand):
        return self + operand

    def __sub__(self, operand):
        result = list() 
        if isinstance(operand, int) or isinstance(operand, float):
            for i in self.values:
                result.append(i - operand)
            return Vector(result)
        elif isinstance(operand, Vector):
            if len(operand.values) != self.size:
                print("Can't subtract these two vectors.")
                return 0
            else:
                for i, data in enumerate(self.values):
                    result.append(self.values[i] - operand.values[i])
                return Vector(result)

    def __rsub__(self, operand):
        return self - operand


