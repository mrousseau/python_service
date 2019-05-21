#!\usr\bin\python
# -*- coding: utf8 -*

import os
import sys
import logging

# print("------> ")
# if len(sys.argv) > 1:
#     print( "count : %s" % len(sys.argv))
#     print("table : ")
#     for arg in sys.argv:
#         print("* %s" % arg)

logging.basicConfig(filename='./commit_pi.log',level=logging.DEBUG,\
              format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')

#recherche des parameters
if len(sys.argv) > 1:
    for param in sys.argv:
        logging.info("* %s" % param )
        if "--prj" in param:
            result = param.replace("--prj=", "")
            logging.info("find param project %s" %result )
        elif "--dest" in param:
            result = param.replace("--dest=", "")
            logging.info("find param destination %s" %result )




for dossier, sous_dossiers, fichiers in os.walk('.'):
    for fichier in fichiers:
        filePath = os.path.abspath(fichier)
        print(filePath)
