# coding: utf-8

import sys

from lib.hipchat import HipChat


config = {
    'token'        : str(sys.argv[1]),
    'room_id'      : str(sys.argv[2]),
    'from_name'    : str(sys.argv[3]),
    'message'      : str(sys.argv[4]),
    'color'        : str(sys.argv[5]),
    'notify'       : str(sys.argv[6]),
    'target_branch': str(sys.argv[7]),
    'build_branch' : str(sys.argv[8]),
}

is_post = False

if config['notify'] == 'true':
    notify = True
if not config['target_branch'] in config['build_branch']:
    is_post = False
if config['target_branch'] == 'all' or config['target_branch'] == config['build_branch']:
    is_post = True

if not is_post:
    print '''Build branch:{build_branch} is not a target of notification.
            target_branch: {target_branch}'''.format(
                build_branch  = config['build_branch'],
                target_branch = config['target_branch']
            )
    sys.exit(0)
