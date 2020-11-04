from rest_framework import serializers, validators
from rest_framework.reverse import reverse
from DriveVilla.models import Seller, Buyer, Vehicle, Advertisement, Question, Answer, AdImage, ChatMessage, Thread, ActiveUser, ChatBotMessage
from rest_framework.exceptions import ValidationError
from users.models import CustomUser

class ActiveUserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ActiveUser
        fields = ['status',]

class ChatBotSerializer(serializers.ModelSerializer):
    response  = serializers.SerializerMethodField(read_only=True)
    customer = serializers.SerializerMethodField(read_only=True)
    seller = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ChatBotMessage
        fields = ['message', 'response', 'customer', 'seller']

    def get_response(self, instance):
        return instance.response

    def get_customer(self, instance):
        return instance.customer.username

    def get_seller(self, instance):
        return instance.ad_seller.username

class ThreadSerializer(serializers.ModelSerializer):
    sender_name = serializers.SerializerMethodField(read_only= True)
    reciepent_name = serializers.SerializerMethodField(read_only= True)

    class Meta:
        model = Thread
        fields = ['id','sender_name', 'reciepent_name']

    def get_sender_name(self, instance):
        return instance.sender.username

    def get_reciepent_name(self, instance):
        return instance.reciepent.username

class ChatMessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.SerializerMethodField(read_only=True)
    thread_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ChatMessage
        fields = ['id', 'content', 'sender_name', 'timestamp', 'thread_id']

    def get_sender_name(self, instance):
        return instance.sender.username

    def get_thread_id(self, instance):
        return instance.thread.id


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'id']


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'username',
                  'email', 'customer_cnic', 'customer_dob']


class SellerSerializer(serializers.ModelSerializer):

    seller_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Seller
        fields = "__all__"

    def get_seller_name(self, instance):
        return instance.customer.username


class BuyerSerializer(serializers.ModelSerializer):

    buyer_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Buyer
        fields = "__all__"

    def get_buyer_name(self, instance):
        return instance.customer.username


class VehicleSerializer(serializers.ModelSerializer):

    seller = serializers.SerializerMethodField()

    class Meta:
        model = Vehicle
        fields = ('vehicle_id', 'color', 'model', 'year',
                  'category', 'manufacturer', 'seller')

    def get_seller(self, instance):
        return instance.seller.customer.username


class AnswerSerializer(serializers.ModelSerializer):

    publisher = serializers.SerializerMethodField(read_only=True)
    ans_slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Answer
        fields = ("content", "publisher", "ans_slug")

    def get_publisher(self, instance):
        return instance.publisher.username


class CustomAnswerHyperLinkedRelatedField(serializers.HyperlinkedRelatedField):
    view_name = "answer-list"
    # queryset = Question.objects.all()

    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'ad_id': obj.question.advertisement.ad_id,
            'slug': obj.question.slug,
            'ans_slug': obj.ans_slug
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
            'ad_id': view_kwargs['ad_id'],
            'slug': view_kwargs['slug'],
            'ans_slug': view_kwargs['ans_slug']
        }
        return self.get_queryset().get(**lookup_kwargs)


class QuestionSerializer(serializers.ModelSerializer):

    publisher = serializers.SerializerMethodField(read_only=True)
    # answers  = AnswerSerializer(many = True, read_only = True)
    answers = CustomAnswerHyperLinkedRelatedField(
        read_only=True, many=True, view_name="answer-list")
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Question
        fields = ("content", "publisher", "answers", "slug")

    def get_publisher(self, instance):
        return instance.publisher.username


class CustomQuestionHyperLinkedRelatedField(serializers.HyperlinkedRelatedField):
    view_name = "question-list"
    # queryset = Question.objects.all()

    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'ad_id': obj.advertisement.ad_id,
            'slug': obj.slug
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
            'ad_id': view_kwargs['ad_id'],
            'slug': view_kwargs['slug']
        }
        return self.get_queryset().get(**lookup_kwargs)


class AdvertisementSerializer(serializers.ModelSerializer):

    seller = serializers.SerializerMethodField()
    seller_name = serializers.SerializerMethodField()
    # questions = QuestionSerializer(many = True, read_only= True)
    questions = CustomQuestionHyperLinkedRelatedField(
        read_only=True, many=True, view_name="question-list")

    class Meta:
        model = Advertisement
        fields = "__all__"

    def get_seller(self, instance):
        return instance.seller.customer.pk

    def get_seller_name(self, instance):
        return instance.seller.customer.username


class FileListSerializer (serializers.Serializer):
    image = serializers.ListField(
        child=serializers.FileField(max_length=100000,
                                    allow_empty_file=False,
                                    use_url=False)
    )

    def create(self, validated_data):
        ad = Advertisement.objects.latest('id')
        image = validated_data.pop('image')
        for img in image:
            photo = AdImage.objects.create(
                image=img, advertisement=ad, **validated_data)
        return photo


class AdImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdImage
        fields = ('id', 'image',)
