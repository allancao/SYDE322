class Course(object):

    course_id = ''
    subject = ''
    catalog_number = ''
    title = ''
    description = ''
    prerequisites = ''

    def __init__(self, course_id, subject, catalog_number, title, description, prerequisites):
        self.course_id = course_id
        self.subject = subject
        self.catalog_number = catalog_number
        self.title = title
        self.description = description
        self.prerequisites = prerequisites


