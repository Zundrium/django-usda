from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import datetime


# Structure based on National Nutrient Database for Standard Reference
# source: https://www.ars.usda.gov/Services/docs.htm?docid=8964


# Based on Table 4 - Food Description File
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Food(models.Model):

    class Meta:
        verbose_name = _('Fooddescription')
        verbose_name_plural = _('Fooddescriptions')
        ordering = ['name']
    id = models.CharField(_("Nutrient Databank number"), db_column="NDB_No", max_length=5, primary_key=True, help_text=_(
        "5-digit NutrientDatabank number that uniquelyidentifies a food item. If this field is defined asnumeric, the leading zero will be lost. "))
    food_group = models.ForeignKey('FoodGroup', db_column="FdGrp_Cd", help_text=_(
        "4-digit code indicating food group to which a food item belongs. "))
    long_description = models.CharField(_("Long description"), db_column="Long_Desc",
                                        max_length=200, help_text=_("200-character description of food item. "))
    short_description = models.CharField(_("Short description"), db_column="Shrt_Desc", max_length=60, help_text=_(
        "60-character abbreviated description of food item.Generated from the 200-character description usingabbreviations in Appendix A. If short description islonger than 60 characters, additional abbreviationsare made. "))
    name = models.CharField(_("Name (Common)"), db_column="ComName", max_length=100, blank=True, null=True, help_text=_(
        "Other names commonly used to describe a food,including local or regionalnames for various foods,for example, 'soda' or'pop' for 'carbonatedbeverages.' "))
    manufacturer_name = models.CharField(_("Manufacturer"), db_column="ManufacName", max_length=65, blank=True, null=True, help_text=_(
        "Indicates the company that manufactured the product, when appropriate. "))
    survey = models.BooleanField(_("Survey"), db_column="Survey", default=False, help_text=_(
        "Indicates if the food item is used in the USDA Foodand Nutrient Database for Dietary Studies (FNDDS)and thus has a complete nutrient profile for the 65FNDDS nutrients. "))
    refuse_description = models.CharField(_("Refuse description"), db_column="Ref_desc", max_length=135, blank=True, null=True, help_text=_(
        "Description of inedible parts of a food item (refuse),such as seeds or bone. "))
    refuse_percentage = models.IntegerField(
        _("Refuse Percentage"), db_column="Refuse", max_length=2, blank=True, null=True, help_text=_("Percentage of refuse."))
    scientific_name = models.CharField(_("Scientific name"), db_column="SciName", max_length=65, blank=True, null=True, help_text=_(
        "Scientific name of the food item. Given for the least processed form of the food (usually raw), if applicable. "))
    n_factor = models.DecimalField(_("N Factor"), db_column="N_Factor", max_digits=6,
                                   decimal_places=2, blank=True, null=True, help_text=_("Factor for converting nitrogen to protein."))
    pro_factor = models.DecimalField(_("Pro Factor"), db_column="Pro_Factor", max_digits=6,
                                     decimal_places=2, blank=True, null=True, help_text=_("Factor for calculating calories from protein."))
    fat_factor = models.DecimalField(_("Fat Factor"), db_column="Fat_Factor", max_digits=6,
                                     decimal_places=2, blank=True, null=True, help_text=_("Factor for calculating calories from fat."))
    cho_factor = models.DecimalField(_("CHO Factor"), db_column="CHO_Factor", max_digits=6,
                                     decimal_places=2, blank=True, null=True, help_text=_("Factor for calculating calories from carbohydrate."))

    def __unicode__(self):
        return self.name


# Based on Table 5 - Food Group Description File
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class FoodGroup(models.Model):

    class Meta:
        verbose_name = _('Food group')
        verbose_name_plural = _('Food groups')
        ordering = ['name']
    id = models.CharField(_("Food Group ID"), db_column="FdGrp_Cd", max_length=4, primary_key=True, help_text=_(
        "4-digit code identifying a food group. Only the first 2 digits are currently assigned. In the future, the last 2 digits may be used. Codes may not be consecutive. "))
    name = models.CharField(_("Name"), db_column="FdGrp_Desc",
                            max_length=60, help_text=_("Name of food group."))

    def __unicode__(self):
        return self.name


