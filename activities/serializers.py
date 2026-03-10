from rest_framework import serializers
from .models import Activity, WorkoutSet

class WorkoutSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSet
        # We exclude 'activity' here because it will be automatically linked by the parent
        fields = ['id', 'exercise_name', 'set_number', 'reps', 'weight']

class ActivitySerializer(serializers.ModelSerializer):
    # This line tells Django to expect a nested list of workout sets
    workout_sets = WorkoutSetSerializer(many=True, required=False)

    class Meta:
        model = Activity
        fields = [
            'id', 'activity_type', 'date', 'duration_minutes', 
            'calories_burned', 'notes', 'workout_sets'
        ]
        # The user will be automatically assigned based on who is logged in via JWT
        read_only_fields = ['id', 'date']

    def create(self, validated_data):
        # 1. Pop the nested workout_sets data out of the dictionary
        workout_sets_data = validated_data.pop('workout_sets', [])
        
        # 2. Create the main Activity session
        activity = Activity.objects.create(**validated_data)
        
        # 3. Loop through and create each associated WorkoutSet
        for set_data in workout_sets_data:
            WorkoutSet.objects.create(activity=activity, **set_data)
            
        return activity
    
    def update(self, instance, validated_data):
        # Basic update logic for the main activity fields
        instance.activity_type = validated_data.get('activity_type', instance.activity_type)
        instance.duration_minutes = validated_data.get('duration_minutes', instance.duration_minutes)
        instance.calories_burned = validated_data.get('calories_burned', instance.calories_burned)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.save()
        
        # Note: For full production, you'd add complex logic here to update/delete 
        # specific nested workout sets, but this is enough to update the main session.
        return instance
