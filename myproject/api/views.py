from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    person = {'Hello': 'This sentence is sent from a server'}
    return Response(person)
