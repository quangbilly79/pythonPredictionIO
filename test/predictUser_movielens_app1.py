import predictionio
engine_client = predictionio.EngineClient(url="http://localhost:8000")
print(engine_client.send_query({"user": "20", "num": 3}))

# buy, rate
# {'itemScores': [{'item': '67', 'score': 20.667889}, {'item': '56', 'score': 18.343277}, {'item': '7', 'score': 17.909407}]}

# buy
# {'itemScores': [{'item': '67', 'score': 11.841336}, {'item': '71', 'score': 10.889812}, {'item': '56', 'score': 10.685967}]}

# rate
# {'itemScores': [{'item': '0', 'score': 9.56989}, {'item': '87', 'score': 9.366764}, {'item': '75', 'score': 8.986314}]}

# buy, rate nhung movie k co' category (properities) tư` $set
#{'itemScores': [{'item': '87', 'score': 18.931458}, {'item': '18', 'score': 17.720736}, {'item': '2', 'score': 17.6954}]}