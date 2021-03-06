# -!- encoding:utf8 -!-
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# file:    cli_option_parser.py
# date:    2017-01-05
# author:  koromodako
# purpose:
#      Code du compilateur de fichiers .sgs
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class CLIOptionsParser(object):
    """docstring for CLIOptionsParser"""
    def __init__(self, argv):
        super(CLIOptionsParser, self).__init__()
        self.argv = argv
        self.prog = None
        self.error = 'n/a'
        self.options = {}

    def parse(self):
        k=0
        separate_value_expected=None
        for k in range(0,len(self.argv)):
            e=self.argv[k]
            if k == 0:
                self.prog = e
            elif separate_value_expected is not None:
                if '-' in e:
                    self.options[e] = ''
                    separate_value_expected=e
                elif '--' in e:
                    if not parse_long(e):
                        return False
                    separate_value_expected=None
                else:
                    self.options[separate_value_expected] = e
                    separate_value_expected=None
            else:
                if '--' in e:
                    if not parse_long(e):
                        return False
                elif '-' in e:
                    self.options[e] = ''
                    separate_value_expected=e
                else:
                    self.error = 'Unexpected argument. (at index %d)' % k
                    return False
        return True

    def parse_long(self, e):
        if '=' in e:
            self.options[e.split('=')[0]] = e.split('=')[-1]
        else:
            self.error = 'Long arguments expects a value specified using equal character. (at index %d)' % k
            return False
        return True

    def has_option(self, key):
        return (self.options.get(key, None) is not None)

    def option_value(self, key, default=''):
        return (self.options.get(key, default))