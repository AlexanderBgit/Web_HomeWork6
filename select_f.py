import sqlite3
import os
from tabulate import tabulate

def execute_query(filename: str, table_name: str = None) -> str:
    query_file_path = os.path.join("query", filename)
    
    try:
        with open(query_file_path, "r") as file:
            sql = file.read()
    except FileNotFoundError:
        print(f"File '{query_file_path}' not found.")
        return ""

    with sqlite3.connect("hw.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        headers = [description[0] for description in cur.description]
        rows = cur.fetchall()
        
        if table_name:
            table_name_str = f"Query: {table_name}\n"
        else:
            table_name_str = ""
            
        result = table_name_str + tabulate(rows, headers, tablefmt="grid")
        print(result) 
        return result

execute_query("query_01.sql", "1: 5 студентів із найбільшим середнім балом з усіх предметів.")
execute_query("query_02.sql", "2: студент із найвищим середнім балом з певного предмета")
execute_query("query_03.sql", "3: середній бал у групах з певного предмета")
execute_query("query_04_0.sql", "4: середній бал на потоці (по всій таблиці оцінок)")
execute_query("query_04_1.sql", "! Мода балу на потоці (по всій таблиці оцінок)") 

execute_query("query_05.sql", "5: курси, що читає певний викладач")
execute_query("query_06.sql", "6: список студентів у певній групі")
execute_query("query_07.sql", "7: оцінки студентів у окремій групі з певного предмета")
execute_query("query_08.sql", "8: середній бал, який ставить певний викладач зі своїх предметів")

execute_query("query_09.sql", "9: список курсів, які відвідує студент")
execute_query("query_10.sql", "10: список курсів, які певному студенту читає певний викладач")
execute_query("query_11.sql", "11: середній бал, який певний викладач ставить певному студентові")
execute_query("query_12.sql", "12: оцінки студентів у певній групі з певного предмета на останньому занятті")



# third.py