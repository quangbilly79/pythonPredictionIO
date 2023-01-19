import predictionio
from predictionio import EventClient
from datetime import datetime
import pytz

# Tao 1 event don gian?, k co' yeu' to' thoi` gian
client = predictionio.EventClient(
    access_key="qUNyatW4EvG7vngt0y15ea4toBmQaAfyrQ-ihQX1sbM-7tJrgfdajzHv1m6_S7Vu",
    url="http://localhost:7070",
    threads=5,
    qsize=500
)

# A user rates an item
client.create_event(
    event="rate",
    entity_type="user",
    entity_id="u99",
    target_entity_type="item",
    target_entity_id="i99",
    properties= { "rating" : float(9.9) }
)

client.create_event(
    event="rate",
    entity_type="user",
    entity_id="u01",
    target_entity_type="item",
    target_entity_id="i01",
    properties= { "rating" : float(8.9) }
)

client.create_event(
    event="rate",
    entity_type="user",
    entity_id="u99",
    target_entity_type="item",
    target_entity_id="i02",
    properties= { "rating" : float(9.9) }
)

# Tao 1 event co' yeu' to' thoi` gian
# client = EventClient('Pk88wfBWtVvVLNNcfGwF15oMRnVuYnfPE_B2xeyQfly1tMtXzXP9-rZhx8rv9J1N', "http://localhost:7070")
#
# first_event_properties = {
#     "rating" : 2.3,
#     "like" : True
#     }
# first_event_time = datetime(
#   2022, 12, 31, 23, 59, 59, 618000, pytz.timezone('US/Mountain'))
# first_event_response = client.create_event(
#     event="my_event2",
#     entity_type="user",
#     entity_id="u03",
#     target_entity_type="item",
#     target_entity_id="i03",
#     properties=first_event_properties,
#     event_time=first_event_time,
# )