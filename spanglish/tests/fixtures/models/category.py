""" fixtures that return an sql statement with a list of values to be inserted."""

def load_category():
    """ return the sql and values of the insert queuery."""

    sql = """
          INSERT INTO Spanglish_Test.Category 
          (
              `name`
          ) 
          VALUES (%s)
        """
    values = [
        (
            'Verb',
        ),
        (
            'Day',
        ),
        (
            'Greeting',
        )
    ]

    return {
        'sql': sql, 
        'values': values
    }
