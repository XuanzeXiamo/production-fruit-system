# -*- coding: utf-8 -*-
"""
水果识别系统（产生式推理）
在原动物识别框架上直接替换知识内容
"""

# ---------- 工具 ----------
def judge_repeat(value, lst=None):
    """判重：value 是否已在 lst 中"""
    if lst is None:
        lst = []
    return 1 if value in lst else 0

# ---------- 最终判定 ----------
def judge_last(lst):
    """
    根据综合数据库 lst 给出最终水果
    规则写法：if 特征/中间结论 in lst -> 水果
    顺序：先匹配先生效
    """
    # 苹果
    if '1' in lst and ('7' in lst or '11' in lst) and '13' in lst and '19' in lst \
       and '22' in lst and '29' in lst:
        print("红色系 + 圆形/扁圆 + 极光滑 + 中小型 + 明显果核 + 核果类 -> 苹果\n")
        print("所识别的水果为苹果")
        return

    # 香蕉
    if '2' in lst and '9' in lst and '13' in lst and '24' in lst and '25' in lst:
        print("黄色系 + 月牙形 + 极光滑 + 可剥皮 + 热带水果 -> 香蕉\n")
        print("所识别的水果为香蕉")
        return

    # 西瓜
    if '3' in lst and ('7' in lst or '8' in lst) and '16' in lst and '20' in lst and '21' in lst:
        print("绿色系 + 圆/长椭圆 + 有条纹 + 大型 + 多汁 -> 西瓜\n")
        print("所识别的水果为西瓜")
        return

    # 橙子
    if '4' in lst and '7' in lst and '14' in lst and '19' in lst and '24' in lst and '28' in lst:
        print("橙黄色 + 正圆 + 粗糙凹坑 + 中小型 + 可剥皮 + 柑橘类 -> 橙子\n")
        print("所识别的水果为橙子")
        return

    # 草莓
    if '1' in lst and '10' in lst and '17' in lst and '23' in lst and '19' in lst and '27' in lst:
        print("红色系 + 圆锥形 + 颗粒突起 + 种子在表面 + 中小型 + 浆果类 -> 草莓\n")
        print("所识别的水果为草莓")
        return

    # 葡萄
    if ('5' in lst or '1' in lst) and '7' in lst and '12' in lst and '18' in lst and '13' in lst and '27' in lst:
        print("紫红/红色 + 正圆 + 成串珠状 + 单果极小 + 极光滑 + 浆果类 -> 葡萄\n")
        print("所识别的水果为葡萄")
        return

    # 芒果
    if '2' in lst and '8' in lst and '13' in lst and '19' in lst and '22' in lst and '24' in lst and '25' in lst:
        print("黄色系 + 长椭圆 + 极光滑 + 中小型 + 明显果核 + 可剥皮 + 热带水果 -> 芒果\n")
        print("所识别的水果为芒果")
        return

    print("\n根据所给条件无法判断为何种水果")

# ---------- 知识库 ----------
dict_before = {
    # 颜色
    '1': '红色系', '2': '黄色系', '3': '绿色系', '4': '橙黄色', '5': '紫红色', '6': '粉红色带白点',
    # 形状
    '7': '正圆形', '8': '长椭圆形', '9': '月牙形', '10': '圆锥形', '11': '扁圆形', '12': '成串珠状',
    # 表皮
    '13': '表皮极光滑', '14': '表皮粗糙有凹坑', '15': '表皮有绒毛', '16': '表皮有规则条纹', '17': '表皮有颗粒状突起',
    # 大小
    '18': '单果极小', '19': '中小型', '20': '大型',
    # 内部
    '21': '果肉多汁', '22': '有明显果核', '23': '种子在表面', '24': '可剥皮',
    # 中间分类
    '25': '热带水果', '26': '温带水果', '27': '浆果类', '28': '柑橘类', '29': '核果类',
    # 最终结果
    '30': '苹果', '31': '香蕉', '32': '西瓜', '33': '橙子', '34': '草莓', '35': '葡萄', '36': '芒果'
}

# ---------- 交互 ----------
print("""输入对应条件前面的数字:
***********************************************************************************
* 颜色: 1红色系 2黄色系 3绿色系 4橙黄色 5紫红色 6粉红白点                          *
* 形状: 7正圆 8长椭圆 9月牙形 10圆锥形 11扁圆 12成串珠状                          *
* 表皮: 13极光滑 14粗糙凹坑 15有绒毛 16有条纹 17颗粒突起                          *
* 大小: 18单果极小 19中小型 20大型                                                *
* 内部: 21多汁 22明显果核 23种子在表面 24可剥皮                                  *
* 中间: 25热带水果 26温带水果 27浆果类 28柑橘类 29核果类                          *
***********************************************************************************
************************* 输入 0 结束并给出结论 ************************************
""")

# 综合数据库
list_real = []
while True:
    num_real = input("请输入：").strip()
    if num_real == '0':
        break
    if num_real not in dict_before:
        print("编号无效，请重新输入")
        continue
    list_real.append(num_real)

print("\n前提条件为：", end="")
for i in range(len(list_real) - 1):      # 去掉最后的'0'
    print(dict_before[list_real[i]], end=" ")
print("\n\n推理过程如下：")

# ---------- 第一层：单条件/简单组合 ----------
for i in list_real:
    # 热带水果
    if i == '9' and '2' in list_real and judge_repeat('25', list_real) == 0:
        list_real.append('25')
        print("月牙形 + 黄色系 -> 热带水果")
    # 核果类
    if i == '7' and '1' in list_real and '13' in list_real and judge_repeat('29', list_real) == 0:
        list_real.append('29')
        print("正圆形 + 红色系 + 极光滑 -> 核果类")
    # 柑橘类
    if i == '4' and '14' in list_real and judge_repeat('28', list_real) == 0:
        list_real.append('28')
        print("橙黄色 + 粗糙凹坑 -> 柑橘类")
    # 浆果类（葡萄路径）
    if i == '12' and '18' in list_real and judge_repeat('27', list_real) == 0:
        list_real.append('27')
        print("成串珠状 + 单果极小 -> 浆果类")
    # 浆果类（草莓路径）
    if i == '17' and '10' in list_real and judge_repeat('27', list_real) == 0:
        list_real.append('27')
        print("颗粒突起 + 圆锥形 -> 浆果类")

# ---------- 第二层：复杂组合 ----------
for i in list_real:
    # 芒果推导（长椭圆+黄+可剥 → 热带）
    if i == '8' and '2' in list_real and '24' in list_real and judge_repeat('25', list_real) == 0:
        list_real.append('25')
        print("长椭圆形 + 黄色系 + 可剥皮 -> 热带水果")

# ---------- 最终判定 ----------
judge_last(list_real)