import json
import logging
import os
import sys
from pathlib import Path

from drain3 import TemplateMiner
from drain3.file_persistence import FilePersistence

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format='%(message)s')

rootPath = str(Path(sys.argv[0]).parent)
dataPath = rootPath+"/data"
configPath = rootPath+"/config"
dataDir = Path(dataPath)
if not dataDir.is_dir():
    os.mkdir(dataPath)
persistence = FilePersistence(dataPath+"/"+sys.argv[1]+".bin")

template_miner = TemplateMiner(persistence, configPath+"/"+sys.argv[1]+".ini")

result = template_miner.add_log_message(sys.argv[2])
result_json = json.dumps(result)
print(result_json)
