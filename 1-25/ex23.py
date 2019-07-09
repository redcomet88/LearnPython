import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)  #递归

def print_line(line, encoding, errors):
    next_lang = line.strip()   #去掉\n
    #这里书上的代码有问题？ 我们得调试一下、
    #好吧，是我打错了！！！
    print(f"Debug: encoding =  {encoding}.")
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding = "utf-8")

main(languages, encoding, error)