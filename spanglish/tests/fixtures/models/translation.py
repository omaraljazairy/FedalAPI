""" fixtures that return an sql statement with a list of values to be inserted."""

def load_translation():
    """ return the sql and values of the insert queuery."""

    sql = """
          INSERT INTO Spanglish_Test.Translation 
          (
              `word_id`, `sentence_id`, `language_id`, `translation`
          ) 
          VALUES (%s, %s, %s, %s)
        """
    values = [
        (
            1, None, 1, 'go'
        ),
        (
            2, None, 1, 'monday'
        ),
        (
            3, None, 1, 'hello'
        ),
        (
            None, 1, 1, 'how are you doing ?'
        ),
        (
            None, 2, 1, 'what day is today ?'
        ),
        
    ]

    return {
        'sql': sql, 
        'values': values
    }
