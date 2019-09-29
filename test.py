#!/usr/bin/env python3

import icli

ap = icli.ArgumentParser(prog='')

sp = ap.add_subparsers(dest='_object', metavar='object', help='Object')

ap_account = sp.add_parser('account', help='Accounts')
sp_account_type = ap_account.add_subparsers(dest='_type',
                                            metavar='type',
                                            help='Account type')

ap_account_bank = sp_account_type.add_parser('bank', help='Bank accounts')
sp_account_bank = ap_account_bank.add_subparsers(dest='_command',
                                                 metavar='command',
                                                 help='Command')

sp_account_bank_list = sp_account_bank.add_parser('list', help='List accounts')

sp_account_bank_add = sp_account_bank.add_parser('add', help='Add account')
sp_account_bank_add.add_argument('account',
                                 metavar='ACCOUNT',
                                 help='Account name')

sp_account_bank_delete = sp_account_bank.add_parser('del',
                                                    help='Delete account')

sp_account_bank_delete.add_argument('account',
                                    metavar='ACCOUNT',
                                    help='Account ID or name')

ap_account_cash = sp_account_type.add_parser('cash', help='Cash accounts')
sp_account_cash = ap_account_cash.add_subparsers(dest='_command',
                                                 metavar='command',
                                                 help='Command')

sp_account_cash_list = sp_account_cash.add_parser('list', help='List accounts')

sp_account_cash_add = sp_account_cash.add_parser('add', help='Add account')
sp_account_cash_add.add_argument('account',
                                 metavar='ACCOUNT',
                                 help='Account name')

sp_account_cash_delete = sp_account_cash.add_parser('del',
                                                    help='Delete account')

sp_account_cash_delete.add_argument('account',
                                    metavar='ACCOUNT',
                                    help='Account ID or name')

ap_invoice = sp.add_parser('invoice', help='Invoice')
sp_invoice = ap_invoice.add_subparsers(dest='_command',
                                       metavar='command',
                                       help='Command')

sp_invoice_list = sp_invoice.add_parser('list', help='List invoices')

ap.sections = {'account': ['bank', 'cash'], 'invoice': []}


def syscmd(cmd):
    import os
    os.system(cmd)


def error():
    print('error')


for c in ('top', 'w', 'uptime'):
    ap.interactive_global_commands[c] = syscmd

ap.handle_interactive_exception = error
ap.interactive_history_file = '~/.test-icli'
ap.interactive()
