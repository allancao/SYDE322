import unittest
import MySQLdb
import UWSchedulerService


class UWSchedulerServiceTest(unittest.TestCase):

    def setUp(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="admin")
        cursor = db.cursor()
        sql = 'CREATE DATABASE mydata'
        cursor.execute(sql)
        sql = 'USE mydata'
        cursor.execute(sql)

        create_uw_accounts = 'CREATE TABLE `uwaccounts` (\
                            `student_id` varchar(10) NOT NULL,\
                            `subject` varchar(45) NOT NULL,\
                            `catalog_number` varchar(45) NOT NULL,\
                            `section` varchar(45) NOT NULL,\
                            `first_name` varchar(45) DEFAULT NULL,\
                            `last_name` varchar(45) DEFAULT NULL,\
                            PRIMARY KEY (`student_id`,`subject`,`catalog_number`,`section`)\
                            ) ENGINE=InnoDB DEFAULT CHARSET=utf8'

        create_courses_schedule = 'CREATE TABLE `courseschedule` ('\
                                  '`subject` varchar(45) NOT NULL,\
                                   `catalog_number` varchar(45) NOT NULL,\
                                   `section` varchar(45) NOT NULL,\
                                   `start_time` varchar(45) DEFAULT NULL,\
                                   `end_time` varchar(45) DEFAULT NULL,\
                                   `weekdays` varchar(45) DEFAULT NULL,\
                                   `start_date` varchar(45) DEFAULT NULL,\
                                   `end_date` varchar(45) DEFAULT NULL,\
                                   `index` int(11) NOT NULL AUTO_INCREMENT,\
                                   PRIMARY KEY (`index`)\
                                 ) ENGINE=InnoDB AUTO_INCREMENT=5704 DEFAULT CHARSET=utf8'

        create_courses = 'CREATE TABLE `uwcourses` (' \
                         '`course_id` varchar(256) NOT NULL,\
                           `subject` varchar(256) NOT NULL,\
                           `catalog_number` varchar(256) NOT NULL,\
                           `title` varchar(256) DEFAULT NULL,\
                           `description` longtext,\
                           `prerequisites` longtext,\
                           PRIMARY KEY (`course_id`,`subject`,`catalog_number`)\
                         ) ENGINE=InnoDB DEFAULT CHARSET=utf8'

        cursor.execute(create_uw_accounts)
        cursor.execute(create_courses_schedule)
        cursor.execute(create_courses)

        sql_uwaccounts_test_data_1 = 'INSERT INTO `uwaccounts` ' \
                          '(student_id, subject, catalog_number, ' \
                          'section, first_name, last_name)' \
                          'VALUES' \
                          '("00000001", "SYDE", "001", "LEC 001", "John", "Doe")'

        sql_uwaccounts_test_data_2 = 'INSERT INTO `uwaccounts` ' \
                          '(student_id, subject, catalog_number, ' \
                          'section, first_name, last_name)' \
                          'VALUES ' \
                          '("00000002", "SYDE", "002", "TUT 001", "Simon", "Smith")'

        sql_courses_schedule_test_data_1 = 'INSERT INTO `courseschedule` ' \
                                           '(subject, catalog_number, section, start_time, ' \
                                           'end_time, weekdays, start_date, end_date) ' \
                                           'VALUES ' \
                                           '("SYDE", "001", "LEC 001", "00:00", ' \
                                           '"23:59", "MTWThF", "1/1", "4/31")'

        sql_courses_schedule_test_data_2 = 'INSERT INTO `courseschedule` ' \
                                           '(subject, catalog_number, section, start_time, ' \
                                           'end_time, weekdays, start_date, end_date) ' \
                                           'VALUES ' \
                                           '("SYDE", "002", "TUT 001", "09:00", ' \
                                           '"21:59", "MTWThF", "5/1", "12/31")'

        sql_courses_test_data_1 = 'INSERT INTO `uwcourses` (' \
                         'course_id, subject, catalog_number, title, description, prerequisites)' \
                         'VALUES ' \
                         '("222222", "SYDE", "999", "Advanced SYDE", ' \
                         '"The real SYDE", "things")'

        sql_courses_test_data_2 = 'INSERT INTO `uwcourses` (' \
                         'course_id, subject, catalog_number, title, description, prerequisites)' \
                         'VALUES ' \
                         '("111111", "SYDE", "001", "Intro to SYDE", ' \
                         '"An intro to systems design engineering", "high school")'

        cursor.execute(sql_uwaccounts_test_data_1)
        cursor.execute(sql_uwaccounts_test_data_2)
        cursor.execute(sql_courses_schedule_test_data_1)
        cursor.execute(sql_courses_schedule_test_data_2)
        cursor.execute(sql_courses_test_data_1)
        cursor.execute(sql_courses_test_data_2)

        cursor.close()
        db.commit()
        db.close()

    def tearDown(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="admin")
        cursor = db.cursor()
        sql = 'DROP DATABASE mydata'
        cursor.execute(sql)

    def test_get_course(self):

        ret = UWSchedulerService.get_course(db_table='mydata.uwcourses')
        self.assertEqual(len(ret), 2, 'incorrect select return size on *')

        ret = UWSchedulerService.get_course(course_id='111111', db_table='mydata.uwcourses')
        self.assertEqual(len(ret), 1, 'incorrect select return size on course_id')

        ret = UWSchedulerService.get_course(subject='SYDE', db_table='mydata.uwcourses')
        self.assertEqual(len(ret), 2, 'incorrect select return size on subject')

        ret = UWSchedulerService.get_course(catalog_number='999', db_table='mydata.uwcourses')
        self.assertEqual(len(ret), 1, 'incorrect select return size on catalog_number')

        ret = UWSchedulerService.get_course(title='Intro to SYDE', db_table='mydata.uwcourses')
        self.assertEqual(len(ret), 1, 'incorrect select return size on title')

        ret = UWSchedulerService.get_course(description='The real SYDE', db_table='mydata.uwcourses')
        self.assertEqual(len(ret), 1, 'incorrect select return size on description')

        ret = UWSchedulerService.get_course(prerequisites='high school', db_table='mydata.uwcourses')
        self.assertEqual(len(ret), 1, 'incorrect select return size on prerequisites')

        ret = UWSchedulerService.get_course(course_id='333333', db_table='mydata.uwcourses')
        self.assertEqual(len(ret), 0, 'incorrect select return size on non-existant course_id')

    def test_get_course_schedule(self):
        ret = UWSchedulerService.get_course_schedule(db_table='mydata.courseschedule')
        self.assertEqual(len(ret), 2, 'incorrect select return size on *')

        ret = UWSchedulerService.get_course_schedule(subject='SYDE', db_table='mydata.courseschedule')
        self.assertEqual(len(ret), 2, 'incorrect select return size on subject')

        ret = UWSchedulerService.get_course_schedule(catalog_number='002', db_table='mydata.courseschedule')
        self.assertEqual(len(ret), 1, 'incorrect select return size on catalog_number')

        ret = UWSchedulerService.get_course_schedule(section='LEC 001', db_table='mydata.courseschedule')
        self.assertEqual(len(ret), 1, 'incorrect select return size on section')

        ret = UWSchedulerService.get_course_schedule(start_time='00:00', db_table='mydata.courseschedule')
        self.assertEqual(len(ret), 1, 'incorrect select return size on start_time')

        ret = UWSchedulerService.get_course_schedule(end_time='23:59', db_table='mydata.courseschedule')
        self.assertEqual(len(ret), 1, 'incorrect select return size on end_time')

        ret = UWSchedulerService.get_course_schedule(weekdays='MTWThF', db_table='mydata.courseschedule')
        self.assertEqual(len(ret), 2, 'incorrect select return size on weekdays')

        ret = UWSchedulerService.get_course_schedule(start_date='1/1', db_table='mydata.courseschedule')
        self.assertEqual(len(ret), 1, 'incorrect select return size on start_date')

        ret = UWSchedulerService.get_course_schedule(end_date='4/31', db_table='mydata.courseschedule')
        self.assertEqual(len(ret), 1, 'incorrect select return size on end_date')

        ret = UWSchedulerService.get_course_schedule(subject='MSCI', db_table='mydata.courseschedule')
        self.assertEqual(len(ret), 0, 'incorrect select return size on non-existant subject')

    def test_get_account_courses(self):
        ret = UWSchedulerService.get_account_courses(db_table='mydata.uwaccounts')
        self.assertEqual(len(ret), 2, 'incorrect select return size on *')

        ret = UWSchedulerService.get_account_courses(student_id='00000001', db_table='mydata.uwaccounts')
        self.assertEqual(len(ret), 1, 'incorrect select return size on student_id')

        ret = UWSchedulerService.get_account_courses(subject='SYDE', db_table='mydata.uwaccounts')
        self.assertEqual(len(ret), 2, 'incorrect select return size on subject')

        ret = UWSchedulerService.get_account_courses(catalog_number='001', db_table='mydata.uwaccounts')
        self.assertEqual(len(ret), 1, 'incorrect select catalog_number size on catalog_number')

        ret = UWSchedulerService.get_account_courses(section='LEC 001', db_table='mydata.uwaccounts')
        self.assertEqual(len(ret), 1, 'incorrect select return size on section')

        ret = UWSchedulerService.get_account_courses(first_name='John', db_table='mydata.uwaccounts')
        self.assertEqual(len(ret), 1, 'incorrect select return size on first_name')

        ret = UWSchedulerService.get_account_courses(last_name='Doe', db_table='mydata.uwaccounts')
        self.assertEqual(len(ret), 1, 'incorrect select return size on last_name')

        ret = UWSchedulerService.get_account_courses(subject='MSCI', db_table='mydata.uwaccounts')
        self.assertEqual(len(ret), 0, 'incorrect select return size on non-existant subject')

    def test_insert_account_courses(self):
        student_id = '00000'
        subject = 'TEST'
        catalog_number = '111'
        section = 'TEST 111'
        first_name = 'TEST_FIRST_NAME'
        last_name = 'TEST_LAST_NAME'

        UWSchedulerService.insert_account_courses(student_id=student_id, subject=subject,
                                                  catalog_number=catalog_number, section=section,
                                                  first_name=first_name, last_name=last_name,
                                                  db_table='mydata.uwaccounts')

        sql = 'SELECT * FROM mydata.uwaccounts WHERE {}'.format('student_id="00000" AND '
                                                                'subject="TEST" AND '
                                                                'catalog_number="111" AND '
                                                                'section="TEST 111" AND '
                                                                'first_name="TEST_FIRST_NAME" AND '
                                                                'last_name="TEST_LAST_NAME"')

        # sql = 'SELECT * FROM mydata.uwaccounts'

        db = MySQLdb.connect(host="localhost", user="root", passwd="admin", db="mydata")
        cursor = db.cursor()
        cursor.execute(sql)
        ret = []
        for row in cursor.fetchall():
            ret.append(row)
        cursor.close()

        print(ret)
        self.assertEqual(len(ret), 1, 'did not insert properly')

    def test_delete_account_courses(self):

        student_id = '00000'
        subject = 'TEST'
        catalog_number = '111'
        section = 'TEST 111'
        first_name = 'TEST_FIRST_NAME'
        last_name = 'TEST_LAST_NAME'

        sql = 'INSERT INTO `uwaccounts` ' \
              '(student_id, subject, catalog_number, ' \
              'section, first_name, last_name)' \
              'VALUES' \
              '("{}", "{}", "{}", "{}", "{}", "{}")'.format(student_id, subject, catalog_number,
                                                            section, first_name, last_name)

        db = MySQLdb.connect(host="localhost", user="root", passwd="admin", db="mydata")
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()

        UWSchedulerService.delete_account_courses(student_id=student_id, subject=subject,
                                                  catalog_number=catalog_number, section=section,
                                                  first_name=first_name, last_name=last_name,
                                                  db_table='mydata.uwaccounts')

        ret = []
        for row in cursor.fetchall():
            ret.append(row)
        cursor.close()

        print(ret)
        self.assertEqual(len(ret), 0, 'did not delete properly')

# UWSchedulerServiceTestSuite = unittest.TestSuite()
# UWSchedulerServiceTestSuite.addTest(UWSchedulerServiceTest('test_get_course'))
# UWSchedulerServiceTestSuite.addTest(UWSchedulerServiceTest('test_get_course_schedule'))
# UWSchedulerServiceTestSuite.addTest(UWSchedulerServiceTest('test_get_account_courses'))
# UWSchedulerServiceTestSuite.addTest(UWSchedulerServiceTest('test_insert_account_courses'))
# UWSchedulerServiceTestSuite.addTest(UWSchedulerServiceTest('test_delete_account_courses'))


