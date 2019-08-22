import sys

def merger_maping ():
    # 1. read ILSVRC2012_mapping.txt
    mapping1 = {}
    text_file = open("./img_maping/ILSVRC2012_mapping.txt", "r")
    lines = text_file.read().split('\n')
    if lines[-1] == "":
        lines.pop()
    for line in lines:
        ILSVRC2012_label = line.split(' ', 1)[0]
        ILSVRC2012_mapping = line.split(' ', 1)[1]
        mapping1[ILSVRC2012_mapping] = ILSVRC2012_label
    
    # 2. read origin dictionary
    mapping2 = {}
    text_file = open("./img_maping/original_label.txt", "r")
    lines = text_file.read().split('\n')
    if lines[-1] == "":
        lines.pop()
    for line in lines:
        ILSVRC2012_mapping = line.split(' ', 1)[0]
        ILSVRC2012_classification = line.split(' ', 1)[1]
        mapping2[ILSVRC2012_classification] = ILSVRC2012_mapping

    # 3. read imagenet1000 dictionary
    mapping3 = {}
    text_file = open("./img_maping/imagenet1000_clsidx_to_labels.txt", "r")
    lines = text_file.read().split('\n')
    if lines[-1] == "":
        lines.pop()
    for line in lines:
        imagenet_label = line.split(' ', 2)[1]
        ILSVRC2012_classification = line.split(' ', 2)[2]
        mapping3[imagenet_label] = ILSVRC2012_classification

    # 4. merger mapping, create file
    my_map = {}
    ff = open("my_maping.txt", 'w+')
    for i in range(1000):
        iamgnet100_label = str(i)
        ILSVRC2012_classification = mapping3[iamgnet100_label]
        ILSVRC2012_mapping =  mapping2[ILSVRC2012_classification]
        ILSVRC2012_label =  mapping1[ILSVRC2012_mapping]
        print(iamgnet100_label, ILSVRC2012_label, ILSVRC2012_mapping, ILSVRC2012_classification)
        content = "%s %s %s %s \n"%(iamgnet100_label, ILSVRC2012_label, ILSVRC2012_mapping, ILSVRC2012_classification)
        ff.write(content)
        my_map[ILSVRC2012_label] = iamgnet100_label
    ff.close()
    return my_map


def create_new_val_lables(my_map_file, labals_file):
    fi = open(my_map_file, 'r+')
    fi_lines = fi.readlines()
    if fi_lines[-1] == "":
        fi_lines.pop()
    my_map = {}
    for line in fi_lines:
        index = line.split(" ")[0]
        temp = line.split(" ")[1]
        my_map[temp] = index
    print(my_map)

    fo = open("my_label.txt", "w+")
    text_file = open(labals_file, "r")
    lines = text_file.read().split('\n')
    if lines[-1] == "":
        lines.pop()
    
    for line in lines:
        print(line)
        fo.write(my_map[line] + '\n')
    fo.close()


if __name__ == '__main__':
    
    label_file = "./img_maping/ILSVRC2012_validation_ground_truth.txt"
    merger_maping()
    create_new_val_lables("my_maping.txt", label_file)

    

