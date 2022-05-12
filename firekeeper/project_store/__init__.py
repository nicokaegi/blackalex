from firekeeper.settings import black_alex_path
import os

if (not os.path.isdir("{}/{}".format(black_alex_path,".trash"))):
    os.makedirs("{}/{}".format(black_alex_path,".trash"))
