#! /usr/bin/python
import json
import os
import time

outputpath = 'output/'
# Load JSON object
with open('srob-firebase.json') as json_data:
    j = json.load(json_data)
    # Look for the node title "data"
    data = j['data']


def sanitizestring( string ):
    bug = string.replace(' ', '-').replace('.','').replace(':','').replace('\'','').replace('/','--').replace(',','').replace('\"','').replace('#','').replace('?','').lower()
    return bug

# A function to find linked titles and return their real names for better linking
def findstring( string ):
    breakup = string.split()
    # Looksup the correct node, returns it as a formatted string, with the folder and filename   
    return breakup[0] + "/" + sanitizestring(j['data'][breakup[0]][breakup[1]]['name']) + ".md"

# Select child
for key in j['data']:
    print("---------- working with key '%s'--------" % key)

    # Let's start with the single items
    if key == 'about':
        # create folder with item name
        if not os.path.exists('output/about'):
            os.makedirs('output/about')

        # create file and structure
        markdown = open('output/about/_index.md', 'w')
        markdown.write('+++\n')
        # # STANDARD DATA BLOCK ##j['data'][breakup[0]][breakup[1]]['name']
        markdown.write('sort_create_date = %d\n' % j['data']['about']['_sort_create_date'])
        markdown.write('sort_last_updated = %d\n' % j['data']['about']['_sort_last_updated'])
        try:
            markdown.write('sort_publish_date = %d\n' % j['data']['about']['_sort_publish_date']) 
        except KeyError:
            markdown.write('sort_publish_date = ""\n')
        markdown.write('create_date = %s\n' % (json.dumps(j['data']['about']['create_date']).encode('utf-8')))
        try:
            markdown.write('publish_date = %d\n' % j['data']['about']['_sort_publish_date']) 
        except KeyError:
            markdown.write('publish_date = ""\n')
        try:
            markdown.write('date = %d\n' % j['data']['about']['_sort_publish_date']) 
        except KeyError:
            markdown.write('date = %s\n' % (json.dumps(j['data']['about']['create_date']).encode('utf-8')))                 
        markdown.write('last_updated = %s\n' % (json.dumps(j['data']['about']['last_updated']).encode('utf-8')))
        try:
            markdown.write('preview_url = %s\n' % (json.dumps(j['data']['about']['preview_url']).encode('utf-8')))
        except KeyError:
            markdown.write('preview_url = ""\n')
        # # END STANDARD DATA BLOCK ##        
        markdown.write('name = %s\n' % (json.dumps(j['data']['about']['name']).encode('utf-8')))
        markdown.write('title = %s\n' % (json.dumps(j['data']['about']['name']).encode('utf-8')))
        markdown.write('+++\n\n')
        markdown.write((j['data']['about']['markdown_text']).encode('utf-8'))
        markdown.close()

    elif key == 'privacy':
        # create folder with item name
        if not os.path.exists('output/privacy'):
            os.makedirs('output/privacy')

        # create file and structure
        markdown = open('output/privacy/_index.md','w')
        markdown.write('+++\n')
        # STANDARD DATA BLOCK # #
        markdown.write('sort_create_date = %d\n' % j['data']['privacy']['_sort_create_date'])
        markdown.write('sort_last_updated = %d\n' % j['data']['privacy']['_sort_last_updated'])
        try:
          markdown.write('sort_publish_date = %d\n' % j['data']['privacy']['_sort_publish_date']) 
        except KeyError:
          markdown.write('sort_publish_date = ""\n')
        markdown.write('create_date = %s\n' % (json.dumps(j['data']['privacy']['create_date']).encode('utf-8')))
        try:
          markdown.write('publish_date = %d\n' % j['data']['privacy']['_sort_publish_date']) 
        except KeyError:
          markdown.write('publish_date = %d\n' % j['data']['privacy']['_sort_create_date'])
        try:
          markdown.write('date = %d\n' % j['data']['privacy']['_sort_publish_date']) 
        except KeyError:
          markdown.write('date = %s\n' % (json.dumps(j['data']['privacy']['create_date']).encode('utf-8')))          
        markdown.write('last_updated = %s\n' % (json.dumps(j['data']['privacy']['last_updated']).encode('utf-8')))
        try:
          markdown.write('preview_url = %s\n' % (json.dumps(j['data']['privacy']['preview_url']).encode('utf-8')))
        except KeyError:
          markdown.write('preview_url = ""\n')
        ## END STANDARD DATA BLOCK ##          
        markdown.write('name = %s\n' % (json.dumps(j['data']['privacy']['name']).encode('utf-8')))
        markdown.write('title = %s\n' % (json.dumps(j['data']['privacy']['name']).encode('utf-8')))
        markdown.write('+++\n\n')
        markdown.write((j['data']['privacy']['markdown_text']).encode('utf-8'))
        markdown.close()

    elif key == 'resources':
        if not os.path.exists('output/resources'):
            os.makedirs('output/resources')

        # create file and structure
        markdown = open('output/resources/_index.md','w')
        markdown.write('+++\n')
        ## STANDARD DATA BLOCK ##        
        markdown.write('sort_create_date = %d\n' % j['data']['resources']['_sort_create_date'])
        markdown.write('sort_last_updated = %d\n' % j['data']['resources']['_sort_last_updated'])
        try:
          markdown.write('sort_publish_date = %d\n' % j['data']['resources']['_sort_publish_date']) 
        except KeyError:
          markdown.write('sort_publish_date = ""\n')
        markdown.write('create_date = %s\n' % (json.dumps(j['data']['resources']['create_date']).encode('utf-8')))
        try:
          markdown.write('publish_date = %d\n' % j['data']['resources']['_sort_publish_date']) 
        except KeyError:   
          markdown.write('publish_date = %d\n' % j['data']['resources']['_sort_create_date'])
        try:
          markdown.write('date = %d\n' % j['data']['resources']['_sort_publish_date']) 
        except KeyError:   
          markdown.write('date = %s\n' % (json.dumps(j['data']['resources']['create_date']).encode('utf-8')))               
        markdown.write('last_updated = %s\n' % (json.dumps(j['data']['resources']['last_updated']).encode('utf-8')))
        try:
          markdown.write('preview_url = %s\n' % (json.dumps(j['data']['resources']['preview_url']).encode('utf-8')))
        except KeyError:
          markdown.write('preview_url = ""\n')
        ## END STANDARD DATA BLOCK ##   
        markdown.write('name = %s\n' % (json.dumps(j['data']['resources']['name']).encode('utf-8')))
        markdown.write('title = %s\n' % (json.dumps(j['data']['resources']['name']).encode('utf-8')))
        markdown.write('+++\n\n')
        markdown.write((j['data']['resources']['markdown_text']).encode('utf-8'))
        markdown.close()

    elif key == 'submissions':
        if not os.path.exists('output/submissions'):
            os.makedirs('output/submissions')

        # create file and structure
        markdown = open('output/submissions/_index.md', 'w')
        markdown.write('+++\n')
        ## STANDARD DATA BLOCK ##        
        markdown.write('sort_create_date = %d\n' % j['data']['submissions']['_sort_create_date'])
        markdown.write('sort_last_updated = %d\n' % j['data']['submissions']['_sort_last_updated'])
        try:
          markdown.write('sort_publish_date = %d\n' % j['data']['submissions']['_sort_publish_date']) 
        except KeyError:
          markdown.write('sort_publish_date = ""\n')
        markdown.write('create_date = %s\n' % (json.dumps(j['data']['submissions']['create_date']).encode('utf-8')))
        try:
          markdown.write('publish_date = %d\n' % j['data']['submissions']['_sort_publish_date']) 
        except KeyError:   
          markdown.write('publish_date = %d\n' % j['data']['submissions']['_sort_create_date'])
        try:
          markdown.write('date = %d\n' % j['data']['submissions']['_sort_publish_date']) 
        except KeyError:   
          markdown.write('date = %s\n' % (json.dumps(j['data']['submissions']['create_date']).encode('utf-8')))              
        markdown.write('last_updated = %s\n' % (json.dumps(j['data']['submissions']['last_updated']).encode('utf-8')))
        try:
          markdown.write('preview_url = %s\n' % (json.dumps(j['data']['submissions']['preview_url']).encode('utf-8')))
        except KeyError:
          markdown.write('preview_url = ""\n')
        ## END STANDARD DATA BLOCK ##   
        markdown.write('name = %s\n' % (json.dumps(j['data']['submissions']['name']).encode('utf-8')))
        markdown.write('title = %s\n' % (json.dumps(j['data']['submissions']['name']).encode('utf-8')))
        markdown.write('+++\n\n')
        markdown.write((j['data']['submissions']['markdown_text']).encode('utf-8'))
        markdown.close()

    elif key == 'sponsor':
        if not os.path.exists('output/sponsor'):
            os.makedirs('output/sponsor')

        # create file and structure
        markdown = open('output/sponsor/_index.md', 'w')
        markdown.write('+++\n')
        ## STANDARD DATA BLOCK ##        
        markdown.write('sort_create_date = %d\n' % j['data']['sponsor']['_sort_create_date'])
        markdown.write('sort_last_updated = %d\n' % j['data']['sponsor']['_sort_last_updated'])
        try:
          markdown.write('sort_publish_date = %d\n' % j['data']['sponsor']['_sort_publish_date']) 
        except KeyError:
          markdown.write('sort_publish_date = ""\n')
        markdown.write('create_date = %s\n' % (json.dumps(j['data']['sponsor']['create_date']).encode('utf-8')))
        try:
          markdown.write('publish_date = %d\n' % j['data']['sponsor']['_sort_publish_date']) 
        except KeyError:   
          markdown.write('publish_date = %d\n' % j['data']['sponsor']['_sort_create_date'])
        try:
          markdown.write('date = %d\n' % j['data']['sponsor']['_sort_publish_date']) 
        except KeyError:   
          markdown.write('date = %s\n' % (json.dumps(j['data']['sponsor']['create_date']).encode('utf-8')))               
        markdown.write('last_updated = %s\n' % (json.dumps(j['data']['sponsor']['last_updated']).encode('utf-8')))
        try:
          markdown.write('preview_url = %s\n' % (json.dumps(j['data']['sponsor']['preview_url']).encode('utf-8')))
        except KeyError:
          markdown.write('preview_url = ""\n')
        ## END STANDARD DATA BLOCK ##   
        markdown.write('name = %s\n' % (json.dumps(j['data']['sponsor']['name']).encode('utf-8')))
        markdown.write('title = %s\n' % (json.dumps(j['data']['sponsor']['name']).encode('utf-8')))
        markdown.write('+++\n\n')
        markdown.write((j['data']['sponsor']['markdown_text']).encode('utf-8'))
        markdown.close()

    # AUTHORS/WRITERS/TRANSLATORS AREA

    elif key == 'authors' or key == 'writers' or key == 'translators':
        if not os.path.exists('output/writers'):
            os.makedirs('output/writers')

        for author in j['data']['authors']:  
            lc_name = sanitizestring(j['data']['authors'][author]['name'])            
            markdown = open('output/writers/' + lc_name + '.md','w')
            markdown.write('+++\n')
            markdown.write('index = %s\n' % json.dumps(author.encode('utf-8')))
            ## STANDARD DATA BLOCK ##        
            markdown.write('sort_create_date = %d\n' % j['data']['authors'][author]['_sort_create_date'])
            markdown.write('sort_last_updated = %d\n' % j['data']['authors'][author]['_sort_last_updated'])
            try:
              markdown.write('sort_publish_date = %d\n' % j['data']['authors'][author]['_sort_publish_date']) 
            except KeyError:
              markdown.write('sort_publish_date = ""\n')
            markdown.write('create_date = %s\n' % (json.dumps(j['data']['authors'][author]['create_date']).encode('utf-8')))
            try:
              markdown.write('publish_date = %s\n' % json.dumps(j['data']['authors'][author]['publish_date'].encode('utf-8')))
            except KeyError:   
              markdown.write('publish_date = ""\n')
            try:
              markdown.write('date = %s\n' % json.dumps(j['data']['authors'][author]['publish_date'].encode('utf-8')))
            except KeyError:   
              markdown.write('date = %s\n' % (json.dumps(j['data']['authors'][author]['create_date']).encode('utf-8')))                 
            markdown.write('last_updated = %s\n' % json.dumps((j['data']['authors'][author]['last_updated']).encode('utf-8')))
            try:
              markdown.write('preview_url = %s\n' % (json.dumps(j['data']['authors'][author]['preview_url']).encode('utf-8')))
            except KeyError:
              markdown.write('preview_url = ""\n')
            ## END STANDARD DATA BLOCK ##   
            markdown.write('byline = %s\n' % (json.dumps(j['data']['authors'][author]['name']).encode('utf-8')))
            markdown.write('title = %s\n' % (json.dumps(j['data']['authors'][author]['name']).encode('utf-8')))
            try:
                markdown.write('alphabetize_by = %s\n' % (json.dumps(j['data']['authors'][author]['alphabetize_by']).encode('utf-8')))
            except KeyError:
                markdown.write('alphabetize_by = ""\n')            
            try:
                markdown.write('is_draft = %s\n' % (json.dumps(j['data']['authors'][author]['is_draft'])))
            except KeyError:
                markdown.write('is_draft = ""\n')
            try:
                markdown.write('is_seattle_pnw_writer = %s\n' % (json.dumps(j['data']['authors'][author]['is_seattle__pnw_writer'])))
            except KeyError:
                markdown.write('is_seattle_pnw_writer = ""\n')
            markdown.write('written_about = ""\n')

            # for the related content lookup keys
            author_temp = ('authors %s' % json.dumps(author.encode('utf-8')).replace('"',''))
            author_temp = findstring( author_temp ).replace('authors','writers').encode('utf-8')            
            markdown.write('books_author = "%s"\n' % author_temp )
            markdown.write('reviews_about = "%s"\n' % author_temp )            
            markdown.write('notes_about = "%s"\n' % author_temp )
            try:
                index_builder = []
                for sponsorship in j['data']['authors'][author]['sponsorships_author']:
                    sponsorship = findstring(sponsorship)
                    index_builder.append(sponsorship.encode('utf-8'))
                markdown.write('sponsorships_author = %s\n' % json.dumps(index_builder))
            except KeyError:
                markdown.write('sponsorships_author = ""\n')
            markdown.write('email = ""\n')
            markdown.write('twitter = ""\n')
            markdown.write('website = ""\n')
            markdown.write('bio = ""\n')
            markdown.write('reviews_byline = ""\n')
            markdown.write('notes_byline = ""\n')
            markdown.write('books_translator = ""\n')
            markdown.write('+++\n')
            markdown.close()

        # START THE WRITERS 

        for writer in j['data']['writers']:
            try:
                thedate = j['data']['writers'][writer]['publish_date']
            except KeyError:
                try:
                    thedate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(j['data']['writers'][writer]['_sort_publish_date']))
                except KeyError:
                    thedate = 'xxxx-xx-xx'        
            lc_name = sanitizestring(j['data']['writers'][writer]['name'])      
            markdown = open('output/writers/' + lc_name + '.md', 'w')
            markdown.write('+++\n')
            markdown.write('index = %s\n' % json.dumps(writer.encode('utf-8')))
            ## STANDARD DATA BLOCK ## 
            try:       
              markdown.write('sort_create_date = %d\n' % j['data']['writers'][writer]['_sort_create_date'])
            except KeyError:
              markdown.write('sort_create_date = ""\n')
            try:
              markdown.write('sort_last_updated = %d\n' % j['data']['writers'][writer]['_sort_last_updated'])
            except KeyError:
              markdown.write('sort_last_updated = ""\n')
            try:
              markdown.write('sort_publish_date = %d\n' % j['data']['writers'][writer]['_sort_publish_date']) 
            except KeyError:
              markdown.write('sort_publish_date = ""\n')
            try:
              markdown.write('create_date = %s\n' % (json.dumps(j['data']['writers'][writer]['create_date']).encode('utf-8')))
            except KeyError:
              markdown.write('create_date = ""\n')
            try:
              markdown.write('publish_date = %s\n' % json.dumps(j['data']['writers'][writer]['publish_date'].encode('utf-8')))
            except KeyError:   
              markdown.write('publish_date = ""\n')
            try:
              markdown.write('date = %s\n' % json.dumps(j['data']['writers'][writer]['publish_date'].encode('utf-8')))
            except KeyError:   
              markdown.write('date = ""\n')           
            try:    
              markdown.write('last_updated = %s\n' % (json.dumps(j['data']['writers'][writer]['last_updated']).encode('utf-8')))
            except KeyError:
              markdown.write('last_updated = ""\n')
            try:
              markdown.write('preview_url = %s\n' % (json.dumps(j['data']['writers'][writer]['preview_url']).encode('utf-8')))
            except KeyError:
              markdown.write('preview_url = ""\n')
            ## END STANDARD DATA BLOCK ##           
            markdown.write('byline = %s\n' % (json.dumps(j['data']['writers'][writer]['name']).encode('utf-8')))
            markdown.write('title = %s\n' % (json.dumps(j['data']['writers'][writer]['name']).encode('utf-8')))
            try:
              markdown.write('alphabetize_by = %s\n' % (json.dumps(j['data']['writers'][writer]['alphabetize_by']).encode('utf-8')))
            except KeyError:
              markdown.write('alphabetize_by = ""\n')
            markdown.write('is_draft = "false"\n')
            markdown.write('is_seattle_pnw_writer = ""\n')
            markdown.write('written_about = ""\n')
            markdown.write('books_author = ""\n')
            markdown.write('reviews_about = ""\n')
            markdown.write('notes_about = ""\n')
            markdown.write('sponsorships_author = ""\n')
            try:
              markdown.write('email = %s\n' % (json.dumps(j['data']['writers'][writer]['email']).encode('utf-8')))
            except KeyError:
              markdown.write('email = ""\n')
            try:
              markdown.write('twitter = %s\n' % (json.dumps(j['data']['writers'][writer]['twitter']).encode('utf-8')))
            except KeyError:
              markdown.write('twitter = ""\n') 
            try:
              markdown.write('website = %s\n' % (json.dumps(j['data']['writers'][writer]['website']).encode('utf-8')))
            except KeyError:
              markdown.write('website = ""\n') 
            try:
              markdown.write('bio = %s\n' % (json.dumps(j['data']['writers'][writer]['bio']).encode('utf-8')))
            except KeyError:
              markdown.write('bio = ""\n')
            writer_temp = ('writers %s' % json.dumps(writer.encode('utf-8')).replace('"',''))
            writer_temp = findstring(writer_temp).encode('utf-8')
            markdown.write('reviews_byline = "%s"\n' % writer_temp )
            markdown.write('notes_byline = "%s"\n' % writer_temp )
            markdown.write('books_translator = ""\n')  
    
            markdown.write('+++\n\n')  
            markdown.close()

        #START THE TRANSLATORS
        for translator in j['data']['translators']:
            try:
                thedate = j['data']['translators'][translator]['publish_date']
            except KeyError:
                try:
                    thedate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(j['data']['translators'][translator]['_sort_publish_date']))
                except KeyError:
                    thedate = 'xxxx-xx-xx'        
            lc_name = sanitizestring(j['data']['translators'][translator]['name'])
            markdown = open('output/writers/' + lc_name + '.md', 'w')
            markdown.write('+++\n')
            markdown.write('index = %s\n' % json.dumps(translator.encode('utf-8')))
            ## STANDARD DATA BLOCK ## 
            try:       
              markdown.write('sort_create_date = %d\n' % j['data']['translators'][translator]['_sort_create_date'])
            except KeyError:
              markdown.write('sort_create_date = ""\n')
            try:
              markdown.write('sort_last_updated = %d\n' % j['data']['translators'][translator]['_sort_last_updated'])
            except KeyError:
              markdown.write('sort_last_updated = ""\n')
            try:
              markdown.write('sort_publish_date = %d\n' % j['data']['translators'][translator]['_sort_publish_date']) 
            except KeyError:
              markdown.write('sort_publish_date = ""\n')
            try:
              markdown.write('create_date = %s\n' % (json.dumps(j['data']['translators'][translator]['create_date']).encode('utf-8')))
            except KeyError:
              markdown.write('create_date = ""\n')
            try:
              markdown.write('publish_date = %s\n' % json.dumps(j['data']['translators'][translator]['publish_date'].encode('utf-8')))
            except KeyError:   
              markdown.write('publish_date = ""\n') 
            try:
              markdown.write('date = %s\n' % json.dumps(j['data']['translators'][translator]['publish_date'].encode('utf-8')))
            except KeyError:   
              markdown.write('date = ""\n')           
            try:    
              markdown.write('last_updated = %s\n' % (json.dumps(j['data']['translators'][translator]['last_updated']).encode('utf-8')))
            except KeyError:
              markdown.write('last_updated = ""\n')
            try:
              markdown.write('preview_url = %s\n' % (json.dumps(j['data']['translators'][translator]['preview_url']).encode('utf-8')))
            except KeyError:
              markdown.write('preview_url = ""\n')
            ## END STANDARD DATA BLOCK ##           
            markdown.write('byline = %s\n' % (json.dumps(j['data']['translators'][translator]['name']).encode('utf-8')))
            markdown.write('title = %s\n' % (json.dumps(j['data']['translators'][translator]['name']).encode('utf-8')))
            markdown.write('alphabetize_by = ""\n')
            markdown.write('is_draft = ""\n')
            markdown.write('is_seattle_pnw_writer = ""\n')
            markdown.write('written_about = ""\n')
            markdown.write('books_author = ""\n')
            markdown.write('reviews_about = ""\n')
            markdown.write('notes_about = ""\n')
            markdown.write('sponsorships_author = ""\n')
            markdown.write('email = ""\n')
            markdown.write('twitter = ""\n')
            markdown.write('website = ""\n')
            markdown.write('bio = ""\n')
            markdown.write('reviews_byline = ""\n')
            markdown.write('notes_byline = ""\n')
            translator_temp = ('translators %s' % json.dumps(translator.encode('utf-8')).replace('"',''))
            translator_temp = findstring( translator_temp ).replace('translators','writers').encode('utf-8')             
            markdown.write('books_translator = "%s"\n' % translator_temp )        
            markdown.write('+++\n\n')  
            markdown.close()


    # BOOKS AREA
    elif key == 'books':
        if not os.path.exists('output/books'):
            os.makedirs('output/books')

        for book in j['data']['books']:
            try:
                thedate = j['data']['books'][book]['publish_date']
            except KeyError:
                try:
                    thedate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(j['data']['books'][book]['_sort_publish_date']))
                except KeyError:
                    thedate = 'xxxx-xx-xx'
           # print( j['data']['books'][book]['name'] )
            lc_name = sanitizestring(j['data']['books'][book]['name'])            
            markdown = open('output/books/' + lc_name + '.md','w')
            markdown.write('+++\n')         
            markdown.write('index = %s\n' % json.dumps(book.encode('utf-8')))
            ## STANDARD DATA BLOCK ## 
            try:       
              markdown.write('sort_create_date = %d\n' % j['data']['books'][book]['_sort_create_date'])
            except KeyError:
              markdown.write('sort_create_date = ""\n')
            try:
              markdown.write('sort_last_updated = %d\n' % j['data']['books'][book]['_sort_last_updated'])
            except KeyError:
              markdown.write('sort_last_updated = ""\n')
            try:
              markdown.write('sort_publish_date = %d\n' % j['data']['books'][book]['_sort_publish_date']) 
            except KeyError:
              markdown.write('sort_publish_date = ""\n')
            try:
              markdown.write('create_date = %s\n' % (json.dumps(j['data']['books'][book]['create_date']).encode('utf-8')))
            except KeyError:
              markdown.write('create_date = ""\n')
            try:
              markdown.write('publish_date = %s\n' % json.dumps(j['data']['books'][book]['publish_date'].encode('utf-8')))
            except KeyError:   
              markdown.write('publish_date = ""\n')
            try:
              markdown.write('date = %s\n' % json.dumps(j['data']['books'][book]['publish_date'].encode('utf-8')))
            except KeyError:   
              markdown.write('date = ""\n')               
            try:    
              markdown.write('last_updated = %s\n' % (json.dumps(j['data']['books'][book]['last_updated']).encode('utf-8')))
            except KeyError:
              markdown.write('last_updated = ""\n')
            try:
              markdown.write('preview_url = %s\n' % (json.dumps(j['data']['books'][book]['preview_url']).encode('utf-8')))
            except KeyError:
              markdown.write('preview_url = ""\n')
            ## END STANDARD DATA BLOCK ##               
            markdown.write('name = %s\n' % (json.dumps(j['data']['books'][book]['name']).encode('utf-8')))

            try:
                markdown.write('subtitle = %s\n' % (json.dumps(j['data']['books'][book]['subtitle']).encode('utf-8')))
            except KeyError:
                markdown.write('subtitle = ""\n')

            try:
                markdown.write('isbn = %s\n' % (json.dumps(j['data']['books'][book]['isbn']).encode('utf-8')))
            except KeyError:
                markdown.write('isbn = ""\n')

            try:
                markdown.write('isbn_13 = %s\n' % (json.dumps(j['data']['books'][book]['isbn_13']).encode('utf-8')))
            except KeyError:
                markdown.write('isbn_13 = ""\n') 

            try:
                markdown.write('page_count = %s\n' % (json.dumps(j['data']['books'][book]['page_count']).encode('utf-8')))
            except KeyError:
                markdown.write('page_count = ""\n')

            try:
                markdown.write('description = %s\n' % (json.dumps(j['data']['books'][book]['description']).encode('utf-8')))
            except KeyError:
                markdown.write('description = ""\n')

            try:
                markdown.write('publication_date = %s\n' % (json.dumps(j['data']['books'][book]['publication_date']).encode('utf-8')))
            except KeyError:
                markdown.write('publication_date = ""\n') 

            try:
                markdown.write('how_we_acquired = %s\n' % (json.dumps(j['data']['books'][book]['how_we_acquired']).encode('utf-8')))
            except KeyError:
                markdown.write('how_we_acquired = ""\n')

            try:
                markdown.write('is_sponsorship = %s\n' % (json.dumps(j['data']['books'][book]['is_sponsorship'])))
            except KeyError:
                markdown.write('is_sponsorship = ""\n')

            try:
                markdown.write('alt_purchase_link = %s\n' % (json.dumps(j['data']['books'][book]['alt_purchase_link']).encode('utf-8')))
            except KeyError:
                markdown.write('alt_purchase_link = ""\n')  

            try:
                markdown.write('alt_purchase_label = %s\n' % (json.dumps(j['data']['books'][book]['alt_purchase_label']).encode('utf-8')))
            except KeyError:
                markdown.write('alt_purchase_label = ""\n')  

            try:
                markdown.write('ebook_purchase = %s\n' % (json.dumps(j['data']['books'][book]['ebook_purchase']).encode('utf-8')))
            except KeyError:
                markdown.write('ebook_purchase = ""\n') 

            try:
                markdown.write('alt_ebook_label = %s\n' % (json.dumps(j['data']['books'][book]['alt_ebook_label']).encode('utf-8')))
            except KeyError:
                markdown.write('alt_ebook_label = ""\n')                                                                                                                

            # Category can either be an item or an object so we need to check for both, and in this case, flatten them
            try:
                markdown.write('category = %s\n' % (json.dumps(j['data']['books'][book]['category']).encode('utf-8')))
            except AttributeError:
                index_builder = ""
                for category in j['data']['books'][book]['category']:
                    category = findstring(category)
                    index_builder = index_builder + category.encode('utf-8')
                markdown.write('category = %s\n' % json.dumps(index_builder))
            except KeyError:
                markdown.write('category = ""\n')

            try:
                index_builder = ""
                for relationship in j['data']['books'][book]['publisher_relationship']:
                    relationship = findstring(relationship)
                    print(relationship)
                    index_builder = index_builder + relationship.encode('utf-8')
                markdown.write('books_publisher = %s\n' % json.dumps(index_builder))
            except KeyError:
                markdown.write('books_publisher = ""\n')

            try:
                index_builder = ""
                for translator in j['data']['books'][book]['translator']: 
                    translator = findstring(translator)
                    translator = findstring(translator)                   
                    index_builder = index_builder + translator.encode('utf-8')
                markdown.write('books_translator = %s\n' % json.dumps(index_builder))
            except KeyError:
                markdown.write('books_translator = ""\n')

            #try:
            #    index_builder = []
            #    for review in j['data']['books'][book]['review_relationship']:
            #        review = findstring(review)
            #        index_builder.append(review.encode('utf-8'))
            #    markdown.write('reviews_books = %s\n' % json.dumps(index_builder))
            #except KeyError:
            #    markdown.write('reviews_books = ""\n')
            books_temp = ('books %s' % json.dumps(book.encode('utf-8')).replace('"',''))
            books_temp = findstring( books_temp ).encode('utf-8') 
            markdown.write('reviews_books = ["%s"]\n' % books_temp )                

            try:
                index_builder = []
                for author in j['data']['books'][book]['author_relationship']:
                    author = findstring(author)
                    index_builder.append(author.encode('utf-8'))                    
                markdown.write('books_author = %s\n' % json.dumps(index_builder))
            except KeyError:
                markdown.write('books_author = ""\n')                                

            try:
                index_builder = []
                for sponsorship in j['data']['books'][book]['sponsorships_book']:
                    sponsorship = findstring(sponsorship)
                    index_builder.append(sponsorship.encode('utf-8'))
                markdown.write('sponsorships_book = %s\n' % json.dumps(index_builder))
            except KeyError:
                markdown.write('sponsorships_book = ""\n')

            try:
                index_builder = []
                for notes in j['data']['books'][book]['notes_relationship']:
                    notes = findstring(notes)
                    index_builder.append(notes.encode('utf-8'))
                markdown.write('notes_relationship = %s\n' % json.dumps(index_builder))
            except KeyError:
                markdown.write('notes_relationship = ""\n')

            try:
                markdown.write('[[image]]\n')
                for image in j['data']['books'][book]['image']:
                    if image == 'width':
                        markdown.write('width = %d\n' % j['data']['books'][book]['image'][image])
                    elif image == 'height':
                        markdown.write('height = %d\n' % j['data']['books'][book]['image'][image])
                    elif image == 'resize_url':
                        markdown.write('resize_url = %s\n' % json.dumps(j['data']['books'][book]['image'][image]).encode('utf-8'))
                    elif image == 'url':
                        markdown.write('url = %s\n' % json.dumps(j['data']['books'][book]['image'][image]).encode('utf-8'))
                    elif image == 'type':
                        markdown.write('type = %s\n' % json.dumps(j['data']['books'][book]['image'][image]).encode('utf-8'))
                    elif image == 'size':
                        markdown.write('size = %d\n\n' % j['data']['books'][book]['image'][image])
            except KeyError:
                markdown.write('image = ""\n')                

            markdown.write('+++\n')
            markdown.close()

    # END BOOKS AREA #

    # CALENDAR #

    #elif key == 'calendar':
    #    if not os.path.exists('output/calendar'):
    #        os.makedirs('output/calendar')
