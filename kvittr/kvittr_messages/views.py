from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from kvittr_messages.models import Message

# Create your views here.
def message_listing(request):
	messages = Message.objects.all()

	page_number = request.GET.get('page')
	paginator = Paginator(messages, 5)
	try:
		messages = paginator.page(page_number)
	except PageNotAnInteger:
		messages = paginator.page(1)
	except EmptyPage:
		messages = paginator.page(paginator.num_pages)



	context = {'messages': messages}
	return render(request, 'kvittr_messages/message_listing.html', context)
	#return HttpResponse("It worked!")