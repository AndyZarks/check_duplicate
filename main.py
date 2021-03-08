import re


def pre(filename: str) -> list:
    lines = open(filename, encoding='utf8').readlines()
    wordlist = []
    c_plus_keyword = open("c++keyword.txt").read()
    keyword_list = c_plus_keyword.split()
    for i in range(lines.__len__()):
        lines[i] = re.sub('//.*$|#.*$|[(){};,\"\']', ' ', lines[i])
        for word in lines[i].split():
            word = word.strip()
            if word not in keyword_list and word != '':
                wordlist.append(word)
    return wordlist


def check(source: list, target: list, factor: int):
    full_length = source.__len__()
    repeated_words = 0
    repeated_words_list = []
    i = 0
    while i != full_length - 1:
        try:
            index = target.index(source[i])
        except ValueError:
            i += 1
        else:
            list_pop = []
            matched_words = 0
            while source[i] == target[index]:
                list_pop.append(target.pop(index))
                matched_words += 1
                if i + 1 < full_length:
                    i += 1
                else:
                    break
            if matched_words >= factor:
                repeated_words += matched_words
                repeated_words_list.append(list_pop)
    ratio = repeated_words * 100 / full_length
    print("重复率为: {:.3f}%".format(ratio))
    print("重复的段落为: ")
    for sentence in repeated_words_list:
        print(sentence)


file1 = pre('bubble_sort.txt')
file2 = pre('bubble_sort_better.txt')
dp_factor = int(input("请输入重复率检测的阈值(连续重复的字数):"))
check(file1, file2, dp_factor)
