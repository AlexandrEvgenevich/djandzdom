from django.urls import path
from measurement.views import MeasurementsView


urlpatterns = [
    path('measurements/', MeasurementsView.as_view()),
]


# TODO: зарегистрируйте необходимые маршруты