#
    #    for calendar in j['data']['calendar']:
    #        try:
    #            thedate = j['data']['calendars'][calendar]['publish_date']
    #        except KeyError:
    #            try:
    #                thedate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(j['data']['calendars'][calendar]['_sort_publish_date']))
    #            except KeyError:
    #                thedate = 'xxxx-xx-xx'
    #        lc_name = sanitizestring(j['data']['calendar'][calendar]['name'])
    #        markdown = open('output/calendar/' + lc_name + '.md', 'w')
    #        markdown.write('+++\n')
    #        markdown.write('index = %s\n' % json.dumps((calendar).encode('utf-8')))
    #        # # STANDARD DATA BLOCK ## 
    #        try:       
    #          markdown.write('sort_create_date = %d\n' % j['data']['calendar'][calendar]['_sort_create_date'])
    #        except KeyError:
    #          markdown.write('sort_create_date = ""\n')
    #        try:
    #          markdown.write('sort_last_updated = %d\n' % j['data']['calendar'][calendar]['_sort_last_updated'])
    #        except KeyError:
    #          markdown.write('sort_last_updated = ""\n')
    #        try:
    #          markdown.write('sort_publish_date = %d\n' % j['data']['calendar'][calendar]['_sort_publish_date']) 
    #        except KeyError:
    #          markdown.write('sort_publish_date = ""\n')
    #        try:
    #          markdown.write('create_date = %s\n' % (json.dumps(j['data']['calendar'][calendar]['create_date']).encode('utf-8')))
    #        except KeyError:
    #          markdown.write('create_date = ""\n')
    #        try:
    #          markdown.write('publish_date = %s\n' % json.dumps(j['data']['calendar'][calendar]['publish_date'].encode('utf-8')))
    #        except KeyError:   
    #          markdown.write('publish_date = ""\n')
    #        try:
    #          markdown.write('date = %s\n' % json.dumps(j['data']['calendar'][calendar]['publish_date'].encode('utf-8')))
    #        except KeyError:   
    #          markdown.write('date = %s\n' % (json.dumps(j['data']['calendar'][calendar]['create_date']).encode('utf-8')))               
    #        try:    
    #          markdown.write('last_updated = %s\n' % (json.dumps(j['data']['calendar'][calendar]['last_updated']).encode('utf-8')))
    #        except KeyError:
    #          markdown.write('last_updated = ""\n')
    #        try:
    #          markdown.write('preview_url = %s\n' % (json.dumps(j['data']['calendar'][calendar]['preview_url']).encode('utf-8')))
    #        except KeyError:
    #          markdown.write('preview_url = ""\n')
    #        ## END STANDARD DATA BLOCK ##             
    #        markdown.write('name = %s\n' % (json.dumps(j['data']['calendar'][calendar]['name']).encode('utf-8')))
    #        markdown.write('title = %s\n' % (json.dumps(j['data']['calendar'][calendar]['name']).encode('utf-8')))
    #        # IMAGE
    #        try:
    #            markdown.write('[[image]]\n')
    #            for image in j['data']['calendar'][calendar]['image']:
    #                if image == 'width':
    #                    markdown.write('width = %d\n' % j['data']['calendar'][calendar]['image'][image])
    #                elif image == 'height':
    #                    markdown.write('height = %d\n' % j['data']['calendar'][calendar]['image'][image])
    #                elif image == 'resize_url':
    #                    markdown.write('resize_url = %s\n' % json.dumps(j['data']['calendar'][calendar]['image'][image]).encode('utf-8'))
    #                elif image == 'url':
    #                    markdown.write('url = %s\n' % json.dumps(j['data']['calendar'][calendar]['image'][image]).encode('utf-8'))
    #                elif image == 'type':
    #                    markdown.write('type = %s\n' % json.dumps(j['data']['calendar'][calendar]['image'][image]).encode('utf-8'))
    #                elif image == 'size':
    #                    markdown.write('size = %d\n\n' % j['data']['calendar'][calendar]['image'][image])                
    #        except KeyError:
    #            markdown.write('image = ""\n')
    #        
    #        try:
    #          markdown.write('link = %s\n' % (json.dumps(j['data']['calendar'][calendar]['link']).encode('utf-8')))
    #        except:
    #          markdown.write('link = ""\n')
    #
    #        try:
    #          markdown.write('date = %s\n' % (json.dumps(j['data']['calendar'][calendar]['date']).encode('utf-8')))
    #        except:
    #          markdown.write('date = ""\n') 
    #        try:
    #          markdown.write('start_time = %s\n' % (json.dumps(j['data']['calendar'][calendar]['start_time']).encode('utf-8')))
    #        except:
    #          markdown.write('start_time = ""\n') 
    #        try:
    #          markdown.write('end_time = %s\n' % (json.dumps(j['data']['calendar'][calendar]['end_time']).encode('utf-8')))
    #        except:
    #          markdown.write('end_time = ""\n')  
    #        try:
    #          markdown.write('time_description = %s\n' % (json.dumps(j['data']['calendar'][calendar]['time_description']).encode('utf-8')))
    #        except:
    #          markdown.write('time_description = "\n')
    #        try:
    #          markdown.write('end_time = %s\n' % (json.dumps(j['data']['calendar'][calendar]['end_time']).encode('utf-8')))
    #        except:
    #          markdown.write('end_time = ""\n')   
    #        try:
    #          markdown.write('enddate = %s\n' % (json.dumps(j['data']['calendar'][calendar]['enddate']).encode('utf-8')))
    #        except:
    #          markdown.write('enddate = ""\n')
    #        try:
    #            markdown.write('is_sponsorship = %s\n' % (json.dumps(j['data']['calendar'][calendar]['is_sponsorship'])))
    #        except KeyError:
    #            markdown.write('is_sponsorship = ""\n')  
