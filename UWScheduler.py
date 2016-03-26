from uwaterlooapi import UWaterlooAPI
from pprint import pprint
import json
import UWHttp
import Course

with open('auth.json') as data_file:
    data = json.load(data_file)

courses_math = UWHttp.get_all_courses_by_term('1161')
# course = uw.course('ACC','621')

list_of_courses = []
for i in courses_math:
    list_of_courses.append([i['subject'], i['catalog_number']])

list_of_courses_details = []
for i in list_of_courses:
    res = UWHttp.get_course(i[0], i[1])
    course = Course(res['course_id'], res['subject'], res['catalog_number'],
                    res['title'], res['description'], res['prerequisites'])




