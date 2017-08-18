from django.http import HttpResponse

#Initial Database
from pymongo import MongoClient
from bson.json_util import dumps
client = MongoClient('localhost', 27017)
db = client.hospital_info

# Create your views here.
def index(request):
    return HttpResponse("API index.")

def user(request, user_id):
    members = db.member_info
    query = [
        {
            "$match": {"user_id": user_id}
        }
    ]
    member = members.aggregate(query)
    return HttpResponse(dumps(member))
