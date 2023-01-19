import predictionio
engine_client = predictionio.EngineClient(url="http://localhost:8000")
print(engine_client.send_query({"user": "u-4", "num": 5}))

# "eventNames": [
# 					"purchase", "view", "category-pref"
# 				],
# 				"blacklistIndicators": ["purchase"],
# 				"expireDateName": "expires",
# 				"availableDateName": "available",
# 				"dateName": "date",
# 				"num": 15
#u1: {'itemScores': [{'item': 'Nexus', 'score': 0.9116078}, {'item': 'Surface', 'score': 0.2876821}]}
#u-4: {'itemScores': [{'item': 'Ipad-retina', 'score': 1.6047549}, {'item': 'Nexus', 'score': 1.4224334}, {'item': 'Surface', 'score': 0.0}]}

# "eventNames": [
# 	                "purchase", "view", "category-pref"
#               ],
#               "blacklistIndicators": ["purchase"]
#u1: {'itemScores': [{'item': 'Nexus', 'score': 0.9116078}, {'item': 'Surface', 'score': 0.2876821}]}
#u-4: {'itemScores': [{'item': 'Iphone 6', 'score': 2.1155806}, {'item': 'Ipad-retina', 'score': 1.6047549}, {'item': 'Nexus', 'score': 1.4224334}, {'item': 'Surface', 'score': 0.0}]}


