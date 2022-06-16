from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import notesModel

# Create your views here.

@api_view(['GET'])
def getRoutes(request):

    data = [
            {
                "title": "to make a blinded choice to reject or provident to task",
                "body": "because he receives and accepts the accepted consequences that are unencumbered and when he finds annoyance"
            },
            {
                "title": "abuse her as an exercise in who she or she is",
                "body": "and who is blinded by the pleasure of the just but by what right to choose, or to the pleasure of the pains or the accusers?"
            },
            {
                "title": "he is blinded",
                "body": "to obtain any pleasure by rejecting one's love and often taking care of things is a fault\nobody is obliged to know the thing and the pain itself is right\nobody wants the pleasure of things"
            },
        ]
    return Response(data)



@api_view(['GET'])
def notesView(request):
    data = notesModel.objects.all()
    return Response('notes')
