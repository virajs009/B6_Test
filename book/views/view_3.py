from .importer import *

# Create your views here.

logger = logging.getLogger("first")

def homepage(request):
    """For adding book data"""
    name = request.POST.get("bname")
    price = request.POST.get("bprice")
    qty = request.POST.get("bqty")

    if request.method == "POST":
        if not request.POST.get("bid"):
            book_name = name
            if book_name == "":
                logger.error("Please provide book name")
                return HttpResponse("Please provide book name")
            book_price = price
            book_qty = qty
            logger.info(request.POST)
            try:
                Book.objects.create(name = book_name, price = book_price, qty = book_qty)
            except ValueError as msg:
                logger.error(msg)
                return HttpResponse("All fields are mandatory")
            else:
                return redirect("homepage")                                         # returning to same page after filling data
        else:
            bid = request.POST.get("bid")
            try:
                book_obj = Book.objects.get(id=bid)
            except Book.DoesNotExist as err_msg:
                logger.error(err_msg)
            book_obj.name = name
            book_obj.price = price
            book_obj.qty = qty
            book_obj.save()
            return redirect("show_all_books")

    elif request.method == "GET":
        all_books = Book.objects.all()
        data = {"books": all_books}
        return render(request, "home1.html", context=data)
        # return render(request, template_name="home1.html")    # alternate way

def show_all_books(request):
    """To show all books"""
    all_books = Book.objects.filter(is_active="Y")              # To get only active books
    cont = {"books": all_books}                                 # same as aliasing
    logger.info(f"All active books: {all_books}")
    return render(request, "show_books.html", context=cont)     # to return show_books.html while hitting url

def edit_data(request, id):
    """To edit single book data by id"""
    book = Book.objects.get(id=id)
    logger.info(f"Editing book: {book}")
    return render(request, template_name="home1.html", context={"single_book": book})

def delete_single_data(request, id):
    """To delete single data by id"""
    if request.method == "POST":
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist as err_msg:
            traceback.print_exc()                                   # For printing exception as it is in console
            logger.error(err_msg)
            return HttpResponse(f"Book does not exist: {id}")
        else:
            logger.warning(f"Deleting book: {book}")
            book.delete()
        return redirect("show_all_books")
    else:
        return HttpResponse(f"Request method: {request.method} not allowed..")

# for multiple data fetch using - request.POST.getlist("books") -- o/p in [] for single data also

def delete_all_data(request):
    """To delete all books"""
    books = Book.objects.filter(is_active="Y")
    logger.warning(f"Deleting all active books: {books}")
    books.delete()
    return redirect("homepage")

def soft_delete_data(request, id):
    """To remove single book from active books data"""
    if request.method == "POST":
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist as msg:
            logger.error(msg)
            return HttpResponse(f"Book does not exist: {id}")
        else:
            book.is_active = "N"
            book.save()
            logger.warning(f"Soft deleting active book: {book}")
        return redirect("show_all_books")
    else:
        return HttpResponse(f"Request method: {request.method} not allowed..")

def soft_delete_all_data(request):
    """To remove all books from active books list"""
    books = Book.objects.filter(is_active="Y")
    for book in books:
        book.is_active = "N"
        book.save()
    logger.warning(f"Soft deleting all active books: {books}")
    return redirect("homepage")

def show_soft_deleted_books(request):
    """To show all inactive books"""
    inactive_books = Book.inactive_books.all()                              # using custom model manager
    cont = {"books": inactive_books}
    logger.info(f"All soft deleted books: {inactive_books}")
    return render(request, "show_soft_deleted_books.html", context=cont)    # context takes ref of cont

def restore_soft_deleted_book(request, id):
    """To restore single inactive book"""
    if request.method == "POST":
        try:
            book = Book.inactive_books.get(id=id)                           # getting specified book from custom model manager
        except Book.DoesNotExist as msg:
            logger.error(err_msg)
            return HttpResponse(f"Book does not exist: {id}")
        else:
            book.is_active = "Y"
            book.save()
            logger.info(f"Restoring soft deleted book: {book}")
        return redirect("show_soft_deleted_books")
    else:
        return HttpResponse(f"Request method {request.method} not allowed..")

def restore_all_soft_deleted_books(request):
    """To restore all inactive books"""
    books = Book.inactive_books.all()
    for book in books:
        book.is_active = "Y"
        book.save()
    logger.info(f"Restoring all soft deleted books: {books}")
    return redirect("show_soft_deleted_books")

# def form_home(request):
#     context = {"form": StudentForm()}
#     return render(request, "form_home.html", context)

# def form_home(request):
#     if request.method == "POST":
#         pass
#     else:
#         print("In get request")
#         context = {"form": AddressForm()}
#         return render(request, "form_home.html", context)

def form_home(request):                     # function based view
    if request.method == "POST":
        print(request.POST)
        print("In post request")
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data['name'])
            messages.success(request, "Data saved successfully")
            messages.info(request, "Redirecting to homepage")
        else:
            messages.error(request, "Invalid Data")
        return redirect("form_home")

    elif request.method == "GET":
        print("In get request")
        context = {"form": BookForm()}
        return render(request, "Form_home.html", context)
    else:
        return HttpResponse("Invalid HTTP Method", status=405)

class HomePage(View):
    Name = None
    def get(self, request):
        print(self.Name)
        print("In get request")
        return HttpResponse("In GET")

    def post(self, request):
        print("In post request")
        return HttpResponse("In POST", status=201)

    def delete(self, request):
        print("In delete request")
        return HttpResponse("In DELETE", status=204)

    def put(self, request):
        print("In put request")
        return HttpResponse("In PUT", status=200)

    def patch(self, request):
        print("In path request")
        return HttpResponse("In PATCH")


class CBVTemplateView(TemplateView):
    extra_context = {"form": BookForm()}
    template_name = "form_home.html"


# class CBVTemplateView(TemplateView):
#     url = "http://127.0.0.1:8000/homepage/"

# generic views
class EmployeeCreate(CreateView):
    model = Employee
    fields = "__all__"
    success_url = reverse_lazy("book:EmployeeCreate")
    # return render(request, "book/employee_form.html", {"form": EmployeeForm})

class EmployeeRetrieve(ListView):
    model = Employee
    # return render(request, "book/employee_list.html", {"object_list": data})


class EmployeeDetail(DetailView):
    model = Employee
    # return render(request, "book/employee_detail.html", {"object": data})

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = "__all__"
    success_url = reverse_lazy("book:EmployeeCreate")
    # return render(request, "book/employee_form.html", {"form": EmployeeForm})

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy("book:EmployeeCreate")
    # return render(request, "book/employee_confirm_delete.html", {"object": data})




