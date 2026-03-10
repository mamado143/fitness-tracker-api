from django.db import models
from django.conf import settings

class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('weightlifting', 'Weightlifting'),
        ('tae_bo', 'Tae Bo'),
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('other', 'Other'),
    ]

    # Link every activity to our CustomUser
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='activities')
    
    # High-level session details
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    date = models.DateTimeField(auto_now_add=True)
    duration_minutes = models.PositiveIntegerField(help_text="Total time spent in minutes")
    calories_burned = models.PositiveIntegerField(null=True, blank=True)
    notes = models.TextField(blank=True, help_text="How did the workout feel?")

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Activities"

    def __str__(self):
        return f"{self.user.email} - {self.get_activity_type_display()} on {self.date.strftime('%Y-%m-%d')}"


class WorkoutSet(models.Model):
    """
    Specifically for tracking the granular details of resistance training.
    """
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='workout_sets')
    exercise_name = models.CharField(max_length=100, help_text="E.g., Barbell Squat, Overhead Press")
    set_number = models.PositiveIntegerField(default=1)
    reps = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2, help_text="Weight lifted (kg/lbs)")

    class Meta:
        ordering = ['activity', 'set_number']

    def __str__(self):
        return f"{self.exercise_name}: {self.reps} reps @ {self.weight}"
