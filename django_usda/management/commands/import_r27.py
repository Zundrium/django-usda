from django.core.management.base import BaseCommand, CommandError
from django.db.models.loading import get_model
from django_usda.models import Food, FoodGroup, FoodLanguaLFactor, LanguaLFactor, NutrientData, Nutrient, Source, Derivation, Weight, Footnote, DataLink, DataSource, DeletedFood, DeletedNutrient, DeletedFootnote
import zipfile
import csv
import json
import time
from django.db import IntegrityError
from django import db

appLabel = "django_usda"

modelMap = [
    {"fileName": "DATA_SRC.txt", 	"model": DataSource},
    {"fileName": "FD_GROUP.txt",	"model": FoodGroup},
    {"fileName": "FOOD_DES.txt",	"model": Food},
    {"fileName": "LANGDESC.txt",	"model": LanguaLFactor},
    {"fileName": "LANGUAL.txt", 	"model": FoodLanguaLFactor},
    {"fileName": "NUTR_DEF.txt", 	"model": Nutrient},
    {"fileName": "DERIV_CD.txt",	"model": Derivation},
    {"fileName": "SRC_CD.txt",		"model": Source},
    {"fileName": "NUT_DATA.txt",	"model": NutrientData},
    {"fileName": "WEIGHT.txt",		"model": Weight},
    {"fileName": "FOOTNOTE.txt",	"model": Footnote},
    {"fileName": "DATSRCLN.txt",	"model": DataLink}
]


def filter(value):
    newValue = value.replace("\r\n", "")
    if newValue == "":
        return None
    return newValue


def importFile(file, model):
    contents = file.readlines()
    bulk = []
    print "Creating objects."
    for counter, line in enumerate(contents):
        values = line.replace("~", "").decode(
            'iso-8859-1').encode('utf8').split("^")
        fields = list(model._meta.fields)
        if fields[0].get_internal_type() == "AutoField":
            del fields[0]
        newModel = createObject(model, fields, values)
        if newModel:
            bulk.append(newModel)
    importObjects(model, bulk)


def importObjects(model, bulk):
    length = len(bulk)
    chunkSize = 50000
    if length > chunkSize:
        for counter, chunk in enumerate(chunks(bulk, chunkSize)):
            print "Importing %s/%s objects into the database." % (counter * chunkSize + len(chunk), length)
            importChunk(model, chunk)
    else:
        print "Importing %s objects into the database." % len(bulk)
        importChunk(model, bulk)


def importChunk(model, chunk):
    try:
        model.objects.bulk_create(chunk)
    except IntegrityError as e:
        if "Duplicate entry" not in str(e):
            print "Database Error: %s" % e
            print chunk


def createObject(model, fields, values):
    linkedFields = {}
    try:
        for counter, value in enumerate(values):
            value = filter(value)
            field = fields[counter]
            key = field.name
            if not field.null and value == "":
                raise Exception(
                    "%s: Field required but null given." % field.name)
            fieldType = field.get_internal_type()
            if fieldType == "ForeignKey":
                key = key + "_id"
            elif fieldType == "BooleanField":
                value = False
                if value == "Y":
                    value = True
            linkedFields[key] = value
        return model(**linkedFields)
    except Exception as e:
        print "Model creation error for pk '%s': %s" % (values[0], e)
    return False


def chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i + n]


class Command(BaseCommand):
    args = "<zipFile>"
    help = 'Import the nutrition database (Only R27 Supported)'

    def handle(self, *args, **options):
        openedZipFile = zipfile.ZipFile(args[0])
        order = 0
        for info in modelMap:
            print "Importing file '%s' as %s" % (info["fileName"], info["model"]._meta.verbose_name_plural.title())
            importFile(openedZipFile.open(info["fileName"]), info["model"])
        openedZipFile.close()
