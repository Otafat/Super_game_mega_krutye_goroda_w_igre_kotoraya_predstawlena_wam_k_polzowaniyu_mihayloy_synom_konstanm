import sqlite3
import time

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

id = 30806644
sql = f"""UPDATE users
            SET balance=1000
            WHERE vk_id = {id}
"""
cursor.execute(sql)
conn.commit()

def add_mission(id, name, desc, reward):
    sql = f"""INSERT INTO missions(id, name, desc, reward)
    VALUES({id}, "{name}", "{desc}", "{reward}")"""
    cursor.execute(sql)
    conn.commit()

add_mission(1, 'Помощь бабушце', 'Помозите бабушце донести воду до дома', 'exp+5, wood+1')
add_mission(2, 'Древорубня', 'Нарубь маленько деревцы, да отнеси домовь.', 'exp+12, wood+10')
add_mission(3, 'Во имя Нила Армстронга', 'Посадите картошку на луне', 'exp+500, food+200, gold+500')
add_mission(4, 'Плотничество', 'Сделайте стол.', 'exp+10, gold+10')
add_mission(5, 'Охота', 'Заколи трёх диких коз', 'exp+20, food+13')
add_mission(6, 'Водораздел', 'Полей огороды', 'exp+3')
add_mission(7, 'Самоослепление', 'Съешь гнилой картофель и выживи', 'exp+60')
add_mission(8, 'Во имя Ленина', 'Захватите Америку', 'exp+6000, gold+50000, food+9000')
add_mission(9, 'Глобальная вакцинация', 'Заразите всю деревню оспой, а потом вылечите её', 'exp+150, gold+200')
add_mission(10, 'Воин', 'Победите стадо Морлоков', 'exp+200, gold+300, wood+600, iron+300, food+900')


#id = 30806644
#sql = f"""SELECT *
#            FROM users
#            WHERE vk_id = {id}            
#"""
#cursor.execute(sql)
#user = cursor.fetchall()
#print(user)

#sql = f"""INSERT INTO users(vk_id, nick)
#            VALUES(30806644,  'nongi')
#"""
#cursor.execute(sql)
#conn.commit()

# sql = f"""create table missions(
#             id integer PRIMARY KEY NOT NULL UNIQUE,
#             name text,
#             desc text,
#             reward text)"""
# cursor.execute(sql)
# conn.commit()