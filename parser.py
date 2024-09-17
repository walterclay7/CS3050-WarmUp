
#userIn is the string to be tokenized
#returns a list of strings, which are the tokens
#tokens are separated by spaces, but not spaces that are inside double quotes
def tokenize(userIn):
    startsWithDoubleQuote = False
    intermediate = []
    output = []

    userIn.strip()
    #If the string is empty, return a list with an empty string
    if len(userIn) == 0:
        output.append("")
        return output
    #Track whether the string starts with a "
    if userIn[1] == '"':
        startsWithDoubleQuote = True
    
    #Separate by "
    intermediate = userIn.split('"')

    #Iterate through these strings in order to separate the ones that weren't in double quotes by spaces
    i = 0
    while i < len(intermediate):
        #If we started with a ", every odd string is not in double quotes
        if startsWithDoubleQuote:
            if i % 2 != 0:                              #Odd string
                intermediate[i].split()                 #Not in "", split it
                j = 0
                while j < len(intermediate[i]):
                    output.append(intermediate[i][j])
                    j += 1
            else:
                output.append(intermediate[i])          #In "", add it whole
        #Otherwise, every even string
        else:
            if i % 2 == 0:                              #Even string
                print(intermediate)
                intermediate[i].split()                 #Not in "", split it
                print(intermediate)
                j = 0
                while j < len(intermediate[i]):
                    output.append(intermediate[i][j])
                    j += 1
            else:
                output.append(intermediate[i])          #In "", add it whole
        i += 1
    
    return output


def main():

    print(tokenize('The quick brown fox "Jumped over" the dazy log'))
    return 0

main()