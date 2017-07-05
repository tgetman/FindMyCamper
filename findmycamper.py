#!/usr/bin/python

import cognitive_face as CF
import httplib, urllib, base64

headers = {
	# Request headers
	'Content-Type': 'application/json',
	'Ocp-Apim-Subscription-Key': 'fd330f9307be48f4bd4a59c5b57ab4cf',
}

params = urllib.urlencode({
	# Request parameters
	'returnFaceId': 'true',
	'returnFaceLandmarks': 'false',
})


KEY = 'fd330f9307be48f4bd4a59c5b57ab4cf'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
#img_url1 = 'http://worldversus.com/img/george-clooney.jpg'
#img_url2 = 'https://thumbs.dreamstime.com/z/two-women-hugging-smiling-15631732.jpg'

urls = []
numberofphotos = int(raw_input("enter number of photos"))

while len(urls) < numberofphotos:
	urls.insert(0, raw_input("enter photo urls"))
	print urls
	print len(urls)




#img_url1 = urls[0]
#img_url2 = urls[1]

#detect1 = CF.face.detect(img_url1)
#print detect1
#faceId1 = detect1[0]['faceId']
#print faceId1

#detect2 = CF.face.detect(img_url2)
#print detect2
#faceId2 = detect2[0]['faceId']
#print faceId2
#faceId3 = detect2[1]['faceId']
#print faceId3

#result1 = CF.face.verify(faceId1 , faceId2 )
#result2 = CF.face.verify(faceId1, faceId3 )


#print result1
#print result2

#if result1['isIdentical']== 'True':
#	print "face 1 and 2"
#if result2['isIdentical']== 'True':
#	print "face 1 and 3"


