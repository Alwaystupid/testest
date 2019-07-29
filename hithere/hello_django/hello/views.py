from django.shortcuts import render,HttpResponse
# from hello.modles.py import Owner,Pet

# Create your views here.

def first_try(request):
   # boss = Owner(name='zhang3',birthday='1992-5-7',gender='M')
    # dog = Pet(owner=boss,name='yx',type='D')
    return HttpResponse('hello world')
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    context['neirong'] = '一捧江山在掌握'
    return render(request, 'hello.html', context)
