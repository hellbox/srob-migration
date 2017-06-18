#! /usr/bin/python
import json
import os

# Load JSON object
with open('srob-firebase.json') as json_data:
    j = json.load(json_data)
    # Look for the node title "data"
    data = j['data']

# Select child
for key in j['data']:
    print("------------------- working with key '%s'-----------------------" % key)

    #Let's start with the single items
    if key == 'about':
        #create folder with item name
        if not os.path.exists('output/about'):
            os.makedirs('output/about')

        #create file and structure
        markdown = open('output/about/about.toml','w')
        markdown.write('+++\n')
        markdown.write('_sort_create_date = %d\n' % j['data']['about']['_sort_create_date'])
        markdown.write('_sort_last_updated = %d\n' % j['data']['about']['_sort_last_updated'])
        markdown.write('create_date = %r\n' % (j['data']['about']['create_date']).encode('utf-8'))
        markdown.write('last_updated = %r\n' % (j['data']['about']['last_updated']).encode('utf-8'))
        markdown.write('name = %r\n' % (j['data']['about']['name']).encode('utf-8'))
        markdown.write('preview_url = %r\n' % (j['data']['about']['preview_url']).encode('utf-8'))
        markdown.write('+++\n\n')
        markdown.write((j['data']['about']['markdown_text']).encode('utf-8'))
        markdown.close()

    elif key == 'privacy':
        #create folder with item name
        if not os.path.exists('output/privacy'):
            os.makedirs('output/privacy')

        #create file and structure
        markdown = open('output/privacy/privacy.toml','w')
        markdown.write('+++\n')
        markdown.write('_sort_create_date = %d\n' % j['data']['privacy']['_sort_create_date'])
        markdown.write('_sort_last_updated = %d\n' % j['data']['privacy']['_sort_last_updated'])
        markdown.write('create_date = %r\n' % (j['data']['privacy']['create_date']).encode('utf-8'))
        markdown.write('last_updated = %r\n' % (j['data']['privacy']['last_updated']).encode('utf-8'))
        markdown.write('name = %r\n' % (j['data']['privacy']['name']).encode('utf-8'))
        markdown.write('preview_url = %r\n' % (j['data']['privacy']['preview_url']).encode('utf-8'))
        markdown.write('+++\n\n')
        markdown.write((j['data']['privacy']['markdown_text']).encode('utf-8'))
        markdown.close()

    elif key == 'resources':
        if not os.path.exists('output/resources'):
            os.makedirs('output/resources')

        #create file and structure
        markdown = open('output/resources/resources.toml','w')
        markdown.write('+++\n')
        markdown.write('_sort_create_date = %d\n' % j['data']['resources']['_sort_create_date'])
        markdown.write('_sort_last_updated = %d\n' % j['data']['resources']['_sort_last_updated'])
        markdown.write('create_date = %r\n' % (j['data']['resources']['create_date']).encode('utf-8'))
        markdown.write('last_updated = %r\n' % (j['data']['resources']['last_updated']).encode('utf-8'))
        markdown.write('name = %r\n' % (j['data']['resources']['name']).encode('utf-8'))
        markdown.write('preview_url = %r\n' % (j['data']['resources']['preview_url']).encode('utf-8'))
        markdown.write('+++\n\n')
        markdown.write((j['data']['resources']['markdown_text']).encode('utf-8'))
        markdown.close()

    elif key == 'submissions':
        if not os.path.exists('output/submissions'):
            os.makedirs('output/submissions')

        #create file and structure
        markdown = open('output/submissions/submissions.toml','w')
        markdown.write('+++\n')
        markdown.write('_sort_create_date = %d\n' % j['data']['submissions']['_sort_create_date'])
        markdown.write('_sort_last_updated = %d\n' % j['data']['submissions']['_sort_last_updated'])
        markdown.write('create_date = %r\n' % (j['data']['submissions']['create_date']).encode('utf-8'))
        markdown.write('last_updated = %r\n' % (j['data']['submissions']['last_updated']).encode('utf-8'))
        markdown.write('name = %r\n' % (j['data']['submissions']['name']).encode('utf-8'))
        markdown.write('preview_url = %r\n' % (j['data']['submissions']['preview_url']).encode('utf-8'))
        markdown.write('+++\n\n')
        markdown.write((j['data']['submissions']['markdown_text']).encode('utf-8'))
        markdown.close()

    elif key == 'sponsor':
        if not os.path.exists('output/sponsor'):
            os.makedirs('output/sponsor')

        #create file and structure
        markdown = open('output/sponsor/sponsor.toml','w')
        markdown.write('+++\n')
        markdown.write('_sort_create_date = %d\n' % j['data']['sponsor']['_sort_create_date'])
        markdown.write('_sort_last_updated = %d\n' % j['data']['sponsor']['_sort_last_updated'])
        markdown.write('create_date = %r\n' % (j['data']['sponsor']['create_date']).encode('utf-8'))
        markdown.write('last_updated = %r\n' % (j['data']['sponsor']['last_updated']).encode('utf-8'))
        markdown.write('name = %r\n' % (j['data']['sponsor']['name']).encode('utf-8'))
        markdown.write('preview_url = %r\n' % (j['data']['sponsor']['preview_url']).encode('utf-8'))
        markdown.write('+++\n\n')
        markdown.write((j['data']['sponsor']['markdown_text']).encode('utf-8'))
        markdown.close()

    
    # AUTHORS AREA

    elif key == 'authors':
        if not os.path.exists('output/authors'):
            os.makedirs('output/authors')

        for author in j['data']['authors']:
            #print("  the key %s is an author." % author)
            # print ("    author has a creation date of %s" % j['data']['authors'][author]['_sort_create_date'])            
            #Convert author name to LC and replace spaces with dashes to make good file names
            lc_name = (j['data']['authors'][author]['name']).replace(' ', '-').replace('.','').lower()
            markdown = open('output/authors/' + lc_name + '.toml','w')
            markdown.write('+++\n')
            markdown.write('index = %r\n' % author.encode('utf-8'))
            markdown.write('_sort_create_date = %d\n' % j['data']['authors'][author]['_sort_create_date'])           
            markdown.write('_sort_last_updated = %d\n' % j['data']['authors'][author]['_sort_last_updated'])
            markdown.write('last_updated = %r\n' % (j['data']['authors'][author]['last_updated']).encode('utf-8'))
            markdown.write('name = %r\n' % (j['data']['authors'][author]['name']).encode('utf-8'))
            markdown.write('publish_date = %r\n' % (j['data']['authors'][author]['publish_date']).encode('utf-8'))
            try:
            	markdown.write('alphabetize_by = %r\n' % (j['data']['authors'][author]['alphabetize_by']).encode('utf-8'))
            except KeyError:
            	markdown.write('alphabetize_by = ""\n')
            try:
            	markdown.write('isDraft = %r\n' % (j['data']['authors'][author]['isDraft']))
            except KeyError:
            	markdown.write('isDraft = ""\n')
            try:
            	markdown.write('create_date = %r\n' % (j['data']['authors'][author]['create_date']).encode('utf-8'))
            except KeyError:
            	markdown.write('create_date = ""\n')
            try:
            	markdown.write('is_seattle__pnw_writer = %r\n' % (j['data']['authors'][author]['is_seattle__pnw_writer']))
            except KeyError:
            	markdown.write('is_seattle__pnw_writer = ""\n')
            try:
            	markdown.write('preview_url = %r\n' % (j['data']['authors'][author]['preview_url']).encode('utf-8'))
            except KeyError:
            	markdown.write('preview_url = ""\n')
            try:
            	markdown.write('written_about = %r\n' % (j['data']['authors'][author]['written_about']).encode('utf-8'))
            except KeyError:
            	markdown.write('written_about = ""\n')            	
            try:
            	index_builder = []
            	for book in j['data']['authors'][author]['books']:
            		index_builder.append(book.encode('utf-8'))
            	markdown.write('books = %r\n' % index_builder)       	
            except KeyError:
            	markdown.write('books = ""\n')
            try:
            	index_builder = []
            	for calendar in j['data']['authors'][author]['calendar_author']:
            		index_builder.append(calendar.encode('utf-8'))
            	markdown.write('calendar_author = %r\n' % index_builder)             	      	
            except KeyError:
            	markdown.write('calendar_author = ""\n')
            try:
            	index_builder = []
            	for reviews in j['data']['authors'][author]['reviews']:
            		index_builder.append(reviews.encode('utf-8'))
            	markdown.write('reviews = %r\n' % index_builder)            	     	
            except KeyError:
            	markdown.write('reviews = ""\n') 
            try:
            	index_builder = []
            	for note in j['data']['authors'][author]['notes']:
            		index_builder.append(note.encode('utf-8'))
            	markdown.write('notes = %r\n' % index_builder)               	
            except KeyError:
            	markdown.write('notes = ""\n')
            try:
            	index_builder = []
            	for sponsorship in j['data']['authors'][author]['sponsorships_author']:
            		index_builder.append(sponsorship.encode('utf-8'))
            	markdown.write('sponsorships_author = %r\n' % index_builder)
            except KeyError:
            	markdown.write('sponsorships_author = ""\n')         	
            markdown.write('+++\n')
            markdown.close()

    # BOOKS AREA
    elif key == 'books':
        if not os.path.exists('output/books'):
            os.makedirs('output/books')

        for book in j['data']['books']:
        	lc_name = (j['data']['books'][book]['name']).replace(' ', '-').replace('.','').replace('/','--').lower()
        	markdown = open('output/books/' + lc_name + '.toml','w')
        	markdown.write('+++\n')
        	markdown.write('index = %r\n' % book.encode('utf-8'))
        	markdown.write('_sort_create_date = %d\n' % j['data']['authors'][author]['_sort_create_date'])
        	markdown.write('_sort_last_updated = %d\n' % j['data']['authors'][author]['_sort_last_updated'])
        	markdown.write('last_updated = %r\n' % (j['data']['authors'][author]['last_updated']).encode('utf-8'))
        	markdown.write('name = %r\n' % (j['data']['authors'][author]['name']).encode('utf-8'))

        	try:
        		markdown.write('subtitle = %r\n' % (j['data']['books'][book]['subtitle']).encode('utf-8'))
    		except KeyError:
    			markdown.write('subtitle = ""\n')

        	try:
        		markdown.write('isbn = %r\n' % (j['data']['books'][book]['isbn']).encode('utf-8'))
    		except KeyError:
    			markdown.write('isbn = ""\n')

        	try:
        		markdown.write('isbn_13 = %r\n' % (j['data']['books'][book]['isbn_13']).encode('utf-8'))
    		except KeyError:
    			markdown.write('isbn_13 = ""\n') 

        	try:
        		markdown.write('page_count = %r\n' % (j['data']['books'][book]['page_count']).encode('utf-8'))
    		except KeyError:
    			markdown.write('page_count = ""\n')

        	try:
        		markdown.write('description = %r\n' % (j['data']['books'][book]['description']).encode('utf-8'))
    		except KeyError:
    			markdown.write('description = ""\n')

        	try:
        		markdown.write('publication_date = %r\n' % (j['data']['books'][book]['publication_date']).encode('utf-8'))
    		except KeyError:
    			markdown.write('publication_date = ""\n') 

        	try:
        		markdown.write('how_we_acquired = %r\n' % (j['data']['books'][book]['how_we_acquired']).encode('utf-8'))
    		except KeyError:
    			markdown.write('how_we_acquired = ""\n')

        	try:
        		markdown.write('is_sponsorship = %r\n' % (j['data']['books'][book]['is_sponsorship']))
    		except KeyError:
    			markdown.write('is_sponsorship = ""\n')

        	try:
        		markdown.write('alt_purchase_link = %r\n' % (j['data']['books'][book]['alt_purchase_link']).encode('utf-8'))
    		except KeyError:
    			markdown.write('alt_purchase_link = ""\n')  

        	try:
        		markdown.write('alt_purchase_label = %r\n' % (j['data']['books'][book]['alt_purchase_label']).encode('utf-8'))
    		except KeyError:
    			markdown.write('alt_purchase_label = ""\n')  

        	try:
        		markdown.write('ebook_purchase = %r\n' % (j['data']['books'][book]['ebook_purchase']).encode('utf-8'))   
    		except KeyError:
    			markdown.write('ebook_purchase = ""\n') 

        	try:
        		markdown.write('alt_ebook_label = %r\n' % (j['data']['books'][book]['alt_ebook_label']).encode('utf-8'))
    		except KeyError:
    			markdown.write('alt_ebook_label = ""\n')       			      			     			     			       			      			      			

        	# Category can either be an item or an object so we need to check for both, and in this case, flatten them
        	try:
        		markdown.write('category = %r\n' % (j['data']['books'][book]['category']).encode('utf-8'))
        	except AttributeError:
        		index_builder = ""
        		for category in j['data']['books'][book]['category']:
        			index_builder = index_builder + category.encode('utf-8')
        		markdown.write('category = %r\n' % index_builder)
        		print(index_builder)
        	except KeyError:
        		markdown.write('category = ""\n')

 

        	# LOOPS #
        	# image
        		# height
        		# resize_url
        		# size
        		# type
        		# url
        		# width
        	# publisher_relationship
			# translator
        	# review_relationship
        	# sponsorships_book
        	# translator
        	# notes_relationship

        	markdown.write('+++\n')
        	markdown.close() 

#    # TEMPLATE AREA
#	elif key == 'xxxx':
#        if not os.path.exists('output/xxxx'):
#            os.makedirs('output/xxxx')
#
#        for book in j['data']['xxxx']:
#        	lc_name = (j['data']['xxxx'][xxxx]['name']).replace(' ', '-').replace('.','').lower()
#            markdown = open('output/xxxx/' + lc_name + '.toml','w')
#            markdown.write('+++\n')
#            markdown.write('+++\n')  
#            markdown.close()                            
#

