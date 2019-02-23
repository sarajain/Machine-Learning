import csv

#filename = 'azj-train.txt'

filename = 'input.csv'

# key = "yigilmis,3"
# value = "yig^ilmis"
# hash($key) = $value
#
# Algorithm:
# Convert all diecritic words into norrmal English words
# Next find most frequently used word for each English word
#   E.g. finalHash(yiglimis) = "yig^ilmis" ;# chose/save one with 3-frequency
# Then open input.csv
# For every word in input.csv
#   If the word is in finalHash container
#     Replace current word with the value of this container and write it out
#   Else
#     Just write out the word read as-as from input.csv

def convertIntoEnglish(diacriticWord):

    #print "before eachLine: ",eachLine
    eachLine = diacriticWord;

    eachLine = eachLine.replace('\xc9\x99','e')
    eachLine = eachLine.replace('\xc5\x9f','s')
    eachLine = eachLine.replace('\xc3\xa7','c')
    eachLine = eachLine.replace('\xc4\xb1','i')
    eachLine = eachLine.replace('\xc4\x9f','g')
    eachLine = eachLine.replace('\xc3\xbc','u')
    eachLine = eachLine.replace('\xc3\xb6','o')

    # Now handle uppcases
    eachLine = eachLine.replace('\xc6\x8f','E')
    eachLine = eachLine.replace('\xc5\x9e','S')
    eachLine = eachLine.replace('\xd2\xaa','C')
    eachLine = eachLine.replace('\xc4\xb0','I')
    eachLine = eachLine.replace('\xc4\xa2','G')
    eachLine = eachLine.replace('\xc3\x9c','U')
    eachLine = eachLine.replace('\xc3\x96','O')
        
    #print "after eachLine: ",eachLine    

    return eachLine


with open(filename) as f:
    data = f.readlines()
    #print 'data ', data

    wfd = open("training_data_output.txt", "w")

    hash_collection = {}

    # initialize the frquency container; calculate real frequencies in another loop

    for n, line in enumerate(data):
        eachLine = data[n]
        hash_collection[eachLine] = 0

    # calculate frequency of each diacritic-word in book as they appear

    for n, line in enumerate(data):
        eachLine = data[n]
        hash_collection[eachLine] += 1
        #updatedLine = convertIntoEnglish(eachLine)

    # initialize English->freq# hash-container with no items in them yet

    english_to_frequency = {}

    # English->Diacritic

    english_to_diacritic = {}

    # first initialize english_to_frequency[] such that every diacritic word has 0-frquency

    for diacriticWord, frequency in hash_collection.items():
        #wfd.write(diacriticWord + " " + str(frequency) + "\n")
        #wfd.write(diacriticWord)
        #wfd.write("\n")
        #wfd.write(str(frequency))
        #wfd.write("\n")
        #wfd.write(updatedLine)

        english = convertIntoEnglish(diacriticWord)
        english_to_frequency[english] = 0

    # find highest frequencyy diacritic word in english_to_frequency[] (english_to_frequency[english]->freq#, english_to_diacritic[english]->diacritic):

    # For each diacritic-word in hash_collection[] above
    #   if current word hasn't been recorded in english_to_frequency[]
    #     Save current word it english_to_frequency[] along with its frequency
    #   else if current wod's frequency is higher than previously recorded (i.e. have same English translation) in english_to_frequency[]
    #     Overwrite older one with newer diacritic word in english_to_frequency[]

    for diacriticWord, frequency in hash_collection.items():
        english = convertIntoEnglish(diacriticWord)
        if english_to_frequency[english] == 0:
            english_to_frequency[english] = frequency
            english_to_diacritic[english] = diacriticWord

        else:
            if english_to_frequency[english] < frequency:
                english_to_frequency[english] = frequency
                english_to_diacritic[english] = diacriticWord

    # use the new diacritic word for the file wherever it is found

    for n, line in enumerate(data):
        eachLine = data[n]
        english = convertIntoEnglish(eachLine)
        diacriticWord = english_to_diacritic[english]
        wfd.write(diacriticWord)
        #wfd.write("\n")

    wfd.close()
f.close()





