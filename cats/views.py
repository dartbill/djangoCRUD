from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import Cat
from django.core import serializers
from .serializers import CatSerializer
import json
# from rest_framework.generics import ListAPIView


def index(request):
    return HttpResponse("Hello, world.")


def get_cats(request):
    qs = Cat.objects.all()
    qs_json = serializers.serialize('json', qs)
    return HttpResponse(qs_json, content_type='application/json')


def get_one_cat(request, cat_id):
    cat = Cat.objects.filter(pk=cat_id)
    qs_json = serializers.serialize('json', cat)
    return HttpResponse(qs_json, content_type='application/json')


@csrf_exempt
def create_cat(request):
    if request.method == 'POST':
        new_cat = json.loads(request.body)
        Cat.objects.create(name=new_cat['name'], age=new_cat['age'])
    return JsonResponse({'message': 'Cat successfully created'})


@csrf_exempt
def update_cat(request, cat_id):
    if request.method == 'PATCH':
        updated_cat = json.loads(request.body)
        Cat.objects.filter(pk=cat_id).update(
            name=updated_cat['name'], age=updated_cat['age'])
    return JsonResponse({'message': 'Cat successfully updated'})


@csrf_exempt
def delete_cat(request, cat_id):
    if request.method == 'DELETE':
        Cat.objects.filter(pk=cat_id).delete()
    return JsonResponse({'message': 'Cat successfully deleted'})
