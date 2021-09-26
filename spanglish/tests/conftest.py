import pytest
import logging
import configs.dbtables as dbtable
from tests.fixtures.models.language import load_language
from tests.fixtures.models.category import load_category
from tests.fixtures.models.verb import load_verb
from tests.fixtures.models.word import load_word
from tests.fixtures.models.sentence import load_sentence
from tests.fixtures.models.translation import load_translation
from services.dbconnection import DBConnection

logger = logging.getLogger('test')
dbconn = DBConnection()
conn = dbconn.get_connection()

def insert_fixtures_db(sql:str, values:list):
    """ provide the db_conn, sql and values as list to be inserted. """

    
    cursor = conn.cursor()
    total_records = 0

    for args in values:
        try:
            cursor.execute(sql, args)
            result = cursor.rowcount
            total_records += result 
            logger.debug("records inserted: %s", result)
        except Exception as e:
            logger.error("Error inserting fixtures: %s", str(e))
    
    logger.info("total records inserted = %s", total_records)


def delete_fixtures_db(table:str):
    """ provide the db_conn and the table to be have its records deleted. """

    # dbconn = db_conn
    logger.debug("table received: %s", table)

    cursor = conn.cursor()
    
    sql = "TRUNCATE `Spanglish_Test`.".__add__(table)
    args = ()
    
    logger.debug("sql query: %s", sql)

    try:
        cursor.execute(sql, args)
        result = cursor.rowcount
        logger.debug("total records delete from table %s successfully: %s", table, result)
    except Exception as e:
        logger.error("Error deleting fixtures: %s", str(e))


def pytest_sessionstart(session):
    """ start before tests start. """

    logger.info("======================= SESSION START  ======================")
    # insert and delete records from the database tables.

    # create a list of tables to have their data deleted
    tables = [
        dbtable.LANGUAGE,
        dbtable.CATEGORY,
        dbtable.WORD,
        dbtable.VERB,
        dbtable.SENTENCE,
        dbtable.TRANSLATION
    ]

    # create a list of fixture models to be executed when loading fixtures. 
    models = [
        load_language(),
        load_category(),
        load_word(),
        load_verb(),
        load_sentence(),
        load_translation()
    ]

    # loop through the tables list to be deleted.
    for table in tables:
       delete_fixtures_db(table=table)

    # loop through the models list to insert data. 

    for data in models:
        sql = data['sql']
        values = data['values']

        logger.debug("sql received: %s", sql)
        logger.debug("values received: %s", values)

        insert_fixtures_db(
            sql=sql, 
            values=values,
        )


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """

    logger.info("======================= SESSION FINISH  ======================")

    conn.close()
