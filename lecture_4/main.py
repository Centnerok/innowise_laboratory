import sqlite3 # import sqlite3 library
con = sqlite3.connect("lecture_4\\school.db") # connect sqlite3 with school.db

cur = con.cursor()
