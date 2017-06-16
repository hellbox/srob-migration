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

	#Let's start with the single items
	if key == 'about':		
	    #create folder with item name
	    if not os.path.exists('output/about'):
	        os.makedirs('output/about')

	    #create file and structure
	    markdown = open('output/about/about.md','w')
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
		markdown = open('output/privacy/privacy.md','w')
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
		markdown = open('output/resources/resources.md','w')
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
		markdown = open('output/submissions/submissions.md','w')
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
		markdown = open('output/sponsor/sponsor.md','w')
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

	#And now for the things with more complex relationships. Here we go

	elif key == 'authors':
		if not os.path.exists('output/authors'):
			os.makedirs('output/authors')

		for author in j['data']['authors']:


			#Convert author name to LC and replace spaces with dashes to make good file names
			lc_name = (j['data']['authors'][author]['name']).replace(' ', '-').replace('.','').lower()
			markdown = open('output/authors/' + lc_name + '.md','w')
			markdown.write('+++\n')
			markdown.write('index = %r\n' % author.encode('utf-8'))

			########### HELP ME PLEASE ##################
			
			# This throws a 'KeyError', so somewhere in the loop, there is an entry that doesn't have the expected key. 
			# markdown.write('_sort_create_date = %d\n' % j['data']['authors'][author]['_sort_create_date'])

			# The solution for that is to wrap the call in get(), but this throws a TypeError:
			# markdown.write('_sort_create_date = %d\n' % j.get(j['data']['authors'][author]['_sort_create_date']))

			# That makes me think my formatting is correct for get(), and becuase it's returning "none", but it expects a number, it's erroring. 
			
			# But if I do this, with a unicode string converted to UTF-8, I get an attribute error. 			
			# markdown.write('alphabetize_by = %r\n' % j.get(j['data']['authors'][author]['alphabetize_by']).encode('utf-8'))

			# Or, without UTF-8 encoding, I get a KeyError again.
			# markdown.write('alphabetize_by = %r\n' % j.get(j['data']['authors'][author]['alphabetize_by']))

			# So, I think I'm doing something wrong here, but I'm cahsing my tail figuring it out. Ideas?


			######## END HELP ME PLEASE SECTION #########
			




			### CALLS COMMENTED OUT UNTIL I FIGURE OUT HOW THE ABOVE SHOULD WORK

			#markdown.write('_sort_create_date = %d\n' % get(j['data']['authors'][author]['_sort_create_date']))
			#markdown.write('_sort_last_updated = %d\n' % j['data']['authors'][author]['_sort_last_updated'])
			########alphabetize_by = j.get((j['data']['authors'][author]['alphabetize_by']).encode('utf-8'))
			#markdown.write('isDraft = %r\n' % (j['data']['authors'][author]['isDraft']).encode('utf-8'))
			##books loop
			#markdown.write('create_date = %r\n' % (j['data']['authors'][author]['create_date']).encode('utf-8'))
			#markdown.write('isDraft = %r\n' % (j['data']['authors'][author]['isDraft']).encode('utf-8'))
			#markdown.write('is_seattle__pnw_writer = %r\n' % (j['data']['authors'][author]['is_seattle__pnw_writer']).encode('utf-8'))
			#markdown.write('last_updated = %r\n' % (j['data']['authors'][author]['last_updated']).encode('utf-8'))
			#markdown.write('name = %r\n' % (j['data']['authors'][author]['name']).encode('utf-8'))
			##notes loop
			#markdown.write('preview_url = %r\n' % (j['data']['authors'][author]['preview_url']).encode('utf-8'))
			#markdown.write('publish_date = %r\n' % (j['data']['authors'][author]['publish_date']).encode('utf-8'))
			
			#books
			#notes
			markdown.write('+++\n')			
			markdown.close()

