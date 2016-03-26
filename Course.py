class Course(object):

    def __init__(self, course_id, subject, catalog_number, title, description, prerequisite, terms_offered):
        self.course_id = course_id
        self.subject = subject
        self.catalog_number = catalog_number
        self.title = title
        self.description = description
        self.prerequisite = prerequisite
        self.terms_offered = terms_offered

