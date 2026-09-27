from django.db import models
from django.conf import settings
from projects.models import Environment

class FeatureFlag(models.Model):

    environment = models.ForeignKey(
        Environment,
        on_delete=models.CASCADE,
        related_name='feature_flags'
    )

    name = models.CharField(max_length=150)

    key = models.SlugField()

    description = models.TextField(blank=True)

    enabled = models.BooleanField(default=False)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_feature_flags'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['environment', 'key'],
                name='unique_feature_flag_per_environment'
            )
        ]

    def __str__(self):
        return f"{self.environment.name} - {self.name}"