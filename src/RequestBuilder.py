'''
Created on Oct 30, 2014

@author: i51434
'''
import sys, requests, urllib

def main(argv):
    searchField = 'at New York Knicks Tickets'
    url = 'http://www.stubhub.com/listingCatalog/select/?q='
    
    encodedField = urllib.quote_plus(searchField)
    
    request = (url+
               '%252BstubhubDocumentType%253Aevent%250D%250A%252B'
               '%2Bleaf%253A%2Btrue%250D%250A%252B'
               '%2Bdescription%253A%2B%22'
               +searchField+
               '%22%250D%250A%252B' 
               '%3B$sort_what%20$sort_how' 
               '&version=2.2' 
               '&start=0' 
               '&indent=on' 
               '&wt=json' 
               '&fl=description+event_date+event_date_local+event_time_local+geography_parent+venue_name+city+state+genreUrlPath+urlpath+leaf+channel'
               )

    print(request)

if __name__ == '__main__':
    main(sys.argv)

