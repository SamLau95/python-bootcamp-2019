test = {   'name': 'q6a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> 0 <= rows_in_table <= 1e6\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> 0 <= unique_ins_ids <= '
                                               'rows_in_table\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.isclose(rows_in_table, '
                                               '14222, rtol=5)\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> np.isclose(unique_ins_ids, '
                                               '5766, rtol=5)\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
