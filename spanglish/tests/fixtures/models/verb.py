from enums.dbenums import VerbTense
""" fixtures that return an sql statement with a list of values to be inserted."""

def load_verb():
    """ return the sql and values of the insert queuery."""

    sql = """
          INSERT INTO Spanglish_Test.Verb 
          (
              `tense`, `word_id`, `yo`, `tu`, 
              `usted`, `nosotros`, `vosotros`, `ustedes`
          ) 
          VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
    values = [
        (
            VerbTense.PRESENT_PERFECT.value, 1, 'voy', 'vas', 'va', 'vamos', 'vais', 'van'
        ),
        (
            VerbTense.PRESENT_PERFECT.value, 3, 'vee', 'ves', 've', 'vamos', 'veis', 'ven'
        ),
        (
            VerbTense.PRESENT_PERFECT.value, 4, 'como', 'comes', 'come', 'comemos', 'comeis', 'comen'
        ),                
    ]

    return {
        'sql': sql, 
        'values': values
    }
