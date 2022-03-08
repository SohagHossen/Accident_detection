from django.shortcuts import render

# Create your views here.
def GroupChat(reguest):
    return render(reguest,'chat/groupChat.html')