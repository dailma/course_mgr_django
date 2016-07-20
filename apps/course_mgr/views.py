from django.shortcuts import redirect, render
from .models import Course

def index(request):
	context = { "courses": Course.objects.all() }
	return render(request, "course_mgr/index.html", context)

def course_destroy(request, id):
	context = { "course": Course.objects.get(id=id) }
	return render(request, "course_mgr/confirm.html", context)

def course_add(request):
	Course.objects.create(name=request.POST['inp_name'],
						  description=request.POST['inp_description'])
	return redirect("/")

def course_delete(request, id):
	if request.method == "POST":
		if "destroy" in request.POST:
			Course.objects.get(id=id).delete()
	return redirect("/")