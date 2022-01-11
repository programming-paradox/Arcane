from django.shortcuts import render
from .models import SearchResult
from .serializers import SearchResultSerializer

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def SearchResultApi(request, query): 
    if request.method == 'GET':
        results = SearchResult.objects.filter(title__icontains =query)
        results_serializer = SearchResultSerializer(results, many=True)
        return JsonResponse(results_serializer.data, safe=False)
