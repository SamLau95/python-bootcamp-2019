test = {   'name': 'q8b',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               "np.isclose(sum(inspections_by_id_and_year['count']), "
                                               '14222,rtol=5)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'list(inspections_by_id_and_year.index.names)\n'
                                               "['business_id', 'year']",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'inspections_by_id_and_year_sol '
                                               '= '
                                               "ins.groupby([ins['business_id'], "
                                               'ins[\'year\']]).size().rename("count").to_frame();\n'
                                               '>>> '
                                               'inspections_by_id_and_year_sol.sort_values(ascending=False, '
                                               'by = ["count", "business_id"], '
                                               'inplace=True);\n'
                                               '>>> '
                                               'inspections_by_id_and_year.sort_values(ascending=False, '
                                               'by = ["count", "business_id"], '
                                               'inplace=True);\n'
                                               '>>> '
                                               'np.allclose(inspections_by_id_and_year_sol, '
                                               'inspections_by_id_and_year)\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
