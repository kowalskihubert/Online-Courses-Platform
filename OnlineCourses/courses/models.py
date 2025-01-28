from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Review(models.Model):
    RATING_CHOICES = [
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Użytkownik"
    )
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Ocena"
    )
    text = models.TextField(
        max_length=500,
        blank=True,
        verbose_name="Treść opinii"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data dodania"
    )
    approved = models.BooleanField(
        default=False,
        verbose_name="Zatwierdzona"
    )

    class Meta:
        verbose_name = "Opinia"
        verbose_name_plural = "Opinie"
        ordering = ['-created_at']

    def __str__(self):
        return f"Opinia {self.user.username if self.user else 'Anonim'} ({self.created_at.date()})"


class ContactMessage(models.Model):

    # Make name not required
    name = models.CharField(max_length=50, blank = True)
    reason = models.CharField(max_length=50, default="question")
    message = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.name or 'Anonymous'}: {self.message[:50]}..."


class CourseMaterial(models.Model):
    SUBJECT_CHOICES = [
        ('PHYS', 'Fizyka'),
        ('MATH', 'Matematyka'),
    ]

    subject = models.CharField(max_length=4, choices=SUBJECT_CHOICES)
    topic = models.CharField(max_length=100)
    embed_code = models.TextField(help_text="Paste Google Slides embed iframe code here")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.get_subject_display()} - {self.topic}"


