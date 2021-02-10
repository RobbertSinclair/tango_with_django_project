from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

#Another Helper method
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


#Helper function to handle 
def visitor_cookie_handler(request):
    #Get the number of visists to the site
    visits = int(get_server_side_cookie(request, 'visits', '1'))

    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
        
    else:
        #Set the last visit cookie
        request.session['last_visit'] = last_visit_cookie

    # Update/set the visits cookie
    request.session['visits'] = visits



# Create your views here.
def index(request):
    #Context for the template

    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!', 'categories': category_list, 'pages': page_list}
    
    
    visitor_cookie_handler(request)
    context_dict["views"] = request.session['visits']

    response = render(request, 'rango/index.html', context=context_dict)
    return response

def rango_app(request):
    return HttpResponse("Rango says wow you are in the rango app :)")

def rango_about(request):

    context = {"name": "Robbert Sinclair"}

    visitor_cookie_handler(request)
    context["visits"] = request.session['visits']

    return render(request, "rango/about.html", context=context)

def show_category(request, category_name_slug):

    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages

        context_dict['category'] = category

    except Category.DoesNotExist:

        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)






@login_required
def add_category(request):
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect("/rango/")
        else:
            print(form.errors)

    return render(request, 'rango/add_category.html', {'form': form})

@login_required
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    if category is None:
        return redirect("/rango/")
    
    form = PageForm()

    if request.method == "POST":
        form = PageForm(request.POST)

        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()

                return redirect(reverse("rango:show_category", kwargs={"category_name_slug": category_name_slug}))

        else:
            print(form.errors)

    context_dict = {"form": form, "category": category}
    return render(request, "rango/add_page.html", context=context_dict)

#This is redundant now due to the work in chapter 11 but I will keep it hear for reference in future projects
'''def register(request):

    registered = False

    if request.method == "POST":

        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            
            if "picture" in request.FILES:
                profile.picture = request.FILES["picture"]

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:

        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'rango/register.html', context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})'''


#As with the registration this view is now redundant due to chapter 11 but I am keeping for reference
'''def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)
                return redirect(reverse("rango:index"))
            else:
                return HttpResponse("Your Rango account is disabled")

        else:

            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, "rango/login.html")'''

@login_required
def restricted(request):
    return render(request, "rango/restricted.html")

'''@login_required
def user_logout(request):
    logout(request)

    return redirect(reverse('rango:index'))'''

