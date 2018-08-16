from django.shortcuts import render
def index(request):
    context = {"foo":"bar"}
    return render(request, 'libwebsite/index.html', context)

#check-in view
#check-out view
