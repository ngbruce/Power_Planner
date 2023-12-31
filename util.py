import subprocess
import re

list_plans = []
# fixed_plan_guid_name = "SCHEME_BALANCED"
new_plan_guid=""
dict_lid_option =  {
    0 : '不执行任何操作',
    1 : '睡眠',
    2 : '休眠',
    3 : '关机'
}
# 读取命令行默认编码
def get_chcp_code():
    # 使用 chcp 命令获取当前控制台编码格式
    byte_array = subprocess.check_output('chcp', shell=True)
    if __name__ == '__main__':
        print(byte_array)
    # 找到冒号和回车符的位置
    colon_index = byte_array.index(b':')
    cr_index = byte_array.index(b'\r')
    # 提取数字部分
    number_str = byte_array[colon_index + 2:cr_index].decode()
    return number_str


# 读取系统电源计划，返回一个列表
def get_pwr_plans():
    list_plans= []
    cmd_encoding = get_chcp_code()
    # 使用 powercfg 命令获取当前电源计划的 GUID
    output = subprocess.check_output(['powercfg', '-L'])
    output = output.decode(encoding=cmd_encoding)
    output = output.splitlines()
    name = None
    for line in output:
        # print("一行: ",line)
        if '电源方案' in line:
            # guid = line.split(':')[1].strip()
            # guid = guid.split('(')[0].strip()
            # name = line.split('(')[1].strip()
            # name = name.split(')')[0].strip()
            # active = line.split('(')[1].strip().split(')')[1].strip()
            # # print(f"guid={guid} , name={name}, star={active}")
            # element={'name': name, 'guid':guid,'active':True if active == '*' else  False}
            # if __name__ == '__main__':
            #     print(element)
            # list_plans.append(element)

            # 使用正则表达式匹配符合要求的行
            # match = re.match(r"电源方案 GUID:\s*(?P<guid>[a-f\d-]+)\s+\((?P<name>.*?)\)(?P<active>\s+\*)?", line)
            match = re.match(r"电源方案 GUID:\s*(?P<guid>[a-f\d-]+)\s+\((?P<name>[^()]+(\([^\)]*\)[^()]*)*)\)(?P<active>\s+\*)?", line)
            if match:
                # 如果匹配成功，提取 GUID、名称和是否为推荐方案的信息
                guid = match.group("guid")
                name = match.group("name")
                active = "*" if match.group("active") else ""
                # 打印提取的信息
                # print(f"GUID: {guid}, 名称: {name}{active}")
                element={'name': name, 'guid':guid,'active':True if active == '*' else  False}
                if __name__ == '__main__':
                    print(element)
                list_plans.append(element)
    return list_plans


def set_pwr_plans(guid: str):
    global new_plan_guid
    new_plan_guid = guid
    # 构造 powercfg 命令
    command = f"powercfg /setactive {guid}"
    # 调用 powercfg 命令
    subprocess.run(command, shell=True)
    # 输出结果
    print(f"已选择使用电源计划 {guid}")


# 提示用户选择和激活电源计划
def select_pwr_plan():
    global list_plans
    list_plans = get_pwr_plans()
    print("选择电源计划\n--------------------")
    # 输出列表
    for i, plan in enumerate(list_plans, start=1):
        print(f"{i}. {plan['name']}  {'*活动*' if plan['active'] else ''}")
    # 选择方案
    selected_index = None
    while selected_index is None:
        try:
            input_str = input("--------------------\n选择一个方案编号 (输入为空则退出) ：")
            if input_str.strip() == '':
                return False
            selected_index = int(input_str)
            if selected_index < 1 or selected_index > len(list_plans):
                raise ValueError
        except ValueError:
            print("输入的编号无效，请重新输入")
            selected_index = None
    # 输出 GUID
    selected_plan = list_plans[selected_index - 1]
    print(f"你选择的方案的 GUID 是：{selected_plan['guid']}")
    set_pwr_plans(selected_plan['guid'])
    return True

def set_lid(idx:int = 0, pwr:str="ac"):
    command = "powercfg -set" + pwr + \
              "valueindex "+"SCHEME_CURRENT"+" 4f971e89-eebd-4455-a8de-9e59040e7347 5ca83367-6e45-459f-a27b-476b1d01c936 " + \
              str(idx)
    print(f"命令为 {command}")
    subprocess.run(command, shell=True)
    command = "powercfg -SetActive SCHEME_CURRENT"
    subprocess.run(command, shell=True)
    # for item in list_plans:
    #     command = "powercfg -set" + pwr + \
    #               "valueindex " + item['guid'] + \
    #               " 4f971e89-eebd-4455-a8de-9e59040e7347 5ca83367-6e45-459f-a27b-476b1d01c936 " + \
    #               str(idx)
    #     print(f"命令为 {command}")
    #     subprocess.run(command, shell=True)


# 提示用户选择关闭盖子操作
def select_lid():
    # 输出列表
    # for i, plan in enumerate(dict_lid_option, start=0):
    #     print(f"{i}. {plan}")2
    print("--------------------\n选择关闭笔记本盖子的操作\n--------------------")
    for key in sorted(dict_lid_option):
        print(f"{key}: {dict_lid_option[key]}")
    # 选择方案
    selected_index = None
    while selected_index is None:
        try:
            input_str = input("--------------------\n请选择一个方案的编号(输入为空则退出)：")
            if input_str.strip() == '':
                return 
            selected_index = int(input_str)
            if selected_index < 0 or selected_index >= len(dict_lid_option):
                raise ValueError
        except ValueError:
            print("输入的编号无效，请重新输入")
            selected_index = None
    # 输出 GUID
    selected_plan = dict_lid_option[selected_index ]
    print(f"你选择的方案是：{selected_plan} , idx={selected_index}")
    set_lid(selected_index, "ac")


if __name__ == '__main__':
    list_plans = get_pwr_plans()
    print (f"got list: \n{list_plans}\n==================\n")
    # set_lid(3,"ac")
    select_lid()


