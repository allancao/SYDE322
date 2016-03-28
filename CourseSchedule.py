class CourseSchedule(object):

    subject = ''
    catalog_number = ''
    section = ''
    start_time = ''
    end_time = ''
    weekdays = ''
    start_date = ''
    end_date = ''

    def __init__(self, subject, catalog_number, section, start_time, end_time,
                 weekdays, start_date, end_date):
        self.subject = subject
        self.catalog_number = catalog_number
        self.section = section
        self.start_time = start_time
        self.end_time = end_time
        self.weekdays = weekdays
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):

        ret = 'subject={}, catalog_number={}, section={}, start_time={}, ' \
              'end_time={}, weekdays={}, start_date={}, end_date={}'\
            .format(self.subject, self.catalog_number, self.section, self.start_time,
                    self.end_time, self.weekdays, self.start_date, self.end_date)

        return ret

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
