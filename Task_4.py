sentece = input("Enter a sentence:")
word = sentece.split()
freq = {}
for word in word :
        if word in freq :
             freq[word]+= 1
        else:
            freq[word]= 1
            print(freq)
    