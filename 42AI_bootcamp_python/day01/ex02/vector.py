
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
            if len(elem) != 2:
                print("input in (int, int) format.")
                return None
            for i in elem:
                if not isinstance(i, int):
                    print("input in (int, int) format.")
                    return None
            self.values = list()
            for i in range(elem[0], elem[1]):
                self.values.append(float(i))
        self.size = len(self.values)


    def __str__(self):
        return "(Vector " + repr(self.values) + ")"

    def __repr__(self):
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

    def __truediv__(self, operand):
        result = list()
        if isinstance(operand, int) or isinstance(operand, float):
            for i in self.values:
                result.append(i / operand)
            return Vector(result)
        else:
            print("Can't divide with Vector with Vector.")
            return 0
    
    def __rtruediv__(self, operand):
        return self / operand

    def __mul__(self, operand):
        if isinstance(operand, int) or isinstance(operand, float):
            result = list()
            for i in self.values:
                result.append(i * operand)
            return Vector(result)
        elif isinstance(operand, Vector):
            if len(operand.values) != self.size:
                print("Can't execute dot product between these two vectors.")
                return 0
            else:
                result = 0
                for i, data in enumerate(self.values):
                    result += self.values[i] * operand.values[i]
                return result

    def __rmul__(self, operand):
        return self * operand