# Based on Table 6 - LanguaL Factor File
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class FoodLanguaLFactor(models.Model):

    class Meta:
        verbose_name = _('Food LanguaL factor')
        verbose_name_plural = _('Food LanguaL factors')
        unique_together = ("food", "langual_factor")
    food = models.ForeignKey('Food', db_column="NDB_No", help_text=_(
        "5-digit NutrientDatabank number that uniquelyidentifies a food item. If this field is defined asnumeric, the leading zero will be lost. "))
    langual_factor = models.ForeignKey('LanguaLFactor', db_column="Factor_Code", help_text=_(
        "The LanguaL factor from the Thesaurus."))

    def __unicode__(self):
        return "%s - %s" % (self.food, self.langual_factor)


# Based on Table 7 - LanguaL Factor Description File
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class LanguaLFactor(models.Model):

    class Meta:
        verbose_name = _('LanguaL factor')
        verbose_name_plural = _('LanguaL factors')
        ordering = ['name']
    id = models.CharField(_("Factor ID"), db_column="Factor_Code", max_length=5, primary_key=True, help_text=_(
        " TheLanguaL factor from the Thesaurus. Only thosecodes used to factor the foods contained in theLanguaL Factor file are included in this file."))
    name = models.CharField(_("Description"), db_column="Description", max_length=140, help_text=_(
        "The description of the LanguaL Factor Code from the thesaurus "))

    def __unicode__(self):
        return self.name


# Based on Table 8 - Nutrient Data File
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class NutrientData(models.Model):

    class Meta:
        verbose_name = _('Nutrient Data')
        verbose_name_plural = _('Nutrient Datas')
        unique_together = ("food", "nutrient")
    food = models.ForeignKey('Food', db_column="NDB_No",
                             help_text=_("5-digit Nutrient Databank number."))
    nutrient = models.ForeignKey('Nutrient', db_column="Nutr_No", help_text=_(
        "Unique 3-digit identifier code for a nutrient. "))
    ounce = models.DecimalField(_("Ounce"), db_column="Nutr_Val", max_digits=13,
                                decimal_places=3, help_text=_("Amount in 100 grams, edible portion."))
    data_points = models.IntegerField(_("Data points"), db_column="Num_Data_Pts", max_length=5, help_text=_(
        "Number of data points (previously called Sample_Ct)is the number of analyses used to calculate thenutrient value. If the numberof data points is 0, thevalue was calculated or imputed."))
    error = models.DecimalField(_("Error (Standard)"), db_column="Std_Error", max_digits=14, decimal_places=3, blank=True, null=True, help_text=_(
        "Standard error of the mean. Null if cannot be calculated. The standard error is also not given if the number of data points is less than three."))
    data_type = models.ForeignKey(
        'Source', db_column="Src_Cd", help_text=_("Code indicating type of data."))
    derivation = models.ForeignKey('Derivation', db_column='Deriv_Cd', blank=True, null=True, help_text=_(
        "Data Derivation Code giving specific information on how the value is determined. This field is populated only for items added or updated starting with SR14."))
    food_reference = models.ForeignKey('Food', db_column="Ref_NDB_No", related_name="food_reference_set", blank=True, null=True, help_text=_(
        "NDB number of the item used tocalculate a missingvalue. Populated onlyfor items added or updatedstarting with SR14."))
    added_nutrient = models.BooleanField(_("Added nutrient"), db_column="Add_Nutr_Mark", default=False, help_text=_(
        "Indicates a vitamin or mineral addedfor fortificationor enrichment. This fieldis populated for ready-to-eat breakfast cereals and many brand-name hotcereals in food group 8."))
    studies = models.IntegerField(
        _("Studies (amount)"), db_column="Num_Studies", blank=True, null=True)
    minimum_value = models.DecimalField(
        _("Minimum value"), db_column="Min", max_digits=14, decimal_places=3, blank=True, null=True)
    maximum_value = models.DecimalField(
        _("Maximum value"), db_column="Max", max_digits=14, decimal_places=3, blank=True, null=True)
    degrees_of_freedom = models.IntegerField(
        _("Degrees of freedom"), db_column="DF", max_length=4, blank=True, null=True)
    lower_error_bound = models.DecimalField(_("Lower error bound"), db_column="Low_EB",
                                            max_digits=14, decimal_places=3, blank=True, null=True, help_text=_("Lower 95% error bound."))
    uppper_error_bound = models.DecimalField(
        _("Upper error bound"), db_column="Up_EB", max_digits=14, decimal_places=3, blank=True, null=True, help_text=_("Upper 95% error bound."))
    statistical_comments = models.CharField(_("Statistical comments"), db_column="Stat_cmt", max_length=10,
                                            blank=True, null=True, help_text=_("Statistical comments. See documentation page 33."))
    last_modified = models.CharField(_("Last modified"), db_column="AddMod_Date", max_length=10, blank=True, null=True, help_text=_(
        "Indicates when a value was either added to the database or last modified."))
    confidence_code = models.IntegerField(_("Confidence code"), db_column="CC", max_length=1, blank=True, null=True, help_text=_(
        " Confidence Code indicating data quality, based on evaluation of sample plan, sample handling, analytical method, analytic al quality control, and number of samples analyzed. Not included in this release, but is planned for future releases. "))

    def __unicode__(self):
        return "%s - %s" % (self.food, self.nutrient)


