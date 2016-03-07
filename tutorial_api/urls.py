from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from snippets.views import SnippetViewSet, UserViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    # Login and logout views for the browsable API
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
