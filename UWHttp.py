import requests
import json

with open('auth.json') as data_file:
    data = json.load(data_file)
payload = {'key' : data['uw_api_key']}
base_url = 'https://api.uwaterloo.ca/v2{}'


def get_course(subject, catalogue_number):
    course_url = '/courses/{}/{}.json'.format(subject, catalogue_number)
    req = requests.get(base_url.format(course_url), params=payload)
    return req.json()


def get_all_courses_by_term(term):
    course_url = '/terms/{}/courses'.format(term)
    req = requests.get(base_url.format(course_url), params=payload)
    return req.json()

print(get_course('SYDE', '522'))


