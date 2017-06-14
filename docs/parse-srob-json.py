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
