import requests

sentiments = requests.get("https://hackthevalley.herokuapp.com/sentiment").json()
senti_vals = []
for entry in sentiments:
    currVal = float(entry[1])
    senti_vals.append(currVal)

print(senti_vals)