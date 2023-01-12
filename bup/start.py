import sys
import time
import os

if __name__ == '__main__':
    cmd = os.environ['EXECUTE_CMD']
    print("cmd="+cmd)
    print("timeout="+os.environ['EXECUTE_TIMEOUT'])
    index = 1
    timeout = 3
    if os.environ['EXECUTE_TIMEOUT']:
        timeout = os.environ['EXECUTE_TIMEOUT']
    while True:
        print(f"执行第{index}次任务")
        os.system(cmd)
        # 休眠5分钟
        time.sleep(int(timeout) * 60)
        index = index + 1


