import sqlite3

DB_NAME = "sqlite_db.db"

# Create new table
# with sqlite3.connect(DB_NAME) as cn:
#     sql = '''create table if not exists courses(
#                 id integer primary key,
#                 title text not null,
#                 qty integer,
#                 reviews integer
#             );'''
#     cn.execute(sql)

# with sqlite3.connect(DB_NAME) as cn:
#     sql = '''insert into courses values(?, ?, ?, ?)'''
#
#     courses = [
#         (1, "Python course", 100, 5),
#         (2, "C# course", 10, 5),
#         (3, "JS course", 1, 0)
#     ]
#     for course in courses:
#         print(cn.execute(sql, course))
#     cn.commit()

with sqlite3.connect(DB_NAME) as cn:
    sql = '''select * from courses where qty > 1'''
    cur = cn.execute(sql)
    # for rec in cur:
    #     print(rec)

    courses = cur.fetchall()
    print(courses)
