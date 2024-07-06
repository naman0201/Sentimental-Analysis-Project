from django.shortcuts import render

# Create your views here.
def Input(request):

    return render(request,"CriminalDataSentiment\InputPage.html",{})