from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import Details
from sample.views import no_details
# Create your views here.

def details_view(request):
	username = request.user.username
	try:
		queryset = Details.objects.get(user_id=username)
		context = {"objects" : queryset }
	except Exception as e:
		return redirect(no_details)
	return render(request,"view_details.html",context)