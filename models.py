from django.db import models

class Team(models.Model):
	team_name = models.CharField(max_length=100)
	score = models.IntegerField()

	def __unicode__(self):  # Python 3: def __str__(self):
        	return self.team_name

class Match(models.Model):
	match_name = models.CharField(max_length=100)
	blue_team = models.ForeignKey(Team, related_name='match_blue_teams')
	white_team = models.ForeignKey(Team, related_name='match_white_teams')

	def __unicode__(self):  # Python 3: def __str__(self):
        	return self.match_name

