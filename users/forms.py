from django_registration.forms import RegistrationForm
from users.models import CustomUser

class CustomUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = CustomUser    
        fields = ('username','first_name','last_name', 'email', 'customer_cnic', 'customer_dob',)
        

