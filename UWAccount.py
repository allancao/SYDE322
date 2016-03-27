class UWAccount(object):

    student_id = ''
    subject = ''
    catalog_number = ''
    section = ''
    first_name = ''
    last_name = ''

    def __init__(self, student_id, subject, catalog_number,
                 section, first_name, last_name):
        self.student_id = student_id
        self.catalog_number = catalog_number
        self.section = section
        self.subject = subject
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):

        ret = 'student_id={}, subject={}, catalog_number={}, section={}, ' \
              'first_name={}, last_name={}'\
            .format(self.student_id, self.subject, self.catalog_number,
                    self.section, self.first_name, self.last_name)

        return ret

