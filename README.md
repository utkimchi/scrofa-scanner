# scrofa-scanner

A locally hosted twitter bot @scrofa_scanner that tells a user how close the last recorded hog sighting was. When an account tweets at the bot, the bot takes the location metadata of the tweet and queries GBIF's (https://www.gbif.org) API using the GPS coords from the tweet. The closest recorded hog sighting with a photo is returned and posted to the account. Depending on how close the hog sighting is to the user the text above the photo is alarming or passive.


![alt text](https://github.com/utkimchi/scrofa-scanner/blob/master/scrofascanner.png)
