from __future__ import unicode_literals

from django.db import models


class Role(models.Model):
    label = models.CharField(max_length=50)


class Politician(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    slug = models.CharField(max_length=50)
    honesty_score = models.IntegerField(null=True, default=None)
    party = models.CharField(max_length=20)
    roles = models.ManyToManyField(Role)


class Statement(models.Model):
    TRUE = 0
    MOSTLY_TRUE = 1
    HALF_TRUE = 2
    MOSTLY_FALSE = 3
    FALSE = 4
    PANTS_ON_FIRE = 5
    NO_FLIP = 6
    HALF_FLIP = 7
    FULL_FLOP = 8

    RULING_CHOICES = (
        (TRUE, 'True'),
        (MOSTLY_TRUE, 'Mostly True'),
        (HALF_TRUE, 'Half True'),
        (MOSTLY_FALSE, 'Mostly False'),
        (FALSE, 'False'),
        (PANTS_ON_FIRE, 'Pants on Fire'),
        (NO_FLIP, 'No Flip'),
        (HALF_FLIP, 'Half Flip'),
        (FULL_FLOP, 'Full Flop'),
    )

    speaker = models.ForeignKey(Politician, related_name='statements')
    ruling = models.IntegerField(default=0, choices=RULING_CHOICES)
    ruling_headline = models.TextField()
    quote = models.TextField()
    context = models.TextField()
    url = models.TextField()
    statement_date = models.DateField(null=True)
    ruling_date = models.DateField(null=True)

    def get_ruling_gif(self):
        url_base = 'http://static.politifact.com.s3.amazonaws.com:80/' \
            'rulings%2Ftom-{0}.gif'
        gif_slugs = ['true', 'mostlytrue', 'halftrue', 'mostlyfalse', 'false',
                     'pantsonfire', 'noflip', 'halfflip', 'fullflop']
        return url_base.format(gif_slugs[self.ruling])

    def save(self, *args, **kwargs):
        super(Statement, self).save(*args, **kwargs)
        statement_scores = [1, 0, -0.5, -1, -2, -3, 0.5, -0.5, -2]
        if self.speaker.honesty_score:
            self.speaker.honesty_score += statement_scores[self.ruling]
        else:
            self.speaker.honesty_score = statement_scores[self.ruling]
        self.speaker.save()
