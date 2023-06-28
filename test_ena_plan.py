import subprocess

# 定义电源计划的 GUID
guid = "cc8b826a-3de8-47ef-b7ae-4f29d28c01eb"

# 构造 powercfg 命令
command = f"powercfg /setactive {guid}"

# 调用 powercfg 命令
subprocess.run(command, shell=True)

# 输出结果
print(f"已选择使用电源计划 {guid}。")