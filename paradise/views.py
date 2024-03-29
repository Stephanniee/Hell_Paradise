from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Merch
from .form import Form
from .form import ContactForm
from django.core.mail import EmailMessage

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
    context = {'merchs': merch}
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
            return render(request, 'paradise/confirmation.html', {'message': message})
    else:
        form = Form()   


    return render(request, 'paradise/add_merch.html', {'form': form})


def edit_merch(request, id):
    merch = Merch.objects.get(id=id)
    form = Form(request.POST or None, request.FILES or None,  instance=merch)
    if form.is_valid():
        form.save()
        return redirect('merch')
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
            except Exception as e:
                print("Email sending failed:", e)
                return redirect('error')  
            return redirect('success')  
    else:
        form = ContactForm()
    return render(request, 'paradise/contact.html', {'form': form})
def success(request):
    return render(request, 'paradise/success.html')
    