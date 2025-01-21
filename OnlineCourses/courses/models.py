from django.db import models

# Create your models here.

class Review(models.Model):
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    review_text = models.TextField()
    rating = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name + ": " + self.review_text[:50] + "..."