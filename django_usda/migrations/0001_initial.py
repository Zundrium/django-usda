# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataLink',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Data link',
                'verbose_name_plural': 'Data links',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.CharField(primary_key=True, db_column=b'DataSrc_ID', serialize=False, max_length=6,
                                        help_text='Unique number identifying the reference/source. ', verbose_name='DataSource ID')),
                ('authors', models.CharField(db_column=b'Authors', max_length=255, blank=True,
                                             help_text='List of authors for a journal article or name of sponsoring organization for other documents. ', null=True, verbose_name='Authors')),
                ('name', models.CharField(db_column=b'Title', max_length=255, blank=True,
                                          help_text='Title of article or name of document, such as a report from a company or trade association. ', null=True, verbose_name='Name')),
                ('year', models.IntegerField(db_column=b'Year', max_length=4, blank=True,
                                             help_text=' Year article or document was published.', null=True, verbose_name='Year')),
                ('journal', models.CharField(db_column=b'Journal', max_length=135, blank=True,
                                             help_text='Name of the journal in which the article was published. ', null=True, verbose_name='Journal')),
                ('volume', models.CharField(db_column=b'Vol_City', max_length=16, blank=True,
                                            help_text=' Volume number for journal articles, books, or reports; city where sponsoring organization is located. ', null=True, verbose_name='Volume')),
                ('issue_state', models.CharField(db_column=b'Issue_State', max_length=5, blank=True,
                                                 help_text=' Issue number for journal article; State where the sponsoring organization is located. ', null=True, verbose_name='Issue (state)')),
                ('start_page', models.IntegerField(db_column=b'Start_Page', max_length=5, blank=True,
                                                   help_text='Starting page number of article/document. ', null=True, verbose_name='Start page')),
                ('end_page', models.IntegerField(db_column=b'End_Page', max_length=5, blank=True,
                                                 help_text='Ending page number of article/document. ', null=True, verbose_name='End page')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Data source',
                'verbose_name_plural': 'Data sources',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeletedFood',
            fields=[
                ('food_id', models.CharField(primary_key=True, db_column=b'NDB_No', serialize=False, max_length=5,
                                             help_text='Unique 5-digit number identifying deleted item. ', verbose_name='Nutrient Databank number')),
                ('name', models.CharField(help_text='60-character abbreviated description of food item. ',
                                          max_length=60, verbose_name='Name', db_column=b'Shrt_Desc')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Deleted food',
                'verbose_name_plural': 'Deleted foods',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeletedFootnote',
            fields=[
                ('food_id', models.CharField(primary_key=True, db_column=b'NDB_No', serialize=False, max_length=5,
                                             help_text='Unique 5-digit number identifying the item that contains the deleted nutrient record. ', verbose_name='Nutrient Databank number')),
                ('sequence', models.CharField(
                    max_length=4, verbose_name='Sequence', db_column=b'Footnt_No')),
                ('type', models.CharField(help_text='Type of footnote of deleted record. ', max_length=1, verbose_name='FootnoteType', db_column=b'Footnt_Typ', choices=[
                 (b'D', 'Footnote adding information to the food description'), (b'M', 'Footnote adding information to measure description'), (b'N', 'Footnote providing additional information on a nutrient value')])),
            ],
            options={
                'verbose_name': 'LanguaL factor',
                'verbose_name_plural': 'LanguaL factors',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeletedNutrient',
            fields=[
                ('food_id', models.CharField(primary_key=True, db_column=b'NDB_No', serialize=False, max_length=5,
                                             help_text='Unique 5-digit number identifying the item that contains the deleted nutrient record. ', verbose_name='Nutrient Databank number')),
                ('nutrient_id', models.CharField(help_text='Nutrient number of deleted record. ',
                                                 max_length=3, verbose_name='Nutrient ID', db_column=b'Nutr_No')),
            ],
            options={
                'ordering': ['nutrient_id'],
                'verbose_name': 'Deleted nutrient',
                'verbose_name_plural': 'Deleted nutrients',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Derivation',
            fields=[
                ('id', models.CharField(primary_key=True, db_column=b'Deriv_Cd', serialize=False,
                                        max_length=4, help_text='4-digit code', verbose_name='Derivation ID')),
                ('name', models.CharField(help_text='Description of derivation code giving specific information on how the value was determined. ',
                                          max_length=120, verbose_name='Name', db_column=b'Deriv_Desc')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Derivation',
                'verbose_name_plural': 'Derivations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.CharField(primary_key=True, db_column=b'NDB_No', serialize=False, max_length=5,
                                        help_text='5-digit NutrientDatabank number that uniquelyidentifies a food item. If this field is defined asnumeric, the leading zero will be lost. ', verbose_name='Nutrient Databank number')),
                ('long_description', models.CharField(help_text='200-character description of food item. ',
                                                      max_length=200, verbose_name='Long description', db_column=b'Long_Desc')),
                ('short_description', models.CharField(help_text='60-character abbreviated description of food item.Generated from the 200-character description usingabbreviations in Appendix A. If short description islonger than 60 characters, additional abbreviationsare made. ',
                                                       max_length=60, verbose_name='Short description', db_column=b'Shrt_Desc')),
                ('name', models.CharField(db_column=b'ComName', max_length=100, blank=True,
                                          help_text="Other names commonly used to describe a food,including local or regionalnames for various foods,for example, 'soda' or'pop' for 'carbonatedbeverages.' ", null=True, verbose_name='Name (Common)')),
                ('manufacturer_name', models.CharField(db_column=b'ManufacName', max_length=65, blank=True,
                                                       help_text='Indicates the company that manufactured the product, when appropriate. ', null=True, verbose_name='Manufacturer')),
                ('survey', models.BooleanField(
                    default=False, help_text='Indicates if the food item is used in the USDA Foodand Nutrient Database for Dietary Studies (FNDDS)and thus has a complete nutrient profile for the 65FNDDS nutrients. ', verbose_name='Survey', db_column=b'Survey')),
                ('refuse_description', models.CharField(db_column=b'Ref_desc', max_length=135, blank=True,
                                                        help_text='Description of inedible parts of a food item (refuse),such as seeds or bone. ', null=True, verbose_name='Refuse description')),
                ('refuse_percentage', models.IntegerField(db_column=b'Refuse', max_length=2, blank=True,
                                                          help_text='Percentage of refuse.', null=True, verbose_name='Refuse Percentage')),
                ('scientific_name', models.CharField(db_column=b'SciName', max_length=65, blank=True,
                                                     help_text='Scientific name of the food item. Given for the least processed form of the food (usually raw), if applicable. ', null=True, verbose_name='Scientific name')),
                ('n_factor', models.DecimalField(decimal_places=2, db_column=b'N_Factor', max_digits=6, blank=True,
                                                 help_text='Factor for converting nitrogen to protein.', null=True, verbose_name='N Factor')),
                ('pro_factor', models.DecimalField(decimal_places=2, db_column=b'Pro_Factor', max_digits=6, blank=True,
                                                   help_text='Factor for calculating calories from protein.', null=True, verbose_name='Pro Factor')),
                ('fat_factor', models.DecimalField(decimal_places=2, db_column=b'Fat_Factor', max_digits=6, blank=True,
                                                   help_text='Factor for calculating calories from fat.', null=True, verbose_name='Fat Factor')),
                ('cho_factor', models.DecimalField(decimal_places=2, db_column=b'CHO_Factor', max_digits=6, blank=True,
                                                   help_text='Factor for calculating calories from carbohydrate.', null=True, verbose_name='CHO Factor')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Fooddescription',
                'verbose_name_plural': 'Fooddescriptions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('id', models.CharField(primary_key=True, db_column=b'FdGrp_Cd', serialize=False, max_length=4,
                                        help_text='4-digit code identifying a food group. Only the first 2 digits are currently assigned. In the future, the last 2 digits may be used. Codes may not be consecutive. ', verbose_name='Food Group ID')),
                ('name', models.CharField(help_text='Name of food group.',
                                          max_length=60, verbose_name='Name', db_column=b'FdGrp_Desc')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Food group',
                'verbose_name_plural': 'Food groups',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodLanguaLFactor',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('food', models.ForeignKey(db_column=b'NDB_No', to='django_usda.Food',
                                           help_text='5-digit NutrientDatabank number that uniquelyidentifies a food item. If this field is defined asnumeric, the leading zero will be lost. ')),
            ],
            options={
                'verbose_name': 'Food LanguaL factor',
                'verbose_name_plural': 'Food LanguaL factors',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Footnote',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sequence', models.CharField(help_text=' Sequence number. Ifa given footnote applies tomore than one nutrient number, the same footnotenumber is used. As a result, this file cannot beindexed. ',
                                              max_length=4, verbose_name='Sequence', db_column=b'Footnt_No')),
                ('type', models.CharField(help_text='Type of footnote:D = footnote adding information to the fooddescription;M = footnote adding information to measuredescription;N = footnote providing additional information on anutrient value. If the Footnt_typ = N, the Nutr_No willalso be filled in. ',
                                          max_length=1, verbose_name='Type', db_column=b'Footnt_Typ', choices=[(b'D', 'Footnote adding information to the food description'), (b'M', 'Footnote adding information to measure description'), (b'N', 'Footnote providing additional information on a nutrient value')])),
                ('name', models.CharField(help_text='Footnote text.',
                                          max_length=200, verbose_name='Name', db_column=b'Footnt_Txt')),
                ('food', models.ForeignKey(db_column=b'NDB_No', to='django_usda.Food',
                                           help_text='5-digit Nutrient Databank number.')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'LanguaL factor',
                'verbose_name_plural': 'LanguaL factors',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LanguaLFactor',
            fields=[
                ('id', models.CharField(primary_key=True, db_column=b'Factor_Code', serialize=False, max_length=5,
                                        help_text=' TheLanguaL factor from the Thesaurus. Only thosecodes used to factor the foods contained in theLanguaL Factor file are included in this file.', verbose_name='Factor ID')),
                ('name', models.CharField(help_text='The description of the LanguaL Factor Code from the thesaurus ',
                                          max_length=140, verbose_name='Description', db_column=b'Description')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'LanguaL factor',
                'verbose_name_plural': 'LanguaL factors',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('id', models.CharField(primary_key=True, db_column=b'Nutr_No', serialize=False, max_length=3,
                                        help_text='Unique 3-digit identifier code for a nutrient. ', verbose_name='Nutrient ID')),
                ('units', models.CharField(help_text=' Units of measure (mg, g, and so on).',
                                           max_length=7, verbose_name='Units', db_column=b'Units')),
                ('tagname', models.CharField(db_column=b'Tagname', max_length=20, blank=True,
                                             help_text=' International Network of Food Data Systems(INFOODS) Tagnames. A unique abbreviation for anutrient/food component developed by INFOODS toaid in the interchange of data.', null=True, verbose_name='Tagname')),
                ('name', models.CharField(help_text='Name of nutrient/food component.',
                                          max_length=60, verbose_name='Name', db_column=b'NutrDesc')),
                ('decimals', models.IntegerField(help_text='Number of decimal places to which a nutrient value is rounded. ',
                                                 max_length=1, verbose_name='Decimals', db_column=b'Num_Dec')),
                ('order', models.IntegerField(help_text='Used to sort nutrient records in the same order as various reports produced from SR. ',
                                              max_length=6, verbose_name='Order', db_column=b'SR_Order')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Nutrient',
                'verbose_name_plural': 'Nutrients',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NutrientData',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ounce', models.DecimalField(help_text='Amount in 100 grams, edible portion.',
                                              decimal_places=3, verbose_name='Ounce', max_digits=13, db_column=b'Nutr_Val')),
                ('data_points', models.IntegerField(help_text='Number of data points (previously called Sample_Ct)is the number of analyses used to calculate thenutrient value. If the numberof data points is 0, thevalue was calculated or imputed.',
                                                    max_length=5, verbose_name='Data points', db_column=b'Num_Data_Pts')),
                ('error', models.DecimalField(decimal_places=3, db_column=b'Std_Error', max_digits=14, blank=True,
                                              help_text='Standard error of the mean. Null if cannot be calculated. The standard error is also not given if the number of data points is less than three.', null=True, verbose_name='Error (Standard)')),
                ('added_nutrient', models.BooleanField(default=False, help_text='Indicates a vitamin or mineral addedfor fortificationor enrichment. This fieldis populated for ready-to-eat breakfast cereals and many brand-name hotcereals in food group 8.',
                                                       verbose_name='Added nutrient', db_column=b'Add_Nutr_Mark')),
                ('studies', models.IntegerField(
                    null=True, verbose_name='Studies (amount)', db_column=b'Num_Studies', blank=True)),
                ('minimum_value', models.DecimalField(db_column=b'Min', decimal_places=3,
                                                      max_digits=14, blank=True, null=True, verbose_name='Minimum value')),
                ('maximum_value', models.DecimalField(db_column=b'Max', decimal_places=3,
                                                      max_digits=14, blank=True, null=True, verbose_name='Maximum value')),
                ('degrees_of_freedom', models.IntegerField(max_length=4, null=True,
                                                           verbose_name='Degrees of freedom', db_column=b'DF', blank=True)),
                ('lower_error_bound', models.DecimalField(decimal_places=3, db_column=b'Low_EB', max_digits=14,
                                                          blank=True, help_text='Lower 95% error bound.', null=True, verbose_name='Lower error bound')),
                ('uppper_error_bound', models.DecimalField(decimal_places=3, db_column=b'Up_EB', max_digits=14,
                                                           blank=True, help_text='Upper 95% error bound.', null=True, verbose_name='Upper error bound')),
                ('statistical_comments', models.CharField(db_column=b'Stat_cmt', max_length=10, blank=True,
                                                          help_text='Statistical comments. See documentation page 33.', null=True, verbose_name='Statistical comments')),
                ('last_modified', models.CharField(db_column=b'AddMod_Date', max_length=10, blank=True,
                                                   help_text='Indicates when a value was either added to the database or last modified.', null=True, verbose_name='Last modified')),
                ('confidence_code', models.IntegerField(db_column=b'CC', max_length=1, blank=True,
                                                        help_text=' Confidence Code indicating data quality, based on evaluation of sample plan, sample handling, analytical method, analytic al quality control, and number of samples analyzed. Not included in this release, but is planned for future releases. ', null=True, verbose_name='Confidence code')),
            ],
            options={
                'verbose_name': 'Nutrient Data',
                'verbose_name_plural': 'Nutrient Datas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.CharField(primary_key=True, db_column=b'Src_Cd', serialize=False,
                                        max_length=2, help_text='2-digit code.', verbose_name='Source ID')),
                ('name', models.CharField(help_text='Description of source codethat identifies the type ofnutrient data. ',
                                          max_length=60, verbose_name='Name', db_column=b'SrcCd_Desc')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Source',
                'verbose_name_plural': 'Sources',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sequence', models.CharField(help_text='Sequence number.',
                                              max_length=5, verbose_name='Sequence', db_column=b'Seq')),
                ('amount', models.DecimalField(help_text="Unit modifier (for example, 1 in '1 cup'). ",
                                               decimal_places=3, verbose_name='Amount', max_digits=8, db_column=b'Amount')),
                ('name', models.CharField(help_text='Description (for example, cup, diced, and 1-inch pieces). ',
                                          max_length=84, verbose_name='Name', db_column=b'Msre_Desc')),
                ('grams', models.DecimalField(help_text='Gram weight.', decimal_places=1,
                                              verbose_name='Grams', max_digits=8, db_column=b'Gm_Wgt')),
                ('data_points', models.IntegerField(db_column=b'Num_Data_Pts', max_length=3, blank=True,
                                                    help_text='Number of data points. ', null=True, verbose_name='Data points')),
                ('standard_derivation', models.DecimalField(db_column=b'Std_Dev', decimal_places=3,
                                                            max_digits=10, blank=True, null=True, verbose_name='Derivation (Standard)')),
                ('food', models.ForeignKey(db_column=b'NDB_No', to='django_usda.Food',
                                           help_text='5-digit Nutrient Databank number.')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'LanguaL factor',
                'verbose_name_plural': 'LanguaL factors',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='weight',
            unique_together=set([('food', 'sequence')]),
        ),
        migrations.AddField(
            model_name='nutrientdata',
            name='data_type',
            field=models.ForeignKey(
                db_column=b'Src_Cd', to='django_usda.Source', help_text='Code indicating type of data.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nutrientdata',
            name='derivation',
            field=models.ForeignKey(db_column=b'Deriv_Cd', blank=True, to='django_usda.Derivation',
                                    help_text='Data Derivation Code giving specific information on how the value is determined. This field is populated only for items added or updated starting with SR14.', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nutrientdata',
            name='food',
            field=models.ForeignKey(
                db_column=b'NDB_No', to='django_usda.Food', help_text='5-digit Nutrient Databank number.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nutrientdata',
            name='food_reference',
            field=models.ForeignKey(related_name='food_reference_set', db_column=b'Ref_NDB_No', blank=True, to='django_usda.Food',
                                    help_text='NDB number of the item used tocalculate a missingvalue. Populated onlyfor items added or updatedstarting with SR14.', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nutrientdata',
            name='nutrient',
            field=models.ForeignKey(db_column=b'Nutr_No', to='django_usda.Nutrient',
                                    help_text='Unique 3-digit identifier code for a nutrient. '),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='nutrientdata',
            unique_together=set([('food', 'nutrient')]),
        ),
        migrations.AddField(
            model_name='footnote',
            name='nutrient',
            field=models.ForeignKey(db_column=b'Nutr_No', blank=True, to='django_usda.Nutrient',
                                    help_text=' Unique 3-digit identifier code for a nutrient to which footnote applies. ', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='foodlangualfactor',
            name='langual_factor',
            field=models.ForeignKey(
                db_column=b'Factor_Code', to='django_usda.LanguaLFactor', help_text='The LanguaL factor from the Thesaurus.'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='foodlangualfactor',
            unique_together=set([('food', 'langual_factor')]),
        ),
        migrations.AddField(
            model_name='food',
            name='food_group',
            field=models.ForeignKey(db_column=b'FdGrp_Cd', to='django_usda.FoodGroup',
                                    help_text='4-digit code indicating food group to which a food item belongs. '),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='datalink',
            name='data_source',
            field=models.ForeignKey(
                db_column=b'DataSrc_ID', to='django_usda.DataSource', help_text='Unique ID identifying the reference/source. '),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='datalink',
            name='food',
            field=models.ForeignKey(
                db_column=b'NDB_No', to='django_usda.Food', help_text='5-digit Nutrient Databank number.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='datalink',
            name='nutrient',
            field=models.ForeignKey(db_column=b'Nutr_No', to='django_usda.Nutrient',
                                    help_text='Unique 3-digit identifier code for a nutrient. '),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='datalink',
            unique_together=set([('food', 'nutrient', 'data_source')]),
        ),
    ]
