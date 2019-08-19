test = {   'name': 'q1a',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(bike, '
                                               'pd.DataFrame)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> bike['holiday'].dtype == "
                                               "np.dtype('O')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "list(bike['holiday'].iloc[370:375]) "
                                               "== ['no', 'no', 'yes', 'yes', "
                                               "'yes']\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> bike['weekday'].dtype == "
                                               "np.dtype('O')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> bike['workingday'].dtype "
                                               "== np.dtype('O')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> bike['weathersit'].dtype "
                                               "== np.dtype('O')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> bike.shape == (17379, 17) '
                                               'or bike.shape == (17379, 18)\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "print(list(bike['weekday'].iloc[::2000]))\n"
                                               "['Sat', 'Tue', 'Mon', 'Mon', "
                                               "'Mon', 'Sun', 'Sun', 'Sat', "
                                               "'Sun']\n",
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "print(list(bike['workingday'].iloc[::2000]))\n"
                                               "['no', 'yes', 'yes', 'yes', "
                                               "'yes', 'no', 'no', 'no', "
                                               "'no']\n",
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "print(list(bike['weathersit'].iloc[::2000]))\n"
                                               "['Clear', 'Clear', 'Clear', "
                                               "'Clear', 'Clear', 'Clear', "
                                               "'Clear', 'Clear', 'Clear']\n",
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
