import subprocess
import re
import util

cmd_encoding = util.get_chcp_code()
# 使用 powercfg 命令获取当前电源计划的 GUID
output = subprocess.check_output(['powercfg', '-getactivescheme'])
guid = output.decode(encoding=cmd_encoding).strip().split()[-1]
name = None
for line in output.decode(encoding=cmd_encoding).splitlines():
    print(line)
    if '电源方案' in line:
        name = line.split(':')[1].strip()
        name = name.split('(')[0].strip()
        break

# 输出当前电源计划的名称
if name is not None:
    print(f"当前电源计划id：{name}")
else:
    print("无法获取当前电源计划的名称。")