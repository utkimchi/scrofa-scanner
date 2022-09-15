# scrofa-scanner

A locally hosted twitter bot @scrofa_scanner that tells a user how close the last recorded hog sighting was. When an account tweets "help" or "save me" at the bot, the bot takes the location metadata of the tweet and queries GBIF's (https://www.gbif.org) API using the tweet's GPS coords. The closest recorded hog sighting with a photo is returned and posted in response to the call for help. Depending on how close the hog sighting is to the user, the text above the photo may shift in tone.


![alt text](https://github.com/utkimchi/scrofa-scanner/blob/master/scrofascanner.png)


Further work may assist with identifying if the photo actually contains a hog or not. 
