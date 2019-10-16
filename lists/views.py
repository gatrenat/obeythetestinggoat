from django.http import HttpResponse

# Create your views here.
def home_page(request):
    contents = '<html><title>To-Do list</title></html>'
    return HttpResponse(contents)

