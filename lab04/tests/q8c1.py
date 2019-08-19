test = {   'name': 'q8c1',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               'isinstance(scores_pairs_by_business, '
                                               'pd.DataFrame)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'scores_pairs_by_business.columns\n'
                                               "Index(['score_pair'], "
                                               "dtype='object')",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # SOLUTION 1;\n'
                                               '>>> \n'
                                               '>>> student_arr = '
                                               'np.array(scores_pairs_by_business.values.tolist()).squeeze();\n'
                                               '>>> \n'
                                               '>>> # Now we will check the '
                                               'head score pares;\n'
                                               '>>> # score_pair;\n'
                                               '>>> # business_id;\n'
                                               '>>> # 24 [96, 98];\n'
                                               '>>> # 45 [78, 84];\n'
                                               '>>> # 66 [98, 100];\n'
                                               '>>> # 67 [87, 94];\n'
                                               '>>> # 76 [100, 98];\n'
                                               '>>> [96, 98] in student_arr '
                                               'and [78, 84] in student_arr '
                                               'and [98, 100] in student_arr '
                                               'and [87, 94] in student_arr '
                                               'and [100, 98] in student_arr\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
