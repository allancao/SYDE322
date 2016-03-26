import MySQLdb
from Course import Course

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="admin",
                     db="uwcoursedb")


def insert(table, cols, values):

    cur = db.cursor()
    # query = 'SET SQL_SAFE_UPDATES=0;'
    query = ''

    cols_constructor = ','.join(cols)
    values_constructor = ','.join(values)
    query += 'INSERT INTO {} ({}) VALUES ({});'.format(table, cols_constructor, values_constructor)
    print(query)
    cur.execute('INSERT INTO {} ({}) VALUES ({});'.format(table, cols_constructor, values_constructor))

    db.commit()
    db.close()


def select(table, cols, where_clause):

    cur = db.cursor()
    # query = 'SET SQL_SAFE_UPDATES=0;'
    query = ''

    cols_constructor = ','.join(cols)
    if len(where_clause) > 0:
        where_clause_constructor = ' AND '.join(where_clause)
        query += 'SELECT {} FROM {} WHERE {};'.format(table, cols_constructor, where_clause_constructor)
        print(query)
        cur.execute(query)
    else:
        query += 'SELECT {} FROM {};'.format(cols_constructor, table)
        print(query)
        cur.execute(query)

    for row in cur.fetchall():
        print row

    db.commit()
    db.close()


def update(table, cols, values, where_clause):

    cur = db.cursor()
    # query = 'SET SQL_SAFE_UPDATES=0;'
    query = ''

    col_value_constructor = ''
    for i in range(0, len(cols)):
        col_value_constructor += ('{}={},'.format(cols[i], values[i]))

    col_value_constructor = col_value_constructor[:-1]
    print(col_value_constructor)

    if len(where_clause) > 0:
        where_clause_constructor = ' AND '.join(where_clause)
        query += 'UPDATE {} SET {} WHERE {};'.format(table, col_value_constructor,
                                                     where_clause_constructor)
        print(query)
        cur.execute(query)
    else:
        query += 'UPDATE {} SET {};'.format(col_value_constructor, table)
        print(query)
        cur.execute(query)

    for row in cur.fetchall():
        print row

    db.commit()
    db.close()


def delete(table, where_clause):

    cur = db.cursor()
    # query = 'SET SQL_SAFE_UPDATES=0;'
    query = ''

    where_clause_constructor = ' AND '.join(where_clause)
    query += 'DELETE FROM {} WHERE {};'.format(table, where_clause_constructor)
    print(query)
    cur.execute(query)

    db.commit()
    db.close()


# course = Course('"123456"', '"SYDE"', '"322"',
#                 '"Soft Design"', '"Intro to UML things"', '"like, basic programming"')
# select('uwcoursedb.uwcourses', ['*'], [])
# insert('uwcoursedb.uwcourses',
#        ['course_id', 'subject', 'catalog_number', 'title', 'description', 'prerequisite'],
#        [course.course_id, course.subject, course.catalog_number, course.title, course.description,
#         course.prerequisite])
# update('uwcoursedb.uwcourses', ['courseID'], ['"22229"'], ['catalogNumber="522"'])
delete('uwcoursedb.uwcourses', ['course_id="123456"'])
