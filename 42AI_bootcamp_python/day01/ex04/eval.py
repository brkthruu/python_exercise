class Evaluator:
    @staticmethod
    def val_check(coefs, words):
        if len(coefs) != len(words):
            print('The length of coefs and words should be the same.')
            return 1
        else:
            return 0

    @staticmethod
    def zip_evaluate(coefs, words):
        if Evaluator.val_check(coefs, words) == 1:
            return -1
        result = 0
        for c, w in zip(coefs, words):
            result += c * len(w)
        return result

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if Evaluator.val_check(coefs, words) == 1:
            return -1
        result = 0
        for i, c in enumerate(coefs):
            result += c * len(words[i])
        return result
