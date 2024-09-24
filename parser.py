# userIn is the string to be tokenized
# returns a list of strings, which are the tokens
# tokens are separated by spaces, but not spaces that are inside double quotes
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

# Prints the help menu.
# Returns 0.
def printHelp():
    print('help: returns this menu.')
    print('title is "text": returns a list of all book titles where the title includes'
          ' the text between the quotation marks.'
          '\nIn the case of an exact match, instead returns all information on record'
          ' about the book.')
    print('author is "text": returns a list of all book titles where the author\'s'
          ' name includes the text between the quotation marks.')
    print('genre is "text": returns a list of all book titles where the genre on'
          ' record includes the text between the quotation marks.')
    print('published in/before/after year: returns a list of all books published'
          ' before, after, or on the specified integer year. Use negative numbers'
          ' for years BCE.')
    print('all titles/authors/genres: returns a list of all titles, authors, or'
          ' genres on file')
    print('quit: exit the program')
    return 0


def validate_query(input_list):
    if not input_list or not isinstance(input_list, list):
        return False, "Invalid input."

    type = ""
    compound = False
    
    # Check for compound query
    if "AND" in [word.upper() for word in input_list]:
        compound = True

    first_word = input_list[0].upper()

    if first_word == "TITLE" or first_word == "AUTHOR" or first_word == "GENRE":
        if len(input_list) >= 2 and input_list[1].upper() == "IS":
            type = first_word.capitalize()
        else:
            return False, "Invalid query structure for title/author/genre."
    
    elif first_word == "PUBLISHED":
        if len(input_list) >= 3 and input_list[1].upper() in ["IN", "BEFORE", "AFTER"]:
            type = "Year"
        else:
            return False, "Invalid query structure for published date."
    
    elif first_word == "ALL":
        if len(input_list) >= 2 and input_list[1].upper() in ["TITLES", "AUTHORS", "GENRES"]:
            type = f"All_{input_list[1].capitalize()}"
        else:
            return False, "Invalid 'all' query."

    elif first_word == "HELP":
        type = "Help"

    elif first_word == "QUIT":
        type = "Quit"
    
    else:
        return False, "Invalid keyword."

    return True, f"Valid {type} query{' with compound' if compound else ''}."


def main():

    print(tokenize('The quick brown fox "Jumped over" the dazy log'))
    return 0

main()

