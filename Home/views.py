from django.shortcuts import render

def Home(reguest):
    return render(reguest,'Home.html')
def Base(reguest):
    return render(reguest,'Base.html')
