test = {   'name': 'q1',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(trump, '
                                               'pd.DataFrame)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> 10000 < trump.shape[0] < '
                                               '11000\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> trump.shape[1] >= 4\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> 831846101179314177 in '
                                               'trump.index\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> all(col in trump.columns '
                                               "for col in ['time', 'source', "
                                               "'text', 'retweet_count'])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.sometrue([('Twitter for "
                                               "iPhone' in s) for s in "
                                               "trump['source'].unique()])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> trump['time'].dtype == "
                                               "np.dtype('<M8[ns]')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> trump['text'].dtype == "
                                               "np.dtype('O')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "trump['retweet_count'].dtype "
                                               "== np.dtype('int64')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> 753063644578144260 in '
                                               'trump.index\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> 15000 < '
                                               "trump['retweet_count'].mean() "
                                               '< 15200\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
