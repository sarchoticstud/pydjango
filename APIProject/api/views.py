from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Article
from api.serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.
# def Index(request):
#     return HttpResponse("It is Working, Champ Gadhe , Khushi rocks!!")

@csrf_exempt
def article_list(request):
    #getting all article objects available
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many = True) #since articles is a queryset we used many=True
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def article_details(request, pk):
    try:
        article = Article.objects.get(pk = pk)
    except Article.DoesNotExist:
        return HttpResponse(status = 404)
    
    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)
    
    elif request.method == "DELETE":
        article.delete()
        return HttpResponse(status = 204)