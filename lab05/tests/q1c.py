test = {   'name': 'q1c',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               "np.round(daily_counts['casual'].mean())\n"
                                               '848.0',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "np.round(daily_counts['casual'].var())\n"
                                               '471450.0',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "np.round(daily_counts['registered'].mean())\n"
                                               '3656.0',
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "np.round(daily_counts['registered'].var())\n"
                                               '2434400.0',
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "sorted(list(daily_counts['workingday'].value_counts()))\n"
                                               '[231, 500]',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
