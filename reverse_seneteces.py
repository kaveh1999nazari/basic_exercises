sentence = input('Enter your sentence = ')
def Reverse(sentence):
    make_lst = sentence.split()
    y = list(map(lambda x : ''.join(x[::-1]),make_lst))
    reverse = ''.join(i + " " for i in y )
    return reverse
print(Reverse(sentence))