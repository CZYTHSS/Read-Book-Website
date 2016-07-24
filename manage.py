#!/usr/bin/env python
import os
import sys
from imp import reload

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
    reload(sys) 
    #sys.setdefaultencoding('gb18030')#否则加载css文件仍会出错