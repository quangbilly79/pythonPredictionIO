import csv
import pymysql
import pandas as pd
# conn = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='quang',
#     db='waka',
#     charset='utf8mb4',
#     cursorclass=pymysql.cursors.DictCursor
# )
#
# cursor = conn.cursor()

with open('E:\\waka\\content_category_brid.csv', encoding = 'utf-8') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    # header = next(reader)
    rows = list(reader)

# for i, row in enumerate(rows):
#     if row[0] in ['1186', '2067', '2152']:
#         print(row)
#         print(row[1])
#         print("--------------")
#     else:
#         pass
#         #print(row[0])

with open('E:\\waka\\content_category_brid.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter = ';', lineterminator = '\n')
    writer.writerows(rows)