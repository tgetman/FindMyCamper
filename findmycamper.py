#!/usr/bin/python


import cognitive_face as CF
import http.client, urllib.request, urllib.parse, urllib.error, base64
from azure.storage.file import FileService
from azure.storage.file import ContentSettings
from tkinter import Tk, Label, Button
from tkinter.filedialog import askopenfilename


file_service = FileService(account_name='cs28b777e132996x486dx860', account_key='+NXtMDMhWvZvxuHfr12oCZNIo/6WT7Y3gl0Mq91QRP2tUeIJ6bEL/acgFK+4f8LHX5s+AWRgejNvfwWtoH7Ivg==')
file_service.create_share('myshare')


headers = {
	# Request headers
	'Content-Type': 'application/json',
	'Ocp-Apim-Subscription-Key': 'fd330f9307be48f4bd4a59c5b57ab4cf',
}

params = urllib.parse.urlencode({
	# Request parameters
	'returnFaceId': 'true',
	'returnFaceLandmarks': 'false',
})


KEY = 'fd330f9307be48f4bd4a59c5b57ab4cf'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)


pathtochild = str(input("Drag Photo of Your Child"))
print(pathtochild)

numbertocut = pathtochild.rfind("/") + 1

childphoto = pathtochild[numbertocut:]

print(pathtochild[numbertocut:])


file_service.create_file_from_path(
	'myshare',
	None, # We want to create this blob in the root directory, so we specify None for the directory_name
	'myfile',
	pathtochild,
	content_settings=ContentSettings(content_type='image/png'))
	
file_service.get_file_to_path('myshare', None, 'myfile', 'out-'+childphoto)



myChild = CF.face.detect('out-'+childphoto)
myChildFaceId = myChild[0]['faceId']

urls = []
numberofphotos = int(input("enter number of photos "))
count = 0

while len(urls) < numberofphotos:
	urls.insert(0, input("enter photo urls "))
	print (urls)
	print((len(urls)))
	


if len(urls) == 1:
	img_url1 = urls[0]
	
	
	detect1 = CF.face.detect(img_url1)
	
	if len(detect1) == 1:
		faceId1 = detect1[0]['faceId']
		
		result1 = CF.face.verify(myChildFaceId, faceId1)
		
	
		
		if result1['isIdentical'] == True:
			print("match")
		else:
			print("no match")

			
	if len(detect1) == 2:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
		
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		
		results = (result1,result2)
		
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print ("match")
		else:
			print ("no match")
			
	if len(detect1) == 3:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
		faceId3 = detect1[2]['faceId']
		
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		
		results = (result1,result2,result3)
		
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print ("match")
		else:
			print ("no match")
			
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
			print ("match")
		else:
			print ("no match")
			
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
			print ("match")
		else:
			print ("no match")
			
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
				print("match")
			else:
				print("no match")
	
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
				print("match")
			else:
				print("no match")

	
