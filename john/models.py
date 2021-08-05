from django.db import models

# HOME SECTION

class Home(models.Model):
    name = models.CharField(max_length=200)
    greetings_1 = models.CharField(max_length=50)
    greetings_2 = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='picture/')
    # save time when modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ABOUT SECTION

class About(models.Model):
    heading = models.CharField(max_length=500)
    career = models.CharField(max_length=200)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')
    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career


class Profile(models.Model):
    about = models.ForeignKey(About,
                                on_delete=models.CASCADE)
    social_name = models.CharField(max_length=100)
    link = models.URLField(max_length=200)



# SKILLS SECTION

class Category(models.Model):
    name = models.CharField(max_length=200)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category,
                                on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=200)

    

# PORTFOLIO SECTION

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return f'Portfolio {self.id}'


class Games(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='games/')
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Streamers(models.Model):
    name = models.CharField(max_length=200)

    link = models.CharField(max_length=200)
    ytID =  models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to='streamers/')
    descr = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Profile2(models.Model):
    streamers = models.ForeignKey(Streamers,
                                  on_delete=models.CASCADE)
    social_name = models.CharField(max_length=100)
    link = models.URLField(max_length=200)


class CodTournaments(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    host = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tournaments/')
    tournament_type = models.CharField(max_length=100)
    details = models.TextField()
    when = models.DateTimeField(null=True)
    streamer = models.ForeignKey(Streamers, on_delete=models.CASCADE)
    roomlink = models.CharField(max_length=200, null=True, blank=True)

    

    class Meta:
        verbose_name = 'COD Participant'
        verbose_name_plural = 'COD Participants'

    def __str__(self):
        return self.tournament_type


class CODMParticipants(models.Model):
    tournament = models.ForeignKey(CodTournaments,
                                   on_delete=models.CASCADE)
    team_name = models.CharField(max_length=20)


class F1Tournaments(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    host = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tournaments/')
    tournament_type = models.CharField(max_length=100)
    details = models.TextField()
    when = models.DateTimeField(null=True)
    streamer = models.ForeignKey(Streamers, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'F1 Participant'
        verbose_name_plural = 'F1 Participants'

    def __str__(self):
        return self.tournament_type


class F1Participants(models.Model):
    tournament = models.ForeignKey(F1Tournaments,
                                   on_delete=models.CASCADE)
    team_name = models.CharField(max_length=20)


class McTournaments(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    host = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tournaments/')
    tournament_type = models.CharField(max_length=100)
    details = models.TextField()
    when = models.DateTimeField(null=True)
    streamer = models.ForeignKey(Streamers, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Minecraft Participant'
        verbose_name_plural = 'Minecraft Participants'

    def __str__(self):
        return self.tournament_type


class McParticipants(models.Model):
    tournament = models.ForeignKey(McTournaments,
                                   on_delete=models.CASCADE)
    team_name = models.CharField(max_length=20)


class ArmaTournaments(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    host = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tournaments/')
    tournament_type = models.CharField(max_length=100)
    details = models.TextField()
    when = models.DateTimeField(null=True)
    streamer = models.ForeignKey(Streamers, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Arma Participant'
        verbose_name_plural = 'Arma Participants'

    def __str__(self):
        return self.tournament_type


class ArmaParticipants(models.Model):
    tournament = models.ForeignKey(ArmaTournaments,
                                   on_delete=models.CASCADE)
    team_name = models.CharField(max_length=20)


class CSTournaments(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    host = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tournaments/')
    tournament_type = models.CharField(max_length=100)
    details = models.TextField()
    when = models.DateTimeField(null=True)
    streamer = models.ForeignKey(Streamers, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'CSGO Participant'
        verbose_name_plural = 'CSGO Participants'

    def __str__(self):
        return self.tournament_type


class CSParticipants(models.Model):
    tournament = models.ForeignKey(CSTournaments,
                                   on_delete=models.CASCADE)
    team_name = models.CharField(max_length=20)


class ACTournaments(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    host = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tournaments/')
    tournament_type = models.CharField(max_length=100)
    details = models.TextField()
    when = models.DateTimeField(null=True)
    streamer = models.ForeignKey(Streamers, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'AC Participant'
        verbose_name_plural = 'AC Participants'

    def __str__(self):
        return self.tournament_type


class ACParticipants(models.Model):
    tournament = models.ForeignKey(ACTournaments,
                                   on_delete=models.CASCADE)
    team_name = models.CharField(max_length=20)
    
    


class Video(models.Model):
    title = models.CharField(max_length=200)
    YTlink = models.CharField(max_length=200, null=True, blank=True)
    FBlink = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
class News(models.Model):
    topic = models.CharField(max_length=300)
    link = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic
    
