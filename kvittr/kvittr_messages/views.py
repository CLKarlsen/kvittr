from django.shortcuts import render
from django.http import HttpResponse

from kvittr_messages.models import Message

# Create your views here.
def message_listing(request):
	messages = Message.objects.all()
	context = {'messages': messages}
	return render(request, 'kvittr_messages/message_listing.html', context)
	#return HttpResponse("It worked!")