"""
Import sample data for recommendation engine
"""
# MyApp1
# sample_movielens_data.txt
import predictionio
import argparse
import random

RATE_ACTIONS_DELIMITER = "::"
SEED = 3

def import_events(client, file):
  f = open(file, 'r')
  random.seed(SEED)
  count = 0
  print("Importing data...")
  for line in f:
    data = line.rstrip('\r\n').split(RATE_ACTIONS_DELIMITER)
    # For demonstration purpose, randomly mix in some buy events
    # For the UR add some item metadata
    # File co dang userID, itemID, rating (1-5)
    # 0::2::3
    # 0::3::1
    # 0::5::2
    # 0::9::4
    if (random.randint(0, 1) == 1):
      client.create_event(
        event="rate",
        entity_type="user",
        entity_id=data[0],
        target_entity_type="item",
        target_entity_id=data[1],
      )
    else:
      client.create_event(
        event="buy",
        entity_type="user",
        entity_id=data[0],
        target_entity_type="item",
        target_entity_id=data[1],
      )
    if (random.randint(0, 1) == 1):
      client.create_event(
        # $set: gan' properities cho cac' entity (kieu? ten, dia chi cho user, category cho movie)
        # An entity may peform some events (e.g user 1 does something),
        # entity may have properties associated with it (e.g. user may have gender, age, email etc)
        # the properties of the entity may change over time (for example, user may have new address, item may have new categories).
        # In order to record such changes of an entity's properties. Special events $set , $unset and $delete are introduced
        event="$set",
        entity_type="item",
        entity_id=data[1],
        properties= { "category": ["cat1", "cat5"] }
      )
    else:
      client.create_event(
        event="$set",
        entity_type="item",
        entity_id=data[1],
        properties= { "category": ["cat1", "cat2"] }
      )
    count += 1
  f.close()
  print("%s events are imported." % count)

#MyApp1 AccessKey: Pk88wfBWtVvVLNNcfGwF15oMRnVuYnfPE_B2xeyQfly1tMtXzXP9-rZhx8rv9J1N
if __name__ == '__main__':
  client = predictionio.EventClient(
    access_key="Pk88wfBWtVvVLNNcfGwF15oMRnVuYnfPE_B2xeyQfly1tMtXzXP9-rZhx8rv9J1N",
    url="http://localhost:7070",
    threads=5,
    qsize=500)
  import_events(client, "../data/sample_movielens_data.txt")
  print("finished")


#sample-handmade-data.txt
#http://localhost:7070/events.json?accessKey=Pk88wfBWtVvVLNNcfGwF15oMRnVuYnfPE_B2xeyQfly1tMtXzXP9-rZhx8rv9J1N