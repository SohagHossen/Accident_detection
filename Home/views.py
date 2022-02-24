from django.shortcuts import render

def Home(reguest):
    return render(reguest,'index.html')