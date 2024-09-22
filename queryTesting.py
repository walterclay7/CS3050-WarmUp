import query

def simple_query_test():
    #author tests
    if(query.query_retrieve(['author'],['=='],['Homer']) == ['The Iliad', 'The Odyssey']):
        print("PASSED AUTHOR SIMPLE")
    else:
        print("FAILED AUTHOR SIMPLE")
    #genre tests
    if(query.query_retrieve(['genre'],['=='],['Southern Gothic']) == ['The Sound and the Fury']):
        print("PASSED GENRE SIMPLE")
    else:
        print("FAILED GENRE SIMPLE")
    #title tests
    if(query.query_retrieve(['title'],['=='],['The Hobbit']) == ['The Hobbit',1937,'J.R.R. Tolkien','Fantasy']):
        print("PASSED TITLE SIMPLE")
    else:
        print("FAILED TITLE SIMPLE") 
    #published_year tests
    if(query.query_retrieve(['published_year'],['<='],[0]) == ['The Iliad', 'The Odyssey']):
        print("PASSED PUBLISHED SIMPLE")
    else:
        print("FAILED PUBLISHED SIMPLE")
    #failed query
    if(query.query_retrieve(['author'],['=='],['triangle']) == []):
        print("PASSED WRONG SIMPLE")
    else:
        print("FAILED WRONG SIMPLE")
    
def all_query_test():
    #all authors
    if(len(query.query_retrieve(['author'],['=='],['ALL'])) == 26):
        print('PASSED ALL AUTHORS')
    else:
        print("FAILED ALL AUTHORS")
    #all genres 
    if(len(query.query_retrieve(['genre'],['=='],['ALL'])) == 15):
        print('PASSED ALL GENRES')
    else:
        print("FAILED ALL GENRES")
    #all titles 
    if(len(query.query_retrieve(['title'],['=='],['ALL'])) == 30):
        print("PASSED ALL TITLES")
    else:
        print("FAILED ALL TITLES")
    #all years 
    if(len(query.query_retrieve(['published_year'],['=='],['ALL'])) == 29):
        print("PASSED ALL PUBLISHED YEARS")
    else:
        print("FAILED ALL PUBLISHED YEARS")

def compound_simple():

    # Author first genre seconds
    if(query.query_retrieve(["author", "genre"],["==","=="],["J.R.R. Tolkien", "Fantasy"]) == ['The Hobbit', 'The Lord of the Rings']):
        print('PASSED AUTHOR, GENRE')
    else:
        print('FAILED AUTHOR,GENRE')

    # Author first year second
    if(query.query_retrieve(["author", "published_year"],["==","=="],["J.R.R. Tolkien", 1937]) == ['The Hobbit']):
        print('PASSED AUTHOR, YEAR')
    else:
        print('FAILED AUTHOR, YEAR')

    # Author first title second
    if(query.query_retrieve(["author", "title"],["==","=="],["J.R.R. Tolkien", "The Hobbit"]) == ['The Hobbit',1937,'J.R.R. Tolkien','Fantasy']):
        print('PASSED AUTHOR, TITLE')
    else:
        print('FAILED AUTHOR, TITLE')

    # Title first author second
    if(query.query_retrieve(["title", "author"],["==","=="],['The Hobbit', "J.R.R. Tolkien"]) == ['The Hobbit',1937,'J.R.R. Tolkien','Fantasy']):
        print('PASSED TITLE, AUTHOR')
    else:
        print('FAILED TITLE, AUTHOR')

    # Title first genre second
    if(query.query_retrieve(["title", "genre"],["==","=="],['The Hobbit', "Fantasy"]) == ['The Hobbit',1937,'J.R.R. Tolkien','Fantasy']):
        print('PASSED TITLE, GENRE')
    else:
        print('FAILED TITLE, GENRE')

    # Title first year second
    if(query.query_retrieve(["title", "published_year"],["==","=="],['The Hobbit', 1937]) == ['The Hobbit',1937,'J.R.R. Tolkien','Fantasy']):
        print('PASSED TITLE, YEAR')
    else:
        print('FAILED TITLE, YEAR')

    # Genre first author second
    if(query.query_retrieve(["genre", "author"],["==","=="],['Fantasy', 'J.R.R. Tolkien']) == ['The Hobbit', 'The Lord of the Rings']):
        print('PASSED GENRE, AUTHOR')
    else:
        print('FAILED GENRE, AUTHOR')

    # Genre first year second
    if(query.query_retrieve(["genre", "published_year"],["==","=="],['Fantasy', 1937]) == ['The Hobbit']):
        print('PASSED GENRE, YEAR')
    else:
        print('FAILED GENRE, YEAR')

    # Genre first title second
    if(query.query_retrieve(["genre", "title"],["==","=="],['Fantasy', 'The Hobbit']) == ['The Hobbit',1937,'J.R.R. Tolkien','Fantasy']):
        print('PASSED GENRE, TITLE')
    else:
        print('FAILED GENRE, TITLE')

    # Year first author second
    if(query.query_retrieve(["published_year", "author"],["==","=="],[1937, 'J.R.R. Tolkien']) == ['The Hobbit']):
        print('PASSED YEAR, AUTHOR')
    else:
        print('FAILED YEAR, AUTHOR')

    # Year first genre second
    if(query.query_retrieve(["published_year", "genre"],["==","=="],[1937, 'Fantasy']) == ['The Hobbit']):
        print('PASSED YEAR, GENRE')
    else:
        print('FAILED YEAR, GENRE')

    # Year first title second
    if(query.query_retrieve(["published_year", "title"],["==","=="],[1937, 'The Hobbit']) == ['The Hobbit',1937,'J.R.R. Tolkien','Fantasy']):
        print('PASSED YEAR, TITLE')
    else:
        print('FAILED YEAR, TITLE')


