# print(10/0)
import traceback

try:
    print("------------------------")
    print(1 / 0)
except:
    traceback.print_exc()
# try except 语句自行理解
# 该程序目的是找到错误 报错正常
