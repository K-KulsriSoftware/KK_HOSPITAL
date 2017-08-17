from django.http import HttpResponse

#Initial Database
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.hospital_info
import pprint

# Create your views here.
def index(request):
    return HttpResponse("API index.")

def user(request, user_id):
    members = db.member_info
    for member in members.find():
        pprint.pprint(member)
    return HttpResponse(collection)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
