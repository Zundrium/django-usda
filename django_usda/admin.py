from django.contrib import admin
from .models import Food, FoodGroup, FoodLanguaLFactor, LanguaLFactor, NutrientData, Nutrient, Source, Derivation, Weight, Footnote, DataLink, DataSource, DeletedFood, DeletedNutrient, DeletedFootnote


class FoodAdmin(admin.ModelAdmin):
    model = Food

admin.site.register(Food, FoodAdmin)


class FoodGroupAdmin(admin.ModelAdmin):
    model = FoodGroup

admin.site.register(FoodGroup, FoodGroupAdmin)


class FoodLanguaLFactorAdmin(admin.ModelAdmin):
    model = FoodLanguaLFactor

admin.site.register(FoodLanguaLFactor, FoodLanguaLFactorAdmin)


class LanguaLFactorAdmin(admin.ModelAdmin):
    model = LanguaLFactor

admin.site.register(LanguaLFactor, LanguaLFactorAdmin)


class NutrientDataAdmin(admin.ModelAdmin):
    model = NutrientData

admin.site.register(NutrientData, NutrientDataAdmin)


class NutrientAdmin(admin.ModelAdmin):
    model = Nutrient

admin.site.register(Nutrient, NutrientAdmin)


class SourceAdmin(admin.ModelAdmin):
    model = Source

admin.site.register(Source, SourceAdmin)


class DerivationAdmin(admin.ModelAdmin):
    model = Derivation

admin.site.register(Derivation, DerivationAdmin)


class WeightAdmin(admin.ModelAdmin):
    model = Weight

admin.site.register(Weight, WeightAdmin)


class FootnoteAdmin(admin.ModelAdmin):
    model = Footnote

admin.site.register(Footnote, FootnoteAdmin)


class DataLinkAdmin(admin.ModelAdmin):
    model = DataLink

admin.site.register(DataLink, DataLinkAdmin)


class DataSourceAdmin(admin.ModelAdmin):
    model = DataSource

admin.site.register(DataSource, DataSourceAdmin)


class DeletedFoodAdmin(admin.ModelAdmin):
    model = DeletedFood

admin.site.register(DeletedFood, DeletedFoodAdmin)


class DeletedNutrientAdmin(admin.ModelAdmin):
    model = DeletedNutrient

admin.site.register(DeletedNutrient, DeletedNutrientAdmin)


class DeletedFootnoteAdmin(admin.ModelAdmin):
    model = DeletedFootnote

admin.site.register(DeletedFootnote, DeletedFootnoteAdmin)
