from django.db import models

# Create your models here.

class Phi:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

phis = [
  Phi('Democracy', 'tabby', 'foul little demon', 3),
]