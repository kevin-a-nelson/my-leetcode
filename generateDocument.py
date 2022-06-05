from pydoc import doc


def getCharOccurences(str):

    charOccurences = {}
    for char in str:
        if char in charOccurences:
            charOccurences[char] += 1
        else:
            charOccurences[char] = 1

    return charOccurences


def generateDocument(characters, document):

    charactersOccurence = getCharOccurences(characters)
    documentOccurence = getCharOccurences(document)

    for char in document:
        if char not in charactersOccurence:
            return False
        if documentOccurence[char] <= charactersOccurence[char]:
            return False

    return True


characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"

print(generateDocument(characters, document))
