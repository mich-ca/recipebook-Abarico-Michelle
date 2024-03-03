from django.contrib import admin
from .models import Recipe, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):
  model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
  model = Recipeinlines = [RecipeIngredientInline]

admin.site.register(Recipe, RecipeAdmin)
