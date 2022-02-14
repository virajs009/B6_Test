from .importer import *

def view_c(request):
    return HttpResponse("in view_c")

def view_d(request):
    return HttpResponse("in view_d")



def index(request):                               # pagination
    user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'user_list.html', { 'users': users })


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'  
    context_object_name = 'users'  
    paginate_by = 10
    queryset = User.objects.all()  


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('Thanks')
    else:
        form = NameForm()
    return render(request, 'name.html', {'form': form})


