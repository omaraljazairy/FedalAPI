""" fixtures that return an sql statement with a list of values to be inserted."""

def load_language():
    """ return the sql and values of the insert queuery."""

    sql = """
          INSERT INTO Spanglish_Test.Language 
          (
              `name`, `iso-639-1`
          ) 
          VALUES (%s, %s)
        """
    values = [
        (
            'English', 'EN'
        ),
        (
            'Spanish', 'ES'
        ),
        (
            'Dutch', 'NL'
        )
    ]

    return {
        'sql': sql, 
        'values': values
    }
