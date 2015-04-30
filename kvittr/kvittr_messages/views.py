from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone

from kvittr_messages.models import Message

# Create your views here.
def message_listing(request):

	new_post = request.POST.get('new_post')
	if new_post:
		post = Message()
		post.message = new_post
		post.created_datetime = timezone.now()
		post.created_by = request.user
		post.save()

	messages = Message.objects.all()
	page_number = request.GET.get('page')
	paginator = Paginator(messages, 6)
	try:
		messages = paginator.page(page_number)
	except PageNotAnInteger:
		messages = paginator.page(1)
	except EmptyPage:
		messages = paginator.page(paginator.num_pages)

	context = {'messages': messages}
	return render(request, 'kvittr_messages/message_listing.html', context)

def message_details(request, message_id):
	message = Message.objects.get(pk=message_id)
	messages = Message.objects.all()
	context = {'message': message}
	return render(request, 'kvittr_messages/message_details.html', context)

def add_likes(request, message_id):
	message = Message.objects.get(pk=message_id)
	message.likes = message.likes + 1
	message.save()
	data = {'likes_updated': message.likes}
	return JsonResponse(data)