# Based on Table 9 - Nutrient Definition File
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Nutrient(models.Model):

    class Meta:
        verbose_name = _('Nutrient')
        verbose_name_plural = _('Nutrients')
        ordering = ['name']
    id = models.CharField(_("Nutrient ID"), db_column="Nutr_No", max_length=3,
                          primary_key=True, help_text=_("Unique 3-digit identifier code for a nutrient. "))
    units = models.CharField(_("Units"), db_column="Units", max_length=7, help_text=_(
        " Units of measure (mg, g, and so on)."))
    tagname = models.CharField(_("Tagname"), db_column="Tagname", max_length=20, blank=True, null=True, help_text=_(
        " International Network of Food Data Systems(INFOODS) Tagnames. A unique abbreviation for anutrient/food component developed by INFOODS toaid in the interchange of data."))
    name = models.CharField(_("Name"), db_column="NutrDesc",
                            max_length=60, help_text=_("Name of nutrient/food component."))
    decimals = models.IntegerField(_("Decimals"), db_column="Num_Dec", max_length=1, help_text=_(
        "Number of decimal places to which a nutrient value is rounded. "))
    order = models.IntegerField(_("Order"), db_column="SR_Order", max_length=6, help_text=_(
        "Used to sort nutrient records in the same order as various reports produced from SR. "))

    def __unicode__(self):
        return self.name


# Based on Table 10 - Source Code File
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Source(models.Model):

    class Meta:
        verbose_name = _('Source')
        verbose_name_plural = _('Sources')
        ordering = ['name']
    id = models.CharField(_("Source ID"), db_column="Src_Cd",
                          max_length=2, primary_key=True, help_text=_("2-digit code."))
    name = models.CharField(_("Name"), db_column="SrcCd_Desc", max_length=60, help_text=_(
        "Description of source codethat identifies the type ofnutrient data. "))

    def __unicode__(self):
        return self.name


# Based on Table 11 - Derivation Code File
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Derivation(models.Model):

    class Meta:
        verbose_name = _('Derivation')
        verbose_name_plural = _('Derivations')
        ordering = ['name']
    id = models.CharField(_("Derivation ID"), db_column="Deriv_Cd",
                          max_length=4, primary_key=True, help_text=_("4-digit code"))
    name = models.CharField(_("Name"), db_column="Deriv_Desc", max_length=120, help_text=_(
        "Description of derivation code giving specific information on how the value was determined. "))

    def __unicode__(self):
        return self.name


