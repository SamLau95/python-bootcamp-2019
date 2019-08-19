test = {
    'name':
    'q32',
    'points':
    1,
    'suites': [{
        'cases': [{
            'code': r"""
          >>> type(imdb) == pd.DataFrame
          True
          """,
            'hidden': False,
            'locked': False
        }, {
            'code': r"""
          >>> imdb.shape
          (250, 5)
          """,
            'hidden': False,
            'locked': False
        }, {
            'code': r"""
          >>> print(imdb.sort_values('Votes').head().to_string(index=False))
          Votes  Rating                        Title  Year  Decade
          26012     8.0                  Kumonosu-jô  1957    1950
          28012     8.0                  Le samouraï  1967    1960
          31003     8.1        Le salaire de la peur  1953    1950
          32385     8.0       La battaglia di Algeri  1966    1960
          35983     8.1  The Best Years of Our Lives  1946    1940
          """,
            'hidden': False,
            'locked': False
        }],
        'scored':
        True,
        'setup':
        '',
        'teardown':
        '',
        'type':
        'doctest'
    }]
}
