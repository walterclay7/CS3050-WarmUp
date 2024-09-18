import query

def simple_query_test():
    #author tests
    if(query.queryRetieve(['author'],['=='],['homer']) == ['The Iliad', 'The Odyssey']):
        print("PASSED AUTHOR SIMPLE")
    else:
        print("FAILED AUTHOR SIMPLE")
    #genre tests
    if(query.queryRetieve(['genre'],['=='],['Southern Gothic']) == ['The Sound and the Fury']):
        print("PASSED GENRE SIMPLE")
    else:
        print("FAILED GENRE SIMPLE")
    #title tests
    if(query.queryRetieve(['title'],['=='],['the hobbit']) == ['J.R.R. Tolkien','Fantasy',1937,'The Hobbit']):
        print("PASSED TITLE SIMPLE")
    else:
        print("FAILED TITLE SIMPLE") 
    #published_year tests
    if(query.queryRetieve(['published_year'],['<='],[0]) == ['The Iliad', 'The Odyssey']):
        print("PASSED PUBLISHED SIMPLE")
    else:
        print("FAILED PUBLISHED SIMPLE")
    #failed query
    if(query.queryRetieve(['author'],['=='],['triangle']) == []):
        print("PASSED WRONG SIMPLE")
    else:
        print("FAILED WRONG SIMPLE")
    
def all_query_test():
    #all authors
    if(len(query.query_retrieve(['author'],['=='],['ALL'])) == 26):
        print('PASSED ALL AUTHORS')
    else:
        print("FAILED ALL AUTHORS")
    #all genres TODO
    if(len(query.query_retrieve(['genre'],['=='],['ALL'])) == 27):
        print('PASSED ALL GENRES')
    else:
        print("FAILED ALL GENRES")
    #all titles TODO
    if(len(query.query_retrieve(['title'],['=='],['ALL'])) == 27):
        print("PASSED ALL TITLES")
    else:
        print("FAILED ALL TITLES")
    #all years TODO
    if(len(query.query_retrieve(['pubslished_year'],['=='],['ALL'])) == 27):
        print("PASSED ALL PUBLISHED YEARS")
    else:
        print("FAILED ALL PUBLISHED YEARS")