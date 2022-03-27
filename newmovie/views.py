from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import AddMovieForm, AddUserForm, CreateUserForm, AccountForm #formlarni primoy databazadan olish un
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
# Create your views here.
@unauthenticated_user
def registerPage(request):
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')


                messages.success(request, 'Akkount ' + username + " uchun ro'yxatdan o'tqazildi")

                return redirect('login')

        context = {'form':form}
        return render(request, 'newmovie/register.html', context)



@unauthenticated_user
def loginPage(request):
        if request.method =="POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username or password is incorrect")
                return redirect('login')
        context = {}
        return render(request, 'newmovie/login.html', context)

def logoutUser(request):
    logout(request)

    return redirect('login')




@login_required(login_url='login')  #faqat login qiganlar kira olishi un
@allowed_users(allowed_roles=['user'])
def accountSettings(request):
    user = request.user.usermine
    form = AccountForm(instance=user)
    if request.method == "POST":
        form = AccountForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'newmovie/account_settings.html', context)

@login_required(login_url='login')  #faqat login qiganlar kira olishi un
@admin_only
def home(request):
    users = UserMine.objects.all()
    movies = Movie.objects.all()

    total_users = users.count()

    total_movies = movies.count()
    top_rank = movies.filter(status="Eng reytingi baland").count()

    context = {'users': users, 'movies': movies,
               'total_users': total_users, 'total_movies': total_movies, 'top_rank': top_rank}

    return render(request, 'newmovie/dashboard.html', context)


@login_required(login_url='login')  #faqat login qiganlar kira olishi un
def movie(request):

    films = Movie.objects.all()
    paginator = Paginator(films, 3)
    page = request.GET.get('page')

    films = paginator.get_page(page)
    context = {'films': films}

    return render(request, 'newmovie/movie.html', context)

@login_required(login_url='login')  #faqat login qiganlar kira olishi un
def movie_id(request, pk):
    film_id = Movie.objects.get(id=pk)

    context = {'film_id': film_id }
    return render(request, 'newmovie/movie_id.html', context)

@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')  #faqat login qiganlar kira olishi un
def customer(request, pk):

    customer = UserMine.objects.get(id=pk)
    orders = customer.order_set.all()
    context = {'customer':customer}
    return render(request, 'newmovie/user.html', context)



@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')  #faqat login qiganlar kira olishi un
def add_movie(request):
    form = AddMovieForm()
    if request.method == "POST":
        form = AddMovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'newmovie/order_form.html', context)


@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')  #faqat login qiganlar kira olishi un
def updateMovie(request, pk):
    movie = Movie.objects.get(id=pk)
    form = AddMovieForm(instance=movie)

    if request.method == "POST":
        form = AddMovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'newmovie/order_form.html', context)

@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')  #faqat login qiganlar kira olishi un
def deleteMovie(request, pk):
    movie = Movie.objects.get(id=pk)
    if request.method == "POST":
        movie.delete()
        return redirect('/')
    context = {'movie':movie}
    return render(request, 'newmovie/delete.html', context)

@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')  #faqat login qiganlar kira olishi un
def updateUser(request, pk):
    user = UserMine.objects.get(id=pk)
    form = AddUserForm(instance=user)

    if request.method == "POST":
        form = AddUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'newmovie/order_form.html', context)


@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')  #faqat login qiganlar kira olishi un
def deleteUser(request, pk):
    user = UserMine.objects.get(id=pk)
    if request.method == "POST":
        user.delete()
        return redirect('/')
    context = {'user':user}
    return render(request, 'newmovie/delete_user.html', context)

@login_required(login_url='login')  #faqat login qiganlar kira olishi un
def searchBar(request):
        if request.method == "POST":
            search = request.POST['search']
            result = Movie.objects.filter(title__contains=search)
        context = {'search':search,'result':result}
        return render(request, 'newmovie/searchbar.html', context)




















@login_required(login_url='login')  #faqat login qiganlar kira olishi un
def filtering_movie_2021(request):
    movies = Movie.objects.all()

    filter_by_year_2021 = movies.filter(year_of_production__year='2021')

    context = {'filter_by_year_2021':filter_by_year_2021}
    return render(request, 'newmovie/filter_movie_2021.html', context)
@login_required(login_url='login')  #faqat login qiganlar kira olishi un
def filtering_movie_2020(request):
    movies = Movie.objects.all()

    filter_by_year_2020 = movies.filter(year_of_production__year='2020')

    context = {'filter_by_year_2020':filter_by_year_2020}
    return render(request, 'newmovie/filter_movie_2020.html', context)
@login_required(login_url='login')  #faqat login qiganlar kira olishi un
def filtering_movie_2019(request):
    movies = Movie.objects.all()

    filter_by_year_2019 = movies.filter(year_of_production__year='2019')

    context = {'filter_by_year_2019':filter_by_year_2019}
    return render(request, 'newmovie/filter_movie_2019.html', context)
@login_required(login_url='login')  #faqat login qiganlar kira olishi un
def filtering_movie_2018(request):
    movies = Movie.objects.all()

    filter_by_year_2018 = movies.filter(year_of_production__year='2018')

    context = {'filter_by_year_2018':filter_by_year_2018}
    return render(request, 'newmovie/filter_movie_2018.html', context)

@login_required(login_url='login')  #faqat login qiganlar kira olishi un
def filtering_movie_action(request):
    movies = Movie.objects.all()
    action = movies.filter(category__name="ACTION")
    context = {'action': action}
    return render(request, 'newmovie/action.html', context)
@login_required(login_url='login')  #faqat login qiganlar kira olishi un
def filtering_movie_drama(request):
    movies = Movie.objects.all()
    drama = movies.filter(category__name="DRAMA")
    context = {'drama': drama}
    return render(request, 'newmovie/drama.html', context)
@login_required(login_url='login')  #faqat login qiganlar kira olishi un
def filtering_movie_triller(request):
    movies = Movie.objects.all()
    triller = movies.filter(category__name="TRILLER")
    context = {'triller': triller}
    return render(request, 'newmovie/triller.html', context)
@login_required(login_url='login')  #faqat login qiganlar kira olishi un
def filtering_movie_comedy(request):
    movies = Movie.objects.all()
    comedy = movies.filter(category__name="COMEDY")
    context = {'comedy': comedy}
    return render(request, 'newmovie/comedy.html', context)
@login_required(login_url='login')  #faqat login qiganlar kira olishi un
def filtering_movie_downloaded(request):
    movies = Movie.objects.all()
    downloaded = movies.filter(status="Eng ko'p yuklangan")
    context = {'downloaded': downloaded}
    return render(request, 'newmovie/downloaded.html', context)

@login_required(login_url='login')  #faqat login qiganlar kira olishi un
def filtering_movie_watched(request):
    movies = Movie.objects.all()
    watched = movies.filter(status="Eng ko'p ko'rilgan")
    context = {'watched': watched}
    return render(request, 'newmovie/watched.html', context)

@login_required(login_url='login')  #faqat login qiganlar kira olishi un
def filtering_movie_top_rank(request):
    movies = Movie.objects.all()
    top_rank = movies.filter(status="Eng reytingi baland")
    context = {'top_rank': top_rank }
    return render(request, 'newmovie/top_rank.html', context)