from django.db import models
from organizations.models import Organization


class Project(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='projects'
    )

    name = models.CharField(max_length=150)
    key = models.SlugField()

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['organization', 'key'],
                name='unique_project_key_per_organization'
            )
        ]

    def __str__(self):
        return self.name


class Environment(models.Model):

    ENVIRONMENT_TYPES = [
        ('DEVELOPMENT', 'Development'),
        ('STAGING', 'Staging'),
        ('PRODUCTION', 'Production'),
    ]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='environments'
    )

    name = models.CharField(max_length=100)

    key = models.SlugField()

    environment_type = models.CharField(
        max_length=20,
        choices=ENVIRONMENT_TYPES
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['project', 'key'],
                name='unique_environment_key_per_project'
            )
        ]

    def __str__(self):
        return f"{self.project.name} - {self.name}"