#
    #        try:
    #            index_builder = []
    #            for authors in j['data']['calendar'][calendar]['authors']:
    #                authors = findstring(authors)
    #                index_builder.append(authors.encode('utf-8'))
    #            markdown.write('authors = %s\n' % json.dumps(index_builder))
    #        except KeyError:
    #            markdown.write('authors = ""\n')
    #
    #        try:
    #            index_builder = []
    #            for sponsorship_event in j['data']['calendar'][calendar]['sponsorship_event']:
    #                sponsorship_event = findstring(sponsorship_event)
    #                index_builder.append(sponsorship_event.encode('utf-8'))
    #            markdown.write('sponsorship_event = %s\n' % json.dumps(index_builder))
    #        except KeyError:
    #            markdown.write('sponsorship_event = ""\n')                  
    #
    #        try:
    #          index_builder = ""
    #          for venues in j['data']['calendar'][calendar]['venues']:
    #            venues = findstring(venues)
    #            venue = index_builder + venue.encode('utf-8')
    #          markdown.write('venues = %s\n' % json.dumps(index_builder))
    #        except KeyError:
    #          markdown.write('venues = ""\n')
    #
    #        try:
    #          markdown.write((j['data']['calendar'][calendar]['details']).encode('utf-8')) 
    #        except:
    #          markdown.write('')
    #        markdown.close() 

    elif key == 'notes':
      if not os.path.exists('output/notes'):
        os.makedirs('output/notes')

      for note in j['data']['notes']:
        try:
            thedate = j['data']['notes'][note]['publish_date']
        except KeyError:
            try:
                thedate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(j['data']['notes'][note]['_sort_publish_date']))
            except KeyError:
                thedate = 'xxxx-xx-xx'        
        lc_name = sanitizestring(j['data']['notes'][note]['name'])
        markdown = open('output/notes/' + lc_name + '.md', 'w')
        markdown.write('+++\n') 
        markdown.write('index = %s\n' % json.dumps((note).encode('utf-8')))
        ## STANDARD DATA BLOCK ## 
        try:       
          markdown.write('sort_create_date = %d\n' % j['data']['notes'][note]['_sort_create_date'])
        except KeyError:
          markdown.write('sort_create_date = ""\n')
        try:
          markdown.write('sort_last_updated = %d\n' % j['data']['notes'][note]['_sort_last_updated'])
        except KeyError:
          markdown.write('sort_last_updated = ""\n')
        try:
          markdown.write('sort_publish_date = %d\n' % j['data']['notes'][note]['_sort_publish_date']) 
        except KeyError:
          markdown.write('sort_publish_date = ""\n')
        try:
          markdown.write('create_date = %s\n' % (json.dumps(j['data']['notes'][note]['create_date']).encode('utf-8')))
        except KeyError:
          markdown.write('create_date = ""\n')
        try:
          markdown.write('publish_date = %s\n' % json.dumps(j['data']['notes'][note]['publish_date'].encode('utf-8')))
        except KeyError:   
          markdown.write('publish_date = ""\n')
        try:
          markdown.write('date = %s\n' % json.dumps(j['data']['notes'][note]['publish_date'].encode('utf-8')))
        except KeyError:   
          markdown.write('date = ""\n')           
        try:    
          markdown.write('last_updated = %s\n' % (json.dumps(j['data']['notes'][note]['last_updated']).encode('utf-8')))
        except KeyError:
          markdown.write('last_updated = ""\n')
        try:
          markdown.write('preview_url = %s\n' % (json.dumps(j['data']['notes'][note]['preview_url']).encode('utf-8')))
        except KeyError:
          markdown.write('preview_url = ""\n')
        ## END STANDARD DATA BLOCK ##           
        markdown.write('name = %s\n' % (json.dumps(j['data']['notes'][note]['name']).encode('utf-8')))
        markdown.write('title = %s\n' % (json.dumps(j['data']['notes'][note]['name']).encode('utf-8')))
        markdown.write('type = %s\n' % (json.dumps(j['data']['notes'][note]['type']).encode('utf-8')))

        try:
          markdown.write('link = %s\n' % (json.dumps(j['data']['notes'][note]['url']).encode('utf-8')))
        except KeyError:
          markdown.write('link = ""\n')
        try:
          markdown.write('shareimage = %s\n' % (json.dumps(j['data']['notes'][note]['shareimage']).encode('utf-8')))
        except KeyError:
          markdown.write('shareimage = ""\n') 
        try:
          markdown.write('twitterauto = %s\n' % (json.dumps(j["data"]["notes"][note]["twitterauto"]).encode("utf-8")))
        except KeyError:
          markdown.write('twitterauto = ""\n')               
        try:
          markdown.write('facebookauto = %s\n' % (json.dumps(j["data"]["notes"][note]["facebookauto"]).encode("utf-8")))
        except KeyError:
          markdown.write('facebookauto = ""\n')
        try:
          markdown.write('make_image_tweet = %s\n' % json.dumps((str(j['data']['notes'][note]['make_image_tweet']))))
        except KeyError:
          markdown.write('make_image_tweet = ""\n')

        try:
            index_builder = []
            for byline in j['data']['notes'][note]['byline']:
                byline = findstring(byline)
                index_builder.append(byline.encode('utf-8'))
            markdown.write('notes_byline = %s\n' % json.dumps(index_builder))
        except KeyError:
            markdown.write('notes_byline = ""\n')
        #try:
        #    index_builder = []
        #    for tags_notes in j['data']['notes'][note]['tags_notes']:
        #        tags_notes = findstring(tags_notes)
        #        index_builder.append(tags_notes.encode('utf-8'))
        #    markdown.write('tags_notes = %s\n' % json.dumps(index_builder))
        #except KeyError:
        #    markdown.write('tags_notes = ""\n')
        tags_temp = ('notes %s' % json.dumps(note.encode('utf-8')).replace('"',''))
        tags_temp = findstring(tags_temp).encode('utf-8')
        markdown.write('notes_tags = "%s"\n' % tags_temp )         

        try:
            index_builder = []
            for authors_notes in j['data']['notes'][note]['authors_notes']:
                authors_notes = findstring(authors_notes)
                index_builder.append(authors_notes.encode('utf-8'))
            markdown.write('notes_about = %s\n' % json.dumps(index_builder))
        except KeyError:
            markdown.write('notes_about = ""\n')
        try:
            index_builder = []
            for books in j['data']['notes'][note]['books']:
                books = findstring(books)
                index_builder.append(books.encode('utf-8'))
            markdown.write('books = %s\n' % json.dumps(index_builder))
        except KeyError:
            markdown.write('books = ""\n')                                      


        markdown.write('+++\n')
        
        markdown.write((j['data']['notes'][note]['post']).encode('utf-8'))

        markdown.close()

    elif key == 'publishers':
      if not os.path.exists('output/publishers'):
        os.makedirs('output/publishers')

      for publisher in j['data']['publishers']:
        try:
            thedate = j['data']['publishers'][publisher]['publish_date']
        except KeyError:
            try:
                thedate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(j['data']['publishers'][publisher]['_sort_publish_date']))
            except KeyError:
                thedate = 'xxxx-xx-xx'        
        lc_name = sanitizestring(j['data']['publishers'][publisher]['name'])
        markdown = open('output/publishers/' + lc_name + '.md', 'w')
        markdown.write('+++\n')    
        markdown.write('index = %s\n' % json.dumps(publisher.encode('utf-8')))
        ## STANDARD DATA BLOCK ## 
        try:       
          markdown.write('sort_create_date = %d\n' % j['data']['publishers'][publisher]['_sort_create_date'])
        except KeyError:
          markdown.write('sort_create_date = ""\n')
        try:
          markdown.write('sort_last_updated = %d\n' % j['data']['publishers'][publisher]['_sort_last_updated'])
        except KeyError:
          markdown.write('sort_last_updated = ""\n')
        try:
          markdown.write('sort_publish_date = %d\n' % j['data']['publishers'][publisher]['_sort_publish_date']) 
        except KeyError:
          markdown.write('sort_publish_date = ""\n')
        try:
          markdown.write('create_date = %s\n' % (json.dumps(j['data']['publishers'][publisher]['create_date']).encode('utf-8')))
        except KeyError:
          markdown.write('create_date = ""\n')
        try:
          markdown.write('publish_date = %s\n' % json.dumps(j['data']['publishers'][publisher]['publish_date'].encode('utf-8')))
        except KeyError:   
          markdown.write('publish_date = ""\n')
        try:
          markdown.write('date = %s\n' % json.dumps(j['data']['publishers'][publisher]['publish_date'].encode('utf-8')))
        except KeyError:   
          markdown.write('date = "2018-04-12T12:01:00-07:00"\n')  #hard coding date because of build fails         
        try:    
          markdown.write('last_updated = %s\n' % (json.dumps(j['data']['publishers'][publisher]['last_updated']).encode('utf-8')))
        except KeyError:
          markdown.write('last_updated = ""\n')
        try:
          markdown.write('preview_url = %s\n' % (json.dumps(j['data']['publishers'][publisher]['preview_url']).encode('utf-8')))
        except KeyError:
          markdown.write('preview_url = ""\n')
        ## END STANDARD DATA BLOCK ##           
        markdown.write('name = %s\n' % (json.dumps(j['data']['publishers'][publisher]['name']).encode('utf-8')))
        markdown.write('title = %s\n' % (json.dumps(j['data']['publishers'][publisher]['name']).encode('utf-8')))
        #try:
        #    index_builder = []
        #    for publisher in j['data']['publishers'][publisher]['books_by_this_publisher']:
        #        publisher = findstring(publisher)
        #        index_builder.append(publisher.encode('utf-8'))
        #    markdown.write('books_by_this_publisher = %s\n' % json.dumps(index_builder))
        #except KeyError:
        #    markdown.write('books_by_this_publisher = ""\n')          
        # books_by_this_publisher
        # publisher_relationship books_publisher
        publisher_temp = ('publishers %s' % json.dumps(publisher.encode('utf-8')).replace('"',''))
        publisher_temp = findstring(publisher_temp).encode('utf-8')
        markdown.write('books_publisher = "%s"\n' % publisher_temp )        
        markdown.write('+++\n')
        markdown.close()

    elif key == 'reviews':
      if not os.path.exists('output/reviews'):
        os.makedirs('output/reviews')

      for review in j['data']['reviews']:
        try:
            thedate = j['data']['reviews'][review]['publish_date']
        except KeyError:
            try:
                thedate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(j['data']['reviews'][review]['_sort_publish_date']))
            except KeyError:
                thedate = 'xxxx-xx-xx'        
        lc_name = sanitizestring(j['data']['reviews'][review]['name'])
        markdown = open('output/reviews/' + lc_name + '.md', 'w')
        markdown.write('+++\n')
        markdown.write('index = %s\n' % json.dumps(review.encode('utf-8')))
        ## STANDARD DATA BLOCK ## 
        try:       
          markdown.write('sort_create_date = %d\n' % j['data']['reviews'][review]['_sort_create_date'])
        except KeyError:
          markdown.write('sort_create_date = ""\n')
        try:
          markdown.write('sort_last_updated = %d\n' % j['data']['reviews'][review]['_sort_last_updated'])
        except KeyError:
          markdown.write('sort_last_updated = ""\n')
        try:
          markdown.write('sort_publish_date = %d\n' % j['data']['reviews'][review]['_sort_publish_date']) 
        except KeyError:
          markdown.write('sort_publish_date = ""\n')
        try:
          markdown.write('create_date = %s\n' % (json.dumps(j['data']['reviews'][review]['create_date']).encode('utf-8')))
        except KeyError:
          markdown.write('create_date = ""\n')
        try:
          markdown.write('publish_date = %s\n' % json.dumps(j['data']['reviews'][review]['publish_date'].encode('utf-8')))
        except KeyError:   
          markdown.write('publish_date = ""\n')
        try:
          markdown.write('date = %s\n' % json.dumps(j['data']['reviews'][review]['publish_date'].encode('utf-8')))
        except KeyError:   
          markdown.write('date = ""\n')           
        try:    
          markdown.write('last_updated = %s\n' % (json.dumps(j['data']['reviews'][review]['last_updated']).encode('utf-8')))
        except KeyError:
          markdown.write('last_updated = ""\n')
        try:
          markdown.write('preview_url = %s\n' % (json.dumps(j['data']['reviews'][review]['preview_url']).encode('utf-8')))
        except KeyError:
          markdown.write('preview_url = ""\n')
        ## END STANDARD DATA BLOCK ##           
        markdown.write('name = %s\n' % (json.dumps(j['data']['reviews'][review]['name']).encode('utf-8')))
        markdown.write('title = %s\n' % (json.dumps(j['data']['reviews'][review]['name']).encode('utf-8')))
        markdown.write('dek = %s\n' % (json.dumps(j['data']['reviews'][review]['dek']).encode('utf-8')))
        try:
          markdown.write('facebookauto = %s\n' % (json.dumps(j['data']['reviews'][review]['facebookauto']).encode('utf-8')))
        except KeyError:
          markdown.write

        try:
          markdown.write('twitterauto = %s\n' % (json.dumps(j['data']['reviews'][review]['twitterauto']).encode('utf-8')))
        except KeyError:
          markdown.write

        try:
            index_builder = []
            for by in j['data']['reviews'][review]['by']:
                by = findstring(by)
                index_builder.append(by.encode('utf-8'))
            markdown.write('reviews_byline = %s\n' % json.dumps(index_builder))
        except KeyError:
            markdown.write('reviews_byline = ""\n')

        try:
            index_builder = []
            for books_in_this_review in j['data']['reviews'][review]['books_in_this_review']:
                books_in_this_review = findstring(books_in_this_review)
                index_builder.append(books_in_this_review.encode('utf-8'))
            markdown.write('reviews_books = %s\n' % json.dumps(index_builder))
        except KeyError:
            markdown.write('reviews_books = ""\n')
        #review_temp = ('reviews %s' % json.dumps(review.encode('utf-8')).replace('"',''))
        #review_temp = findstring( review_temp ).encode('utf-8') 
        #markdown.write('review_relationship = ["%s"]\n' % review_temp )

        #try:
        #    index_builder = []
        #    for tags_reviews in j['data']['reviews'][review]['tags_reviews']:
        #        tags_reviews = findstring(tags_reviews)
        #        index_builder.append(tags_reviews.encode('utf-8'))
        #    markdown.write('reviews_tags = %s\n' % json.dumps(index_builder))
        #except KeyError:
        #    markdown.write('reviews_tags = ""\n')
        tags_temp = ('reviews %s' % json.dumps(review.encode('utf-8')).replace('"',''))
        tags_temp = findstring( tags_temp ).encode('utf-8') 
        markdown.write('reviews_tags = ["%s"]\n' % tags_temp )            

        try:
            index_builder = []
            for authors_reviews in j['data']['reviews'][review]['authors_reviews']:
                authors_reviews = findstring(authors_reviews)
                index_builder.append(authors_reviews.encode('utf-8'))
            markdown.write('reviews_about = %s\n' % json.dumps(index_builder))
        except KeyError:
            markdown.write('reviews_about = ""\n')                                  
        markdown.write('+++\n\n')
        markdown.write((j['data']['reviews'][review]['review']).encode('utf-8'))
        markdown.close()

    elif key == 'tags':
      if not os.path.exists('output/tags'):
        os.makedirs('output/tags')

      for tag in j['data']['tags']:
        try:
            thedate = j['data']['tags'][tag]['publish_date']
        except KeyError:
            try:
                thedate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(j['data']['tags'][tag]['_sort_publish_date']))
            except KeyError:
                thedate = 'xxxx-xx-xx'        
        lc_name = sanitizestring(j['data']['tags'][tag]['name'])
        markdown = open('output/tags/' + lc_name + '.md', 'w')
        markdown.write('+++\n')
        markdown.write('index = %s\n' % json.dumps(tag.encode('utf-8')))
        ## STANDARD DATA BLOCK ## 
        try:       
          markdown.write('sort_create_date = %d\n' % j['data']['tags'][tag]['_sort_create_date'])
        except KeyError:
          markdown.write('sort_create_date = ""\n')
        try:
          markdown.write('sort_last_updated = %d\n' % j['data']['tags'][tag]['_sort_last_updated'])
        except KeyError:
          markdown.write('sort_last_updated = ""\n')
        try:
          markdown.write('sort_publish_date = %d\n' % j['data']['tags'][tag]['_sort_publish_date']) 
        except KeyError:
          markdown.write('sort_publish_date = ""\n')
        try:
          markdown.write('create_date = %s\n' % (json.dumps(j['data']['tags'][tag]['create_date']).encode('utf-8')))
        except KeyError:
          markdown.write('create_date = ""\n')
        try:
          markdown.write('publish_date = %s\n' % json.dumps(j['data']['tags'][tag]['publish_date'].encode('utf-8')))
        except KeyError:   
          markdown.write('publish_date = ""\n')
        try:
          markdown.write('date = %s\n' % json.dumps(j['data']['tags'][tag]['publish_date'].encode('utf-8')))
        except KeyError:   
          markdown.write('date = ""\n')           
        try:    
          markdown.write('last_updated = %s\n' % (json.dumps(j['data']['tags'][tag]['last_updated']).encode('utf-8')))
        except KeyError:
          markdown.write('last_updated = ""\n')
        try:
          markdown.write('preview_url = %s\n' % (json.dumps(j['data']['tags'][tag]['preview_url']).encode('utf-8')))
        except KeyError:
          markdown.write('preview_url = ""\n')
        ## END STANDARD DATA BLOCK ##           
        markdown.write('name = %s\n' % (json.dumps(j['data']['tags'][tag]['name']).encode('utf-8')))
        markdown.write('title = %s\n' % (json.dumps(j['data']['tags'][tag]['name']).encode('utf-8')))
        try:
            markdown.write('is_column = %s\n' % (json.dumps(j['data']['tags'][tag]['is_column'])))
        except KeyError:
            markdown.write('is_column = ""\n')  

        try:
            index_builder = []
            for reviews in j['data']['tags'][tag]['reviews']:
                reviews = findstring(reviews)
                index_builder.append(reviews.encode('utf-8'))
            markdown.write('reviews_tags = %s\n' % json.dumps(index_builder))
        except KeyError:
            markdown.write('reviews_tags = ""\n')
        try:
            index_builder = []
            for notes in j['data']['tags'][tag]['notes']:
                notes = findstring(notes)
                index_builder.append(notes.encode('utf-8'))
            markdown.write('notes_tags = %s\n' % json.dumps(index_builder))
        except KeyError:
            markdown.write('notes_tags = ""\n')        

        markdown.write('+++\n\n')  
        markdown.close()
             




# TODO:
# 1. Replace ## REPLACE WITH STANDARD DATA BLOCK