from django.shortcuts import render

def status(reguest):
    return render(reguest,'status.html')