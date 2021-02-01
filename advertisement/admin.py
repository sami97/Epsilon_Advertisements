from django.contrib import admin
from .models import Site
from .models import Customer_Details
from .models import Site_Details
from .models import User_Authentication
from .models import Agreement_Details

# Register your models here.
admin.site.register(Site)
admin.site.register(Customer_Details)
admin.site.register(Site_Details)
admin.site.register(User_Authentication)
admin.site.register(Agreement_Details)