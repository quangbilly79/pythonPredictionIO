from impala.dbapi import connect

import time

timestart = time.time()
conn = connect(host='172.25.48.129', port=21050, database='waka') # 21050 la Impala Deamon Frontend port
cursorUser = conn.cursor()
userid = 9999999 # 3269007 / [91, 99, 188, 84, 33, 45, 73, 155, 61, 177, 182, 71, 94, 117, 44, 101, 81, 39, 40, 176, 100]
cursorUser.execute(f"""select user_id, group_concat(distinct cast(ccb.category_id as string)) as category
                from waka_pd_fact_reader as wr
                join content_category_brid as ccb
                on wr.content_id = ccb.content_id
                where user_id = {userid} and data_date_key >= 20220101
                group by user_id order by user_id""")

# and data_date_key >= 20220601 and data_date_key < 20220701
row = cursorUser.fetchone()
if row == None:
    print("A")
print(row[1])
list1 = row[1].split(", ")
print(list1)

timeend = time.time()
print(timestart)
print(timeend)
print(timeend-timestart)


# cursorItem = conn.cursor()
# itemid = 36302 # 36032 / 41, 71
# cursorItem.execute(f"""
# select cd.content_id, group_concat(distinct cast(category_id as string)) as category
# from content_dim as cd
# join content_category_brid as ccb
# on cd.content_id = ccb.content_id
# where cd.content_id = {itemid}
# group by cd.content_id
# """)
#
# row1=cursorItem.fetchone()
# list1 = row1[1].split(", ")
#
# timeend = time.time()
# print(timestart)
# print(timeend)
# print(timeend-timestart) #0.54 0.51