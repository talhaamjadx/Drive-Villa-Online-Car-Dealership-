from django.db import models
from users.models import CustomUser

# Create your models here.

class ActiveUser(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)

class ChatBotMessage(models.Model):
    message  = models.CharField(max_length= 300)
    response = models.CharField(max_length= 300)
    customer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)

class Thread(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name = "thread_sender")
    reciepent = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name = "thread_reciever")

    def get_thread_name(self):
        return f'chat_{self.id}'

class ChatMessage(models.Model):
    content = models.CharField(max_length=1000)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name = "message_sender")
    reciepent = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name = "message_reciever")
    timestamp = models.TimeField(auto_now_add= True)
    thread = models.ForeignKey(Thread, on_delete= models.CASCADE, related_name= "chat_message", null = True, blank= True) 


class Seller(models.Model):
    customer = models.OneToOneField(
        CustomUser, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.username


class Buyer(models.Model):
    customer = models.OneToOneField(
        CustomUser, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.username


class Vehicle(models.Model):

    CATEGORIES = [
        ('SUV', 'SUVs'),
        ('SEDAN', 'Sedan'),
        ('TRUCK', 'Truck')
    ]

    vehicle_id = models.AutoField(verbose_name="Vehicle ID", primary_key=True)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    year = models.DateField()
    category = models.CharField(choices=CATEGORIES, max_length=50)
    manufacturer = models.CharField(max_length=50)
    buyer = models.ForeignKey(
        Buyer, on_delete=models.CASCADE, null=True, blank=True, related_name="vehicle_b")
    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE, null=True, blank=True, related_name="vehicle_s")

    def __str__(self):
        return self.model+" "+str(self.vehicle_id)


class Advertisement(models.Model):
    ad_id = models.AutoField(verbose_name="Advertisement ID", primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    expected_price = models.CharField(max_length=20)
    vehicle_id = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE, related_name="vehicle_ad")
    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE, related_name="advertisement")

    def __str__(self):
        return self.title


class Question(models.Model):
    content = models.CharField(max_length=200)
    advertisement = models.ForeignKey(
        Advertisement, on_delete=models.CASCADE, related_name="questions")
    publisher = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="questions")
    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True)

    def __str__(self):
        return self.content


class Answer(models.Model):
    content = models.CharField(max_length=200)
    publisher = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers")
    ans_slug = models.SlugField(
        max_length=250, unique=True, null=True, blank=True)

    def __str__(self):
        return self.content


class AdImage(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
