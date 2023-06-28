import subprocess
import util

cmd_encoding = util.get_chcp_code()
# 构造 powercfg 命令，获取电源选项设置
command = "powercfg /q"

# 调用 powercfg 命令，并获取输出结果
result = subprocess.run(command, shell=True, capture_output=True)
print("====================")
print(result)
print("====================")
# 将输出结果转换为字符串，并提取关闭盖子时的操作设置
output_str = result.stdout.decode(encoding=cmd_encoding)
print("====================")
print(output_str)
print("====================")
index = output_str.find("盖子")
if index != -1:
    setting_str = output_str[index:].split("\n")[0].split(":")[1].strip()
    print(f"关闭笔记本盖子时的操作设置：{setting_str}")
else:
    print("未找到关闭笔记本盖子时的操作设置。")