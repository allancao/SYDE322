import UWHttpParse
import UWDB

# term = ayym
# a = (0, before 2000, or 1, after 2000)
# yy = (last two digits of year)
# m = start month of the term


def init_load_all_courses():
    database_name = 'uwcoursedb.uwcourses'
    UWDB.truncate(database_name)
    current_term = '1161'
    courses_data = UWHttpParse.parse_all_courses_by_term(current_term)
    print(courses_data)

    for course_data in courses_data:
        print(course_data['subject'])
        print(course_data['catalog_number'])

        course = UWHttpParse.parse_course(course_data['subject'], course_data['catalog_number'])
        print('ID: {}'.format(course.course_id))
        print('Subject: {}'.format(course.subject))
        print('Cata num: {}'.format(course.catalog_number))
        print('Title: {}'.format(course.title))
        print('Desc: {}'.format(course.description))
        print('Prereq: {}'.format(course.prerequisites))
        print()
        if course.course_id:
            UWDB.insert(database_name,
                        ['course_id', 'subject', 'catalog_number', 'title', 'description', 'prerequisites'],
                        [course.course_id, course.subject, course.catalog_number, course.title,
                            course.description, course.prerequisites])


def init_load_all_schedules():
    database_name = 'uwcoursedb.courseschedule'
    UWDB.truncate(database_name)
    current_term = '1161'
    courses_data = UWHttpParse.parse_all_courses_by_term(current_term)
    print(courses_data)

    for course_data in courses_data:
        print(course_data['subject'])
        print(course_data['catalog_number'])

        schedules = UWHttpParse.parse_course_schedule((course_data['subject']),
                                                      (course_data['catalog_number']))
        if schedules:
            for schedule in schedules:

                print('Subject: {}'.format(schedule.subject))
                print('Cata num: {}'.format(schedule.catalog_number))
                print('Section: {}'.format(schedule.section))
                print('Start Time: {}'.format(schedule.start_time))
                print('End Time: {}'.format(schedule.end_time))
                print('Weekdays: {}'.format(schedule.weekdays))
                print('Start Date: {}'.format(schedule.start_date))
                print('End Date: {}'.format(schedule.end_date))
                print()
                if schedule.subject and schedule.start_time:
                    UWDB.insert(database_name,
                                ['subject', 'catalog_number', 'section', 'start_time', 'end_time',
                                 'weekdays', 'start_date', 'end_date'],
                                [schedule.subject, schedule.catalog_number, schedule.section,
                                 schedule.start_time,schedule.end_time, schedule.weekdays,
                                 schedule.start_date, schedule.end_date])


init_load_all_schedules()
# init_load_all_courses()