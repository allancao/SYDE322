import MySQLdb


def insert(table, cols, values):
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="admin",
                         db="uwcoursedb")

    cur = db.cursor()
    # query = 'SET SQL_SAFE_UPDATES=0;'
    query = ''
    cols_constructor = ','.join(cols)
    values_constructor = ','.join(values)
    # values_constructor = ''
    # for value in values:
    #     values_constructor += ('\"{}\",'.format(value))
    # values_constructor = values_constructor[:-1]

    query += 'INSERT INTO {} ({}) VALUES ({});'.format(table, cols_constructor, values_constructor)
    print(query)
    cur.execute('INSERT INTO {} ({}) VALUES ({});'.format(table, cols_constructor, values_constructor))

    db.commit()
    db.close()


def select(table, cols_values, values):
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="admin",
                         db="uwcoursedb")

    cur = db.cursor()
    # query = 'SET SQL_SAFE_UPDATES=0;'
    query = ''

    if cols_values:

        where_clause_constructor = []
        for i in range(0, len(values)):
            where_clause_constructor.append('{}={}'.format(cols_values[i], values[i]))
        where_clause_constructor = ' AND '.join(where_clause_constructor)

        query += 'SELECT * FROM {} WHERE {};'.format(table, where_clause_constructor)
        print(query)
        cur.execute(query)
    else:
        query += 'SELECT * FROM {};'.format(table)
        print(query)
        cur.execute(query)

    ret = []
    for row in cur.fetchall():
        ret.append(row)

    db.commit()
    db.close()

    return ret


def update(table, cols, values, where_clause):
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="admin",
                         db="uwcoursedb")

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
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="admin",
                         db="uwcoursedb")

    cur = db.cursor()
    # query = 'SET SQL_SAFE_UPDATES=0;'
    query = ''

    where_clause_constructor = ' AND '.join(where_clause)
    query += 'DELETE FROM {} WHERE {};'.format(table, where_clause_constructor)
    print(query)
    cur.execute(query)

    db.commit()
    db.close()


def truncate(table):
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="admin",
                         db="uwcoursedb")

    cur = db.cursor()
    # query = 'SET SQL_SAFE_UPDATES=0;'
    query = ''

    query += 'TRUNCATE TABLE {};'.format(table)
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
# delete('uwcoursedb.uwcourses', ['course_id="123456"'])

