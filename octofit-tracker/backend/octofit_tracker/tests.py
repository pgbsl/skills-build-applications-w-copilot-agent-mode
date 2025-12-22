from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email='test@hero.com', name='Test Hero', team='Marvel')
        self.assertEqual(user.email, 'test@hero.com')
        self.assertEqual(user.team, 'Marvel')

    def test_team_creation(self):
        team = Team.objects.create(name='Avengers')
        self.assertEqual(team.name, 'Avengers')

    def test_activity_creation(self):
        activity = Activity.objects.create(user='Test Hero', activity_type='Running', duration=20)
        self.assertEqual(activity.activity_type, 'Running')

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(team='Avengers', points=100)
        self.assertEqual(lb.points, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', difficulty='Easy')
        self.assertEqual(workout.difficulty, 'Easy')
