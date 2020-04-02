from peewee import *
from datetime import datetime
import os

from module_log import get_log_formatter
from environs import Env
env = Env()
env.read_env()

try:
    if os.environ['DATABASE'] != None:
        db = MySQLDatabase(
            "sp_odesi",
            user="root",
            passwd="helloWORLD123",
            port=3306
            )
except:
    db = SqliteDatabase('odesi.db', pragmas={'journal_mode': 'wal'})

class AnalysisModes(Model):
    """AnalysisModes

    """
    a_mode_id       = AutoField()
    analysis_mode   = CharField(max_length=30, unique=True, null=False)

    class Meta:
        database = db

class Collections(Model):
    """Collections

    """
    collection_id   = AutoField()
    collection_name = CharField(max_length=30, null=False)

    class Meta:
        database    = db

class Dates(Model):
    """Dates

    """
    date_id         = AutoField()
    date            = DateField(null=False, unique=True)
    #should remove day_of_the_week
    day_of_week     = IntegerField(null=False)
    session         = IntegerField(null=False)

    class Meta:
        database = db

class ExportTypes(Model):
    """ExportTypes

    """
    e_type_id       = AutoField()
    export_type     = CharField(max_length=30, unique=False, null=False)

    class Meta:
        database = db
        #table_name ="ExportTypes"

class Groups(Model):
    """Groups

    """
    school_id       = AutoField()
    school_name     = CharField(max_length=45, null=False)
    coll_ids        = CharField(max_length=100, null=False)

    class Meta:
        database = db

class Modes(Model):
    """Modes

    """
    mode_id         = AutoField()
    mode            = CharField(max_length=45, null=False)
    coll_ids        = CharField(max_length=100, unique=True, null=False)

    class Meta:
        database = db

class Patterns(Model):
    """Patterns

    """
    ranges          = CharField(max_length=45, null=False)
    school_id       = ForeignKeyField(Groups, null=False)

    class Meta:
        database = db

class RegressionModes(Model):
    """RegressionModes

    """
    r_mode_id       = AutoField()
    regression_mode = CharField(max_length=45, unique=True, null=False)

    class Meta:
        database = db

class SearchTerms(Model):
    """SearchTerms

    """
    s_term_id       = AutoField()
    search_term     = CharField(max_length=300, unique=True, null=False)

    class Meta:
        database = db

class SearchTypes(Model):
    """SearchTypes

    """
    s_type_id       = AutoField()
    search_type     = CharField(max_length=10, unique=True, null=False)

    class Meta:
        database = db

class Surveys(Model):
    """Surveys

    """
    survey_id       = CharField(max_length=100, unique=True, null=False)
    dash_survey_id  = CharField(max_length=100, unique=True, null=False)
    collection_id   = ForeignKeyField(Collections, null=False)
    survey_name     = CharField(max_length=100, unique=True, null=False)

    class Meta:
        database = db

class OdesiDailyAccess(Model):
    """OdesiDailyAccess

    """
    date_id             = ForeignKeyField(Dates, null=False)
    school_id           = ForeignKeyField(Groups, null=False)
    access_main         = IntegerField(null=False, default=0)
    execute_download    = IntegerField(null=False, default=0)
    survey_id           = ForeignKeyField(Surveys, null=False)
    s_term_id           = ForeignKeyField(SearchTerms, null=False)
    s_type_id           = ForeignKeyField(SearchTypes, null=False)
    mode_id             = ForeignKeyField(Modes, null=False)
    r_mode_id           = ForeignKeyField(RegressionModes, null=False)
    a_mode_id           = ForeignKeyField(AnalysisModes, null=False)
    e_type_id           = ForeignKeyField(ExportTypes, null=False)
    counter             = IntegerField(null=False, default=0)

    class Meta:
        database = db

def create_table():
    app_log = get_log_formatter()
    AnalysisModes.create_table()
    Collections.create_table()
    Dates.create_table()
    ExportTypes.create_table()
    Groups.create_table()
    Modes.create_table()
    Patterns.create_table()
    RegressionModes.create_table()
    SearchTerms.create_table()
    SearchTypes.create_table()
    Surveys.create_table()
    OdesiDailyAccess.create_table()
    #db.create_tables([Service, Chat, Queue, Staff])
    app_log.info("Created 12 tables for ODESI" )

def destroy_table():
    app_log = get_log_formatter()
    AnalysisModes.delete().execute()
    Collections.delete().execute()
    Dates.delete().execute()
    ExportTypes.delete().execute()
    Groups.delete().execute()
    Modes.delete().execute()
    Patterns.delete().execute()
    RegressionModes.delete().execute()
    SearchTerms.delete().execute()
    SearchTypes.delete().execute()
    Surveys.delete().execute()
    OdesiDailyAccess.delete().execute()
    #db.create_tables([Service, Chat, Queue, Staff])
    app_log.info("Created 12 tables for ODESI" )

if __name__ == '__main__':
    #destroy_table()
    create_table()
    print("\n\t\tAll Tables are now created")