# Based on Table 12 - Weight Code File
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Weight(models.Model):

    class Meta:
        verbose_name = _('LanguaL factor')
        verbose_name_plural = _('LanguaL factors')
        ordering = ['name']
        unique_together = ("food", "sequence")
    food = models.ForeignKey('Food', db_column="NDB_No",
                             help_text=_("5-digit Nutrient Databank number."))
    sequence = models.CharField(
        _("Sequence"), db_column="Seq", max_length=5, help_text=_("Sequence number."))
    amount = models.DecimalField(_("Amount"), db_column="Amount", max_digits=8,
                                 decimal_places=3, help_text=_("Unit modifier (for example, 1 in '1 cup'). "))
    name = models.CharField(_("Name"), db_column="Msre_Desc", max_length=84, help_text=_(
        "Description (for example, cup, diced, and 1-inch pieces). "))
    grams = models.DecimalField(_("Grams"), db_column="Gm_Wgt",
                                max_digits=8, decimal_places=1, help_text=_("Gram weight."))
    data_points = models.IntegerField(_("Data points"), db_column="Num_Data_Pts",
                                      max_length=3, blank=True, null=True, help_text=_("Number of data points. "))
    standard_derivation = models.DecimalField(
        _("Derivation (Standard)"), db_column="Std_Dev", max_digits=10, decimal_places=3, blank=True, null=True)

    def __unicode__(self):
        return self.name


# Based on Table 13 - Footnote File
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

FOOTNOTE_CHOICES = (
    ('D', _('Footnote adding information to the food description')),
    ('M', _('Footnote adding information to measure description')),
    ('N', _(
        'Footnote providing additional information on a nutrient value')),
)


class Footnote(models.Model):

    class Meta:
        verbose_name = _('LanguaL factor')
        verbose_name_plural = _('LanguaL factors')
        ordering = ['name']
    food = models.ForeignKey('Food', db_column="NDB_No",
                             help_text=_("5-digit Nutrient Databank number."))
    sequence = models.CharField(_("Sequence"), db_column="Footnt_No", max_length=4, help_text=_(
        " Sequence number. Ifa given footnote applies tomore than one nutrient number, the same footnotenumber is used. As a result, this file cannot beindexed. "))
    type = models.CharField(_("Type"), db_column="Footnt_Typ", max_length=1, choices=FOOTNOTE_CHOICES, help_text=_(
        "Type of footnote:D = footnote adding information to the fooddescription;M = footnote adding information to measuredescription;N = footnote providing additional information on anutrient value. If the Footnt_typ = N, the Nutr_No willalso be filled in. "))
    nutrient = models.ForeignKey('Nutrient', db_column="Nutr_No", blank=True, null=True, help_text=_(
        " Unique 3-digit identifier code for a nutrient to which footnote applies. "))
    name = models.CharField(_("Name"), db_column="Footnt_Txt",
                            max_length=200, help_text=_("Footnote text."))

    def __unicode__(self):
        return self.name


# Based on Table 14 - Data Link File
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class DataLink(models.Model):

    class Meta:
        verbose_name = _('Data link')
        verbose_name_plural = _('Data links')
        unique_together = ("food", "nutrient", 'data_source')
    food = models.ForeignKey('Food', db_column="NDB_No",
                             help_text=_("5-digit Nutrient Databank number."))
    nutrient = models.ForeignKey('Nutrient', db_column="Nutr_No", help_text=_(
        "Unique 3-digit identifier code for a nutrient. "))
    data_source = models.ForeignKey('DataSource', db_column="DataSrc_ID", help_text=_(
        "Unique ID identifying the reference/source. "))

    def __unicode__(self):
        return "%s - %s - %s" % (food, nutrient, data_source)


