import query

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
    if userIn[0] == '"':
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
    print('You can also combine two queries by putting \"and\" between them. This will return only'
          ' items that both queries would return.')
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

        if first_word == "TITLE":
            if len(query) >= 2 and query[1].upper() == "IS":
                return True, "TITLE"
            else:
                return False, "Invalid query structure for TITLE."
        
        elif first_word == "AUTHOR":
            if len(query) >= 2 and query[1].upper() == "IS":
                return True, "AUTHOR"
            else:
                return False, "Invalid query structure for AUTHOR."
        
        elif first_word == "GENRE":
            if len(query) >= 2 and query[1].upper() == "IS":
                return True, "GENRE"
            else:
                return False, "Invalid query structure for GENRE."
        
        elif first_word == "PUBLISHED":
            if len(query) >= 3 and query[1].upper() == "IN":
                return True, "IN"
            elif len(query) >= 3 and query[1].upper() == "BEFORE":
                return True, "BEFORE"
            elif len(query) >= 3 and query[1].upper() == "AFTER":
                return True, "AFTER"
            else:
                return False, "Invalid query structure for published date."
        
        elif first_word == "HELP":
            return True, "HELP"
        
        elif first_word == "QUIT":
            return True, "QUIT"
        
        else:
            return False, "Invalid keyword."

    # Validate the first part of the query
    valid_first, result_first = validate_single_query(first_query)
    
    # If compound query, validate the second part as well
    if compound:
        valid_second, result_second = validate_single_query(second_query)
        if valid_first and valid_second:
            # Return list of two types for compound query
            return True, [result_first, result_second]  
        elif not valid_first:
            return False, result_first
        else:
            return False, result_second
    else:
        # Return a list for single query
        return valid_first, [result_first] if valid_first else result_first  



# dataHandler will get the data and print it formatted
# userIn is an array containing 1 or 2 strings to match the query
# type is an array containing 1 or 2 strings that tell us what data to get and how to print it
# valid elements of type include "TITLE, AUTHOR, GENRE, AFTER, BEFORE, IN, HELP, QUIT"
# type is not case sensitive
# called by validate_single_queries
# returns 0 if everything went well, 1 if something went wrong.
def dataHandler(userIn, type):
    result = []

    type[0] = type[0].upper()

    # Ensure the parameters are the right length
    if len(userIn) > 2 or len(userIn) < 1 or len(userIn) != len(type):
        return 1
    # Check if compound or not
    compound = False
    if len(userIn) == 2:
        compound = True
        type[1] = type[1].upper()

    # /// Now we ask for the data \\\
    
    if compound:
        if type[0] == "IN" or type[0] == "BEFORE" or type[0] == "AFTER":
            keyword1 = "published_year"
            userIn[0] = int(userIn[0])
            if type[0] == "BEFORE":
                operator1 = "<="
            elif type[0] == "AFTER":
                operator1 = ">="
            else:
                operator1 = "=="
        else: 
            keyword1 = type[0].lower()
            operator1 = "=="

        if type[1] == "IN" or type[1] == "BEFORE" or type[1] == "AFTER":
            keyword2 = "published_year"
            userIn[1] = int(userIn[1])
            if type[1] == "BEFORE":
                operator2 = "<="
            elif type[1] == "AFTER":
                operator2 = ">="
            else:
                operator2 = "=="
        else: 
            keyword2 = type[1].lower()
            operator2 = "=="

        result = query.query_retrieve([keyword1, keyword2], [operator1, operator2], userIn)

    else: # Not compound
        if type[0] == "IN" or type[0] == "BEFORE" or type[0] == "AFTER":
            if type[0] == "BEFORE":
                operator1 = "<="
            elif type[0] == "AFTER":
                operator1 = ">="
            else:
                operator1 = "=="
            result = query.query_retrieve(["published"], [operator1], userIn)
        else:
            result = query.query_retrieve([type[0].lower()], ["=="], userIn)

    # /// Print the output for the user, cause they need that stuff \\\

    isSingleBook = False
    for val in result:
        if isinstance(val, int):
            isSingleBook = True

    # if isinstance(result[0], int):
    #     isSingleBook = True
    # if isinstance(result[0], str):
    #     if result[0].isnumeric():
    #         isSingleBook = True

    if compound:
        print("Here are the results:")
        if isSingleBook: # Checking whether the list is the info about a single book
            print("Title: " + result[0])
            print("Published: " + result[1])
            print("Author: " + result[2])
            if len(result) == 4:
                print("Genre: " + result[3])
            return 0
        else:
            printList(result)
            return 0
    
    if userIn == "ALL":
        if type[0] == "TITLE":
            print("All book titles:")
        elif type[0] == "AUTHOR":
            print("All authors on record:")
        elif type[0] == "GENRE":
            print("All genres on record:")
        printList(result)
        return 0

    if type[0] == "IN":
        print("Books published in " + userIn[0] + ":")
        printList(result)
        return 0
    elif type[0] == "BEFORE":
        print("Books published before " + userIn[0] + ":")
        printList(result)
        return 0
    elif type[0] == "AFTER":
        print("Books published after " + userIn[0] + ":")
        printList(result)
        return 0
    
    
    if isSingleBook: # Checking whether the list is the info about a single book
        print("Title: " + result[0])
        print("Published: " + str(result[1]))
        print("Author: " + result[2])
        if len(result) == 4:
            print("Genre: " + result[3])
        return 0

    if type[0] == "TITLE":
        print("All books where title includes: " + userIn[0] + ":")
    elif type[0] == "AUTHOR":
        print("All books where author's name includes: " + userIn[0] + ":")
    elif type[0] == "GENRE":
        print("All books where genre includes: " + userIn[0] + ":")
    printList(result)
    return 0
        

    
# prints all items in a list, one item per line, with a small indent.
# returns 0.
def printList(list):
    for i in list:
        print("   " + i)
    return 0

def main():
    print("Welcome. type \"Help\" for help")
    run = True
    while(run):
        print("[]? ", end='')
        userIn = input()
        token = tokenize(userIn)
        valid, result = validate_query(token)

        if "HELP" in result:
            printHelp()
        if "QUIT" in result:
            return 0
        if valid:
            if len(token) > 3: # Compound query
                dataHandler([token[2], token[-1]], result)
            else:
                dataHandler([token[-1]], result)
    return 0

main()