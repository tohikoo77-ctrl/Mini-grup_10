from django.urls import path
from core.views.auth_views import RegisterView, LoginView, LogoutView
from core.views.recent_verify import ResentVerifyCodeView


urlpatterns = [
      path("logout/", LogoutView.as_view()),
      path('login/', LoginView.as_view()),
      path('register/', RegisterView.as_view()),
      path("resend-code/", ResentVerifyCodeView.as_view()),
]