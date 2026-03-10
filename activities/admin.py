from django.contrib import admin
from .models import Activity, WorkoutSet

class WorkoutSetInline(admin.TabularInline):
    model = WorkoutSet
    extra = 1

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'date', 'duration_minutes')
    list_filter = ('activity_type', 'date')
    search_fields = ('user__email', 'notes')
    inlines = [WorkoutSetInline]

@admin.register(WorkoutSet)
class WorkoutSetAdmin(admin.ModelAdmin):
    list_display = ('activity', 'exercise_name', 'set_number', 'reps', 'weight')
    search_fields = ('exercise_name',)
