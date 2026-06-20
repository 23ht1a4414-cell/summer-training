class EmptySentenceError(Exception):
    pass

class InvalidSentenceError(Exception):
    pass

class SentenceTooLongError(Exception):
    pass


class SentenceAnalyzer:
    def analyze(self, sentence):
        if len(sentence.strip()) == 0:
            raise EmptySentenceError("EmptySentenceError")

        if len(sentence) > 100:
            raise SentenceTooLongError("SentenceTooLongError")

        if sentence.strip().isdigit():
            raise InvalidSentenceError("InvalidSentenceError")

        vowels = sum(1 for ch in sentence if ch.lower() in "aeiou")
        words = len(sentence.split())
        uppercase = sum(1 for ch in sentence if ch.isupper())

        print("Vowel count:", vowels)
        print("Word count:", words)
        print("Uppercase count:", uppercase)


sentence = input()

analyzer = SentenceAnalyzer()

try:
    analyzer.analyze(sentence)
except Exception as e:
    print(e) 