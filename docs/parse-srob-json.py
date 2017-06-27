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
    print("---------- working with key '%s'--------" % key)

    # Let's start with the single items
    if key == 'about':
        # create folder with item name
        if not os.path.exists('output/about'):
            os.makedirs('output/about')

        # create file and structure
        markdown = open('output/about/about.toml', 'w')
        markdown.write('+++\n')
        ## REPLACE WITH STANDARD DATA BLOCK        
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
        # create folder with item name
        if not os.path.exists('output/privacy'):
            os.makedirs('output/privacy')

        # create file and structure
        markdown = open('output/privacy/privacy.toml','w')
        markdown.write('+++\n')
        ## REPLACE WITH STANDARD DATA BLOCK        
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

        # create file and structure
        markdown = open('output/resources/resources.toml','w')
        markdown.write('+++\n')
        ## REPLACE WITH STANDARD DATA BLOCK        
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

        # create file and structure
        markdown = open('output/submissions/submissions.toml', 'w')
        markdown.write('+++\n')
        ## REPLACE WITH STANDARD DATA BLOCK        
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

        # create file and structure
        markdown = open('output/sponsor/sponsor.toml', 'w')
        markdown.write('+++\n')
        ## REPLACE WITH STANDARD DATA BLOCK        
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
            # Convert author name to LC and replace spaces with dashes to make good file names
            lc_name = (j['data']['authors'][author]['name']).replace(' ', '-').replace('.','').lower()
            markdown = open('output/authors/' + lc_name + '.toml','w')
            markdown.write('+++\n')
        ## REPLACE WITH STANDARD DATA BLOCK            
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
            ## REPLACE WITH STANDARD DATA BLOCK            
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
            except KeyError:
                markdown.write('category = ""\n')

            try:
                index_builder = ""
                for relationship in j['data']['books'][book]['publisher_relationship']:
                    index_builder = index_builder + relationship.encode('utf-8')
                markdown.write('publisher_relationship = %r\n' % index_builder)
            except KeyError:
                markdown.write('publisher_relationship = ""\n')

            try:
                index_builder = ""
                for translator in j['data']['books'][book]['translator']:
                    index_builder = index_builder + translator.encode('utf-8')
                markdown.write('translator = %r\n' % index_builder)
            except KeyError:
                markdown.write('translator = ""\n')

            try:
                index_builder = {}
                for image in j['data']['books'][book]['image']:
                    if image == 'width':
                        index_builder['width'] = j['data']['books'][book]['image'][image]
                    elif image == 'height':
                        index_builder['height'] = j['data']['books'][book]['image'][image]
                    elif image == 'resize_url':
                        index_builder['resize_url'] = (j['data']['books'][book]['image'][image]).encode('utf-8')
                    elif image == 'url':
                        index_builder['url'] = (j['data']['books'][book]['image'][image]).encode('utf-8')
                    elif image == 'type':
                        index_builder['type'] = (j['data']['books'][book]['image'][image]).encode('utf-8')
                    elif image == 'size':
                        index_builder['size'] = j['data']['books'][book]['image'][image]                    
                markdown.write('image = %r\n' % index_builder)
            except KeyError:
                markdown.write('image = ""\n')

            try:
                index_builder = []
                for review in j['data']['books'][book]['review_relationship']:
                    index_builder.append(review.encode('utf-8'))
                markdown.write('review_relationship = %r\n' % index_builder)
            except KeyError:
                markdown.write('review_relationship = ""\n')

            try:
                index_builder = []
                for sponsorship in j['data']['books'][book]['sponsorships_book']:
                    index_builder.append(sponsorship.encode('utf-8'))
                markdown.write('sponsorships_book = %r\n' % index_builder)
            except KeyError:
                markdown.write('sponsorships_book = ""\n')

            try:
                index_builder = []
                for notes in j['data']['books'][book]['notes_relationship']:
                    index_builder.append(notes.encode('utf-8'))
                markdown.write('notes_relationship = %r\n' % index_builder)                
            except KeyError:
                markdown.write('notes_relationship = ""\n')

            markdown.write('+++\n')
            markdown.close()

    # END BOOKS AREA #

    # CALENDAR #

    elif key == 'calendar':
        if not os.path.exists('output/calendar'):
            os.makedirs('output/calendar')

        for calendar in j['data']['calendar']:
          lc_name = (j['data']['calendar'][calendar]['name']).replace(' ', '-').replace('.', '').replace('/','--').lower()
          markdown = open('output/calendar/' + lc_name + '.toml', 'w')
          markdown.write('+++\n')
          markdown.write('index = %r\n' % (calendar).encode('utf-8'))
          markdown.write('name = %r\n' % (j['data']['calendar'][calendar]['name']).encode('utf-8'))
          # IMAGE
          try:
              index_builder = {}
              for image in j['data']['calendar'][calendar]['image']:
                  if image == 'width':
                      index_builder['width'] = j['data']['calendar'][calendar]['image'][image]
                  elif image == 'height':
                      index_builder['height'] = j['data']['calendar'][calendar]['image'][image]
                  elif image == 'resize_url':
                      index_builder['resize_url'] = (j['data']['calendar'][calendar]['image'][image]).encode('utf-8')
                  elif image == 'url':
                      index_builder['url'] = (j['data']['calendar'][calendar]['image'][image]).encode('utf-8')
                  elif image == 'type':
                      index_builder['type'] = (j['data']['calendar'][calendar]['image'][image]).encode('utf-8')
                  elif image == 'size':
                      index_builder['size'] = j['data']['calendar'][calendar]['image'][image]                    
              markdown.write('image = %r\n' % index_builder)
          except KeyError:
              markdown.write('image = ""\n')
          
          try:
            markdown.write('link = %r\n' % (j['data']['calendar'][calendar]['link']).encode('utf-8')) 
          except:
            markdown.write('link = ""\n')

          try:
            markdown.write('date = %r\n' % (j['data']['calendar'][calendar]['date']).encode('utf-8')) 
          except:
            markdown.write('date = ""\n') 
          try:
            markdown.write('start_time = %r\n' % (j['data']['calendar'][calendar]['start_time']).encode('utf-8')) 
          except:
            markdown.write('start_time = ""\n') 
          try:
            markdown.write('end_time = %r\n' % (j['data']['calendar'][calendar]['end_time']).encode('utf-8')) 
          except:
            markdown.write('end_time = ""\n')  
          try:
            markdown.write('time_description = %r\n' % (j['data']['calendar'][calendar]['time_description']).encode('utf-8')) 
          except:
            markdown.write('time_description = "\n')
          try:
            markdown.write('end_time = %r\n' % (j['data']['calendar'][calendar]['end_time']).encode('utf-8')) 
          except:
            markdown.write('end_time = ""\n')   
          try:
            markdown.write('enddate = %r\n' % (j['data']['calendar'][calendar]['enddate']).encode('utf-8')) 
          except:
            markdown.write('enddate = ""\n')
          try:
              markdown.write('is_sponsorship = %r\n' % (j['data']['calendar'][calendar]['is_sponsorship']))
          except KeyError:
              markdown.write('is_sponsorship = ""\n')  

        try:
            index_builder = []
            for authors in j['data']['calendar'][calendar]['authors']:
                index_builder.append(authors.encode('utf-8'))
            markdown.write('authors = %r\n' % index_builder)
        except KeyError:
            markdown.write('authors = ""\n')

        try:
            index_builder = []
            for sponsorship_event in j['data']['calendar'][calendar]['sponsorship_event']:
                index_builder.append(sponsorship_event.encode('utf-8'))
            markdown.write('sponsorship_event = %r\n' % index_builder)
        except KeyError:
            markdown.write('sponsorship_event = ""\n')                  

        try:
          index_builder = ""
          for venues in j['data']['calendar'][calendar]['venues']:
            venue = index_builder + venue.encode('utf-8')
          markdown.write('venues = %r\n' % index_builder)
        except KeyError:
          markdown.write('venues = ""\n')

        try:
          markdown.write((j['data']['calendar'][calendar]['details']).encode('utf-8')) 
        except:
          markdown.write('')
        markdown.close() 

    elif key == 'notes':
      if not os.path.exists('output/notes'):
        os.makedirs('output/notes')

      for note in j['data']['notes']:
        lc_name = (j['data']['notes'][note]['name']).replace(' ', '-').replace('.', '').replace('/','--').lower()
        markdown = open('output/notes/' + lc_name + '.toml', 'w')
        markdown.write('+++\n')
        ## REPLACE WITH STANDARD DATA BLOCK        
        markdown.write('index = %r\n' % (note).encode('utf-8'))
        markdown.write('name = %r\n' % (j['data']['notes'][note]['name']).encode('utf-8'))
        markdown.write('type = %r\n' % (j['data']['notes'][note]['type']).encode('utf-8'))

        try:
          markdown.write('url = %r\n' % (j['data']['notes'][note]['url']).encode('utf-8'))
        except KeyError:
          markdown.write('url = ""\n')
        try:
          markdown.write('shareimage = %r\n' % (j['data']['notes'][note]['shareimage']).encode('utf-8'))
        except KeyError:
          markdown.write('shareimage = ""\n') 
        try:
          markdown.write('twitterauto = %r\n' % (j['data']['notes'][note]['twitterauto']).encode('utf-8'))
        except KeyError:
          markdown.write('twitterauto = ""\n')               
        try:
          markdown.write('facebookauto = %r\n' % (j['data']['notes'][note]['facebookauto']).encode('utf-8'))
        except KeyError:
          markdown.write('facebookauto = ""\n')
        try:
          markdown.write('make_image_tweet = %r\n' % (j['data']['notes'][note]['make_image_tweet']))
        except KeyError:
          markdown.write('make_image_tweet = ""\n')

        try:
            index_builder = []
            for byline in j['data']['notes'][note]['byline']:
                index_builder.append(byline.encode('utf-8'))
            markdown.write('byline = %r\n' % index_builder)
        except KeyError:
            markdown.write('byline = ""\n')
        try:
            index_builder = []
            for tags_notes in j['data']['notes'][note]['tags_notes']:
                index_builder.append(tags_notes.encode('utf-8'))
            markdown.write('tags_notes = %r\n' % index_builder)
        except KeyError:
            markdown.write('tags_notes = ""\n')
        try:
            index_builder = []
            for authors_notes in j['data']['notes'][note]['authors_notes']:
                index_builder.append(authors_notes.encode('utf-8'))
            markdown.write('authors_notes = %r\n' % index_builder)
        except KeyError:
            markdown.write('authors_notes = ""\n')
        try:
            index_builder = []
            for books in j['data']['notes'][note]['books']:
                index_builder.append(books.encode('utf-8'))
            markdown.write('books = %r\n' % index_builder)
        except KeyError:
            markdown.write('books = ""\n')                                      


        markdown.write('+++\n')
        
        markdown.write((j['data']['notes'][note]['post']).encode('utf-8'))

        markdown.close()

    elif key == 'publishers':
      if not os.path.exists('output/publishers'):
        os.makedirs('output/publishers')

      for publisher in j['data']['publishers']:
        lc_name = (j['data']['publishers'][publisher]['name']).replace(' ', '-').replace('.','').replace('/','--').lower()
        markdown = open('output/publishers/' + lc_name + '.toml', 'w')
        markdown.write('+++\n')
        ## REPLACE WITH STANDARD DATA BLOCK        
        markdown.write('index = %r\n' % publisher.encode('utf-8'))
        try:
          markdown.write('create_date = %r\n' % j['data']['publishers'][publisher]['create_date'])
        except KeyError:
          markdown.write('create_date = ""\n')
        try:
          markdown.write('last_updated = %r\n' % (j['data']['publishers'][publisher]['last_updated']).encode('utf-8'))
        except KeyError:
          markdown.write('last_updated = ""\n')
        markdown.write('name = %r\n' % (j['data']['publishers'][publisher]['name']).encode('utf-8'))
        try:
          markdown.write('publish_date = %r\n' % (j['data']['publishers'][publisher]['publish_date']).encode('utf-8'))        
        except:
          markdown.write('publish date = ""\n') 
        try:
            index_builder = []
            for publisher in j['data']['publishers'][publisher]['books_by_this_publisher']:
                index_builder.append(publisher.encode('utf-8'))
            markdown.write('books_by_this_publisher = %r\n' % index_builder)
        except KeyError:
            markdown.write('books_by_this_publisher = ""\n')          
        # books_by_this_publisher
        markdown.write('+++\n')
        markdown.close()

    elif key == 'reviews':
      if not os.path.exists('output/reviews'):
        os.makedirs('output/reviews')

      for review in j['data']['reviews']:
        lc_name = (j['data']['reviews'][review]['name']).replace(' ', '-').replace('.','').lower()
        markdown = open('output/reviews/' + lc_name + '.toml', 'w')
        markdown.write('+++\n')
        ## REPLACE WITH STANDARD DATA BLOCK
        markdown.write('index = %r\n' % review.encode('utf-8'))
        markdown.write('name = %r\n' % (j['data']['reviews'][review]['name']).encode('utf-8'))        
        markdown.write('dek = %r\n' % (j['data']['reviews'][review]['dek']).encode('utf-8'))
        try:
          markdown.write('facebookauto = %r\n' % (j['data']['reviews'][review]['facebookauto']).encode('utf-8'))
        except KeyError:
          markdown.write

        try:
          markdown.write('twitterauto = %r\n' % (j['data']['reviews'][review]['twitterauto']).encode('utf-8'))
        except KeyError:
          markdown.write

        try:
            index_builder = []
            for by in j['data']['reviews'][review]['by']:
                index_builder.append(by.encode('utf-8'))
            markdown.write('by = %r\n' % index_builder)
        except KeyError:
            markdown.write('by = ""\n')

        try:
            index_builder = []
            for books_in_this_review in j['data']['reviews'][review]['books_in_this_review']:
                index_builder.append(books_in_this_review.encode('utf-8'))
            markdown.write('books_in_this_review = %r\n' % index_builder)
        except KeyError:
            markdown.write('books_in_this_review = ""\n')

        try:
            index_builder = []
            for tags_reviews in j['data']['reviews'][review]['tags_reviews']:
                index_builder.append(tags_reviews.encode('utf-8'))
            markdown.write('tags_reviews = %r\n' % index_builder)
        except KeyError:
            markdown.write('tags_reviews = ""\n')

        try:
            index_builder = []
            for authors_reviews in j['data']['reviews'][review]['authors_reviews']:
                index_builder.append(authors_reviews.encode('utf-8'))
            markdown.write('authors_reviews = %r\n' % index_builder)
        except KeyError:
            markdown.write('authors_reviews = ""\n')                                  
        markdown.write('+++\n\n')
        markdown.write((j['data']['reviews'][review]['review']).encode('utf-8'))
        markdown.close()

    elif key == 'tags':
      if not os.path.exists('output/tags'):
        os.makedirs('output/tags')

      for tag in j['data']['tags']:
        lc_name = (j['data']['tags'][tag]['name']).replace(' ', '-').replace('.','').replace('/','--').lower()
        markdown = open('output/tags/' + lc_name + '.toml', 'w')
        markdown.write('+++\n')
        ## REPLACE WITH STANDARD DATA BLOCK
        markdown.write('index = %r\n' % tag.encode('utf-8'))
        markdown.write('name = %r\n' % (j['data']['tags'][tag]['name']).encode('utf-8'))                
        try:
            markdown.write('is_column = %r\n' % (j['data']['tags'][tag]['is_column']))
        except KeyError:
            markdown.write('is_column = False\n')  

        try:
            index_builder = []
            for reviews in j['data']['tags'][tag]['reviews']:
                index_builder.append(reviews.encode('utf-8'))
            markdown.write('reviews = %r\n' % index_builder)
        except KeyError:
            markdown.write('reviews = ""\n')
        try:
            index_builder = []
            for notes in j['data']['tags'][tag]['notes']:
                index_builder.append(notes.encode('utf-8'))
            markdown.write('notes = %r\n' % index_builder)
        except KeyError:
            markdown.write('notes = ""\n')        
            
        markdown.write('+++\n\n')  
        markdown.close()   





#    # TEMPLATE AREA
#   elif key == 'xxxx':
#        if not os.path.exists('output/xxxx'):
#            os.makedirs('output/xxxx')
#
#        for book in j['data']['xxxx']:
#           lc_name = (j['data']['xxxx'][xxxx]['name']).replace(' ', '-').replace('.','').lower()
#            markdown = open('output/xxxx/' + lc_name + '.toml','w')
#            markdown.write('+++\n')
#            markdown.write('+++\n')  
#            markdown.close()                            
#

