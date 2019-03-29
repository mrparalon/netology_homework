import psycopg2


db_config = {'dbname': 'netology_db',
             'user': 'netology_user_1',
             'password': '1234',
             'host': '127.0.0.1'}


student_table = ', '.join(['id serial PRIMARY KEY',
                           'name varchar(100) not null',
                           'gpa numeric(10,2)',
                           'birth timestamp with time zone'])

course_table = 'id serial PRIMARY KEY,\
                name varchar(100) not null'

student_course_table = 'id serial PRIMARY KEY,\
                        course_id int not null,\
                        student_id int not null'


def create_db():
    with psycopg2.connect(**db_config) as con:
        with con.cursor() as cur:
            student_req = 'create table student \
                                        (id serial PRIMARY KEY,\
                                        name varchar(100) not null,\
                                        gpa numeric(10,2),\
                                        birth timestamp with time zone);'
            course_req = 'create table course\
                                        (id serial PRIMARY KEY,\
                                        name varchar(100) not null);'
            student_course_req = 'create table student_course\
                                        (id serial PRIMARY KEY,\
                                        student_id int not null,\
                                        course_id int not null)'
            cur.execute(student_req)
            cur.execute(course_req)
            cur.execute(student_course_req)
            print(f'Tables student, course, student-course created')


def get_student(student_id):
    with psycopg2.connect(**db_config) as con:
        with con.cursor() as cur:
            cur.execute('select %d from student' % student_id)
            return cur.fetchone()


student = {
    'name': 'Алексей Шерченков',
    'gpa': '4.0',
    'birth': '1991-12-08'
}


def add_student(student):
    with psycopg2.connect(**db_config) as con:
        with con.cursor() as cur:
            req = "insert into student (name, gpa, birth) \
                 values ('%(name)s', '%(gpa)s', '%(birth)s');" % student
            cur.execute(req)


def create_course(course_name):
    with psycopg2.connect(**db_config) as con:
        with con.cursor() as cur:
            cur.execute("insert into course (name) values ('%s')" %
                        (course_name, ))


def drop_table(table_name):
    with psycopg2.connect(**db_config) as con:
        with con.cursor() as cur:
            cur.execute('drop table %s' % table_name)


if __name__ == '__main__':
    try:
        drop_table('student')
    except psycopg2.ProgrammingError:
        pass
    try:
        drop_table('course')
    except psycopg2.ProgrammingError:
        pass
    try:
        drop_table('student_course')
    except psycopg2.ProgrammingError:
        pass
    create_db()
    courses = ['Frontend-разработчик с нуля',
               'Android-разработчик с нуля',
               'Python-разработчик',
               'Веб-разработчик нуля',
               'Digital-start: первый шаг к востребованной профессии']
    for course in courses:
        create_course(course)
    add_student(student)
    print(get_student(1))
