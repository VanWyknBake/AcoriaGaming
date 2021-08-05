from django.contrib import admin
from .models import CSParticipants, CSTournaments, Games, Home, About, F1Participants,CODMParticipants, News, Profile, Category, Profile2, Skills, Portfolio, CodTournaments, F1Tournaments, McParticipants, McTournaments, ArmaTournaments, ArmaParticipants, ACTournaments, ACParticipants, Streamers, Video


# Home
admin.site.register(Home)
admin.site.register(News)



class Profile2Inline(admin.TabularInline):
    model = Profile2
    extra = 1
@admin.register(Streamers)
class StreamersAdmin(admin.ModelAdmin):
    inlines = [
        Profile2Inline,
    ]
admin.site.register(Video)



# About
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
     inlines = [
        ProfileInline,
    ]

# Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [
        SkillsInline,
    ]


# Portfolio
admin.site.register(Portfolio)

# games
admin.site.register(Games)


class CODMParticipantsInline(admin.TabularInline):
    model = CODMParticipants
    extra = 2


@admin.register(CodTournaments)
class TournamentAdmin(admin.ModelAdmin):
    inlines = [
        CODMParticipantsInline,
    ]


class F1ParticipantsInline(admin.TabularInline):
    model = F1Participants
    extra = 2


@admin.register(F1Tournaments)
class TournamentAdmin(admin.ModelAdmin):
    inlines = [
        F1ParticipantsInline,
    ]


class McParticipantsInline(admin.TabularInline):
    model = McParticipants
    extra = 2


@admin.register(McTournaments)
class TournamentAdmin(admin.ModelAdmin):
    inlines = [
        McParticipantsInline,
    ]


class ArmaParticipantsInline(admin.TabularInline):
    model = ArmaParticipants
    extra = 2


@admin.register(ArmaTournaments)
class TournamentAdmin(admin.ModelAdmin):
    inlines = [
        ArmaParticipantsInline,
    ]


class CSParticipantsInline(admin.TabularInline):
    model = CSParticipants
    extra = 2


@admin.register(CSTournaments)
class TournamentAdmin(admin.ModelAdmin):
    inlines = [
        CSParticipantsInline, 
    ]

class ACParticipantsInline(admin.TabularInline):
    model = ACParticipants
    extra = 2


@admin.register(ACTournaments)
class TournamentAdmin(admin.ModelAdmin):
    inlines = [
        ACParticipantsInline, 
    ]
