from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('events', views.EventsView)

urlpatterns = [
    path('wastara/foundation/api/events/lists/', include(router.urls))
]
