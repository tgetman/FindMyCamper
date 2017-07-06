#!/usr/bin/python

import cognitive_face as CF
import httplib, urllib, base64
from azure.storage.file import FileService
from azure.storage.file import ContentSettings



file_service = FileService(account_name='cs28b777e132996x486dx860', account_key='+NXtMDMhWvZvxuHfr12oCZNIo/6WT7Y3gl0Mq91QRP2tUeIJ6bEL/acgFK+4f8LHX5s+AWRgejNvfwWtoH7Ivg==')
file_service.create_share('myshare')


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
file_service.get_file_to_path('myshare', None, 'myfile', 'out-IMG_2024.png')

myChild = CF.face.detect('out-IMG_2024.png')
myChildFaceId = myChild[0]['faceId']

urls = []
numberofphotos = int(raw_input("enter number of photos "))
count = 0

while len(urls) < numberofphotos:
	urls.insert(0, raw_input("enter photo urls "))
	print urls
	print len(urls)


if len(urls) == 1:
	img_url1 = urls[0]
	
	
	detect1 = CF.face.detect(img_url1)
	
	if len(detect1) == 1:
		faceId1 = detect1[0]['faceId']
		
		result1 = CF.face.verify(myChildFaceId, faceId1)
		
		results = (result1)
		
		if results[0]['isIdentical'] == True:
			print "match"
			
	if len(detect1) == 2:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
		
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		
		results = (result1,result2)
		
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print "match"
			
	if len(detect1) == 3:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
		faceId3 = detect1[2]['faceId']
		
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		
		results = (result1,result2,result3)
		
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print "match"
			
	if len(detect1) == 4:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
		faceId3 = detect1[2]['faceId']
		faceId4 = detect1[3]['faceId']
		
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		
		results = (result1,result2,result3,result4)
		
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print "match"
			
	if len(detect1) == 5:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
		faceId3 = detect1[2]['faceId']
		faceId4 = detect1[3]['faceId']
		faceId5 = detect1[4]['faceId']
		
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
		
		results = (result1,result2,result3,result4,result5)
		
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print "match"
			
	if len(detect1) == 6:
			faceId1 = detect1[0]['faceId']
			faceId2 = detect1[1]['faceId']
			faceId3 = detect1[2]['faceId']
			faceId4 = detect1[3]['faceId']
			faceId5 = detect1[4]['faceId']
			faceId6 = detect1[5]['faceId']
			
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			
			results = (result1,result2,result3,result4,result5,result6)
			
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print "match"
	
	if len(detect1) == 7:
			faceId1 = detect1[0]['faceId']
			faceId2 = detect1[1]['faceId']
			faceId3 = detect1[2]['faceId']
			faceId4 = detect1[3]['faceId']
			faceId5 = detect1[4]['faceId']
			faceId6 = detect1[5]['faceId']
			faceId7 = detect1[6]['faceId']
			
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
			
			results = (result1,result2,result3,result4,result5,result6,result7)
			
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print "match"

	
if len(urls) == 2:
	img_url1 = urls[0]
	img_url2 = urls[1]
	
	detect1 = CF.face.detect(img_url1)
	detect2 = CF.face.detect(img_url2)
		
	faceId1 = detect1[0]['faceId']
	faceId2 = detect2[0]['faceId']
		
	result1 = CF.face.verify(myChildFaceId, faceId1)
	result2 = CF.face.verify(myChildFaceId, faceId2)
	

	
if len(urls) == 3:
	img_url1 = urls[0]
	img_url2 = urls[1]
	img_url3 = urls[2]
	
	detect1 = CF.face.detect(img_url1)
	detect2 = CF.face.detect(img_url2)
	detect3 = CF.face.detect(img_url3)
			
	faceId1 = detect1[0]['faceId']
	faceId2 = detect2[0]['faceId']
	faceId3 = detect3[0]['faceId']
			
	result1 = CF.face.verify(myChildFaceId, faceId1)
	result2 = CF.face.verify(myChildFaceId, faceId2)
	result3 = CF.face.verify(myChildFaceId, faceId3)

if len(urls) == 4:
	img_url1 = urls[0]
	img_url2 = urls[1]
	img_url3 = urls[2]
	img_url4 = urls[3]
	
	detect1 = CF.face.detect(img_url1)
	detect2 = CF.face.detect(img_url2)
	detect3 = CF.face.detect(img_url3)
	detect4 = CF.face.detect(img_url4)
			
	faceId1 = detect1[0]['faceId']
	faceId2 = detect2[0]['faceId']
	faceId3 = detect3[0]['faceId']
	faceId4 = detect4[0]['faceId']
			
	result1 = CF.face.verify(myChildFaceId, faceId1)
	result2 = CF.face.verify(myChildFaceId, faceId2)
	result3 = CF.face.verify(myChildFaceId, faceId3)
	result4 = CF.face.verify(myChildFaceId, faceId4)
if len(urls) == 5:
	img_url1 = urls[0]
	img_url2 = urls[1]
	img_url3 = urls[2]
	img_url4 = urls[3]
	img_url5 = urls[4]
if len(urls) == 6:
	img_url1 = urls[0]
	img_url2 = urls[1]
	img_url3 = urls[2]
	img_url4 = urls[3]
	img_url5 = urls[4]
	img_url6 = urls[5]
if len(urls) == 7:
	img_url1 = urls[0]
	img_url2 = urls[1]
	img_url3 = urls[2]
	img_url4 = urls[3]
	img_url5 = urls[4]
	img_url6 = urls[5]
	img_url7 = urls[6]
if len(urls) == 8:
	img_url1 = urls[0]
	img_url2 = urls[1]
	img_url3 = urls[2]
	img_url4 = urls[3]
	img_url5 = urls[4]
	img_url6 = urls[5]
	img_url7 = urls[6]
	img_url8 = urls[7]
if len(urls) == 9:
	img_url1 = urls[0]
	img_url2 = urls[1]
	img_url3 = urls[2]
	img_url4 = urls[3]
	img_url5 = urls[4]
	img_url6 = urls[5]
	img_url7 = urls[6]
	img_url8 = urls[7]
	img_url9 = urls[8]
if len(urls) == 10:
	img_url1 = urls[0]
	img_url2 = urls[1]
	img_url3 = urls[2]
	img_url4 = urls[3]
	img_url5 = urls[4]
	img_url6 = urls[5]
	img_url7 = urls[6]
	img_url8 = urls[7]
	img_url9 = urls[8]
	img_url10 = urls[9]
	

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


