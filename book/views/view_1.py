from .importer import *

def view_a(request):
    return HttpResponse("in view_a")

def view_b(request):
    return HttpResponse("in view_b")

 
 
def responseform(request):
    form = FeedbackForm()
    return render(request, 'responseform.html', {'form':form})


