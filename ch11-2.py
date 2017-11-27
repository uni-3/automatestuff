# config utf-8

import requests
import bs4

import re
import os


KEYWORD = 'cat'

MAX_IMAGES = 10

SAVE_DIR = 'images'
os.makedirs(SAVE_DIR, exist_ok=True)



def get_flickr():
	url = 'https://www.flickr.com/search/?text=' + KEYWORD
	res = requests.get(url)
	res.raise_for_status()

	return res.text

def get_images(res_text):
	sp = bs4.BeautifulSoup(res_text, 'lxml')
	links = sp.select('.photo-list-photo-view')

	for i in range(min(MAX_IMAGES, len(links))):

		img_url = 'https:' + re.search(r'url\((.+?)\)', links[i].get('style')).group(1)
		print("download from...: ", img_url)

		img_res = requests.get(img_url)
		img_res.raise_for_status()
		img_file = open(os.path.join(SAVE_DIR, os.path.basename(img_url)), 'wb')

		for chunk in img_res.iter_content(100000):
			img_file.write(chunk)
		img_file.close()

if __name__ == '__main__':
	res_text = get_flickr()

	get_images(res_text)


