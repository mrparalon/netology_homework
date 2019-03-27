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

# Я не придумал, как лучше передавать схему в функцию. Были варианты сделать
# словарь или список списков с параметрами, но он бы потом собирался в строку.
# Поэтому я решил все оставить простой строкой.


def create_db(name, table):
    with psycopg2.connect(**db_config) as con:
        with con.cursor() as cur:
            req = 'create table %s (%s);' % (name, table)
            cur.execute(req)
            print(f'Table {name} created')
            return name


def create_course(course_name, course_table_name):
    with psycopg2.connect(**db_config) as con:
        with con.cursor() as cur:
            cur.execute("insert into %s (name) values ('%s')" %
                        (course_table_name, course_name))


if __name__ == '__main__':
    student_table_name = create_db('student', student_table)
    course_table_name = create_db('course', course_table)
    student_course_table_name = create_db('student_course',
                                          student_course_table)
    courses = ['Frontend-разработчик с нуля',
               'Android-разработчик с нуля'
               'Python-разработчик',
               'Веб-разработчик нуля',
               'Digital-start: первый шаг к востребованной профессии']
    for course in courses:
        create_course(course, course_table_name)
