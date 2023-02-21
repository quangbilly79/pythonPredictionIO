import pymysql.cursors
import time
timestart = time.time()
connection = pymysql.connect(host='172.25.0.101',
                             user='etl',
                             password='Vega123312##',
                             database='waka',
                             cursorclass=pymysql.cursors.DictCursor)
with connection:
    with connection.cursor() as cursor:
        # Read a single record
        itemid = 99999
        sqlUser = f"""
            select cd.content_id, group_concat(distinct cast(category_id as char(5))) as category
            from content_dim as cd
            join content_category_brid as ccb
            on cd.content_id = ccb.content_id
            where cd.content_id = {itemid}
            group by cd.content_id
            """
        cursor.execute(sqlUser)
        result = cursor.fetchone()
        print(result)
        list1 = result["category"].split(",")
        print(list1)



timeend = time.time()
print(timestart)
print(timeend)
print(timeend-timestart) #0.02 0.01