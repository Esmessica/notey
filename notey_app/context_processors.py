from datetime import date
from .models import Mood


def mood_context(request):
    # Initialize mood as None by default
    mood = None

    if request.user.is_authenticated:
        today_date = date.today()
        mood_record = Mood.objects.filter(author=request.user, mood_date=today_date).first()
        mood = 'mood_advice' if mood_record else 'mood'

    return {'mood': mood}