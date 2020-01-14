from pygbif import occurrences as occ
import json
from datetime import datetime

def latStat(left,right,top,bottom):
	latCheck = str(bottom) + "," + str(top)
	longCheck = str(left) + "," + str(right)
	return [latCheck,longCheck]


#IF NOT HOG FOUND FIND CLOSEST ONE

def hogSearch(left,right,top,bottom):
	l = left
	r = right
	t = top
	b = bottom
	coords = latStat(l,r,t,b)
	hog = occ.search(decimalLatitude = coords[0], decimalLongitude = coords[1], scientificName = 'Sus scrofa')
	print(hog['count'])
	dist = 0
	while hog['count'] == 0:
		dist += 0.7
		l -= .01
		r += .01
		t += .01
		b -= .01
		coords = latStat(l,r,t,b)
		print(coords[0],coords[1])
		hog = occ.search(decimalLatitude = coords[0], decimalLongitude = coords[1], scientificName = 'Sus scrofa')



	hogHistoric = []
	hog2019 = []
	nDic = hog['results']
	print(nDic)

	for sightings in nDic:
		si = sightings["eventDate"]
		hogHistoric.append(si)
		if '2019' in sightings["eventDate"]:
			hog2019.append(si)

	pigs2019 = []
	for hd in hog2019:
		nd = hd[:10]
		dd = nd.split('-',2)
		pigs2019.append(datetime(int(dd[0]),int(dd[1]),int(dd[2])))

	allpigs = []
	for allHog in hogHistoric:
		nd = allHog[:10]
		dd = nd.split('-',2)
		allpigs.append(datetime(int(dd[0]),int(dd[1]),int(dd[2])))

	if pigs2019 != []:
		dayDif = str(round((abs(datetime.now() - max(pigs2019)).total_seconds()) / 86400,2))
		bigDay = str(max(pigs2019))[:10]
	else:
		dayDif = str(round((abs(datetime.now() - max(allpigs)).total_seconds()) / 86400,2))
		bigDay = str(max(allpigs))[:10]

	print(dayDif)
	print(bigDay)


	str1 = "WARNING: WE FOUND " + str(len(hogHistoric)) + " HOG RECORDS IN YOUR AREA. "
	str2 = "MOST RECENT HOG WAS SEEN " + dayDif +" DAYS AGO. CHOOSE A MORE SPECIFIC LOCATION FOR BETTER RESULTS."
	pigPic = []
	for ss in nDic:
		print(ss["eventDate"][:10])
		if ss["eventDate"][:10] == str(bigDay):
			pigPic = ss["media"]
			break
	str3 = pigPic[0]['identifier']

	if dist != 0:
		totS = "WARNING: A HOG WAS SPOTTED " + str(dist) + " MILES FROM YOU " + dayDif + " DAYS AGO. "
	else:
		totS = str1+str2

	hogDic = [totS,str3]
	return hogDic