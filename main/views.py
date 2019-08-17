# from django.shortcuts import render
from .models import Category, Book, Order
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views import generic
# Create your views here.


def home(request):
    return redirect("main:categories")


class HomePage(generic.ListView):
    model = Category
    template_name = "main/home.html"
    context_object_name = "categories"


# def categories(request):
#     if not request.user.is_authenticated:
#         messages.info(request, "login first")
#         return redirect("main:login")
#     our_categories = Category.objects.all()
#     return render(request=request,
#                   template_name="main/home.html",
#                   context={'categories': our_categories})


class SearchResult(generic.ListView):
    model = Book
    template_name = "main/books.html"
    context_object_name = "books"

    def get_queryset(self):
        query = self.request.GET.get('q')
        book_list = Book.objects.filter(book_name__contains=query)
        return book_list


def books(request, pk):
    if not request.user.is_authenticated:
        messages.info(request, "login first")
        return redirect("main:login")
    category = get_object_or_404(Category, pk=pk)
    our_books = Book.objects.filter(category_name=category)
    return render(request=request,
                  template_name="main/books.html",
                  context={'books': our_books})


def register(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "New Account created.")
            return redirect("main:profile")
        messages.error(request, form.errors)
        return render(request=request,
                      template_name="main/register.html",
                      context={'form': form})
    form = NewForm()
    return render(request=request,
                  template_name="main/register.html",
                  context={'form': form})


def logout_account(request):
    logout(request)
    return redirect("main:categories")


def login_account(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username)
            print(password)
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "login as %s" % username)
                return redirect("main:profile")
        messages.error(request, "username or password is incorrect.")
        return render(request=request,
                      template_name="main/login.html",
                      context={'form': form})

    form = AuthenticationForm()
    return render(request=request,
                  template_name="main/login.html",
                  context={'form': form})


def order(request, book_pk):
    if not request.user.is_authenticated:
        messages.info(request, "login first")
        return redirect("main:login")
    user = request.user
    orders = Order.objects.filter(profile=user.profile)
    if orders:
        messages.error(request, "you already have book")
        return redirect("main:categories")
    book = Book.objects.get(pk=book_pk)
    if book.count <= 0:
        messages.error(request, "there is no book to order")
        return redirect("main:categories")
    book.count -= 1
    book.save()
    order = Order(book=book, profile=user.profile)
    order.save()
    messages.success(request, "%s taking by %s" % (book, user.username))
    return redirect("main:categories")


def profile(request):
    if not request.user.is_authenticated:
        messages.info(request, "login first")
        return redirect("main:login")
    order = Order.objects.filter(profile=request.user.profile).first()
    return render(request=request,
                  template_name="main/profile.html",
                  context={'user': request.user,
                           'order': order})


def give_back(request, order_pk):
    order = Order.objects.get(pk=order_pk)
    order.book.count += 1
    order.book.save()
    order.delete()
    return redirect("main:profile")
