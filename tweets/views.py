from django.shortcuts import render
from .models import Tweet

# Create your views here.
def list_view(request):
    qs = Tweet.objects.all()
    print(qs)
    context = {'qsVar':qs}
    return render(request, 'tweets/list.html', context)

def detail_view(request, id=1):
    obj = Tweet.objects.get(id=id)
    print(obj)
    context = {'objVar':obj}
    return render(request, 'tweets/detail.html', {'id':id})

