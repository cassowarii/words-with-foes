from django.db import models
from django.db.models.signals import post_save

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

import ast

class ListField(models.CharField):
    pass

class Word(models.Model):
    name = models.CharField(max_length=15, unique=True)
    last_updated = models.DateTimeField('last updated', auto_now_add=True)

class Definition(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)
    part_of_speech = models.CharField(max_length=4)
    text = models.TextField()
    date_submitted = models.DateTimeField('date submitted', auto_now_add=True)

class GameState(models.Model):
    p1_letters = models.CharField(max_length=7)
    p2_letters = models.CharField(max_length=7)
    board = models.CharField(max_length=225)
    draw_pile = models.CharField(max_length=150)
    last_word = models.CharField(max_length=15)
    last_move_pos = models.CharField(max_length=150, default="[]")
    last_move_score = models.IntegerField(default=0)
    p1_score = models.IntegerField(default=0)
    p2_score = models.IntegerField(default=0)
    last_word_defined = models.BooleanField(default=False)

    def __str__(self):
        return 'Game state #'+str(self.id)

class Game(models.Model):
    # Player 1 is the player who created the game
    player_1 = models.ForeignKey(User, related_name='wordsgame_first_player', on_delete=models.CASCADE)
    # Player 2 is the player who accepted the game
    player_2 = models.ForeignKey(User, related_name='wordsgame_second_player', on_delete=models.CASCADE)
    date_started = models.DateTimeField('date started')
    last_move = models.DateTimeField('last move')
    completed = models.BooleanField('completed')
    game_state = models.OneToOneField(GameState, on_delete=models.CASCADE)
    public = models.BooleanField('public')
    p2_first = models.BooleanField('player 2 goes first')
    p1_turn = models.BooleanField('player 1\'s turn')
    someone_moved = models.BooleanField('someone has moved')

    def __str__(self):
        if self.completed:
            return self.player_1.username + ' vs. ' + self.player_2.username + ' (complete)'
        else:
            return self.player_1.username + ' vs. ' + self.player_2.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    fav_color = models.CharField(max_length=30)
    bio = models.TextField()
    def __str__(self):
        return "%s's profile" % self.user.username

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = Profile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
