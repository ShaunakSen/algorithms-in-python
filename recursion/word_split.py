def word_split(phrase, list_of_words, output=None):
    if output is None:
        output = []

    if phrase in list_of_words:
        print "Phrase:", phrase, "found in:", list_of_words
        output.append(phrase)
        print "Final List: ", output
    else:
        for i in range(len(phrase)):
            if phrase[:i] in list_of_words:
                print phrase[:i], "found"
                output.append(phrase[:i])
                list_of_words.remove(phrase[:i])
                print "New List:", list_of_words
                print "Phrase remaining:", phrase[i:]
                return word_split(phrase[i:], list_of_words, output)
        print []
        return []


word_split('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John'])
word_split('themanran', ['the', 'ran', 'man'])
word_split('themanran', ['clown', 'ran', 'man'])
