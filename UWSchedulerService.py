import json
import UWDB
import Course
import CourseSchedule

uw_courses = 'uwcoursedb.uwcourses'
uw_course_schedule = 'uwcoursedb.courseschedule'


def sanitate(values):
    ret = []
    for i in range(0, len(values)):
        ret.append(json.dumps(values[i]))
    return ret


def get_course(course_id=None, subject=None, catalog_number=None,
               title=None, description=None, prerequisites=None):

    values = filter(None, [course_id, subject,
                           catalog_number, title, description, prerequisites])
    cols_values = []

    if course_id:
        cols_values.append('course_id')
    if subject:
        cols_values.append('subject')
    if catalog_number:
        cols_values.append('catalog_number')
    if title:
        cols_values.append('title')
    if description:
        cols_values.append('description')
    if prerequisites:
        cols_values.append('prerequisites')

    values = sanitate(values)
    rows = UWDB.select(uw_courses, cols_values, values)
    rows = ['' if x is None else x for x in rows]
    ret = []

    for row in rows:

        course = Course.Course(row[0], row[1], row[2], row[3], row[4], row[5])
        ret.append(course)

    return ret


def get_course_schedule(subject=None, catalog_number=None, section=None,
                        start_time=None, end_time=None, weekdays=None,
                        start_date=None, end_date=None):
    values = filter(None, [subject, catalog_number, section, start_time,
                           end_time, weekdays, start_date, end_date])

    cols_values = []

    if subject:
        cols_values.append('subject')
    if catalog_number:
        cols_values.append('catalog_number')
    if section:
        cols_values.append('section')
    if start_time:
        cols_values.append('start_time')
    if end_time:
        cols_values.append('end_time')
    if weekdays:
        cols_values.append('end_time')
    if start_date:
        cols_values.append('end_time')
    if end_date:
        cols_values.append('end_time')

    values = sanitate(values)
    rows = UWDB.select(uw_course_schedule, cols_values, values)
    rows = ['' if x is None else x for x in rows]
    ret = []
    
    for row in rows:
        course_schedule = CourseSchedule.CourseSchedule(row[0], row[1], row[2], row[3],
                                                        row[4], row[5], row[6], row[7])
        ret.append(course_schedule)
    
    return ret


list = get_course_schedule(subject='SYDE', catalog_number='322')
for i in list:
    print(i)

# list = get_course(subject='SYDE', catalog_number='322')
# for i in list:
#     print(i)

# get_course(course_id=json.dumps('10000'), subject='subject', catalog_number='catalog_number',
#            title=None, description='description', prerequisites='prereq')