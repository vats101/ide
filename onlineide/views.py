from django.http import HttpResponse,JsonResponse
from rest_framework.viewsets import ModelViewSet
from .models import User,Submissions
from . import utils
import time
from .serializers import UserSerializer,SubmissionSerializer
# Create your views here.
#We would like to create a submission service performing these functions:
#Add status as pending
#Generate a file with the code and proper extension
#compile and run the file
#save the output in output field.


def hello_world(request):
    return JsonResponse({
        "message":"Welcome to ONLINE IDE"
    },status=201)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all();
    serializer_class = UserSerializer

class SubmissionViewSet(ModelViewSet):
    queryset =Submissions.objects.all()
    serializer_class = SubmissionSerializer

    def create(self, request, *args, **kwargs):
        request.data["status"]="P"   #update status to pending
        f1=utils.create_source_file(request.data["code"],request.data["language"])
        print(f1)
        request.data["output"]=utils.execute_file(f1,request.data["language"]) #storing the captured output.
        return super().create(request,args,kwargs)  #whenever you are overding the create method ,first make changes and then call the super method(of base class) as mentioned below:

#for overriding the get method to get all users i.e /user/ :: list method
#for overiding the update method it is :: update method
#for overriding the get/user_id method we will need to override the :: retreive method
#for overiding the post method ,we will need to override the :: create method
#for overrding the delete method we will need to override the :: delete method



