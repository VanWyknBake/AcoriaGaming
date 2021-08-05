from django.http.response import HttpResponse
from django.shortcuts import render
from .models import CSTournaments, CodTournaments, F1Tournaments, Games, Home, About, McTournaments, News, Profile,Profile2, Category, Skills, Portfolio, CodTournaments, ArmaTournaments, ACTournaments, Streamers, Video

def index(request):

    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()

    news = News.objects.order_by('-date')

    # Portfolio
    portfolios = Portfolio.objects.all()

    # Games
    games = Games.objects.all()
    

    context = {
        'home': home,
        'about': about,
        'news': news,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
        'games': games,
    }


    return render(request, 'index.html', context)
    

def tourn(request):
    home = Home.objects.latest('updated')
    mctournaments = McTournaments.objects.all()
    armatournaments = ArmaTournaments.objects.all()
    codtournaments = CodTournaments.objects.all()
    actournaments = ACTournaments.objects.all()

    cstournaments = CSTournaments.objects.all()
    f1tournaments = F1Tournaments.objects.all()
    games = Games.objects.all()

    context = {
        'codtournaments': codtournaments,
        'home': home,
        'actournaments': actournaments,
        'armatournaments': armatournaments,
        'cstournaments': cstournaments,
        'mctournaments': mctournaments,
        'f1tournaments': f1tournaments,
        'games': games,
    }

    return render(request, 'tournaments.html', context)

def codtourn(request):
    home = Home.objects.latest('updated')


    codtournaments = CodTournaments.objects.all()

    context = {
        'home': home,
        'codtournaments': codtournaments,
        
        
    }

    return render(request, 'cod.html', context)

def f1tourn(request):
    home = Home.objects.latest('updated')

    
    f1tournaments = F1Tournaments.objects.all()

    context = {
        'home': home,
        'f1tournaments': f1tournaments,
        
        
    }

    return render(request, 'f1.html', context)


def minecrafttourn(request):
    home = Home.objects.latest('updated')

    mctournaments = McTournaments.objects.all()

    context = {
        'home': home,
        'mctournaments': mctournaments,


    }

    return render(request, 'minecraft.html', context)


def armatourn(request):
    home = Home.objects.latest('updated')

    armatournaments = ArmaTournaments.objects.all()

    context = {
        'home': home,
        'armatournaments': armatournaments,


    }

    return render(request, 'arma.html', context)


def cstourn(request):
    home = Home.objects.latest('updated')

    cstournaments = CSTournaments.objects.all() 

    context = {
        'home': home,
        'cstournaments': cstournaments,
        


    }

    return render(request, 'cs.html', context)


def actourn(request):
    home = Home.objects.latest('updated')

    actournaments = ACTournaments.objects.all()

    context = {
        'home': home,
        'actournaments': actournaments,



    }

    return render(request, 'ac.html', context)


def streamers(request):

    streamers = Streamers.objects.order_by('-updated')
    profiles2 = Profile2.objects.filter(streamers=streamers)

    home = Home.objects.latest('updated')
    video = Video.objects.order_by('-date')


    context = {
        'home': home,
        'video': video,
        "streamers": streamers,
        'profiles2': profiles2,

    }

    return render(request, 'streamers.html', context)




