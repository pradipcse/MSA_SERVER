from django.urls import path, include
from rest_framework.routers import DefaultRouter
from msa_api.views.advisor import AdvisorViewSet
from msa_api.views.alumani import AlumanaiViewSet
from msa_api.views.banner import BannerViewSet
from msa_api.views.emailview import VerifyEmailView
from msa_api.views.gellary import GalleryViewSet  # Fixed typo in 'gellary'
from msa_api.views.history import HistoryViewSet
from msa_api.views.mission import MissionViewSet
from msa_api.views.overview import OverviewViewSet
from msa_api.views.speech import SpeechViewset
from msa_api.views.updateNotice import UpdateAndNoticeViewSet
from .views.login import LoginView
from .views.register import RegisterView
from .views.users import UserListCreateView, UserDetailView
from .views.executive import ExecutiveCommitteeViewSet  
from .views.event import EventViewSet
from .views.adminstatus import CheckAdminStatusView

# Create a router and register the ViewSet
router = DefaultRouter()
router.register(r'executive_committees', ExecutiveCommitteeViewSet, basename="executive_committees")
router.register(r'update_notices', UpdateAndNoticeViewSet, basename="update_notices")
router.register(r'galleries', GalleryViewSet, basename="galleries")  # Removed incorrect '/'
router.register(r'alumanai', AlumanaiViewSet)
router.register(r'advisor', AdvisorViewSet)
router.register(r'speech',SpeechViewset )
router.register(r'events',EventViewSet)
router.register(r'banner', BannerViewSet)
router.register(r'mission', MissionViewSet)
router.register(r'overview', OverviewViewSet)
router.register(r'history', HistoryViewSet)
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('verify-email/<uuid:token>/', VerifyEmailView.as_view(), name='verify_email'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('', include(router.urls)),  # Include all router URLs at the base level
]

