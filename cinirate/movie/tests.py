from django.contrib.auth.models import User
from django.test import TestCase

from .models import Movie, Review


class MovieAverageRatingTests(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title='Test Movie',
            description='A test movie',
            release_date='2026-01-01',
            genre='Drama',
        )

    def test_average_rating_without_reviews_is_zero(self):
        self.assertEqual(self.movie.average_rating(), 0)

    def test_average_rating_uses_movie_review_relation(self):
        first_user = User.objects.create_user(username='first')
        second_user = User.objects.create_user(username='second')
        Review.objects.create(
            user=first_user,
            movie=self.movie,
            rating=3,
            comment='First review',
        )
        Review.objects.create(
            user=second_user,
            movie=self.movie,
            rating=5,
            comment='Second review',
        )

        self.assertEqual(self.movie.average_rating(), 4)
