test = {   'name': 'q3f',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> print(list(bus.columns))\n'
                                               "['business_id', 'name', "
                                               "'address', 'city', 'state', "
                                               "'postal_code', 'latitude', "
                                               "'longitude', 'phone_number', "
                                               "'postal_code_5']\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'sum(bus["postal_code_5"].isin(weird_zip_code_businesses["postal_code_5"])) '
                                               '== 0\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> np.isclose(len(bus), 6146, '
                                               'rtol=5)\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
