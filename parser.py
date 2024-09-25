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

    compound = False
    first_query = []
    second_query = []
    
    # Convert input list to uppercase for keyword checking
    input_upper = [word.upper() for word in input_list]
    
    # Check if AND is part of the input for compound queries
    if "AND" in input_upper:
        compound = True
        and_index = input_upper.index("AND")
        first_query = input_list[:and_index]
        second_query = input_list[and_index + 1:]
    else:
        first_query = input_list

    # Helper function to validate single queries
    def validate_single_query(query):
        if len(query) == 0:
            return False, "Empty query."

        first_word = query[0].upper()

        if first_word == "TITLE" or first_word == "AUTHOR" or first_word == "GENRE":
            if len(query) >= 2 and query[1].upper() == "IS":
                return True, first_word.capitalize()
            else:
                return False, f"Invalid query structure for {first_word.lower()}."
        
        elif first_word == "PUBLISHED":
            if len(query) >= 3 and query[1].upper() in ["IN", "BEFORE", "AFTER"]:
                return True, f"Published {query[1].capitalize()}"
            else:
                return False, "Invalid query structure for published date."
        
        elif first_word == "ALL":
            if len(query) >= 2 and query[1].upper() in ["TITLES", "AUTHORS", "GENRES"]:
                return True, f"All_{query[1].capitalize()}"
            else:
                return False, "Invalid 'all' query."
        
        elif first_word == "HELP":
            return True, "Help"
        
        elif first_word == "QUIT":
            return True, "Quit"
        
        else:
            return False, "Invalid keyword."

    # Validate the first part of the query
    valid_first, result_first = validate_single_query(first_query)
    
    # If compound query, validate the second part as well
    if compound:
        valid_second, result_second = validate_single_query(second_query)
        if valid_first and valid_second:
            return True, f"Valid compound query: [{result_first}] AND [{result_second}]"
        elif not valid_first:
            return False, result_first
        else:
            return False, result_second
    else:
        return valid_first, result_first


def main():

    print(tokenize('The quick brown fox "Jumped over" the dazy log'))
    return 0

main()

