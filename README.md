# Django USDA

An easy to set up Django Rest Framework API that is compatible with the USDA Nutrient Database.

## Requirements
- Python (2.6.5+, 2.7, 3.2, 3.3, 3.4)
- Django (1.4.11+, 1.5.5+, 1.6, 1.7)
- Django Rest Framework (2.4.4)

## Installation
1. You can install Django USDA with Python PIP:

  ```
   pip install git+https://github.com/zundrium/django-usda.git
  ```
  
2. Now you can add Django USDA to your `INSTALLED_APPS` in the `settings.py` of your project together with the required dependencies.

  ```python
   INSTALLED_APPS = (
    ...
    'rest_framework',
    'django_usda',
   )
  ```

3. Add the following settings to the `settings.py` for Django Rest Framework to function properly.

  ```python
  REST_FRAMEWORK = {
      'DEFAULT_PERMISSION_CLASSES': [
          'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
      ],
      'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
      'PAGINATE_BY': 250,
      'PAGINATE_BY_PARAM': 'page_size',
      'MAX_PAGINATE_BY': 250
  }
  ```

4. After that add the ViewSets that you want to use and the required url patterns to the `urls.py` of your project.

  ```python
  from django_usda.modelviewsets import FoodViewSet, FoodGroupViewSet, FoodLanguaLFactorViewSet, LanguaLFactorViewSet, NutrientDataViewSet, NutrientViewSet, SourceViewSet, DerivationViewSet, WeightViewSet, FootnoteViewSet, DataLinkViewSet, DataSourceViewSet, FoodInfoViewSet
  from django.contrib import admin
  
  router = routers.DefaultRouter()
  
  router.register(r'foods', 				FoodViewSet)
  router.register(r'foodgroups', 			FoodGroupViewSet)
  router.register(r'foodlangualfactors', 	FoodLanguaLFactorViewSet)
  router.register(r'langualfactors', 		LanguaLFactorViewSet)
  router.register(r'nutrientdatas', 		NutrientDataViewSet)
  router.register(r'nutrients', 			NutrientViewSet)
  router.register(r'sources', 			SourceViewSet)
  router.register(r'derivations', 		DerivationViewSet)
  router.register(r'weights', 			WeightViewSet)
  router.register(r'footnotes', 			FootnoteViewSet)
  router.register(r'datalinks', 			DataLinkViewSet)
  router.register(r'datasources', 		DataSourceViewSet)
  router.register(r'foodinfo', 			FoodInfoViewSet)
  
  urlpatterns = patterns('',
      ...
      url(r'^', include(router.urls)),
      url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  )
  ```

5. Run `python manage.py migrate` if you have South or Django 1.7 installed. Otherwise use `python manage.py syncdb`.

6. [Download][1] the ASCII version of the 27th release of the USDA Nutrient Database.

7. Run `python manage.py import_r27 <path_to_zipfile>`.

8. Start the development server (Normally `python manage.py runserver`).

9. That's it, now you can use the viewsets in your application! (Example: `http://localhost:8000/foodinfo/01001`).
 
[1]: http://www.ars.usda.gov/Services/docs.htm?docid=24912
