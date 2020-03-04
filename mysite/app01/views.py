from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app01.models import YingHua, Publisher

import json


def add(equest,  id=2):
    with open(f'app01/yinghua{id}.json', 'r') as f:
        yhs = json.loads(f.read())
        for yh in yhs:
            print(yh)
            y = YingHua(name=yh['name'], image_name=yh['i'])
            y.save()
    return HttpResponse(id)

def delete(equest):
    p = Publisher.objects.all()
    return HttpResponse(p)


def update(equest):
    p = Publisher.objects.filter(name="马化").update(country="美国")
    return HttpResponse(p)