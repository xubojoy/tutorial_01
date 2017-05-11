from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from sinppets.models import Snippet
from sinppets.serializers import SnippetSerializer

class JSONResponse(HttpResponse):
    '''
    用来返回json数据
    '''
    def __init__(self,data,**kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse,self).__init__(content,**kwargs)



@csrf_exempt
def snippet_list(request):
    '''
    展示所有的snippet，或者创建新的snippet
    '''
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets,many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONParser(serializer.data,status=201)
        return JSONParser(serializer.errors,status=400)


@csrf_exempt
def snippet_detail(request,pk):
    '''
    显示、更新、、删除一个snippet
    '''
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet,data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors,status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)