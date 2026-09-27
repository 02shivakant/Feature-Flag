from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class OrganizationMember(models.Model):

    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('DEVELOPER', 'Developer'),
        ('VIEWER', 'Viewer'),
    ]

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='members'
    )

    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='organization_memberships'
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='VIEWER'
    )

    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['organization', 'user'],
                name='unique_organization_member'
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.organization.name}"