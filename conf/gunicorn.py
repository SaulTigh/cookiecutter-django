bind = 'unix:/tmp/projectname.sock'
pidfile = '/tmp/projectname.pid'
daemon = False
keepalive = 2
reload = False
raw_env = 'DJANGO_SETTINGS_MODULE=core.settings.production'

import os
import multiprocessing

workers = 2 * multiprocessing.cpu_count()
# threads = 3 * multiprocessing.cpu_count() # do not work

# logging
accesslog = '/var/log/projectname-project/gunicorn/access.log'
errorlog = '/var/log/projectname-project/gunicorn/error.log'

PROJDIR = os.path.abspath(os.path.join(os.path.basename(__file__), os.pardir, os.pardir))
chdir = os.path.abspath(os.path.join(PROJDIR, 'projectname'))
pythonpath = chdir
