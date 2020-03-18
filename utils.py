import random
import json
from bson import ObjectId

def Generate_token(mongo):
    token = random.randint(0,10000)
    if len(list(mongo.db.tokens.find({"token": token}))) == 0:
        return token
    else:
        Generate_token()

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)