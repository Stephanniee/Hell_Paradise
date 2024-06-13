from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from .models import Merch
from .form import Form, ContactForm

def index(request):
    merch = Merch.objects.all()
    context = {'merch': merch}
    return render(request, 'paradise/index.html', context)

def characters(request):
    return render(request, 'paradise/characters.html')

def quiz(request):
    return render(request, 'paradise/quizgame.html')

def merch(request):
    merch = Merch.objects.all()
    context = {'merchs': merch}
    return render(request, 'paradise/merch.html', context)

def merch_detail(request, id):
    merch = get_object_or_404(Merch, id=id)
    context = {'merch': merch}
    return render(request, 'paradise/merch_detail.html', context)

@login_required
def delete_merch(request, id):
    merch = get_object_or_404(Merch, id=id)
    if merch.user == request.user:
        merch.delete()
        messages.success(request, 'Merchandise deleted successfully')
    else:
        messages.error(request, 'You are not authorized to delete this merchandise')
    return redirect('merch')

@login_required
def add_merch(request):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.success(request, 'Product has been added successfully')
            return redirect('merch')
    else:
        form = Form()
    return render(request, 'paradise/add_merch.html', {'form': form})

@login_required
def edit_merch(request, id):
    merch = get_object_or_404(Merch, id=id)
    if merch.user != request.user:
        messages.error(request, 'You are not authorized to edit this merchandise')
        return redirect('merch')

    if request.method == 'POST':
        form = Form(request.POST, request.FILES, instance=merch)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product has been updated successfully')
            return redirect('merch')
    else:
        form = Form(instance=merch)
    return render(request, 'paradise/edit_merch.html', {'form': form, 'merch': merch})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                email_message = EmailMessage(
                    subject='Contact Form Submission: {}'.format(subject),
                    body=message,
                    from_email=email,
                    to=['sandbox.smtp.mailtrap.io'], 
                    reply_to=[email]
                )
                email_message.send()
                return redirect('success')
            except Exception as e:
                messages.error(request, f"Email sending failed: {e}")
                return redirect('error')
    else:
        form = ContactForm()
    return render(request, 'paradise/contact.html', {'form': form})

def success(request):
    return render(request, 'paradise/success.html')
