test = {   'name': 'q1d',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> df_allclose(bus, '
                                               'bus_summary)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> df_allclose(ins, '
                                               'ins_summary)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> df_allclose(vio, '
                                               'vio_summary)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> df_allclose(bus, '
                                               "pd.read_csv('data/businesses.csv', "
                                               "encoding='ISO-8859-1'), "
                                               "['business_id', 'latitude', "
                                               "'longitude'])\n"
                                               'True',
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> df_allclose(ins, '
                                               "pd.read_csv('data/inspections.csv'), "
                                               "['business_id', 'score'])\n"
                                               'True',
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> df_allclose(vio, '
                                               "pd.read_csv('data/violations.csv'), "
                                               "['business_id'])\n"
                                               'True',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
