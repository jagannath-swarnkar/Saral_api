import requests
import json
import os.path
from os import path
import pprint

exist=path.exists("/home/deepanshu/Documents/request.coarses.json")

if not exist:
	def req():
		url="http://saral.navgurukul.org/api/courses"
		page=requests.get(url)

		with open('coarses.json','w') as json_file:
			json.dump(page.text,json_file)
		# print(page.text)		
	req()

def load():
	with open('coarses.json') as data_file:
		data_file=data_file.read()
		data_file=json.loads(data_file)
		data_file=json.loads(data_file)
	courses={}
	for course in data_file['availableCourses']:
		courses[course['id']]=course['name']
	return courses
load()
pprint.pprint(load())
courses=load()

def api_again():
	user=int(input("Enter the Id of the course :"))
	exercise_name=courses[user]
	exists=path.exists("/home/deepanshu/Documents/request.%s.json"%exercise_name)
	if not exists:
		page=requests.get("http://saral.navgurukul.org/api/courses/%s/exercises"%user)
		with open("%s.json"%exercise_name,'w') as content:
			json.dump(page.text,content)
	
	with open("%s.json"%exercise_name)as data_file:
		data_file=data_file.read()
		data_file=json.loads(data_file)
		data_file=json.loads(data_file)
	
	exercise=data_file['data']
	return exercise
exercise=api_again()

index=0
# for slug in exercise:
# 	print(index,slug["slug"])
# 	a=1
# 	for i in slug["childExercises"]:
# 		# if i.isalpha():
# 			print('                ',i)
# 	index+=1

for name in exercise:
	print(index,name['name'])
	index+=1


def laststep(user):
	user_again=input("\nEnter the step you want ?, p- previous ,up- up_navigation ,n- next_nevigation")
	if user_again=='p':
		user=user-1
		slugAaya(user)
	elif user_again=="n":
		user=user+1
		slugAaya(user)
	elif user_again=="up":
		pprint.pprint(load())
		api_again()	
		slugAaya(user)

def slugAaya(user):
	slug=exercise[user]['slug']
	page=requests.get("http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug=%s"%slug)
	print (page.text)
	laststep(user)
user=int(input("Enter the index of childExercise for content:"))
slugAaya(user)







