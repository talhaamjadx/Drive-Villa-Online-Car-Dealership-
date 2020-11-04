from rest_framework.views import APIView
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView,
                                     get_object_or_404, ListAPIView, Http404, RetrieveAPIView, CreateAPIView)
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from DriveVilla.api.serializers import (VehicleSerializer, SellerSerializer,
                                        BuyerSerializer, AdvertisementSerializer,
                                        QuestionSerializer, AnswerSerializer, UserSerializer, AdImageSerializer,
                                        FileListSerializer, CustomUserSerializer, ChatMessageSerializer,
                                        ThreadSerializer, ActiveUserSerializer, ChatBotSerializer)
from DriveVilla.models import Vehicle, Seller, Buyer, Advertisement, Question, Answer, AdImage, ChatMessage, Thread, ActiveUser, ChatBotMessage
from users.models import CustomUser
from DriveVilla.api.permissions import (IsAdPublisherOrReadOnly, IsVehicleSellerOrReadOnly,
                                        IsAdminOrReadOnly, IsAdPublisher, IsQuestionPubOrReadOnly,
                                        IsAnswerPubOrReadOnly)
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.viewsets import ModelViewSet
from model.ConversationCreator import chatConversation
from model.model import CreateUpdateChatbot, LoadChatBot, PredictReply
from DriveVilla import tasks

class ActiveUserAPIView(ListAPIView):
    serializer_class = ActiveUserSerializer
    
    def get_queryset(self):
        username = self.kwargs['username']
        print(username)
        user = CustomUser.objects.get(username=username)
        active = ActiveUser.objects.filter(user=user)
        return active


class ChatBotListAPIView(ListAPIView):

    serializer_class = ChatBotSerializer
    queryset = ChatBotMessage.objects.all()
    # cuda = tasks.createUser.delay('hello', 'talha')

    # def perform_create(self, serializer):

    #     message = self.request.data['message']
    #     user = self.request.user
    #     result = tasks.getResponse.delay(message, user.username)
    #     print(result)
    #     response = result.get(propagate = False)
    #     serializer.save(response=response, customer = user)

class ChatBotListCreateAPIView(ListCreateAPIView):
    serializer_class = ChatBotSerializer
    
    def get_queryset(self):
        buyer = self.request.user
        seller_name = self.kwargs['seller_name']
        seller = CustomUser.objects.get(username= seller_name)
        print(buyer)
        print(seller)
        messages = ChatBotMessage.objects.filter(customer = buyer, ad_seller = seller)
        print(messages)
        return messages

    def perform_create(self, serializer):
        seller_name = self.kwargs['seller_name']
        seller = CustomUser.objects.get(username= seller_name)
        print(seller)
        buyer = self.request.user
        print(buyer)
        message = self.request.data['message']
        result = tasks.getResponse.delay(message, buyer.username)
        response = result.get(propagate = False)
        serializer.save(customer = buyer, ad_seller = seller, response = response)


class ThreadListAPIView(ListAPIView):
    serializer_class = ThreadSerializer

    def get_queryset(self):
        user = self.request.user
        sender_thread = Thread.objects.filter(sender=user)
        reciepent_thread = Thread.objects.filter(reciepent=user)
        return sender_thread | reciepent_thread


class ChatMessageAPIView(ListCreateAPIView):
    serializer_class = ChatMessageSerializer

    def get_queryset(self):
        sender = self.request.user
        reciepent_name = self.kwargs['reciepent_name']
        reciepent = CustomUser.objects.get(username=reciepent_name)
        messages_sender = ChatMessage.objects.filter(
            sender=sender, reciepent=reciepent)
        messages_reciever = ChatMessage.objects.filter(
            sender=reciepent, reciepent=sender)
        messages_combined = messages_sender | messages_reciever
        latest = messages_combined.order_by('timestamp')
        return latest

    def perform_create(self, serializer):
        sender = self.request.user
        reciepent_name = self.kwargs['reciepent_name']
        reciepent = CustomUser.objects.get(username=reciepent_name)
        if Thread.objects.filter(sender=sender, reciepent=reciepent).exists():
            thread = Thread.objects.get(sender=sender, reciepent=reciepent)
        elif Thread.objects.filter(sender=reciepent, reciepent=sender).exists():
            thread = Thread.objects.get(sender=reciepent, reciepent=sender)
        else:
            thread = Thread.objects.create(sender=sender, reciepent=reciepent)
        serializer.save(sender=sender, reciepent=reciepent, thread=thread)


class ChatMessageRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ChatMessageSerializer
    queryset = ChatMessage.objects.all()
    lookup_field = "id"


