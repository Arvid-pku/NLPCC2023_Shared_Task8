# encoding=utf-8
import argparse
import os
parser = argparse.ArgumentParser(description='GEC OpenNMT Service',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--gold_file', default='test1.txt',help='input file path')
parser.add_argument('--modelout_file', default='test2.txt',help='input file path')
opt = parser.parse_args()



def char_D(sentences):
    total = 0  # 总的句子数
    cor = 0  # 正确识别错误的句子数
    al_wro = 0  # 算法识别为“有错误”的句子数
    wro = 0  # 语料中所有错误句子数
    k = 0
    for sentence in sentences:
        k += 1
        total += 1
        lines0 = sentence[0]
        lines1 = sentence[1]
        lines2 = sentence[2]
        if len(lines0) != len(lines1) or len(lines1) != len(lines2):
            print(f"文本长度不一致")
            print(sentence)
        lines_list = [[lines0[i], lines1[i], lines2[i]] for i in range(min(len(lines0), len(lines1), len(lines2)))]
        for char_list in lines_list:
            if char_list[0] != char_list[1] and char_list[0] != char_list[2]:
                cor += 1
            if char_list[0] != char_list[1]:
                wro += 1
            if char_list[0] != char_list[2]:
                al_wro += 1

    try:
        precision = round((cor / al_wro) * 100, 2)
    except:
        precision = "-"
    try:
        recall = round((cor / wro) * 100, 2)
    except:
        recall = "-"
    try:
        f1 = round(precision * recall * 2 / (precision + recall), 2)
    except:
        f1 = "-"

    print(f"char_detect_precision：{precision}({cor}/{al_wro})")
    print(f"char_detect_recall：{recall}({cor}/{wro})")
    print(f"char_detect_F1：{f1}")



def char_C(sentences):
    total = 0  # 总的句子数
    TP = 0  # 正确识别错误的句子数
    FP = 0  # 非错别字被误报为错别字
    FN = 0  # 错别字未能正确识别错别字
    k = 0
    for sentence in sentences:
        k += 1
        total += 1
        lines0 = sentence[0]
        lines1 = sentence[1]
        lines2 = sentence[2]
        lines_list = [[lines0[i], lines1[i], lines2[i]] for i in range(min(len(lines0), len(lines1), len(lines2)))]
        for char_list in lines_list:
            if char_list[0] != char_list[1] and char_list[1] == char_list[2]:
                TP += 1
            if char_list[2] != char_list[1] and char_list[0] != char_list[2]:
                FP += 1
            if char_list[0] != char_list[1] and char_list[1] != char_list[2]:
                FN += 1

    al_wro = TP + FP
    wro = TP + FN
    cor = TP
    try:
        precision = round((cor / al_wro) * 100, 2)
    except:
        precision = "-"
    try:
        recall = round((cor / wro) * 100, 2)
    except:
        recall = "-"
    try:
        f1 = round(precision * recall * 2 / (precision + recall), 2)
    except:
        f1 = "-"
    print(f"char_correct_precision：{precision}({cor}/{al_wro})")
    print(f"char_correct_recall：{recall}({cor}/{wro})")
    print(f"char_correct_F1：{f1}")



def sentence_FPR(sentences):
    all_num = 0
    cuo = 0
    for sentence in sentences:
        if sentence[0] == sentence[1]:
            all_num += 1
            if sentence[0] != sentence[2]:
                cuo += 1
    if all_num == 0:
        fpr = "-"
    else:
        fpr = f"{cuo/all_num*100:.2f}({cuo}/{all_num})"
    print(f"sentence_FPR：{fpr}")


def main():
    sents = {}
    flag = False  # 是否有句子异常
    with open(opt.gold_file, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            lines = line.replace("\n", '').split("\t")
            if "原文" in lines[0] and i == 0:
                continue
            sents[lines[0]] = [lines[0], lines[1]]
    with open(opt.modelout_file, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            lines = line.replace("\n", '').split("\t")
            if "原文" in lines[0] and i == 0:
                continue
            if len(lines[0]) != len(lines[1]):
                flag = True
                print(f"Input and Output have different lengths. Input is {lines[0]}")
                break
            try:
                sents[lines[0]].append(lines[1])
            except:
                flag = True
                print(f"Can't find the gold, maybe the input is wrong. Input is {lines[0]}")
                break
    if not flag:
        sentences = []
        for value in sents.values():
            if len(value) < 3:
                sentences.append([value[0], value[1], value[0]])
            else:
                sentences.append([value[0], value[1], value[2]])

        sentence_FPR(sentences)
        char_D(sentences)
        char_C(sentences)


if __name__ == '__main__':
    main()


