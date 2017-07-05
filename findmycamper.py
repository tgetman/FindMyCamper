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
img_url1 = 'http://worldversus.com/img/george-clooney.jpg'
img_url2 = 'http://i1.wp.com/peopledotcom.files.wordpress.com/2017/05/george-clooney5.jpg?crop=0px%2C0px%2C1454px%2C970.66483516484px&resize=728%2C486&ssl=1'

detect1 = CF.face.detect(img_url1)
print detect1


detect2 = CF.face.detect(img_url2)
print detect2


result1 = CF.face.verify('41bf98c3-4857-4dfe-a9d2-9f2d3f2049f9' , '858adce5-b94d-4e36-828b-d75b636f0eea' )
result2 = CF.face.verify('41bf98c3-4857-4dfe-a9d2-9f2d3f2049f9', '64ddbc97-7496-480d-8e1d-f93a25f8933f' )
result3 = CF.face.verify('41bf98c3-4857-4dfe-a9d2-9f2d3f2049f9', '41bf98c3-4857-4dfe-a9d2-9f2d3f2049f9')

print result1
print result2
print result3