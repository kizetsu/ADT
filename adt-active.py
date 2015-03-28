#!/usr/bin/env python3

import os
#import sys
#import json
#import config


# Update all Drupals
def update(Tree):
    for treeItem in Tree:
#        os.system('cd '+Tree[treeItem]['path']+';ls -la')
        if Tree[treeItem]['setup'] == "multisite":
            print('cd '+Tree[treeItem]['path']+'; drush cc drush')
            for site in Tree[treeItem]['sites']:
                print('cd '+Tree[treeItem]['path']+'; drush up --uri=', site)
        else:
            print('cd '+Tree[treeItem]['path']+'; drush cc drush')
            print('cd '+Tree[treeItem]['path']+'; drush up')


########################
#   Aufbau des Array   #
########################
#
#Tree = {
#    "drupal-test-dir": {
#        "setup": "multisite",
#        "path": "/var/www/drupal-test-dir",
#        "sites": [
#            "test2.drupal.com",
#            "test3.drupal.com",
#            "test.drupal.com"
#        ]
#    },
#    "drupal-test-dir2": {
#        "setup": "singlesite",
#        "path": "/var/www/drupal-test-dir2"
#    }
#}
