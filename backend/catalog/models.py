import uuid

from django.db import models


class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Group(TimeStamped):
    group_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    agency = models.CharField(max_length=100, blank=True)
    debut_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'groups'
        ordering = ['name']

    def __str__(self):
        return self.name


class Idol(TimeStamped):
    idol_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stage_name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.RESTRICT, related_name='idols')
    birth_date = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'idols'
        ordering = ['group__name', 'stage_name']
        constraints = [
            models.UniqueConstraint(fields=['group', 'stage_name'], name='uniq_idol_per_group'),
        ]

    def __str__(self):
        return f'{self.stage_name} ({self.group.name})'

class Photocard(TimeStamped):
    class CardType(models.TextChoices):
        MEMBER = 'member', 'Individual Member'
        GROUP = 'group', 'Group'

    photocard_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.RESTRICT,
        related_name='photocards',
    )
    idols = models.ManyToManyField(
        Idol,
        blank=True,
        related_name='photocards',
    )
    card_type = models.CharField(
        max_length=10,
        choices=CardType.choices,
        default=CardType.MEMBER,
    )
    album_name = models.CharField(max_length=150)
    version = models.CharField(max_length=100, blank=True)
    rarity = models.CharField(max_length=50)
    image_url = models.URLField(blank=True)

    class Meta:
        db_table = 'photocards'
        ordering = ['group__name', 'album_name', 'rarity']

    def __str__(self):
        return f'{self.group.name} - {self.album_name} ({self.card_type})'
