import pandas as pd
import os
def fofa_wj(txt, lx):
    ret = os.path.exists(fr'./{txt}.xlsx')
    if ret:
        if int(lx) == 1 or int(lx) == 2:
            txt1 = txt
            list = shujuchuli(txt)
            if int(lx) == 1:
                txt_os(list, txt1)
            else:
                ywjbc(list,txt1)
        else:
            print("编号输入错误")
    else:
        print('输入的文件不存在！！！')

def shujuchuli(txt):
    path = fr'./{txt}.xlsx'
    # 使用第二行为列索引
    data = pd.read_excel(path, header=2)
    # 删除指定列里面的复合条件的数据,inplace=true 直接修改原dataFrame
    data = data.drop(data[data['banner'] == 'rums/b'].index)
    data = data.drop_duplicates(['ip', '端口'])
    ip_s = list(data['ip'])
    dk_s = list(data['端口'])
    list_s = []
    for i in range(len(ip_s)):
        list_s.append(str(ip_s[i]) + ':' + str(dk_s[i]) + '\n')
    return list_s

def txt_os(data, txt):  # 存储为txt
    # 创建以文件夹
    if not os.path.isdir(fr'./ip'):
        os.makedirs("./ip")
    file = open(f'./ip/{txt}.txt', 'w', encoding="utf8")
    for i in range(len(data)):
        file.writelines(data[i])
    file.close()
    print("成功")

def ywjbc(data,txt):  # 存储为源文件
    # 保存修改的excel文件
    # data.to_excel('文件名',index=false)
    if not os.path.isdir(fr'./ip'):
        os.makedirs("./ip")
    file = open(f'./ip/{txt}.xlsx', 'w', encoding="utf8")
    for i in range(len(data)):
        file.writelines(data[i])
    file.close()
    print("成功")

if __name__ == '__main__':
    txt = input("请输入需提取ip文件名：")
    lx = input("请输入【编号】保存的文件类型【编号1：txt】 【编号2：xlsx】：")
    fofa_wj(txt, lx)
