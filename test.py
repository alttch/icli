#!/usr/bin/env python3

import icli
import sys

try:
    import neotermcolor
except:
    neotermcolor = None

user_accounts = ['john', 'kate', 'max']
api_keys = ['key1', 'key2', 'key3']
documents = ['file1', 'file2', 'file3']


class ComplUsers():

    def __call__(self, prefix, **kwargs):
        return user_accounts


class ArgumentParser(icli.ArgumentParser):

    def run(self, _object, _type=None, _command=None, **kwargs):
        if _object == 'user':
            if _type == 'account':
                if _command == 'list':
                    for i in user_accounts:
                        print(i)
                elif _command == 'add':
                    user_accounts.append(kwargs['account'])
                    print('OK')
                elif _command == 'del':
                    user_accounts.remove(kwargs['account'])
                    print('OK')
            elif _type == 'apikey':
                for i in range(1, 4):
                    print('api key {}'.format(i))
        elif _object == 'document':
            for i in documents:
                print(i)

    def print_global_help(self):
        print('w - who is logged in')
        print('top - processes')
        print('uptime - system uptime')
        print()

    def syscmd(self, cmd):
        import os
        os.system(cmd)

    def handle_interactive_exception(self):
        if neotermcolor:
            neotermcolor.cprint('error', 'red')
        else:
            print('error')
        import traceback
        traceback.print_exc()

    def get_interactive_prompt(self):
        if self.current_section:
            s = '/'.join(self.current_section)
            if neotermcolor:
                s = neotermcolor.colored(s,
                                         color='yellow',
                                         attrs='bold',
                                         readline_safe=True)
            ps = '[{}]{}'.format(s, self.ps)
        else:
            ps = self.ps
        return ps

    def print_repeat_title(self, command, interval):
        import datetime
        t = datetime.datetime.now().strftime('%Y-%m-%d %T')
        if neotermcolor:
            command = neotermcolor.colored(command, color='yellow')
        print('{}  {}  (interval {} sec)'.format(t, command, interval))


ap = ArgumentParser(prog='' if len(sys.argv) < 2 else None)

sp = ap.add_subparsers(dest='_object', metavar='object', help='Object')

ap_user = sp.add_parser('user', help='Users')
sp_user_type = ap_user.add_subparsers(dest='_type',
                                      metavar='type',
                                      help='User object type')

ap_user_account = sp_user_type.add_parser('account', help='User accounts')
sp_user_account = ap_user_account.add_subparsers(dest='_command',
                                                 metavar='command',
                                                 help='Command')

sp_user_account_list = sp_user_account.add_parser('list',
                                                  help='List user accounts')

sp_user_account_add = sp_user_account.add_parser('add', help='Add user account')
sp_user_account_add.add_argument('account',
                                 metavar='ACCOUNT',
                                 help='Account name')

sp_user_account_delete = sp_user_account.add_parser('del',
                                                    help='Delete user account')

sp_user_account_delete.add_argument(
    'account', metavar='NAME', help='Account name').completer = ComplUsers()

ap_user_apikey = sp_user_type.add_parser('apikey', help='API keys')
sp_user_apikey = ap_user_apikey.add_subparsers(dest='_command',
                                               metavar='command',
                                               help='Command')

sp_user_apikey_list = sp_user_apikey.add_parser('list', help='List keys')

ap_document = sp.add_parser('document', help='Documents')
sp_document = ap_document.add_subparsers(dest='_command',
                                       metavar='command',
                                       help='Command')

sp_document_list = sp_document.add_parser('list', help='List documents')

ap.sections = {'user': ['account', 'apikey'], 'document': []}

for c in ('top', 'w', 'uptime'):
    ap.interactive_global_commands[c] = ap.syscmd

ap.interactive_history_file = '~/.test-icli'

#import io

# f = io.StringIO()
# f.write('user account list ; user apikey list\ndocument list')
# f.seek(0)
# ap.batch(f)

if len(sys.argv) > 1:
    ap.launch()
else:
    ap.interactive()
