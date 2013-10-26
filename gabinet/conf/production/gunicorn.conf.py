# Copyright 2013-present CodiLime. All Rights Reserved.

import multiprocessing


bind = u'127.0.0.1:8080'
workers = multiprocessing.cpu_count() * 2 + 1
timeout = 60
