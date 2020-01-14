import os
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def hogPost(url,message,api,tid):
	logger.info("Posting with image")
	filename = 'hogtemp.jpg'
	if url != "":
		request = requests.get(url, stream = True)
		if request.status_code == 200:
			with open(filename,'wb') as image:
				for chunk in request:
					image.write(chunk)
			api.update_with_media(filename,message + " A PHOTO OF THE SUBJECT INCLUDED. ",in_reply_to_status_id=tid)
			os.remove(filename)
		else:
			logger.info("S'pose not")
			api.update_status(message,in_reply_to_status_id=tid)
	else:
		logger.info("S'pose not")
		api.update_status(message,in_reply_to_status_id=tid)