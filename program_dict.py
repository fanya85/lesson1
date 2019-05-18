d = {"City": "Москва", "temperature": 20}
print(d.get("City"))
d["temperature"] = d["temperature"] - 5
print(d)
print("country" in d)
d["country"] =  "Россия"
d["date"] = "27.05.2019"
print(d)
print(len(d))