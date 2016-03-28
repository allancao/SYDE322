import json
import UWDB
import Course
import CourseSchedule
import UWAccount

uw_courses = 'uwcoursedb.uwcourses'
uw_course_schedule = 'uwcoursedb.courseschedule'
uw_accounts = 'uwcoursedb.uwaccounts'


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


def get_account_courses(student_id=None, subject=None, catalog_number=None,
                        section=None, first_name=None, last_name=None):
    values = filter(None, [student_id, subject, catalog_number,
                           section, first_name, last_name])

    cols_values = []

    if student_id:
        cols_values.append('student_id')
    if subject:
        cols_values.append('subject')
    if catalog_number:
        cols_values.append('catalog_number')
    if section:
        cols_values.append('section')
    if first_name:
        cols_values.append('first_name')
    if last_name:
        cols_values.append('last_name')

    values = sanitate(values)
    rows = UWDB.select(uw_accounts, cols_values, values)
    rows = ['' if x is None else x for x in rows]
    ret = []

    for row in rows:
        uw_account = UWAccount.UWAccount(row[0], row[1], row[2],
                                         row[3], row[4], row[5])
        ret.append(uw_account)

    return ret


def insert_account_courses(student_id=None, subject=None, catalog_number=None,
                           section=None, first_name=None, last_name=None):

    values = filter(None, [student_id, subject, catalog_number,
                           section, first_name, last_name])

    cols_values = []

    if student_id:
        cols_values.append('student_id')
    if subject:
        cols_values.append('subject')
    if catalog_number:
        cols_values.append('catalog_number')
    if section:
        cols_values.append('section')
    if first_name:
        cols_values.append('first_name')
    if last_name:
        cols_values.append('last_name')

    values = sanitate(values)
    UWDB.insert(uw_accounts, cols_values, values)


def delete_account_courses(student_id=None, subject=None, catalog_number=None,
                           section=None, first_name=None, last_name=None):

    values = filter(None, [student_id, subject, catalog_number,
                           section, first_name, last_name])

    cols_values = []

    if student_id:
        cols_values.append('student_id')
    if subject:
        cols_values.append('subject')
    if catalog_number:
        cols_values.append('catalog_number')
    if section:
        cols_values.append('section')
    if first_name:
        cols_values.append('first_name')
    if last_name:
        cols_values.append('last_name')

    values = sanitate(values)
    UWDB.delete(uw_accounts, cols_values, values)


# insert_account_courses(student_id='20420902', subject='SYDE', catalog_number='322',
                       # section='LEC 001', first_name='Allan', last_name='Cao')

# list = get_account_courses(student_id='20420902')
# for i in list:
#     print(i)

# delete_account_courses(student_id='20420902')

list = get_course(subject='SYDE', catalog_number='322')
for i in list:
    print(i)

# get_course(course_id=json.dumps('10000'), subject='subject', catalog_number='catalog_number',
#            title=None, description='description', prerequisites='prereq')