import psycopg2

# with conn.cursor() as cur:
#     cur.execute('select * from student limit 1')
#     print(cur.fetchall())
#     cur.execute('select * from student limit 1')
#     print(cur.fetchall())

db_config = {'dbname': 'netology_db',
             'user': 'netology_user_1',
             'password': '1234',
             'host': '127.0.0.1'}


def create_db(name):
    with psycopg2.connect(**db_config) as con:
        with con.cursor() as cur:
            req = 'create table %s(\
                         id serial PRIMARY KEY,\
                         name varchar(100) not null,\
                         gpa numeric(10,2),\
                         birth timestamp with time zone)' % (name,)
            cur.execute(req)


create_db("Student")

# def add_course(name):
#     with psycopg2.connect(db_config) as con:
#         with con.cursor() as cur:
#             cur.execute('insert into course (name) \
#                         values (%s) returning id', (name, ))
#             return cur.fetchall()


# new_course_id = add_course('Программирование на Python')
# print(new_course_id)

# with psycopg2.connect(dbname='netology_db',
#                       user='netology_user_1',
#                       password='1234',
#                       host='127.0.0.1') as con:
#     with con.cursor() as cur:
#         cur.execute('select * from course')
#         print(cur.fetchall())
