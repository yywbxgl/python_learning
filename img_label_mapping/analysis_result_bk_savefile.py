import os, sys
import json
import re

def read_one_output_file():
    file_name = "img_test_output/img_00_500_output_json/ILSVRC2012_val_00000014.jpg_ss.json"
    fo = open(file_name, 'rb')
    content = fo.read()
    content = str(content)
    print(content)
    begin = content.find("[[")
    print(begin)
    end = content.rfind("]]")
    print(end)
    top6 = content[begin+2:end]
    print(top6)
    tops = top6.split(",[")
    tops.pop()
    print(tops)
    wirte_data = ""
    for top in tops:
        wirte_data = wirte_data + top.split(',',1)[0] + ' '
    print(wirte_data)


def read_all_output_file(input_dir, output_name):
    files= os.listdir(input_dir) #得到文件夹下的所有文件名称
    files.sort()
    out_file = open(output_name + '.txt', "w+")
    for f in files:
        print(f)
        fin = open(input_dir + f, 'rb')
        content = fin.read()
        content = str(content)
        begin = content.find("[[")
        end = content.rfind("]]")
        top6 = content[begin+2:end]
        tops = top6.split(",[")
        tops.pop()
        # wirte_data = f.split('.')[0].split('_')[-1] + "  "
        wirte_data = f + " "
        # wirte_data = ""
        for top in tops:
            wirte_data = wirte_data + top.split(',',1)[0] + ' '
        print(wirte_data)
        out_file.write(wirte_data + '\n')
        fin.close()
    out_file.close()


def add_grey_index():
    ff = open("11.txt", "r")
    fout = open("22.txt", "w+")
    append = [34,107,118,126,141,296,317,377,392,429]
    for i in range(1,500):
        if i in append:
            print("write...")
            fout.write("\n")
        else:
            temp = ff.readline()
            # print("write ", temp)
            fout.write(temp)

    ff.close()
    fout.close()


def analyze_accuracy(result_file, label_file):
    f_val_label = open(label_file, "r")
    f_ret = open(result_file, 'r')

    results = f_ret.readlines()
    if results[-1] == "":
        results.pop()

    total_num = len(results)
    print("total: ", total_num)
    blank_num = 0
    top1_num = 0
    top5_num = 0

    val_labels = f_val_label.readlines()
    for val_label in val_labels:
        val_label = val_label.strip('\n')

    print(len(val_labels))

    for i, result in enumerate(results):
        # print(i , result)
        if result == '\n':
            print("blank", i+1)
            blank_num += 1
            continue
        infrenced = result.split("json")[-1].strip("\n")
        label = val_labels[i].strip("\n")
        infrenced_top1 = infrenced.split(" ")[1]
        # print(infrenced_top1)
        top1 = "False"
        top5 = "False"
        if label in infrenced:
            top5 = "True"
            top5_num += 1
        if label in infrenced_top1:
            top1 = "True"
            top1_num += 1
        
        temp = "pic[%d]  result[%s]  lable[%s]  top1[%s]  top5[%s]"%(i + 1, infrenced, label, top1, top5)
        print(temp)
    
    print("total: ", total_num)
    print("no result: ", blank_num)
    print("top1 hit: ", top1_num)
    print("top5 hit: ", top5_num)
    print("top1_accuracy_rate: ", top1_num/(total_num-blank_num))
    print("top5_accuracy_rate: ", top5_num/(total_num-blank_num))

if __name__ == "__main__":
    if len(sys.argv) !=3:
        print("Usage: ", sys.argv[0], " input_json_path  output_file_name")
        sys.exit(-1)
    
    # read_all_output_file(sys.argv[1], sys.argv[2])
    # add_grey_index()

    analyze_accuracy(sys.argv[2] + '.txt', "my_label.txt")

