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