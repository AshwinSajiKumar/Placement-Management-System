from django.shortcuts import render


def index(request):
    if request.user.is_authenticated:
        return render(request,'student_home.html')
    return render(request,'home.html')