def compound_complex():

    # Year <= Author
    if(query.query_retrieve(["published_year", "author"],["<=","=="],[1940, 'J.R.R. Tolkien']) == ['The Hobbit']):
        print('PASSED YEAR <= AUTHOR')
    else:
        print('FAILED YEAR <= AUTHOR')

    # Year <= Title 
    if(query.query_retrieve(["published_year", "title"],["<=","=="],[1940, 'The Hobbit']) == ['The Hobbit',1937,'J.R.R. Tolkien','Fantasy']):
        print('PASSED YEAR <= TITLE')
    else:
        print('FAILED YEAR <= TITLE')

    # Year <= Genre
    if(query.query_retrieve(["published_year", "genre"],["<=","=="],[1940, 'Fantasy']) == ['The Hobbit']):
        print('PASSED YEAR <= AUTHOR')
    else:
        print('FAILED YEAR <= AUTHOR')

    # Year >= Author 
    if(query.query_retrieve(["published_year", "author"],[">=","=="],[1940, 'J.R.R. Tolkien']) == ['The Lord of the Rings']):
        print('PASSED YEAR >= AUTHOR')
    else:
        print('FAILED YEAR >= AUTHOR')

    # Year >= Title 
    if(query.query_retrieve(["published_year", "title"],[">=","=="],[1940, 'The Lord of the Rings']) == ['The Lord of the Rings',1954,'J.R.R. Tolkien','Fantasy']):
        print('PASSED YEAR >= TITLE')
    else:
        print('FAILED YEAR >= TITLE')

    # Year >= Genre
    if(query.query_retrieve(["published_year", "genre"],[">=","=="],[1940, 'Fantasy']) == ['The Lord of the Rings']):
        print('PASSED YEAR >= AUTHOR')
    else:
        print('FAILED YEAR >= AUTHOR')
    

    # Author <= 
    if(query.query_retrieve(['author', 'published_year'],["==","<="],['J.R.R. Tolkien', 1940]) == ['The Hobbit']):
        print('PASSED AUTHOR <= YEAR')
    else:
        print('AUTHOR YEAR <= YEAR')

    # Title <=
    if(query.query_retrieve(["published_year", "title"],["<=","=="],[1940, 'The Hobbit']) == ['The Hobbit',1937,'J.R.R. Tolkien','Fantasy']):
        print('PASSED TITLE <= YEAR')
    else:
        print('FAILED TITLE <= YEAR')

    # Genre <=
    if(query.query_retrieve(['genre', 'published_year'],["==","<="],['Fantasy', 1940]) == ['The Hobbit']):
        print('PASSED GENRE <= YEAR')
    else:
        print('AUTHOR GENRE <= YEAR')

    #############

    # Author >= 
    if(query.query_retrieve(['author', 'published_year'],["==",">="],['J.R.R. Tolkien', 1940]) == ['The Lord of the Rings']):
        print('PASSED AUTHOR >= YEAR')
    else:
        print('AUTHOR YEAR >= YEAR')

    # Title >=
    if(query.query_retrieve(["published_year", "title"],[">=","=="],[1940, 'The Lord of the Rings']) == ['The Lord of the Rings',1954,'J.R.R. Tolkien','Fantasy']):
        print('PASSED TITLE >= YEAR')
    else:
        print('FAILED TITLE >= YEAR')

    # Genre >=
    if(query.query_retrieve(['genre', 'published_year'],["==",">="],['Fantasy', 1940]) == ['The Lord of the Rings']):
        print('PASSED GENRE >= YEAR')
    else:
        print('AUTHOR GENRE >= YEAR')

    # No genre
    



    """Need to test year with greater than and less than also if the genre isnt present"""



simple_query_test()
all_query_test()
compound_simple()
compound_complex()
