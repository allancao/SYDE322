import json
import UWDB
import Course
import CourseSchedule
import UWAccount
import datetime


def sanitate(values):
    ret = []
    for i in range(0, len(values)):
        ret.append(json.dumps(values[i]))
    return ret


def get_course(course_id=None, subject=None, catalog_number=None,
               title=None, description=None, prerequisites=None,
               db_table='uwcoursedb.uwcourses'):

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
    rows = UWDB.select(db_table, cols_values, values)
    rows = ['' if x is None else x for x in rows]
    ret = []

    for row in rows:

        course = Course.Course(row[0], row[1], row[2], row[3], row[4], row[5])
        ret.append(course)

    return ret


def get_course_schedule(subject=None, catalog_number=None, section=None,
                        start_time=None, end_time=None, weekdays=None,
                        start_date=None, end_date=None,
                        db_table='uwcoursedb.courseschedule'):
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
        cols_values.append('weekdays')
    if start_date:
        cols_values.append('start_date')
    if end_date:
        cols_values.append('end_date')

    values = sanitate(values)
    rows = UWDB.select(db_table, cols_values, values)
    rows = ['' if x is None else x for x in rows]
    ret = []

    for row in rows:
        course_schedule = CourseSchedule.CourseSchedule(row[0], row[1], row[2], row[3],
                                                        row[4], row[5], row[6], row[7])
        ret.append(course_schedule)

    return ret


def get_account_courses(student_id=None, subject=None, catalog_number=None,
                        section=None, first_name=None, last_name=None,
                        db_table='uwcoursedb.uwaccounts'):
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
    rows = UWDB.select(db_table, cols_values, values)
    rows = ['' if x is None else x for x in rows]
    ret = []

    for row in rows:
        uw_account = UWAccount.UWAccount(row[0], row[1], row[2],
                                         row[3], row[4], row[5])
        ret.append(uw_account)

    return ret


def get_course_schedule_by_time(subject=None, catalog_number=None, section=None,
                                start_time='00:00', end_time='23:59', weekdays=None,
                                start_date=None, end_date=None,
                                db_table='uwcoursedb.courseschedule'):

    temp = get_course_schedule(subject=subject, catalog_number=catalog_number,
                               section=section, weekdays=weekdays,
                               start_date=start_date, end_date=end_date,
                               db_table=db_table)

    # ret = temp

    time_format = '%H:%M'
    target_start_time = datetime.datetime.strptime(start_time, time_format)
    target_end_time = datetime.datetime.strptime(end_time, time_format)

    remove = []

    for schedule in temp:
        current_start_time = datetime.datetime.strptime(schedule.start_time, time_format)
        current_end_time = datetime.datetime.strptime(schedule.end_time, time_format)

        if target_start_time >= current_start_time or target_end_time <= current_end_time:
            remove.append(schedule)
        else:
            same_course_sections = get_course_schedule(subject=schedule.subject,
                                                       catalog_number=schedule.catalog_number,
                                                       section=schedule.section)

            for same_course_section in same_course_sections:
                current_section_start_time = \
                    datetime.datetime.strptime(same_course_section.start_time, time_format)
                current_section_end_time = \
                    datetime.datetime.strptime(same_course_section.end_time, time_format)
                if target_start_time >= current_section_start_time or \
                        target_end_time <= current_section_end_time:
                    remove.extend(same_course_sections)

    for schedule in remove:
        temp.remove(schedule)
    return temp


def insert_account_courses(student_id=None, subject=None, catalog_number=None,
                           section=None, first_name=None, last_name=None,
                           db_table='uwcoursedb.uwaccounts'):

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
    UWDB.insert(db_table, cols_values, values)


def delete_account_courses(student_id=None, subject=None, catalog_number=None,
                           section=None, first_name=None, last_name=None,
                           db_table='uwcoursedb.uwaccounts'):

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
    UWDB.delete(db_table, cols_values, values)

# insert_account_courses(student_id='20420902', subject='SYDE', catalog_number='322',
#                        section='LEC 001', first_name='Allan', last_name='Cao')

list = get_course_schedule_by_time(subject='SYDE', catalog_number='322', section=None,
                                   start_time='00:00', end_time='23:59', weekdays=None,
                                   start_date=None, end_date=None)

for i in list:
    print(i)

# list = get_course_schedule_by_time(subject='SYDE', catalog_number='322', section=None,
#                                    start_time='14:30', end_time='15:30', weekdays=None,
#                                    start_date=None, end_date=None)
# for i in list:
#     print(i)
#
# delete_account_courses(student_id='20420902')

# list = get_account_courses(student_id='20420902')
# for i in list:
#     print(i)

# delete_account_courses(student_id='20420902')

# list = get_course(subject='SYDE', catalog_number='322')
# for i in list:
#     print(i)

# get_course(course_id=json.dumps('10000'), subject='subject', catalog_number='catalog_number',
#            title=None, description='description', prerequisites='prereq')