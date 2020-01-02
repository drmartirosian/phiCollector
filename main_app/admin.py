from django.contrib import admin
# add Feeding to the import
from .models import Phi, Feeding, Toy, Photo

# register the new Model
admin.site.register(Phi)
admin.site.register(Feeding)
admin.site.register(Toy)
admin.site.register(Photo)