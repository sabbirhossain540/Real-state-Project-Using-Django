
import json

userJson = '{"firstname": "Sabbir", "lastname": "Hossain", "age": 30}'
user = json.loads(userJson)
print(user)

car = {'make': 'Toyota', 'model':'Allion', 'year': 2020}
carJSON = json.dumps(car)
print(carJSON)











