from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'paradise/index.html')

def characters(request):
    context = {}
    return render(request, 'paradise/characters.html')

def quiz(request):
    context = {}
    return render(request, 'paradise/quizgame.html')
