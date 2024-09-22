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

def compound_query_test():
    # Author first genre seconds

    # Author first year second

    # Author first title second

    # Title first author second

    # Title first genre second

    # Title first genre second

    # 




    pass


simple_query_test()
all_query_test()
