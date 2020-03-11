from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponse

from .serializer import AllCleanedCrashDataSerializer
from .models import AllCleanedCrashData, query_data_by_args
# Create your views here.

def index(request):

    return render(request,'index.html')

def demo(request):
    return render(request,'demo.html')

class DemoViewSet(viewsets.ModelViewSet):
    queryset = AllCleanedCrashData.objects.all()
    serializer_class = AllCleanedCrashDataSerializer

    def list(self, request, **kwargs):
        try:
            data = query_data_by_args(**request.query_params)
            serializer = AllCleanedCrashDataSerializer(data['items'], many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = data['draw']
            result['recordsTotal'] = data['total']
            result['recordsFiltered'] = data['count']
            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)
