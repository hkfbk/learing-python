import sys
import os
# 将项目根目录添加到 sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)
from RunTime import runtime # type: ignore
from func import run as func_run
from vector import run as list_run
from dictionary import run as dic_run
from comprehensive import run







def main():
    run()






















if __name__ == '__main__':
    main()