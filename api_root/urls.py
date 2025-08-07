from django.contrib import admin
from django.urls import path
from api_rest.views import QuestionAnswerAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/question-and-answer', QuestionAnswerAPIView.as_view()), 
]
