class ReverseWords:
    def __init__(self, sentence):
        self.sentence = sentence
    def reverse(self):
        words = self.sentence.split(' ')
        reversed_words = words[::-1]
        reversed_sentence = ' '.join(reversed_words)
        return reversed_sentence
rev = ReverseWords("this is nagarjuna")
print(rev.reverse()) #