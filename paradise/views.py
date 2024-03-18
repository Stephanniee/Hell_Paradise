from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Merch
from .form import Form

def index(request):
    context = {'merch': merch}
    return render(request, 'paradise/index.html')

def characters(request):
    context = {}
    return render(request, 'paradise/characters.html')

def quiz(request):
    context = {}
    return render(request, 'paradise/quizgame.html')

def merch(request):
    merch = Merch.objects.all()
    context = {'merch': merch}
    return render(request, 'paradise/merch.html', context)

def merch_detail(request, id):
    merch = Merch.objects.get(id=id)
    context = { 
        'merch': merch
    }
    return render(request, 'paradise/merch_detail.html', context)

def delete_merch(request, id):
    merch = Merch.objects.filter(id=id)
    merch.delete()
    message = 'Merchandise deleted successfully'
    context = {'message': message,
               'merch': merch}

    return render(request, 'paradise/delete.html', context)

def form(request):
    form = Form(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            form.save()
            message = 'Product has been added successfully'
            return render(request, 'merch/confirmation.html', {'message': message})
    else:
        form = Form()   


    return render(request, 'paradise/add_merch.html', {'form': form})


def edit_merch(request, id):
    merch = Merch.objects.get(id=id)
    form = Form(request.POST or None, request.FILES or None,  instance=merch)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'paradise/merch_product.html', {'form': form, 'merch': merch})