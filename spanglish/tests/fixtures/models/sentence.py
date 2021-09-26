""" fixtures that return an sql statement with a list of values to be inserted."""

def load_sentence():
    """ return the sql and values of the insert queuery."""

    sql = """
          INSERT INTO Spanglish_Test.Sentence
          (
              `sentence`, `language_id`, `category_id`
          ) 
          VALUES (%s, %s, %s)
        """
    values = [
        (
            'como estas ?', '2', '3'
        ),
        (
            'que dia es hoy ?', '2', '2'
        )
    ]

    return {
        'sql': sql, 
        'values': values
    }
