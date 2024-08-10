from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our services is very quick'
    feature1.is_true = True

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Clean'
    feature2.details = 'Our services is clean'
    feature2.is_true = False
    
    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Done'
    feature3.details = 'Our services is done'
    feature3.is_true = True

    features = [feature1, feature2, feature3]

    return render(request, 'index.html', {'features': features})

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})