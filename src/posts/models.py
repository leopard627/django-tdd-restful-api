from django.utils import timezone
from django.db import models


class Post(models.Model):

    user = models.ForeignKey(
            'auth.User',
            on_delete=models.SET_NULL,
            null=True,
            db_index=True,
            related_name="user_posts")

    title = models.CharField(null=True, blank=True, max_length=150)

    contents = models.TextField(
            max_length=4500,
            blank=True,
            null=True,
            default=None)

    created_at = models.DateTimeField(
        db_index=True,
        default=timezone.now
    )

    updated_at = models.DateTimeField(
        null=True,
        auto_now=True,
    )

    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        default=None,
        db_index=True
    )

    def __str__(self):
        return '< {} Post>'.format(self.id)

    def __repr__(self):
        return '< {} Post>'.format(self.id)