class CustomUserViewSet(ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    lookup_field = "id"


class CurrentUserRUDAPIView(APIView):
    def get(self, request):
        user = request.user
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = CustomUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserGetAPIView(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class VehicleListCreateAPIView(ListCreateAPIView):
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]
    queryset = Vehicle.objects.all()

    def perform_create(self, serializer):
        request_user = self.request.user
        try:
            seller = Seller.objects.get(customer=request_user)
            serializer.save(seller=seller)
        except Seller.DoesNotExist:
            seller = Seller.objects.create(customer=request_user)
            serializer.save(seller=seller)


class VehicleRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "vehicle_id"
    queryset = Vehicle.objects.all()


class SellerCreateListAPIView(ListCreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class SellerRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()
    lookup_field = "customer_id"
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class BuyerCreateListAPIView(ListCreateAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class BuyerRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BuyerSerializer
    queryset = Buyer.objects.all()
    lookup_field = "customer_id"
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class AdvertisementViewSet(ModelViewSet):
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()
    lookup_field = "ad_id"
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdPublisherOrReadOnly]

    def perform_create(self, serializer):
        request_user = self.request.user
        try:
            seller = Seller.objects.get(customer=request_user)
            serializer.save(seller=seller)
        except Seller.DoesNotExist:
            seller = Seller.objects.create(customer=request_user)
            serializer.save(seller=seller)

    def get_serializer_context(self):
        return {"request": self.request}


class AdvertisementListAPIView(ListCreateAPIView):
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated, IsAdPublisher]

    def get_queryset(self):
        request_user = self.request.user
        try:
            seller = Seller.objects.get(customer=request_user)
            ads = Advertisement.objects.filter(seller=seller)
            return ads
        except Seller.DoesNotExist:
            seller = Seller.objects.create(customer=request_user)
            # serializer.save(seller = seller)

    def perform_create(self, serializer):
        request_user = self.request.user
        try:
            seller = Seller.objects.get(customer=request_user)
            serializer.save(seller=seller)
        except Seller.DoesNotExist:
            seller = Seller.objects.create(customer=request_user)
            serializer.save(seller=seller)


class SellerAdListAPIView(ListAPIView):
    serializer_class = AdvertisementSerializer

    def get_queryset(self):
        seller_id = self.kwargs.get("seller_id")
        custom_user = CustomUser.objects.get(pk=seller_id)
        seller = Seller.objects.get(customer=custom_user)
        ads = Advertisement.objects.filter(seller=seller)
        return ads


class AdvertisementRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated, IsAdPublisher]
    lookup_field = "ad_id"

    def get_queryset(self):
        request_user = self.request.user
        seller = Seller.objects.get(customer=request_user)
        ads = Advertisement.objects.filter(seller=seller)
        return ads


class QuestionListCreateAPIView(ListCreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "ad_id"

    def get_queryset(self):
        ad_id = self.kwargs.get("ad_id")
        advertisement = Advertisement.objects.get(ad_id=ad_id)
        questions = Question.objects.filter(advertisement=advertisement)
        return questions

    def perform_create(self, serializer):
        publisher = self.request.user
        ad_id = self.kwargs.get("ad_id")
        advertisement = Advertisement.objects.get(ad_id=ad_id)
        serializer.save(advertisement=advertisement, publisher=publisher)

    def get_serializer_context(self):
        return {'request': self.request}


class QuestionRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsQuestionPubOrReadOnly]
    lookup_field = "slug"
    queryset = Question.objects.all()

    def get_serializer_context(self):
        return {'request': self.request}


class AnswerListCreateAPIView(ListCreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "slug"

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        question = Question.objects.get(slug=slug)
        answers = Answer.objects.filter(question=question)
        return answers

    def perform_create(self, serializer):
        publisher = self.request.user
        slug = self.kwargs.get("slug")
        question = Question.objects.get(slug=slug)
        # question = Question.objects.filter(advertisement = advertisement)
        serializer.save(question=question, publisher=publisher)


class AnswerRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AnswerSerializer
    lookup_field = "ans_slug"
    permission_classes = [IsAuthenticated, IsAnswerPubOrReadOnly]
    queryset = Answer.objects.all()


class AdImageListCreateAPIView(ListCreateAPIView):
    serializer_class = AdImageSerializer

    def get_queryset(self):
        ad_id = self.kwargs.get('ad_id')
        ad = Advertisement.objects.get(ad_id=ad_id)
        image = AdImage.objects.filter(advertisement=ad)
        return image

    def perform_create(self, serializer):
        ad_id = self.kwargs.get('ad_id')
        print(self.request.FILES)
        ad = Advertisement.objects.get(ad_id=ad_id)
        # image = AdImage.objects.create(advertisement = ad)
        serializer.save(advertisement=ad)


class AdImageRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AdImageSerializer
    lookup_field = 'id'

    def get_queryset(self):
        ad_id = self.kwargs.get('ad_id')
        id = self.kwargs.get('id')
        ad = Advertisement.objects.get(ad_id=ad_id)
        image = AdImage.objects.filter(advertisement=ad, id=id)
        return image
