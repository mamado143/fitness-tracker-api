from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Count
from django_filters.rest_framework import DjangoFilterBackend

from .models import Activity
from .serializers import ActivitySerializer

class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]
    
    # Enable filtering, sorting, and text searching
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    
    # Match these to your README requirements!
    filterset_fields = ['activity_type', 'date']
    ordering_fields = ['duration_minutes', 'calories_burned', 'date']
    search_fields = ['notes'] # Allows users to search text in their workout notes

    def get_queryset(self):
        """Ensure users only see their own data."""
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Automatically assign the logged-in user to the new activity."""
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def metrics(self, request):
        """Route: GET /api/activities/metrics/"""
        user_activities = self.get_queryset()

        stats = user_activities.aggregate(
            total_workouts=Count('id'),
            total_duration=Sum('duration_minutes'),
            total_calories=Sum('calories_burned')
        )

        return Response({
            "total_workouts": stats['total_workouts'] or 0,
            "total_duration_minutes": stats['total_duration'] or 0,
            "total_calories_burned": stats['total_calories'] or 0,
        })