if len(urls) == 2:
	img_url1 = urls[0]
	img_url2 = urls[1]
	
	detect1 = CF.face.detect(img_url1)
	detect2 = CF.face.detect(img_url2)
		
	if len(detect1) == 1:
			faceId1 = detect1[0]['faceId']
			
			result1 = CF.face.verify(myChildFaceId, faceId1)
			

			
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	if len(detect1) == 2:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
		
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
			
		results = (result1,result2)
			
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
				
	if len(detect1) == 3:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
		faceId3 = detect1[2]['faceId']
			
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
			
		results = (result1,result2,result3)
			
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
				
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
			print("match")
		else:
			print("no match")
				
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
			print("match")
		else:
			print("no match")
				
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
				print("match")
			else:
				print("no match")
		
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
				print("match")
			else:
				print("no match")
	if len(detect2) == 1:
			faceId1 = detect2[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
		
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect2) == 2:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 3:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 4:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
		faceId4 = detect2[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 5:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
		faceId4 = detect2[3]['faceId']
		faceId5 = detect2[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 6:
			faceId1 = detect2[0]['faceId']
			faceId2 = detect2[1]['faceId']
			faceId3 = detect2[2]['faceId']
			faceId4 = detect2[3]['faceId']
			faceId5 = detect2[4]['faceId']
			faceId6 = detect2[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	if len(detect2) == 7:
			faceId1 = detect2[0]['faceId']
			faceId2 = detect2[1]['faceId']
			faceId3 = detect2[2]['faceId']
			faceId4 = detect2[3]['faceId']
			faceId5 = detect2[4]['faceId']
			faceId6 = detect2[5]['faceId']
			faceId7 = detect2[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
			else:
				print("no match")

	

	
if len(urls) == 3:
	img_url1 = urls[0]
	img_url2 = urls[1]
	img_url3 = urls[2]
	
	detect1 = CF.face.detect(img_url1)
	detect2 = CF.face.detect(img_url2)
	detect3 = CF.face.detect(img_url3)
	
	
	if len(detect1) == 1:
			faceId1 = detect1[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					
		
					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect1) == 2:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect1) == 3:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
		faceId3 = detect1[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
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
			print("match")
		else:
			print("no match")
						
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
			print("match")
		else:
			print("no match")
						
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
				print("match")
			else:
				print("no match")
				
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
				print("match")
			else:
				print("no match")
	if len(detect2) == 1:
			faceId1 = detect2[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect2) == 2:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 3:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 4:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
		faceId4 = detect2[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 5:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
		faceId4 = detect2[3]['faceId']
		faceId5 = detect2[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 6:
			faceId1 = detect2[0]['faceId']
			faceId2 = detect2[1]['faceId']
			faceId3 = detect2[2]['faceId']
			faceId4 = detect2[3]['faceId']
			faceId5 = detect2[4]['faceId']
			faceId6 = detect2[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	if len(detect2) == 7:
			faceId1 = detect2[0]['faceId']
			faceId2 = detect2[1]['faceId']
			faceId3 = detect2[2]['faceId']
			faceId4 = detect2[3]['faceId']
			faceId5 = detect2[4]['faceId']
			faceId6 = detect2[5]['faceId']
			faceId7 = detect2[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	
	if len(detect3) == 1:
			faceId1 = detect3[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					
	
					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect3) == 2:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 3:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 4:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
		faceId4 = detect3[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 5:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
		faceId4 = detect3[3]['faceId']
		faceId5 = detect3[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 6:
			faceId1 = detect3[0]['faceId']
			faceId2 = detect3[1]['faceId']
			faceId3 = detect3[2]['faceId']
			faceId4 = detect3[3]['faceId']
			faceId5 = detect3[4]['faceId']
			faceId6 = detect3[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	if len(detect3) == 7:
			faceId1 = detect3[0]['faceId']
			faceId2 = detect3[1]['faceId']
			faceId3 = detect3[2]['faceId']
			faceId4 = detect3[3]['faceId']
			faceId5 = detect3[4]['faceId']
			faceId6 = detect3[5]['faceId']
			faceId7 = detect3[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
			else:
				print("no match")

	

if len(urls) == 4:
	img_url1 = urls[0]
	img_url2 = urls[1]
	img_url3 = urls[2]
	img_url4 = urls[3]
	
	detect1 = CF.face.detect(img_url1)
	detect2 = CF.face.detect(img_url2)
	detect3 = CF.face.detect(img_url3)
	detect4 = CF.face.detect(img_url4)
	
	if len(detect1) == 1:
			faceId1 = detect1[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					
		
					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect1) == 2:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect1) == 3:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
		faceId3 = detect1[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
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
			print("match")
		else:
			print("no match")
						
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
			print("match")
		else:
			print("no match")
						
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
				print("match")
			else:
				print("no match")
				
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
				print("match")
			else:
				print("no match")
	if len(detect2) == 1:
			faceId1 = detect2[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect2) == 2:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 3:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 4:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
		faceId4 = detect2[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 5:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
		faceId4 = detect2[3]['faceId']
		faceId5 = detect2[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 6:
			faceId1 = detect2[0]['faceId']
			faceId2 = detect2[1]['faceId']
			faceId3 = detect2[2]['faceId']
			faceId4 = detect2[3]['faceId']
			faceId5 = detect2[4]['faceId']
			faceId6 = detect2[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	if len(detect2) == 7:
			faceId1 = detect2[0]['faceId']
			faceId2 = detect2[1]['faceId']
			faceId3 = detect2[2]['faceId']
			faceId4 = detect2[3]['faceId']
			faceId5 = detect2[4]['faceId']
			faceId6 = detect2[5]['faceId']
			faceId7 = detect2[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	
	if len(detect3) == 1:
			faceId1 = detect3[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					
	
					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect3) == 2:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 3:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 4:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
		faceId4 = detect3[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 5:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
		faceId4 = detect3[3]['faceId']
		faceId5 = detect3[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 6:
			faceId1 = detect3[0]['faceId']
			faceId2 = detect3[1]['faceId']
			faceId3 = detect3[2]['faceId']
			faceId4 = detect3[3]['faceId']
			faceId5 = detect3[4]['faceId']
			faceId6 = detect3[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	if len(detect3) == 7:
			faceId1 = detect3[0]['faceId']
			faceId2 = detect3[1]['faceId']
			faceId3 = detect3[2]['faceId']
			faceId4 = detect3[3]['faceId']
			faceId5 = detect3[4]['faceId']
			faceId6 = detect3[5]['faceId']
			faceId7 = detect3[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
	if len(detect4) == 1:
			faceId1 = detect4[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect4) == 2:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 3:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
		faceId3 = detect4[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 4:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
		faceId3 = detect4[2]['faceId']
		faceId4 = detect4[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 5:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
		faceId3 = detect4[2]['faceId']
		faceId4 = detect4[3]['faceId']
		faceId5 = detect4[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 6:
			faceId1 = detect4[0]['faceId']
			faceId2 = detect4[1]['faceId']
			faceId3 = detect4[2]['faceId']
			faceId4 = detect4[3]['faceId']
			faceId5 = detect4[4]['faceId']
			faceId6 = detect4[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect4) == 7:
			faceId1 = detect4[0]['faceId']
			faceId2 = detect4[1]['faceId']
			faceId3 = detect4[2]['faceId']
			faceId4 = detect4[3]['faceId']
			faceId5 = detect4[4]['faceId']
			faceId6 = detect4[5]['faceId']
			faceId7 = detect4[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")


if len(urls) == 5:
	img_url1 = urls[0]
	img_url2 = urls[1]
	img_url3 = urls[2]
	img_url4 = urls[3]
	img_url5 = urls[4]
	
	detect1 = CF.face.detect(img_url1)
	detect2 = CF.face.detect(img_url2)
	detect3 = CF.face.detect(img_url3)
	detect4 = CF.face.detect(img_url4)
	detect5 = CF.face.detect(img_url5)
	
	if len(detect1) == 1:
			faceId1 = detect1[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					
		
					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect1) == 2:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect1) == 3:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
		faceId3 = detect1[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
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
			print("match")
		else:
			print("no match")
						
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
			print("match")
		else:
			print("no match")
						
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
				print("match")
			else:
				print("no match")
				
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
				print("match")
			else:
				print("no match")
	if len(detect2) == 1:
			faceId1 = detect2[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect2) == 2:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 3:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 4:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
		faceId4 = detect2[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 5:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
		faceId4 = detect2[3]['faceId']
		faceId5 = detect2[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 6:
			faceId1 = detect2[0]['faceId']
			faceId2 = detect2[1]['faceId']
			faceId3 = detect2[2]['faceId']
			faceId4 = detect2[3]['faceId']
			faceId5 = detect2[4]['faceId']
			faceId6 = detect2[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	if len(detect2) == 7:
			faceId1 = detect2[0]['faceId']
			faceId2 = detect2[1]['faceId']
			faceId3 = detect2[2]['faceId']
			faceId4 = detect2[3]['faceId']
			faceId5 = detect2[4]['faceId']
			faceId6 = detect2[5]['faceId']
			faceId7 = detect2[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	
	if len(detect3) == 1:
			faceId1 = detect3[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					
	
					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect3) == 2:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 3:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 4:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
		faceId4 = detect3[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 5:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
		faceId4 = detect3[3]['faceId']
		faceId5 = detect3[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 6:
			faceId1 = detect3[0]['faceId']
			faceId2 = detect3[1]['faceId']
			faceId3 = detect3[2]['faceId']
			faceId4 = detect3[3]['faceId']
			faceId5 = detect3[4]['faceId']
			faceId6 = detect3[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	if len(detect3) == 7:
			faceId1 = detect3[0]['faceId']
			faceId2 = detect3[1]['faceId']
			faceId3 = detect3[2]['faceId']
			faceId4 = detect3[3]['faceId']
			faceId5 = detect3[4]['faceId']
			faceId6 = detect3[5]['faceId']
			faceId7 = detect3[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
	if len(detect4) == 1:
			faceId1 = detect4[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect4) == 2:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 3:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
		faceId3 = detect4[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 4:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
		faceId3 = detect4[2]['faceId']
		faceId4 = detect4[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 5:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
		faceId3 = detect4[2]['faceId']
		faceId4 = detect4[3]['faceId']
		faceId5 = detect4[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 6:
			faceId1 = detect4[0]['faceId']
			faceId2 = detect4[1]['faceId']
			faceId3 = detect4[2]['faceId']
			faceId4 = detect4[3]['faceId']
			faceId5 = detect4[4]['faceId']
			faceId6 = detect4[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect4) == 7:
			faceId1 = detect4[0]['faceId']
			faceId2 = detect4[1]['faceId']
			faceId3 = detect4[2]['faceId']
			faceId4 = detect4[3]['faceId']
			faceId5 = detect4[4]['faceId']
			faceId6 = detect4[5]['faceId']
			faceId7 = detect4[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
				
	
	if len(detect5) == 1:
			faceId1 = detect5[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect5) == 2:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 3:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
		faceId3 = detect5[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 4:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
		faceId3 = detect5[2]['faceId']
		faceId4 = detect5[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 5:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
		faceId3 = detect5[2]['faceId']
		faceId4 = detect5[3]['faceId']
		faceId5 = detect5[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 6:
			faceId1 = detect5[0]['faceId']
			faceId2 = detect5[1]['faceId']
			faceId3 = detect5[2]['faceId']
			faceId4 = detect5[3]['faceId']
			faceId5 = detect5[4]['faceId']
			faceId6 = detect5[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect5) == 7:
			faceId1 = detect5[0]['faceId']
			faceId2 = detect5[1]['faceId']
			faceId3 = detect5[2]['faceId']
			faceId4 = detect5[3]['faceId']
			faceId5 = detect5[4]['faceId']
			faceId6 = detect5[5]['faceId']
			faceId7 = detect5[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")

		
	
	
if len(urls) == 6:
	img_url1 = urls[0]
	img_url2 = urls[1]
	img_url3 = urls[2]
	img_url4 = urls[3]
	img_url5 = urls[4]
	img_url6 = urls[5]
	
	detect1 = CF.face.detect(img_url1)
	detect2 = CF.face.detect(img_url2)
	detect3 = CF.face.detect(img_url3)
	detect4 = CF.face.detect(img_url4)
	detect5 = CF.face.detect(img_url5)
	detect6 = CF.face.detect(img_url6)
	
	if len(detect1) == 1:
			faceId1 = detect1[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					
		
					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect1) == 2:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect1) == 3:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
		faceId3 = detect1[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
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
			print("match")
		else:
			print("no match")
						
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
			print("match")
		else:
			print("no match")
						
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
				print("match")
			else:
				print("no match")
				
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
				print("match")
			else:
				print("no match")
	if len(detect2) == 1:
			faceId1 = detect2[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect2) == 2:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 3:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 4:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
		faceId4 = detect2[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 5:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
		faceId4 = detect2[3]['faceId']
		faceId5 = detect2[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 6:
			faceId1 = detect2[0]['faceId']
			faceId2 = detect2[1]['faceId']
			faceId3 = detect2[2]['faceId']
			faceId4 = detect2[3]['faceId']
			faceId5 = detect2[4]['faceId']
			faceId6 = detect2[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	if len(detect2) == 7:
			faceId1 = detect2[0]['faceId']
			faceId2 = detect2[1]['faceId']
			faceId3 = detect2[2]['faceId']
			faceId4 = detect2[3]['faceId']
			faceId5 = detect2[4]['faceId']
			faceId6 = detect2[5]['faceId']
			faceId7 = detect2[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	
	if len(detect3) == 1:
			faceId1 = detect3[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					
	
					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect3) == 2:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 3:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 4:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
		faceId4 = detect3[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 5:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
		faceId4 = detect3[3]['faceId']
		faceId5 = detect3[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 6:
			faceId1 = detect3[0]['faceId']
			faceId2 = detect3[1]['faceId']
			faceId3 = detect3[2]['faceId']
			faceId4 = detect3[3]['faceId']
			faceId5 = detect3[4]['faceId']
			faceId6 = detect3[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	if len(detect3) == 7:
			faceId1 = detect3[0]['faceId']
			faceId2 = detect3[1]['faceId']
			faceId3 = detect3[2]['faceId']
			faceId4 = detect3[3]['faceId']
			faceId5 = detect3[4]['faceId']
			faceId6 = detect3[5]['faceId']
			faceId7 = detect3[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
	if len(detect4) == 1:
			faceId1 = detect4[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect4) == 2:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 3:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
		faceId3 = detect4[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 4:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
		faceId3 = detect4[2]['faceId']
		faceId4 = detect4[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 5:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
		faceId3 = detect4[2]['faceId']
		faceId4 = detect4[3]['faceId']
		faceId5 = detect4[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 6:
			faceId1 = detect4[0]['faceId']
			faceId2 = detect4[1]['faceId']
			faceId3 = detect4[2]['faceId']
			faceId4 = detect4[3]['faceId']
			faceId5 = detect4[4]['faceId']
			faceId6 = detect4[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect4) == 7:
			faceId1 = detect4[0]['faceId']
			faceId2 = detect4[1]['faceId']
			faceId3 = detect4[2]['faceId']
			faceId4 = detect4[3]['faceId']
			faceId5 = detect4[4]['faceId']
			faceId6 = detect4[5]['faceId']
			faceId7 = detect4[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
				
	
	if len(detect5) == 1:
			faceId1 = detect5[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect5) == 2:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 3:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
		faceId3 = detect5[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 4:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
		faceId3 = detect5[2]['faceId']
		faceId4 = detect5[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 5:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
		faceId3 = detect5[2]['faceId']
		faceId4 = detect5[3]['faceId']
		faceId5 = detect5[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 6:
			faceId1 = detect5[0]['faceId']
			faceId2 = detect5[1]['faceId']
			faceId3 = detect5[2]['faceId']
			faceId4 = detect5[3]['faceId']
			faceId5 = detect5[4]['faceId']
			faceId6 = detect5[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect5) == 7:
			faceId1 = detect5[0]['faceId']
			faceId2 = detect5[1]['faceId']
			faceId3 = detect5[2]['faceId']
			faceId4 = detect5[3]['faceId']
			faceId5 = detect5[4]['faceId']
			faceId6 = detect5[5]['faceId']
			faceId7 = detect5[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
	
	if len(detect6) == 1:
			faceId1 = detect6[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect6) == 2:
		faceId1 = detect6[0]['faceId']
		faceId2 = detect6[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect6) == 3:
		faceId1 = detect6[0]['faceId']
		faceId2 = detect6[1]['faceId']
		faceId3 = detect6[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect6) == 4:
		faceId1 = detect6[0]['faceId']
		faceId2 = detect6[1]['faceId']
		faceId3 = detect6[2]['faceId']
		faceId4 = detect6[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect6) == 5:
		faceId1 = detect6[0]['faceId']
		faceId2 = detect6[1]['faceId']
		faceId3 = detect6[2]['faceId']
		faceId4 = detect6[3]['faceId']
		faceId5 = detect6[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect6) == 6:
			faceId1 = detect6[0]['faceId']
			faceId2 = detect6[1]['faceId']
			faceId3 = detect6[2]['faceId']
			faceId4 = detect6[3]['faceId']
			faceId5 = detect6[4]['faceId']
			faceId6 = detect6[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect6) == 7:
			faceId1 = detect6[0]['faceId']
			faceId2 = detect6[1]['faceId']
			faceId3 = detect6[2]['faceId']
			faceId4 = detect6[3]['faceId']
			faceId5 = detect6[4]['faceId']
			faceId6 = detect6[5]['faceId']
			faceId7 = detect6[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")

		

if len(urls) == 7:
	img_url1 = urls[0]
	img_url2 = urls[1]
	img_url3 = urls[2]
	img_url4 = urls[3]
	img_url5 = urls[4]
	img_url6 = urls[5]
	img_url7 = urls[6]
	
	
	detect1 = CF.face.detect(img_url1)
	detect2 = CF.face.detect(img_url2)
	detect3 = CF.face.detect(img_url3)
	detect4 = CF.face.detect(img_url4)
	detect5 = CF.face.detect(img_url5)
	detect6 = CF.face.detect(img_url6)
	detect7 = CF.face.detect(img_url7)
	
	if len(detect1) == 1:
			faceId1 = detect1[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					
		
					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect1) == 2:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect1) == 3:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
		faceId3 = detect1[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
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
			print("match")
		else:
			print("no match")
						
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
			print("match")
		else:
			print("no match")
						
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
				print("match")
			else:
				print("no match")
				
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
				print("match")
			else:
				print("no match")
	if len(detect2) == 1:
			faceId1 = detect2[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect2) == 2:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 3:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 4:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
		faceId4 = detect2[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 5:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
		faceId4 = detect2[3]['faceId']
		faceId5 = detect2[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 6:
			faceId1 = detect2[0]['faceId']
			faceId2 = detect2[1]['faceId']
			faceId3 = detect2[2]['faceId']
			faceId4 = detect2[3]['faceId']
			faceId5 = detect2[4]['faceId']
			faceId6 = detect2[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	if len(detect2) == 7:
			faceId1 = detect2[0]['faceId']
			faceId2 = detect2[1]['faceId']
			faceId3 = detect2[2]['faceId']
			faceId4 = detect2[3]['faceId']
			faceId5 = detect2[4]['faceId']
			faceId6 = detect2[5]['faceId']
			faceId7 = detect2[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	
	if len(detect3) == 1:
			faceId1 = detect3[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					
	
					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect3) == 2:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 3:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 4:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
		faceId4 = detect3[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 5:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
		faceId4 = detect3[3]['faceId']
		faceId5 = detect3[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 6:
			faceId1 = detect3[0]['faceId']
			faceId2 = detect3[1]['faceId']
			faceId3 = detect3[2]['faceId']
			faceId4 = detect3[3]['faceId']
			faceId5 = detect3[4]['faceId']
			faceId6 = detect3[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	if len(detect3) == 7:
			faceId1 = detect3[0]['faceId']
			faceId2 = detect3[1]['faceId']
			faceId3 = detect3[2]['faceId']
			faceId4 = detect3[3]['faceId']
			faceId5 = detect3[4]['faceId']
			faceId6 = detect3[5]['faceId']
			faceId7 = detect3[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
	if len(detect4) == 1:
			faceId1 = detect4[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect4) == 2:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 3:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
		faceId3 = detect4[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 4:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
		faceId3 = detect4[2]['faceId']
		faceId4 = detect4[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 5:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
		faceId3 = detect4[2]['faceId']
		faceId4 = detect4[3]['faceId']
		faceId5 = detect4[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 6:
			faceId1 = detect4[0]['faceId']
			faceId2 = detect4[1]['faceId']
			faceId3 = detect4[2]['faceId']
			faceId4 = detect4[3]['faceId']
			faceId5 = detect4[4]['faceId']
			faceId6 = detect4[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect4) == 7:
			faceId1 = detect4[0]['faceId']
			faceId2 = detect4[1]['faceId']
			faceId3 = detect4[2]['faceId']
			faceId4 = detect4[3]['faceId']
			faceId5 = detect4[4]['faceId']
			faceId6 = detect4[5]['faceId']
			faceId7 = detect4[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
				
	
	if len(detect5) == 1:
			faceId1 = detect5[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect5) == 2:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 3:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
		faceId3 = detect5[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 4:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
		faceId3 = detect5[2]['faceId']
		faceId4 = detect5[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 5:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
		faceId3 = detect5[2]['faceId']
		faceId4 = detect5[3]['faceId']
		faceId5 = detect5[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 6:
			faceId1 = detect5[0]['faceId']
			faceId2 = detect5[1]['faceId']
			faceId3 = detect5[2]['faceId']
			faceId4 = detect5[3]['faceId']
			faceId5 = detect5[4]['faceId']
			faceId6 = detect5[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect5) == 7:
			faceId1 = detect5[0]['faceId']
			faceId2 = detect5[1]['faceId']
			faceId3 = detect5[2]['faceId']
			faceId4 = detect5[3]['faceId']
			faceId5 = detect5[4]['faceId']
			faceId6 = detect5[5]['faceId']
			faceId7 = detect5[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
	
	if len(detect6) == 1:
			faceId1 = detect6[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect6) == 2:
		faceId1 = detect6[0]['faceId']
		faceId2 = detect6[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect6) == 3:
		faceId1 = detect6[0]['faceId']
		faceId2 = detect6[1]['faceId']
		faceId3 = detect6[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect6) == 4:
		faceId1 = detect6[0]['faceId']
		faceId2 = detect6[1]['faceId']
		faceId3 = detect6[2]['faceId']
		faceId4 = detect6[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect6) == 5:
		faceId1 = detect6[0]['faceId']
		faceId2 = detect6[1]['faceId']
		faceId3 = detect6[2]['faceId']
		faceId4 = detect6[3]['faceId']
		faceId5 = detect6[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect6) == 6:
			faceId1 = detect6[0]['faceId']
			faceId2 = detect6[1]['faceId']
			faceId3 = detect6[2]['faceId']
			faceId4 = detect6[3]['faceId']
			faceId5 = detect6[4]['faceId']
			faceId6 = detect6[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect6) == 7:
			faceId1 = detect6[0]['faceId']
			faceId2 = detect6[1]['faceId']
			faceId3 = detect6[2]['faceId']
			faceId4 = detect6[3]['faceId']
			faceId5 = detect6[4]['faceId']
			faceId6 = detect6[5]['faceId']
			faceId7 = detect6[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
	
	if len(detect7) == 1:
			faceId1 = detect7[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect7) == 2:
		faceId1 = detect7[0]['faceId']
		faceId2 = detect7[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect7) == 3:
		faceId1 = detect7[0]['faceId']
		faceId2 = detect7[1]['faceId']
		faceId3 = detect7[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect7) == 4:
		faceId1 = detect7[0]['faceId']
		faceId2 = detect7[1]['faceId']
		faceId3 = detect7[2]['faceId']
		faceId4 = detect7[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect7) == 5:
		faceId1 = detect7[0]['faceId']
		faceId2 = detect7[1]['faceId']
		faceId3 = detect7[2]['faceId']
		faceId4 = detect7[3]['faceId']
		faceId5 = detect7[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect7) == 6:
			faceId1 = detect7[0]['faceId']
			faceId2 = detect7[1]['faceId']
			faceId3 = detect7[2]['faceId']
			faceId4 = detect7[3]['faceId']
			faceId5 = detect7[4]['faceId']
			faceId6 = detect7[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect7) == 7:
			faceId1 = detect7[0]['faceId']
			faceId2 = detect7[1]['faceId']
			faceId3 = detect7[2]['faceId']
			faceId4 = detect7[3]['faceId']
			faceId5 = detect7[4]['faceId']
			faceId6 = detect7[5]['faceId']
			faceId7 = detect7[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")

		


if len(urls) == 8:
	img_url1 = urls[0]
	img_url2 = urls[1]
	img_url3 = urls[2]
	img_url4 = urls[3]
	img_url5 = urls[4]
	img_url6 = urls[5]
	img_url7 = urls[6]
	img_url8 = urls[7]
	
	detect1 = CF.face.detect(img_url1)
	detect2 = CF.face.detect(img_url2)
	detect3 = CF.face.detect(img_url3)
	detect4 = CF.face.detect(img_url4)
	detect5 = CF.face.detect(img_url5)
	detect6 = CF.face.detect(img_url6)
	detect7 = CF.face.detect(img_url7)
	detect8 = CF.face.detect(img_url8)
	
	if len(detect1) == 1:
			faceId1 = detect1[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					
		
					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect1) == 2:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect1) == 3:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
		faceId3 = detect1[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
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
			print("match")
		else:
			print("no match")
						
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
			print("match")
		else:
			print("no match")
						
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
				print("match")
			else:
				print("no match")
				
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
				print("match")
			else:
				print("no match")
	if len(detect2) == 1:
			faceId1 = detect2[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect2) == 2:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 3:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 4:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
		faceId4 = detect2[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 5:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
		faceId4 = detect2[3]['faceId']
		faceId5 = detect2[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 6:
			faceId1 = detect2[0]['faceId']
			faceId2 = detect2[1]['faceId']
			faceId3 = detect2[2]['faceId']
			faceId4 = detect2[3]['faceId']
			faceId5 = detect2[4]['faceId']
			faceId6 = detect2[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	if len(detect2) == 7:
			faceId1 = detect2[0]['faceId']
			faceId2 = detect2[1]['faceId']
			faceId3 = detect2[2]['faceId']
			faceId4 = detect2[3]['faceId']
			faceId5 = detect2[4]['faceId']
			faceId6 = detect2[5]['faceId']
			faceId7 = detect2[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	
	if len(detect3) == 1:
			faceId1 = detect3[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					
	
					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect3) == 2:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 3:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 4:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
		faceId4 = detect3[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 5:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
		faceId4 = detect3[3]['faceId']
		faceId5 = detect3[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 6:
			faceId1 = detect3[0]['faceId']
			faceId2 = detect3[1]['faceId']
			faceId3 = detect3[2]['faceId']
			faceId4 = detect3[3]['faceId']
			faceId5 = detect3[4]['faceId']
			faceId6 = detect3[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	if len(detect3) == 7:
			faceId1 = detect3[0]['faceId']
			faceId2 = detect3[1]['faceId']
			faceId3 = detect3[2]['faceId']
			faceId4 = detect3[3]['faceId']
			faceId5 = detect3[4]['faceId']
			faceId6 = detect3[5]['faceId']
			faceId7 = detect3[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
	if len(detect4) == 1:
			faceId1 = detect4[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect4) == 2:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 3:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
		faceId3 = detect4[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 4:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
		faceId3 = detect4[2]['faceId']
		faceId4 = detect4[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 5:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
		faceId3 = detect4[2]['faceId']
		faceId4 = detect4[3]['faceId']
		faceId5 = detect4[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 6:
			faceId1 = detect4[0]['faceId']
			faceId2 = detect4[1]['faceId']
			faceId3 = detect4[2]['faceId']
			faceId4 = detect4[3]['faceId']
			faceId5 = detect4[4]['faceId']
			faceId6 = detect4[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect4) == 7:
			faceId1 = detect4[0]['faceId']
			faceId2 = detect4[1]['faceId']
			faceId3 = detect4[2]['faceId']
			faceId4 = detect4[3]['faceId']
			faceId5 = detect4[4]['faceId']
			faceId6 = detect4[5]['faceId']
			faceId7 = detect4[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
				
	
	if len(detect5) == 1:
			faceId1 = detect5[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect5) == 2:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 3:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
		faceId3 = detect5[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 4:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
		faceId3 = detect5[2]['faceId']
		faceId4 = detect5[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 5:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
		faceId3 = detect5[2]['faceId']
		faceId4 = detect5[3]['faceId']
		faceId5 = detect5[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 6:
			faceId1 = detect5[0]['faceId']
			faceId2 = detect5[1]['faceId']
			faceId3 = detect5[2]['faceId']
			faceId4 = detect5[3]['faceId']
			faceId5 = detect5[4]['faceId']
			faceId6 = detect5[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect5) == 7:
			faceId1 = detect5[0]['faceId']
			faceId2 = detect5[1]['faceId']
			faceId3 = detect5[2]['faceId']
			faceId4 = detect5[3]['faceId']
			faceId5 = detect5[4]['faceId']
			faceId6 = detect5[5]['faceId']
			faceId7 = detect5[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
	
	if len(detect6) == 1:
			faceId1 = detect6[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect6) == 2:
		faceId1 = detect6[0]['faceId']
		faceId2 = detect6[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect6) == 3:
		faceId1 = detect6[0]['faceId']
		faceId2 = detect6[1]['faceId']
		faceId3 = detect6[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect6) == 4:
		faceId1 = detect6[0]['faceId']
		faceId2 = detect6[1]['faceId']
		faceId3 = detect6[2]['faceId']
		faceId4 = detect6[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect6) == 5:
		faceId1 = detect6[0]['faceId']
		faceId2 = detect6[1]['faceId']
		faceId3 = detect6[2]['faceId']
		faceId4 = detect6[3]['faceId']
		faceId5 = detect6[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect6) == 6:
			faceId1 = detect6[0]['faceId']
			faceId2 = detect6[1]['faceId']
			faceId3 = detect6[2]['faceId']
			faceId4 = detect6[3]['faceId']
			faceId5 = detect6[4]['faceId']
			faceId6 = detect6[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect6) == 7:
			faceId1 = detect6[0]['faceId']
			faceId2 = detect6[1]['faceId']
			faceId3 = detect6[2]['faceId']
			faceId4 = detect6[3]['faceId']
			faceId5 = detect6[4]['faceId']
			faceId6 = detect6[5]['faceId']
			faceId7 = detect6[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
	
	if len(detect7) == 1:
			faceId1 = detect7[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect7) == 2:
		faceId1 = detect7[0]['faceId']
		faceId2 = detect7[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect7) == 3:
		faceId1 = detect7[0]['faceId']
		faceId2 = detect7[1]['faceId']
		faceId3 = detect7[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect7) == 4:
		faceId1 = detect7[0]['faceId']
		faceId2 = detect7[1]['faceId']
		faceId3 = detect7[2]['faceId']
		faceId4 = detect7[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect7) == 5:
		faceId1 = detect7[0]['faceId']
		faceId2 = detect7[1]['faceId']
		faceId3 = detect7[2]['faceId']
		faceId4 = detect7[3]['faceId']
		faceId5 = detect7[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect7) == 6:
			faceId1 = detect7[0]['faceId']
			faceId2 = detect7[1]['faceId']
			faceId3 = detect7[2]['faceId']
			faceId4 = detect7[3]['faceId']
			faceId5 = detect7[4]['faceId']
			faceId6 = detect7[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect7) == 7:
			faceId1 = detect7[0]['faceId']
			faceId2 = detect7[1]['faceId']
			faceId3 = detect7[2]['faceId']
			faceId4 = detect7[3]['faceId']
			faceId5 = detect7[4]['faceId']
			faceId6 = detect7[5]['faceId']
			faceId7 = detect7[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
				
	
	if len(detect8) == 1:
			faceId1 = detect8[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect8) == 2:
		faceId1 = detect8[0]['faceId']
		faceId2 = detect8[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect8) == 3:
		faceId1 = detect8[0]['faceId']
		faceId2 = detect8[1]['faceId']
		faceId3 = detect8[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect8) == 4:
		faceId1 = detect8[0]['faceId']
		faceId2 = detect8[1]['faceId']
		faceId3 = detect8[2]['faceId']
		faceId4 = detect8[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect8) == 5:
		faceId1 = detect8[0]['faceId']
		faceId2 = detect8[1]['faceId']
		faceId3 = detect8[2]['faceId']
		faceId4 = detect8[3]['faceId']
		faceId5 = detect8[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect8) == 6:
			faceId1 = detect8[0]['faceId']
			faceId2 = detect8[1]['faceId']
			faceId3 = detect8[2]['faceId']
			faceId4 = detect8[3]['faceId']
			faceId5 = detect8[4]['faceId']
			faceId6 = detect8[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect8) == 7:
			faceId1 = detect8[0]['faceId']
			faceId2 = detect8[1]['faceId']
			faceId3 = detect8[2]['faceId']
			faceId4 = detect8[3]['faceId']
			faceId5 = detect8[4]['faceId']
			faceId6 = detect8[5]['faceId']
			faceId7 = detect8[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")

		

	

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
	
	detect1 = CF.face.detect(img_url1)
	detect2 = CF.face.detect(img_url2)
	detect3 = CF.face.detect(img_url3)
	detect4 = CF.face.detect(img_url4)
	detect5 = CF.face.detect(img_url5)
	detect6 = CF.face.detect(img_url6)
	detect7 = CF.face.detect(img_url7)
	detect8 = CF.face.detect(img_url8)
	detect9 = CF.face.detect(img_url9)
	
	if len(detect1) == 1:
			faceId1 = detect1[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					
		
					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect1) == 2:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect1) == 3:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
		faceId3 = detect1[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
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
			print("match")
		else:
			print("no match")
						
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
			print("match")
		else:
			print("no match")
						
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
				print("match")
			else:
				print("no match")
				
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
				print("match")
			else:
				print("no match")
	if len(detect2) == 1:
			faceId1 = detect2[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect2) == 2:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 3:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 4:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
		faceId4 = detect2[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 5:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
		faceId4 = detect2[3]['faceId']
		faceId5 = detect2[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 6:
			faceId1 = detect2[0]['faceId']
			faceId2 = detect2[1]['faceId']
			faceId3 = detect2[2]['faceId']
			faceId4 = detect2[3]['faceId']
			faceId5 = detect2[4]['faceId']
			faceId6 = detect2[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	if len(detect2) == 7:
			faceId1 = detect2[0]['faceId']
			faceId2 = detect2[1]['faceId']
			faceId3 = detect2[2]['faceId']
			faceId4 = detect2[3]['faceId']
			faceId5 = detect2[4]['faceId']
			faceId6 = detect2[5]['faceId']
			faceId7 = detect2[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	
	if len(detect3) == 1:
			faceId1 = detect3[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					
	
					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect3) == 2:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 3:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 4:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
		faceId4 = detect3[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 5:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
		faceId4 = detect3[3]['faceId']
		faceId5 = detect3[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 6:
			faceId1 = detect3[0]['faceId']
			faceId2 = detect3[1]['faceId']
			faceId3 = detect3[2]['faceId']
			faceId4 = detect3[3]['faceId']
			faceId5 = detect3[4]['faceId']
			faceId6 = detect3[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	if len(detect3) == 7:
			faceId1 = detect3[0]['faceId']
			faceId2 = detect3[1]['faceId']
			faceId3 = detect3[2]['faceId']
			faceId4 = detect3[3]['faceId']
			faceId5 = detect3[4]['faceId']
			faceId6 = detect3[5]['faceId']
			faceId7 = detect3[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
	if len(detect4) == 1:
			faceId1 = detect4[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect4) == 2:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 3:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
		faceId3 = detect4[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 4:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
		faceId3 = detect4[2]['faceId']
		faceId4 = detect4[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 5:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
		faceId3 = detect4[2]['faceId']
		faceId4 = detect4[3]['faceId']
		faceId5 = detect4[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 6:
			faceId1 = detect4[0]['faceId']
			faceId2 = detect4[1]['faceId']
			faceId3 = detect4[2]['faceId']
			faceId4 = detect4[3]['faceId']
			faceId5 = detect4[4]['faceId']
			faceId6 = detect4[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect4) == 7:
			faceId1 = detect4[0]['faceId']
			faceId2 = detect4[1]['faceId']
			faceId3 = detect4[2]['faceId']
			faceId4 = detect4[3]['faceId']
			faceId5 = detect4[4]['faceId']
			faceId6 = detect4[5]['faceId']
			faceId7 = detect4[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
				
	
	if len(detect5) == 1:
			faceId1 = detect5[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect5) == 2:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 3:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
		faceId3 = detect5[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 4:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
		faceId3 = detect5[2]['faceId']
		faceId4 = detect5[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 5:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
		faceId3 = detect5[2]['faceId']
		faceId4 = detect5[3]['faceId']
		faceId5 = detect5[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 6:
			faceId1 = detect5[0]['faceId']
			faceId2 = detect5[1]['faceId']
			faceId3 = detect5[2]['faceId']
			faceId4 = detect5[3]['faceId']
			faceId5 = detect5[4]['faceId']
			faceId6 = detect5[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect5) == 7:
			faceId1 = detect5[0]['faceId']
			faceId2 = detect5[1]['faceId']
			faceId3 = detect5[2]['faceId']
			faceId4 = detect5[3]['faceId']
			faceId5 = detect5[4]['faceId']
			faceId6 = detect5[5]['faceId']
			faceId7 = detect5[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
	
	if len(detect6) == 1:
			faceId1 = detect6[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect6) == 2:
		faceId1 = detect6[0]['faceId']
		faceId2 = detect6[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect6) == 3:
		faceId1 = detect6[0]['faceId']
		faceId2 = detect6[1]['faceId']
		faceId3 = detect6[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect6) == 4:
		faceId1 = detect6[0]['faceId']
		faceId2 = detect6[1]['faceId']
		faceId3 = detect6[2]['faceId']
		faceId4 = detect6[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect6) == 5:
		faceId1 = detect6[0]['faceId']
		faceId2 = detect6[1]['faceId']
		faceId3 = detect6[2]['faceId']
		faceId4 = detect6[3]['faceId']
		faceId5 = detect6[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect6) == 6:
			faceId1 = detect6[0]['faceId']
			faceId2 = detect6[1]['faceId']
			faceId3 = detect6[2]['faceId']
			faceId4 = detect6[3]['faceId']
			faceId5 = detect6[4]['faceId']
			faceId6 = detect6[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect6) == 7:
			faceId1 = detect6[0]['faceId']
			faceId2 = detect6[1]['faceId']
			faceId3 = detect6[2]['faceId']
			faceId4 = detect6[3]['faceId']
			faceId5 = detect6[4]['faceId']
			faceId6 = detect6[5]['faceId']
			faceId7 = detect6[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
	
	if len(detect7) == 1:
			faceId1 = detect7[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect7) == 2:
		faceId1 = detect7[0]['faceId']
		faceId2 = detect7[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect7) == 3:
		faceId1 = detect7[0]['faceId']
		faceId2 = detect7[1]['faceId']
		faceId3 = detect7[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect7) == 4:
		faceId1 = detect7[0]['faceId']
		faceId2 = detect7[1]['faceId']
		faceId3 = detect7[2]['faceId']
		faceId4 = detect7[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect7) == 5:
		faceId1 = detect7[0]['faceId']
		faceId2 = detect7[1]['faceId']
		faceId3 = detect7[2]['faceId']
		faceId4 = detect7[3]['faceId']
		faceId5 = detect7[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect7) == 6:
			faceId1 = detect7[0]['faceId']
			faceId2 = detect7[1]['faceId']
			faceId3 = detect7[2]['faceId']
			faceId4 = detect7[3]['faceId']
			faceId5 = detect7[4]['faceId']
			faceId6 = detect7[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect7) == 7:
			faceId1 = detect7[0]['faceId']
			faceId2 = detect7[1]['faceId']
			faceId3 = detect7[2]['faceId']
			faceId4 = detect7[3]['faceId']
			faceId5 = detect7[4]['faceId']
			faceId6 = detect7[5]['faceId']
			faceId7 = detect7[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
				
	
	if len(detect8) == 1:
			faceId1 = detect8[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect8) == 2:
		faceId1 = detect8[0]['faceId']
		faceId2 = detect8[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect8) == 3:
		faceId1 = detect8[0]['faceId']
		faceId2 = detect8[1]['faceId']
		faceId3 = detect8[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect8) == 4:
		faceId1 = detect8[0]['faceId']
		faceId2 = detect8[1]['faceId']
		faceId3 = detect8[2]['faceId']
		faceId4 = detect8[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect8) == 5:
		faceId1 = detect8[0]['faceId']
		faceId2 = detect8[1]['faceId']
		faceId3 = detect8[2]['faceId']
		faceId4 = detect8[3]['faceId']
		faceId5 = detect8[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect8) == 6:
			faceId1 = detect8[0]['faceId']
			faceId2 = detect8[1]['faceId']
			faceId3 = detect8[2]['faceId']
			faceId4 = detect8[3]['faceId']
			faceId5 = detect8[4]['faceId']
			faceId6 = detect8[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect8) == 7:
			faceId1 = detect8[0]['faceId']
			faceId2 = detect8[1]['faceId']
			faceId3 = detect8[2]['faceId']
			faceId4 = detect8[3]['faceId']
			faceId5 = detect8[4]['faceId']
			faceId6 = detect8[5]['faceId']
			faceId7 = detect8[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
	
	if len(detect9) == 1:
			faceId1 = detect9[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect9) == 2:
		faceId1 = detect9[0]['faceId']
		faceId2 = detect9[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect9) == 3:
		faceId1 = detect9[0]['faceId']
		faceId2 = detect9[1]['faceId']
		faceId3 = detect9[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect9) == 4:
		faceId1 = detect9[0]['faceId']
		faceId2 = detect9[1]['faceId']
		faceId3 = detect9[2]['faceId']
		faceId4 = detect9[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect9) == 5:
		faceId1 = detect9[0]['faceId']
		faceId2 = detect9[1]['faceId']
		faceId3 = detect9[2]['faceId']
		faceId4 = detect9[3]['faceId']
		faceId5 = detect9[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect9) == 6:
			faceId1 = detect9[0]['faceId']
			faceId2 = detect9[1]['faceId']
			faceId3 = detect9[2]['faceId']
			faceId4 = detect9[3]['faceId']
			faceId5 = detect9[4]['faceId']
			faceId6 = detect9[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect9) == 7:
			faceId1 = detect9[0]['faceId']
			faceId2 = detect9[1]['faceId']
			faceId3 = detect9[2]['faceId']
			faceId4 = detect9[3]['faceId']
			faceId5 = detect9[4]['faceId']
			faceId6 = detect9[5]['faceId']
			faceId7 = detect9[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")

		

	
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
	
	detect1 = CF.face.detect(img_url1)
	detect2 = CF.face.detect(img_url2)
	detect3 = CF.face.detect(img_url3)
	detect4 = CF.face.detect(img_url4)
	detect5 = CF.face.detect(img_url5)
	detect6 = CF.face.detect(img_url6)
	detect7 = CF.face.detect(img_url7)
	detect8 = CF.face.detect(img_url8)
	detect9 = CF.face.detect(img_url9)
	detect10 = CF.face.detect(img_url10)
	
	if len(detect1) == 1:
			faceId1 = detect1[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					
		
					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect1) == 2:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect1) == 3:
		faceId1 = detect1[0]['faceId']
		faceId2 = detect1[1]['faceId']
		faceId3 = detect1[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
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
			print("match")
		else:
			print("no match")
						
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
			print("match")
		else:
			print("no match")
						
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
				print("match")
			else:
				print("no match")
				
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
				print("match")
			else:
				print("no match")
	if len(detect2) == 1:
			faceId1 = detect2[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect2) == 2:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 3:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 4:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
		faceId4 = detect2[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 5:
		faceId1 = detect2[0]['faceId']
		faceId2 = detect2[1]['faceId']
		faceId3 = detect2[2]['faceId']
		faceId4 = detect2[3]['faceId']
		faceId5 = detect2[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect2) == 6:
			faceId1 = detect2[0]['faceId']
			faceId2 = detect2[1]['faceId']
			faceId3 = detect2[2]['faceId']
			faceId4 = detect2[3]['faceId']
			faceId5 = detect2[4]['faceId']
			faceId6 = detect2[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	if len(detect2) == 7:
			faceId1 = detect2[0]['faceId']
			faceId2 = detect2[1]['faceId']
			faceId3 = detect2[2]['faceId']
			faceId4 = detect2[3]['faceId']
			faceId5 = detect2[4]['faceId']
			faceId6 = detect2[5]['faceId']
			faceId7 = detect2[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	
	if len(detect3) == 1:
			faceId1 = detect3[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					
	
					
			if result1[0]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
						
	if len(detect3) == 2:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 3:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 4:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
		faceId4 = detect3[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 5:
		faceId1 = detect3[0]['faceId']
		faceId2 = detect3[1]['faceId']
		faceId3 = detect3[2]['faceId']
		faceId4 = detect3[3]['faceId']
		faceId5 = detect3[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
		else:
			print("no match")
						
	if len(detect3) == 6:
			faceId1 = detect3[0]['faceId']
			faceId2 = detect3[1]['faceId']
			faceId3 = detect3[2]['faceId']
			faceId4 = detect3[3]['faceId']
			faceId5 = detect3[4]['faceId']
			faceId6 = detect3[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
				
	if len(detect3) == 7:
			faceId1 = detect3[0]['faceId']
			faceId2 = detect3[1]['faceId']
			faceId3 = detect3[2]['faceId']
			faceId4 = detect3[3]['faceId']
			faceId5 = detect3[4]['faceId']
			faceId6 = detect3[5]['faceId']
			faceId7 = detect3[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
			else:
				print("no match")
	if len(detect4) == 1:
			faceId1 = detect4[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect4) == 2:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 3:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
		faceId3 = detect4[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 4:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
		faceId3 = detect4[2]['faceId']
		faceId4 = detect4[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 5:
		faceId1 = detect4[0]['faceId']
		faceId2 = detect4[1]['faceId']
		faceId3 = detect4[2]['faceId']
		faceId4 = detect4[3]['faceId']
		faceId5 = detect4[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect4) == 6:
			faceId1 = detect4[0]['faceId']
			faceId2 = detect4[1]['faceId']
			faceId3 = detect4[2]['faceId']
			faceId4 = detect4[3]['faceId']
			faceId5 = detect4[4]['faceId']
			faceId6 = detect4[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect4) == 7:
			faceId1 = detect4[0]['faceId']
			faceId2 = detect4[1]['faceId']
			faceId3 = detect4[2]['faceId']
			faceId4 = detect4[3]['faceId']
			faceId5 = detect4[4]['faceId']
			faceId6 = detect4[5]['faceId']
			faceId7 = detect4[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
				
	
	if len(detect5) == 1:
			faceId1 = detect5[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect5) == 2:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 3:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
		faceId3 = detect5[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 4:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
		faceId3 = detect5[2]['faceId']
		faceId4 = detect5[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 5:
		faceId1 = detect5[0]['faceId']
		faceId2 = detect5[1]['faceId']
		faceId3 = detect5[2]['faceId']
		faceId4 = detect5[3]['faceId']
		faceId5 = detect5[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect5) == 6:
			faceId1 = detect5[0]['faceId']
			faceId2 = detect5[1]['faceId']
			faceId3 = detect5[2]['faceId']
			faceId4 = detect5[3]['faceId']
			faceId5 = detect5[4]['faceId']
			faceId6 = detect5[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect5) == 7:
			faceId1 = detect5[0]['faceId']
			faceId2 = detect5[1]['faceId']
			faceId3 = detect5[2]['faceId']
			faceId4 = detect5[3]['faceId']
			faceId5 = detect5[4]['faceId']
			faceId6 = detect5[5]['faceId']
			faceId7 = detect5[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
	
	if len(detect6) == 1:
			faceId1 = detect6[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect6) == 2:
		faceId1 = detect6[0]['faceId']
		faceId2 = detect6[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect6) == 3:
		faceId1 = detect6[0]['faceId']
		faceId2 = detect6[1]['faceId']
		faceId3 = detect6[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect6) == 4:
		faceId1 = detect6[0]['faceId']
		faceId2 = detect6[1]['faceId']
		faceId3 = detect6[2]['faceId']
		faceId4 = detect6[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect6) == 5:
		faceId1 = detect6[0]['faceId']
		faceId2 = detect6[1]['faceId']
		faceId3 = detect6[2]['faceId']
		faceId4 = detect6[3]['faceId']
		faceId5 = detect6[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect6) == 6:
			faceId1 = detect6[0]['faceId']
			faceId2 = detect6[1]['faceId']
			faceId3 = detect6[2]['faceId']
			faceId4 = detect6[3]['faceId']
			faceId5 = detect6[4]['faceId']
			faceId6 = detect6[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect6) == 7:
			faceId1 = detect6[0]['faceId']
			faceId2 = detect6[1]['faceId']
			faceId3 = detect6[2]['faceId']
			faceId4 = detect6[3]['faceId']
			faceId5 = detect6[4]['faceId']
			faceId6 = detect6[5]['faceId']
			faceId7 = detect6[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
	
	if len(detect7) == 1:
			faceId1 = detect7[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect7) == 2:
		faceId1 = detect7[0]['faceId']
		faceId2 = detect7[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect7) == 3:
		faceId1 = detect7[0]['faceId']
		faceId2 = detect7[1]['faceId']
		faceId3 = detect7[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect7) == 4:
		faceId1 = detect7[0]['faceId']
		faceId2 = detect7[1]['faceId']
		faceId3 = detect7[2]['faceId']
		faceId4 = detect7[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect7) == 5:
		faceId1 = detect7[0]['faceId']
		faceId2 = detect7[1]['faceId']
		faceId3 = detect7[2]['faceId']
		faceId4 = detect7[3]['faceId']
		faceId5 = detect7[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect7) == 6:
			faceId1 = detect7[0]['faceId']
			faceId2 = detect7[1]['faceId']
			faceId3 = detect7[2]['faceId']
			faceId4 = detect7[3]['faceId']
			faceId5 = detect7[4]['faceId']
			faceId6 = detect7[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect7) == 7:
			faceId1 = detect7[0]['faceId']
			faceId2 = detect7[1]['faceId']
			faceId3 = detect7[2]['faceId']
			faceId4 = detect7[3]['faceId']
			faceId5 = detect7[4]['faceId']
			faceId6 = detect7[5]['faceId']
			faceId7 = detect7[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
				
	
	if len(detect8) == 1:
			faceId1 = detect8[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect8) == 2:
		faceId1 = detect8[0]['faceId']
		faceId2 = detect8[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect8) == 3:
		faceId1 = detect8[0]['faceId']
		faceId2 = detect8[1]['faceId']
		faceId3 = detect8[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect8) == 4:
		faceId1 = detect8[0]['faceId']
		faceId2 = detect8[1]['faceId']
		faceId3 = detect8[2]['faceId']
		faceId4 = detect8[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect8) == 5:
		faceId1 = detect8[0]['faceId']
		faceId2 = detect8[1]['faceId']
		faceId3 = detect8[2]['faceId']
		faceId4 = detect8[3]['faceId']
		faceId5 = detect8[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect8) == 6:
			faceId1 = detect8[0]['faceId']
			faceId2 = detect8[1]['faceId']
			faceId3 = detect8[2]['faceId']
			faceId4 = detect8[3]['faceId']
			faceId5 = detect8[4]['faceId']
			faceId6 = detect8[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect8) == 7:
			faceId1 = detect8[0]['faceId']
			faceId2 = detect8[1]['faceId']
			faceId3 = detect8[2]['faceId']
			faceId4 = detect8[3]['faceId']
			faceId5 = detect8[4]['faceId']
			faceId6 = detect8[5]['faceId']
			faceId7 = detect8[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
	
	if len(detect9) == 1:
			faceId1 = detect9[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect9) == 2:
		faceId1 = detect9[0]['faceId']
		faceId2 = detect9[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect9) == 3:
		faceId1 = detect9[0]['faceId']
		faceId2 = detect9[1]['faceId']
		faceId3 = detect9[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect9) == 4:
		faceId1 = detect9[0]['faceId']
		faceId2 = detect9[1]['faceId']
		faceId3 = detect9[2]['faceId']
		faceId4 = detect9[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect9) == 5:
		faceId1 = detect9[0]['faceId']
		faceId2 = detect9[1]['faceId']
		faceId3 = detect9[2]['faceId']
		faceId4 = detect9[3]['faceId']
		faceId5 = detect9[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect9) == 6:
			faceId1 = detect9[0]['faceId']
			faceId2 = detect9[1]['faceId']
			faceId3 = detect9[2]['faceId']
			faceId4 = detect9[3]['faceId']
			faceId5 = detect9[4]['faceId']
			faceId6 = detect9[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect9) == 7:
			faceId1 = detect9[0]['faceId']
			faceId2 = detect9[1]['faceId']
			faceId3 = detect9[2]['faceId']
			faceId4 = detect9[3]['faceId']
			faceId5 = detect9[4]['faceId']
			faceId6 = detect9[5]['faceId']
			faceId7 = detect9[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")
				
	
	if len(detect10) == 1:
			faceId1 = detect10[0]['faceId']
					
			result1 = CF.face.verify(myChildFaceId, faceId1)
					

					
			if result1[0]['isIdentical'] == True:
				print("match")
						
	if len(detect10) == 2:
		faceId1 = detect10[0]['faceId']
		faceId2 = detect10[1]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
					
		results = (result1,result2)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True:
			print("match")
						
	if len(detect10) == 3:
		faceId1 = detect10[0]['faceId']
		faceId2 = detect10[1]['faceId']
		faceId3 = detect10[2]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
					
		results = (result1,result2,result3)
				
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True:
			print("match")
						
	if len(detect10) == 4:
		faceId1 = detect10[0]['faceId']
		faceId2 = detect10[1]['faceId']
		faceId3 = detect10[2]['faceId']
		faceId4 = detect10[3]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
					
		results = (result1,result2,result3,result4)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True:
			print("match")
						
	if len(detect10) == 5:
		faceId1 = detect10[0]['faceId']
		faceId2 = detect10[1]['faceId']
		faceId3 = detect10[2]['faceId']
		faceId4 = detect10[3]['faceId']
		faceId5 = detect10[4]['faceId']
					
		result1 = CF.face.verify(myChildFaceId, faceId1)
		result2 = CF.face.verify(myChildFaceId, faceId2)
		result3 = CF.face.verify(myChildFaceId, faceId3)
		result4 = CF.face.verify(myChildFaceId, faceId4)
		result5 = CF.face.verify(myChildFaceId, faceId5)
				
		results = (result1,result2,result3,result4,result5)
					
		if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True:
			print("match")
						
	if len(detect10) == 6:
			faceId1 = detect10[0]['faceId']
			faceId2 = detect10[1]['faceId']
			faceId3 = detect10[2]['faceId']
			faceId4 = detect10[3]['faceId']
			faceId5 = detect10[4]['faceId']
			faceId6 = detect10[5]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
						
			results = (result1,result2,result3,result4,result5,result6)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True:
				print("match")
				
	if len(detect10) == 7:
			faceId1 = detect10[0]['faceId']
			faceId2 = detect10[1]['faceId']
			faceId3 = detect10[2]['faceId']
			faceId4 = detect10[3]['faceId']
			faceId5 = detect10[4]['faceId']
			faceId6 = detect10[5]['faceId']
			faceId7 = detect10[6]['faceId']
						
			result1 = CF.face.verify(myChildFaceId, faceId1)
			result2 = CF.face.verify(myChildFaceId, faceId2)
			result3 = CF.face.verify(myChildFaceId, faceId3)
			result4 = CF.face.verify(myChildFaceId, faceId4)
			result5 = CF.face.verify(myChildFaceId, faceId5)
			result6 = CF.face.verify(myChildFaceId, faceId6)
			result7 = CF.face.verify(myChildFaceId, faceId7)
						
			results = (result1,result2,result3,result4,result5,result6,result7)
						
			if results[0]['isIdentical'] == True or results[1]['isIdentical'] == True or results[2]['isIdentical'] == True or results[3]['isIdentical'] == True or results[4]['isIdentical'] == True or results[5]['isIdentical'] == True or results[6]['isIdentical'] == True:
				print("match")

		


	
