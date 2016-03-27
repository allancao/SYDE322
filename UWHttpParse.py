import UWHttp
import Course
import CourseSchedule
import json
import re


def parse_course(subject, catalog_number):

    regex = re.compile('[^a-zA-Z0-9]')
    response = UWHttp.get_course(regex.sub('', subject), regex.sub('', catalog_number))

    data = response['data']
    course = Course.Course('', '', '', '', '', '')

    if data:
        course_id = json.dumps(data['course_id'])
        subject = json.dumps(data['subject'])
        catalog_number = json.dumps(data['catalog_number'])
        title = json.dumps(data['title'])
        description = json.dumps(data['description'])
        prerequisites = json.dumps(data['prerequisites'])

        # print(course_id)
        # print(subject)
        # print(catalog_number)
        # print(title)
        # print(description)
        # print(prerequisites)
        if course_id and subject and catalog_number:
            course = Course.Course(course_id, subject, catalog_number, title, description, prerequisites)

    return course


def parse_all_courses_by_term(term):
    regex = re.compile('[^a-zA-Z0-9]')
    response = UWHttp.get_all_courses_by_term(regex.sub('', term))
    data = response['data']
    courses = []

    if data:
        for course in data:
            courses.append({'subject': json.dumps(course['subject']),
                            'catalog_number': json.dumps(course['catalog_number'])})

    return courses


def parse_course_schedule(subject, catalog_number):
    regex = re.compile('[^a-zA-Z0-9]')
    response = UWHttp.get_course_schedule(regex.sub('', subject), regex.sub('', catalog_number))
    data = response['data']
    course_schedules = []

    for schedule in data:
        section = json.dumps(schedule['section'])
        if 'classes' in schedule:
            for schedule_class in schedule['classes']:

                start_time = json.dumps(schedule_class['date']['start_time'])
                end_time = json.dumps(schedule_class['date']['end_time'])
                weekdays = json.dumps(schedule_class['date']['weekdays'])
                start_date = json.dumps(schedule_class['date']['start_date'])
                end_date = json.dumps(schedule_class['date']['end_date'])

                # print(section)
                # print(catalog_number)
                # print(start_time)
                # print(end_time)
                # print(weekdays)
                # print(start_date)
                # print(end_date)

                if start_time is not 'null' and end_time is not 'null' \
                        and weekdays is not 'null':
                    course_schedule = CourseSchedule.CourseSchedule(subject, catalog_number,
                                                                    section, start_time,
                                                                    end_time, weekdays,
                                                                    start_date, end_date)

                    course_schedules.append(course_schedule)

    return course_schedules

print(parse_course_schedule('SYDE', '322'))
