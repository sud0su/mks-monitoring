from django.shortcuts import render

def index(request):
    template = 'blocks/login.html'
    return render(request, template)

def dashboard(request):
    template = 'blocks/dashboard.html'
    return render(request, template)

def schedule(request):
    template = 'blocks/schedule.html'
    return render(request, template)

def document(request):
    template = 'blocks/documents.html'
    return render(request, template)

def report(request):
    template = 'blocks/report.html'
    return render(request, template)

def setting(request):
    template = 'blocks/setting.html'
    return render(request, template)