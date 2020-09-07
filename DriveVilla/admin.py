from django.contrib import admin
from DriveVilla.models import Advertisement, Seller, Buyer, Vehicle, Question, Answer, AdImage, ChatMessage, Thread, ChatBotMessage, ActiveUser
# Register your models here.
admin.site.register(Vehicle)
admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(Advertisement)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(AdImage)
admin.site.register(ChatMessage)
admin.site.register(Thread)
admin.site.register(ChatBotMessage)
admin.site.register(ActiveUser)