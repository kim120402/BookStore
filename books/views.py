from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


# HOME PAGE
def homePage(request):
    books = Book.objects.all()  # get all books from database
    return render(request, 'home.html', {'books': books})  # send books to home page


# BOOK DETAIL PAGE
def bookDetails(request, bookId):
    book = get_object_or_404(Book, id=bookId)  # get book by id or show 404
    return render(request, 'book_detail.html', {'book': book})  # send one book to detail page


# ADD BOOK
@login_required  # user need to login before adding book
def addBook(request):
    if request.method == "POST":  # if user submit the form
        form = BookForm(request.POST)  # get data from form

        if form.is_valid():  # check if form data is valid
            book = form.save(commit=False)  # create book but don't save yet
            book.posted_by = request.user  # set current logged in user as owner
            book.save()  # save book to database
            return redirect('home')  # go back to home page
    else:
        form = BookForm()  # show empty form

    return render(request, 'add_book.html', {'form': form})  # send form to html


# EDIT BOOK
@login_required  # user need to login before editing book
def editBook(request, bookId):
    book = get_object_or_404(Book, id=bookId)  # get book by id

    if book.posted_by != request.user:  # check if user is the owner
        return HttpResponseForbidden("You are not allowed to edit this book.")

    if request.method == 'POST':  # if user submit updated form
        form = BookForm(request.POST, instance=book)  # fill form with updated data for this book

        if form.is_valid():  # check if form is valid
            form.save()  # save updated book
            return redirect('book_detail', bookId=book.id)  # go back to book detail page
    else:
        form = BookForm(instance=book)  # show form with old book data

    return render(request, 'edit_book.html', {'form': form, 'book': book})  # send form and book to html


# DELETE BOOK
@login_required  # user need to login before deleting book
def deleteBook(request, bookId):
    book = get_object_or_404(Book, id=bookId)  # get book by id

    if book.posted_by != request.user:  # check if user is the owner
        return HttpResponseForbidden("You are not allowed to delete this book.")

    if request.method == 'POST':  # if user confirms delete
        book.delete()  # remove book from database
        return redirect('home')  # go back to home page

    return render(request, 'delete_book.html', {'book': book})  # show delete confirmation page


# REGISTER
def register(request):
    if request.method == 'POST':  # if user submit register form
        form = UserCreationForm(request.POST)  # get register form data

        if form.is_valid():  # check if register data is valid
            form.save()  # create user account
            return redirect('login')  # go to login page
    else:
        form = UserCreationForm()  # show empty register form

    return render(request, 'register.html', {'form': form})  # send form to html


# LOGIN
def loginUser(request):
    if request.method == "POST":  # if user submit login form
        form = AuthenticationForm(request, data=request.POST)  # get username and password

        if form.is_valid():  # check if username and password are correct
            user = form.get_user()  # get the logged in user
            auth_login(request, user)  # login user and create session
            return redirect('home')  # go to home page
    else:
        form = AuthenticationForm()  # show empty login form

    return render(request, 'login.html', {'form': form})  # send form to html


# LOGOUT
def logoutUser(request):
    logout(request)  # logout user and clear session
    return redirect('home')  # go back to home page