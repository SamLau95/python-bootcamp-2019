test = {   'name': 'q5a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(sent, '
                                               'pd.DataFrame)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> sent.shape\n(7503, 1)',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'list(sent.index[5000:5005])\n'
                                               "['perfectness', 'perfecto', "
                                               "'perfects', 'peril', "
                                               "'perjury']",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "np.allclose(sent['polarity'].head(), "
                                               '[-1.5, -0.4, -1.5, -0.4, '
                                               '-0.7])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
