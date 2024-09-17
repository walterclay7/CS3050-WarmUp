
#userIn is the string to be tokenized
#returns a list of strings, which are the tokens
#tokens are separated by spaces, but not spaces that are inside double quotes
def tokenize(userIn):
    startsWithDoubleQuote = False
    intermediate = []
    output = []

    userIn = userIn.strip()
    #If the string is empty, return a list with an empty string
    if len(userIn) == 0:
        return output
    #Track whether the string starts with a "
    if userIn[1] == '"':
        startsWithDoubleQuote = True
    
    #Separate by "
    intermediate = userIn.split('"')

    # Iterate through the strings to separate those not in double quotes by spaces
    for i in range(len(intermediate)):
        # For the parts not in quotes
        if i % 2 == 0:
            # Split and extend the output with the split tokens
            output.extend(intermediate[i].split())
        else:
            # For parts in quotes, append the whole part
            output.append(intermediate[i])

    return output


def main():

    print(tokenize('The quick brown fox "Jumped over" the dazy log'))
    return 0

main()

