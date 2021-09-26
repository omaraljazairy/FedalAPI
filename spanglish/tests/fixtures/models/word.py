""" fixtures that return an sql statement with a list of values to be inserted."""

def load_word():
    """ return the sql and values of the insert queuery."""

    sql = """
          INSERT INTO Spanglish_Test.Word 
          (
              `word`, `language_id`, `category_id`
          ) 
          VALUES (%s, %s, %s)
        """
    values = [
        (
            'Ir', 2, 1
        ),
        (
            'Lunes', 2, 2
        ),
        (
            'Hola', 2, 3
        ),
        (
            'Ver', 2, 1
        ),
        (
            'Comer', 2, 1
        ),
        (
            'Saber', 2, 1
        ),                
    ]

    return {
        'sql': sql, 
        'values': values
    }
