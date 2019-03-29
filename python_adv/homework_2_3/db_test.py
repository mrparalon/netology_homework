import psycopg2


db_config = {'dbname': 'netology_db',
             'user': 'netology_user_1',
             'password': '1234',
             'host': '127.0.0.1'}


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
            cur.execute('select * from student where id=%d' % student_id)
            return cur.fetchone()


def get_students(course_id):
    with psycopg2.connect(**db_config) as con:
        with con.cursor() as cur:
            req = 'select student.id, student.name from student \
                   join student_course on student.id = student_course.student_id \
                   join course on course.id = student_course.course_id \
                   where course.id = %d;' % course_id
            cur.execute(req)
            return cur.fetchall()


def add_students(course_id, students):
    student_id_list = []
    if not isinstance(students, list):
        students = [students]
    for student in students:
        student_id = add_student(student)
        student_id_list.append(student_id)
    with psycopg2.connect(**db_config) as con:
        with con.cursor() as cur:
            for student in student_id_list:
                cur.execute('insert into student_course (student_id, course_id)\
                    values (%s, %s);' % (student, course_id))


def add_student(student):
    with psycopg2.connect(**db_config) as con:
        with con.cursor() as cur:
            req = "insert into student (name, gpa, birth) \
                    values ('%(name)s', '%(gpa)s', '%(birth)s') returning id;"\
                    % student
            cur.execute(req)
            return cur.fetchone()[0]


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
    student = {'name': 'Алексей Шерченков',
               'gpa': '4.0',
               'birth': '1991-08-12'}
    students = [{'name': 'Евгений Маликов',
                 'gpa': '2.3',
                 'birth': '1994-11-03'},
                {'name': 'Николай Дмуха',
                 'gpa': '3.8',
                 'birth': '1990-06-06'},
                {'name': 'Павел Козлов',
                 'gpa': '3.7',
                 'birth': '1985-05-08'}]
    courses = ['Frontend-разработчик с нуля',
               'Android-разработчик с нуля',
               'Python-разработчик',
               'Веб-разработчик нуля',
               'Digital-start: первый шаг к востребованной профессии']
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
    for course in courses:
        create_course(course)
    add_student(student)
    print(get_student(1))
    add_students(2, students)
    add_students(4, student)
    print(get_students(2))
