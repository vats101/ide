from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
router=DefaultRouter()
router.register("user",views.UserViewSet)
router.register("submit",views.SubmissionViewSet)

urlpatterns=[
  path("",views.hello_world)
]
urlpatterns+=router.urls;