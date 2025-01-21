d = {
    "name" : "kelly",
    "age" : 25,
    "salary" : 8000,
    "city" : "new york"
}

d = {"location" if key == "city" else key:
     value for key, value in d.items()}

# d["location"] = d.pop("city")

print(d)