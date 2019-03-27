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


if __name__ == '__main__':
    # create_db('student', student_table)
    # create_db('course', course_table)
    # create_db('student_course', student_course_table)
