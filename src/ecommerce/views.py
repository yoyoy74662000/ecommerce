from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm


def home_page(request):
    context = {
        "title": "I love you"
    }
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "About page"
    }
    # Since home_page.html is a template, we use context to add things in it.
    return render(request, "home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact page",
        "content": "welcome to contact page",
        "form": contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
#    if(request.method == 'POST'):
#         print(request.POST)
#         print(request.POST.get('fullname'))
#         print(request.POST.get('email'))
#         print(request.POST.get('content'))
    return render(request, "contact/view.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User logged in")
    # print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)  # it will show on terminal
        username  = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        # print(request.user.is_authenticated())
        if user is not None:
            # print(request.user.is_authenticated())
            login(request, user)
            # Redirect to a success page.
            # context['form'] = LoginForm()
            return redirect("/login")
        else:
            # Return an 'invalid login' error message.
            print("Error")

    return render(request, "auth/login.html", context)


def register_page(request):
    return render(request, "auth/register.html", {})


def home_page_old(request):
    html_ = """
    <!doctype html>
    <html lang="en">
        <head>
            <title>Hello, world!</title>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

            <!-- Bootstrap CSS -->
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
        </head>
        <body>
            <div class='text-center'> 
                <h1>Hello, world!</h1>
            </div>
            <!-- Optional JavaScript -->
            <!-- jQuery first, then Popper.js, then Bootstrap JS -->
            <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>
        </body>
    </html>
    """
    return HttpResponse(html_)
