from .models import Food, FoodGroup, FoodLanguaLFactor, LanguaLFactor, NutrientData, Nutrient, Source, Derivation, Weight, Footnote, DataLink, DataSource, DeletedFood, DeletedNutrient, DeletedFootnote
from rest_framework import serializers, viewsets
from rest_framework import filters


class NutrientDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = NutrientData
        fields = ("food", "nutrient", "ounce", "data_points", "error", "data_type", "derivation", "food_reference", "added_nutrient", "studies", "minimum_value",
                  "maximum_value", "degrees_of_freedom", "lower_error_bound", "uppper_error_bound", "statistical_comments", "last_modified", "confidence_code")


class NutrientDataViewSet(viewsets.ModelViewSet):
    queryset = NutrientData.objects.all()
    serializer_class = NutrientDataSerializer


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = ("id", "food_group", "long_description", "short_description", "name", "manufacturer_name", "survey",
                  "refuse_description", "refuse_percentage", "scientific_name", "n_factor", "pro_factor", "fat_factor", "cho_factor")


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    filter_backends = (filters.SearchFilter,)
    filter_fields = ("id")
    search_fields = (
        "long_description", "short_description", "name", "manufacturer_name")


class FoodGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodGroup
        fields = ("id", "name")


class FoodGroupViewSet(viewsets.ModelViewSet):
    queryset = FoodGroup.objects.all()
    serializer_class = FoodGroupSerializer


class FoodLanguaLFactorSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodLanguaLFactor
        fields = ("food", "langual_factor")


class FoodLanguaLFactorViewSet(viewsets.ModelViewSet):
    filter_fields = ("food", "langual_factor")
    queryset = FoodLanguaLFactor.objects.all()
    serializer_class = FoodLanguaLFactorSerializer


class LanguaLFactorSerializer(serializers.ModelSerializer):

    class Meta:
        model = LanguaLFactor
        fields = ("id", "name")


class LanguaLFactorViewSet(viewsets.ModelViewSet):
    filter_fields = ("id")
    queryset = LanguaLFactor.objects.all()
    serializer_class = LanguaLFactorSerializer


class NutrientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nutrient
        fields = ("id", "units", "tagname", "name", "decimals", "order")


class NutrientViewSet(viewsets.ModelViewSet):
    filter_fields = ("id")
    queryset = Nutrient.objects.all()
    serializer_class = NutrientSerializer


class SourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Source
        fields = ("id", "name")


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class DerivationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Derivation
        fields = ("id", "name")


class DerivationViewSet(viewsets.ModelViewSet):
    queryset = Derivation.objects.all()
    serializer_class = DerivationSerializer


class WeightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weight
        fields = ("food", "sequence", "amount", "name",
                  "grams", "data_points", "standard_derivation")


class WeightViewSet(viewsets.ModelViewSet):
    filter_fields = ("food")
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer


class FootnoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Footnote
        fields = ("food", "sequence", "type", "nutrient", "name")


class FootnoteViewSet(viewsets.ModelViewSet):
    queryset = Footnote.objects.all()
    serializer_class = FootnoteSerializer


class DataSourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataSource
        fields = ("id", "authors", "name", "year", "journal",
                  "volume", "issue_state", "start_page", "end_page")


class DataSourceViewSet(viewsets.ModelViewSet):
    filter_fields = ("id", "year")
    queryset = DataSource.objects.all()
    serializer_class = DataSourceSerializer


class DataLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataLink
        fields = ("food", "nutrient", "data_source")


class DataLinkViewSet(viewsets.ModelViewSet):
    filter_fields = ("food", "nutrient", "data_source")
    queryset = DataLink.objects.all()
    serializer_class = DataLinkSerializer

# The view and serializers to get all related Food information.


class FoodLanguaLFactorInfoSerializer(serializers.ModelSerializer):
    langual_factor = LanguaLFactorSerializer()

    class Meta:
        model = FoodLanguaLFactor
        fields = ("langual_factor",)


class DataLinkInfoSerializer(serializers.ModelSerializer):
    data_source = DataSourceSerializer()

    class Meta:
        model = DataLink
        fields = ("data_source",)


class NutrientDataInfoSerializer(serializers.ModelSerializer):
    nutrient = NutrientSerializer()
    derivation = DerivationSerializer()
    datatype = SourceSerializer()

    class Meta:
        model = NutrientData
        fields = ("nutrient", "ounce", "data_points", "error", "data_type", "derivation", "food_reference", "added_nutrient", "studies", "minimum_value",
                  "maximum_value", "degrees_of_freedom", "lower_error_bound", "uppper_error_bound", "statistical_comments", "last_modified", "confidence_code")


class FoodInfoSerializer(serializers.ModelSerializer):
    food_group = FoodGroupSerializer()
    footnote_set = FootnoteSerializer()
    nutrientdata_set = NutrientDataInfoSerializer()
    weight_set = WeightSerializer()
    foodlangualfactor_set = FoodLanguaLFactorInfoSerializer()
    datalink_set = DataLinkInfoSerializer()

    class Meta:
        model = Food
        fields = ("id", "food_group", "long_description", "short_description", "name", "manufacturer_name", "survey", "refuse_description", "refuse_percentage",
                  "scientific_name", "n_factor", "pro_factor", "fat_factor", "cho_factor", 'footnote_set', 'nutrientdata_set', 'weight_set', 'foodlangualfactor_set', 'datalink_set')


class FoodInfoViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodInfoSerializer
    filter_fields = ("id",)
