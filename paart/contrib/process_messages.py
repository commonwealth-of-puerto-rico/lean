#!/usr/bin/env python
import sys
import os
import optparse

import sh

APP_LIST = ('acls', 'agencies', 'common', 'data', 'dynamic_search', 'infrastructure',
    'main', 'navigation', 'permissions', 'projects', 'project_setup', 'project_tools',
    'smart_settings', 'telecomm', 'tools', 'user_management', 'web_theme', 'workflows')
LANGUAGE_LIST = ('en', 'es')

makemessages = sh.Command('django-admin.py')
makemessages = makemessages.bake('makemessages')

compilemessages = sh.Command('django-admin.py')
compilemessages = compilemessages.bake('compilemessages')

if hasattr(sys, 'real_prefix'):
    # We are inside a virtual env
    BASE_DIR = os.path.join(os.environ['VIRTUAL_ENV'], '..', 'paart')
else:
    BASE_DIR = os.getcwd()


def process(command, app_list, language_list):
    if command == makemessages:
        print 'Making messages'
    elif command == compilemessages:
        print 'Compiling messages'

    for app in app_list:
        print 'Processing app: %s...' % app
        app_path = os.path.join(BASE_DIR, 'apps', app)
        os.chdir(app_path)
        for lang in language_list:
            print 'Doing language: %s' % lang
            command(locale=lang)


if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-m', '--make', help='create message sources file', dest='make', default=False, action='store_true')
    parser.add_option('-c', '--compile', help='compile message files', dest='compile', default=False, action='store_true')
    parser.add_option('-a', '--app', help='specify which app to process', dest='app', action='store', metavar='appname')
    parser.add_option('-l', '--lang', help='specify which language to process', dest='lang', action='store', metavar='language')
    (opts, args) = parser.parse_args()

    if not opts.make and not opts.compile:
        parser.print_help()

    if opts.app:
        app_list = [opts.app]
    else:
        app_list = APP_LIST

    if opts.lang:
        language_list = [opts.lang]
    else:
        language_list = LANGUAGE_LIST

    if opts.make:
        process(makemessages, app_list, language_list)
    elif opts.compile:
        process(compilemessages, app_list, language_list)