# Based on Table 15 - Data File
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class DataSource(models.Model):

    class Meta:
        verbose_name = _('Data source')
        verbose_name_plural = _('Data sources')
        ordering = ['name']
    id = models.CharField(_("DataSource ID"), db_column="DataSrc_ID", max_length=6,
                          primary_key=True, help_text=_("Unique number identifying the reference/source. "))
    authors = models.CharField(_("Authors"), db_column="Authors", max_length=255, blank=True, null=True, help_text=_(
        "List of authors for a journal article or name of sponsoring organization for other documents. "))
    name = models.CharField(_("Name"), db_column="Title", max_length=255, blank=True, null=True, help_text=_(
        "Title of article or name of document, such as a report from a company or trade association. "))  # optional to make the import work
    year = models.IntegerField(_("Year"), db_column="Year", max_length=4,
                               blank=True, null=True, help_text=_(" Year article or document was published."))
    journal = models.CharField(_("Journal"), db_column="Journal", max_length=135,
                               blank=True, null=True, help_text=_("Name of the journal in which the article was published. "))
    volume = models.CharField(_("Volume"), db_column="Vol_City", max_length=16, blank=True, null=True, help_text=_(
        " Volume number for journal articles, books, or reports; city where sponsoring organization is located. "))
    issue_state = models.CharField(_("Issue (state)"), db_column="Issue_State", max_length=5, blank=True, null=True, help_text=_(
        " Issue number for journal article; State where the sponsoring organization is located. "))
    start_page = models.IntegerField(_("Start page"), db_column="Start_Page", max_length=5,
                                     blank=True, null=True, help_text=_("Starting page number of article/document. "))
    end_page = models.IntegerField(_("End page"), db_column="End_Page", max_length=5,
                                   blank=True, null=True, help_text=_("Ending page number of article/document. "))

    def __unicode__(self):
        return self.name


# Based on Table 16 - Abbreviated File
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Not required for relational databases


# Based on Table 17 - Foods Deleted
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class DeletedFood(models.Model):

    class Meta:
        verbose_name = _('Deleted food')
        verbose_name_plural = _('Deleted foods')
        ordering = ['name']
    food_id = models.CharField(_("Nutrient Databank number"), db_column="NDB_No", max_length=5,
                               primary_key=True, help_text=_("Unique 5-digit number identifying deleted item. "))
    name = models.CharField(_("Name"), db_column="Shrt_Desc", max_length=60, help_text=_(
        "60-character abbreviated description of food item. "))

    def __unicode__(self):
        return self.name


# Based on Table 18 - Nutrients Deleted
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class DeletedNutrient(models.Model):

    class Meta:
        verbose_name = _('Deleted nutrient')
        verbose_name_plural = _('Deleted nutrients')
        ordering = ['nutrient_id']
    food_id = models.CharField(_("Nutrient Databank number"), db_column="NDB_No", max_length=5, primary_key=True, help_text=_(
        "Unique 5-digit number identifying the item that contains the deleted nutrient record. "))
    nutrient_id = models.CharField(_("Nutrient ID"), db_column="Nutr_No",
                                   max_length=3, help_text=_("Nutrient number of deleted record. "))

    def __unicode__(self):
        return self.nutrient_id


# Based on Table 19 - Footnotes Deleted
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class DeletedFootnote(models.Model):

    class Meta:
        verbose_name = _('LanguaL factor')
        verbose_name_plural = _('LanguaL factors')
    food_id = models.CharField(_("Nutrient Databank number"), db_column="NDB_No", max_length=5, primary_key=True, help_text=_(
        "Unique 5-digit number identifying the item that contains the deleted nutrient record. "))
    sequence = models.CharField(
        _("Sequence"), db_column="Footnt_No", max_length=4)
    type = models.CharField(_("FootnoteType"), db_column="Footnt_Typ", max_length=1,
                            choices=FOOTNOTE_CHOICES, help_text=_("Type of footnote of deleted record. "))

    def __unicode__(self):
        return "%s - %s" % (self.food_id, self.sequence)
