from django.urls import path, include
from rest_framework.routers import DefaultRouter
from DriveVilla.api.views import (VehicleRUDAPIView, SellerCreateListAPIView, SellerRUDAPIView,
                                  BuyerCreateListAPIView, BuyerRUDAPIView, VehicleListCreateAPIView,
                                  AdvertisementListAPIView, AdvertisementRUDView,
                                  QuestionListCreateAPIView, QuestionRUDAPIView, AnswerListCreateAPIView,
                                  AnswerRUDAPIView, AdvertisementViewSet, UserGetAPIView,
                                  AdImageListCreateAPIView, AdImageRUDAPIView, SellerAdListAPIView,
                                  CustomUserViewSet, CurrentUserRUDAPIView, ChatMessageAPIView,
                                  ChatMessageRUDAPIView, ThreadListAPIView,  ActiveUserAPIView, ChatBotAPIView)

router = DefaultRouter()
router.register(r"advertisements", AdvertisementViewSet)

router2 = DefaultRouter()
router2.register(r"custom-users", CustomUserViewSet)

urlpatterns = [
     path('active/<str:username>/', ActiveUserAPIView.as_view()),
    path('chatbot/', ChatBotAPIView.as_view()),
    path('thread/', ThreadListAPIView.as_view()),
    path('chat-message/<int:id>/', ChatMessageRUDAPIView.as_view()),
    path('chat-message/<str:reciepent_name>/', ChatMessageAPIView.as_view()),
    path('current-user/', CurrentUserRUDAPIView.as_view()),
    path('', include(router2.urls)),
    path('advertisements/seller/<int:seller_id>/',
         SellerAdListAPIView.as_view()),
    path('vehicles/', VehicleListCreateAPIView.as_view()),
    path('vehicles/<int:vehicle_id>/', VehicleRUDAPIView.as_view()),
    path('sellers/', SellerCreateListAPIView.as_view()),
    path('sellers/<int:customer_id>/', SellerRUDAPIView.as_view()),
    path('buyers/', BuyerCreateListAPIView.as_view()),
    path('buyers/<int:customer_id>/', BuyerRUDAPIView.as_view()),
    path('adlist/', AdvertisementListAPIView.as_view()),
    path('adlist/<int:ad_id>/', AdvertisementRUDView.as_view()),
    path('advertisements/<int:ad_id>/questions/',
         QuestionListCreateAPIView.as_view()),
    path('advertisements/<int:ad_id>/questions/<slug:slug>/',
         QuestionRUDAPIView.as_view(), name="question-list"),
    path('advertisements/<int:ad_id>/questions/<slug:slug>/answers/',
         AnswerListCreateAPIView.as_view()),
    path('advertisements/<int:ad_id>/questions/<slug:slug>/answers/<slug:ans_slug>/',
         AnswerRUDAPIView.as_view(), name="answer-list"),
    path('advertisements/<int:ad_id>/images/<int:id>/',
         AdImageRUDAPIView.as_view()),
    path('advertisements/<int:ad_id>/images/',
         AdImageListCreateAPIView.as_view()),
    path('user/', UserGetAPIView.as_view()),
    path('', include(router.urls)),
]
