"""
Description : Example of using Drain3 to process a real world file
Author      : David Ohana
Author_email: david.ohana@ibm.com
License     : MIT
"""
import json
import logging
import os
import pathlib
import subprocess
import sys
import time
from pathlib import Path

from drain3 import TemplateMiner
from drain3.file_persistence import FilePersistence

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.ERROR,
                    format='%(message)s')

rootPath = str(Path(sys.argv[0]).parent)
dataPath = rootPath+"/data"
configPath = rootPath+"/config"
dataDir = Path(dataPath)
if not dataDir.is_dir():
    os.mkdir(dataPath)
parserKey = sys.argv[1]
fileName = sys.argv[2]
persistence = FilePersistence(dataPath+"/"+parserKey+".bin")

if Path(configPath+"/"+parserKey+".ini").exists():
    template_miner = TemplateMiner(
        persistence, configPath+"/"+parserKey+".ini")
else:
    template_miner = TemplateMiner(persistence, configPath+"/drain3.ini")

reply = open(fileName+"_reply", "a+", encoding='utf-8')
with open(fileName, encoding='utf-8') as f:
    for line in f:
        result = template_miner.add_log_message(line)
        result_json = json.dumps(result)
        reply.write(result_json+"\n")
print(str(Path(fileName+"_reply")), end='')
reply.close()
