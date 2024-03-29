"""
Import sample data for recommendation engine
"""
# MyApp2 u8Ecc-tm8lIJABAkn7Iqd0pIwY8M6dGflPTRdUCCotMa0XBRDD-DSfcxl-D3ov4e
# sample-handmade-data.txt
import predictionio
import argparse
import random
import datetime
import pytz

RATE_ACTIONS_DELIMITER = ","
PROPERTIES_DELIMITER = ":"
SEED = 1


def import_events(client, file):
  f = open(file, 'r')
  random.seed(SEED)
  count = 0
  # year, month, day[, hour[, minute[, second[
  #event_date = datetime.datetime(2015, 8, 13, 12, 24, 41)
  now_date = datetime.datetime.now(pytz.utc) # - datetime.timedelta(days=2.7)
  current_date = now_date
  event_time_increment = datetime.timedelta(days= -0.8)
  available_date_increment = datetime.timedelta(days= 0.8)
  event_date = now_date - datetime.timedelta(days= 2.4)
  available_date = event_date + datetime.timedelta(days=-2)
  expire_date = event_date + datetime.timedelta(days=2)
  print("Importing data...")

  for line in f:
    data = line.rstrip('\r\n').split(RATE_ACTIONS_DELIMITER)
    # For demonstration purpose action names are taken from input along with secondary actions on
    # For the UR add some item metadata
    # u-4,view,Soap
    # u5,view,Soap
    # u1,category-pref,phones
    # u1,category-pref,phones
    # u-4,category-pref,phones
    # u-4,category-pref,phones
    # u5,category-pref,toiletries
    # Iphone 6,$set,categories:Phones:Electronics:Apple
    # Iphone 5,$set,categories:Phones:Electronics:Apple
    if (data[1] != "$set"): # Neu' ptu thu 2 k phai la $set, thi` dung` no' lam` event luon, vd view, category-pref
      client.create_event(
        event=data[1],
        entity_type="user",
        entity_id=data[0],
        target_entity_type="item",
        target_entity_id=data[2],
        event_time = current_date
      )
      print("Event: " + data[1] + " entity_id: " + data[0] + " target_entity_id: " + data[2] + \
            " current_date: " + current_date.isoformat())
    elif (data[1] == "$set"):  # Neu' la` set thi` them properties cho item
      properties = data[2].split(PROPERTIES_DELIMITER)
      # categories:Phones:Electronics:Apple, chia bởi dấu :, lấy prop_name là categories, pro_value là phan` con` lai.
      prop_name = properties.pop(0)
      prop_value = properties if not prop_name == 'defaultRank' else float(properties[0])
      client.create_event(
        event=data[1],
        entity_type="item",
        entity_id=data[0],
        event_time=current_date,
        properties={prop_name: prop_value}
      )
      print("Event: " + data[1] + " entity_id: " + data[0] + " properties/"+prop_name+": " + str(properties) + \
          " current_date: " + current_date.isoformat())
    count += 1
    current_date += event_time_increment

  # Them cac' yeu' to' nhu hsd, ton` kho
  items = ['Iphone 6', 'Ipad-retina', 'Nexus', 'Surface', 'Iphone 4', 'Galaxy', 'Iphone 5']
  print("All items: " + str(items))
  for item in items:

    client.create_event(
      event="$set",
      entity_type="item",
      entity_id=item,
      properties={"expires": expire_date.isoformat(),
                  "available": available_date.isoformat(),
                  "date": event_date.isoformat()}
    )
    print("Event: $set entity_id: " + item + \
            " properties/availableDate: " + available_date.isoformat() + \
            " properties/date: " + event_date.isoformat() + \
            " properties/expireDate: " + expire_date.isoformat())
    expire_date += available_date_increment
    event_date += available_date_increment
    available_date += available_date_increment
    count += 1

  f.close()
  print("%s events are imported." % count)


if __name__ == '__main__':
  client = predictionio.EventClient(
    access_key="u8Ecc-tm8lIJABAkn7Iqd0pIwY8M6dGflPTRdUCCotMa0XBRDD-DSfcxl-D3ov4e",
    url="http://localhost:7070",
    threads=5,
    qsize=500)
  import_events(client, "../data/sample-handmade-data.txt")
  print("finished")


#http://localhost:7070/events.json?accessKey=u8Ecc-tm8lIJABAkn7Iqd0pIwY8M6dGflPTRdUCCotMa0XBRDD-DSfcxl-D3ov4e


