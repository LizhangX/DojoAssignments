from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		# ...all baseball leagues
		"baseballs": League.objects.filter(name__contains='Baseball'),
		# ...all womens' leagues
		"women": League.objects.filter(name__contains='Women'),
		# ...all leagues where sport is any type of hockey
		"hockeys": League.objects.filter(name__contains='Hockey'),
		# ...all leagues where sport is something OTHER THAN football
		"no_footballs": League.objects.exclude(name__contains='Football'),
		# ...all leagues that call themselves "conferences"
		"conferences": League.objects.filter(name__contains='Conference'),
		# ...all leagues in the Atlantic region
		"atlantics": League.objects.filter(name__contains='Atlantic'),
		# ...all teams based in Dallas
		"dallases": Team.objects.filter(location__contains='Dallas'),
		# ...all teams named the Raptors
		"raptorses": Team.objects.filter(team_name__contains='Raptors'),
		# ...all teams whose location includes "City"
		"cities": Team.objects.filter(location__contains='City'),
		# ...all teams whose names begin with "T"
		"ts": Team.objects.filter(team_name__startswith='T'),
		# ...all teams, ordered alphabetically by location
		"orders": Team.objects.order_by('location'),
		# ...all teams, ordered by team name in reverse alphabetical order
		"orders": Team.objects.order_by('-team_name'),
		# ...every player with last name "Cooper"
		"coopers": Player.objects.filter(last_name='Cooper'),
		# ...every player with first name "Joshua"
		"Joshua": Player.objects.filter(first_name='Joshua'),
		# ...every player with last name "Cooper" EXCEPT those with "Joshua" as the first name
		"cooper_no_joshuas": Player.objects.filter(last_name='Cooper').exclude(first_name='Joshua'),
		# ...all players with first name "Alexander" OR first name "Wyatt"
		"alex_wyatts": Player.objects.filter(Q(first_name="Alexander") | Q(first_name="Wyatt"))
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")