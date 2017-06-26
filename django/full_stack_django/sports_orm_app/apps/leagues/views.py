from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q, Count

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
		"alex_wyatts": Player.objects.filter(Q(first_name="Alexander") | Q(first_name="Wyatt")),
		"all_team_atl": Team.objects.filter(league__name="Atlantic Soccer Conference"),
		"current_boston": Player.objects.filter(curr_team__team_name="Penguins"),
		"current_icbc": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
		"current_ACAF_Lopez": Player.objects.filter(last_name="Lopez", curr_team__league__name="American Conference of Amateur Football"),
		"all_football": Player.objects.filter(curr_team__league__name__contains="Football"),
		"team_current_Sophia": Team.objects.filter(curr_players__first_name="Sophia"),
		"league_current_Sophia": League.objects.filter(teams__curr_players__first_name="Sophia"),
		"Flores_not_WR": Player.objects.filter(last_name="Flores").exclude(curr_team__team_name="Roughriders"),
		"all_SE": Team.objects.filter(all_players__first_name="Samuel", all_players__last_name='Evans'),
		"all_MTC": Player.objects.filter(all_teams__team_name='Tiger-Cats'),
		"former_WV": Player.objects.filter(all_teams__team_name='Vikings').exclude(curr_team__team_name='Vikings'),
		"JG_before": Team.objects.filter(all_players__first_name="Jacob", all_players__last_name='Gray').exclude(curr_players__first_name='Jacob', curr_players__last_name='Gray'),
		"Joshua_not_AFABP": Player.objects.filter(first_name='Joshua', all_teams__league__name='Atlantic Federation of Amateur Baseball Players'),
		"12plus": Team.objects.annotate(num_players=Count("all_players")).filter(num_players__gte=12),
		"all_num_team": Player.objects.annotate(num_teams=Count("all_teams")).order_by('num_teams'),

	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")