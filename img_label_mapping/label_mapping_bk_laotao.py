original_label = []
damn_order = [62,92,54,53,36,25,63,0,65,8,68,55,1,58,96,44,85,61,38,91,84,82,87,73,9,72,32,47,30,71,48,69,23,51,16,39,49,24,70,74,81,6,83,88,79,14,45,86,28,27,50,40,60,3,10,94,97,19,80,11,93,64,18,43,34,22,21,17,2,76,15,75,56,46,98,13,37,67,52,7,33,59,5,90,57,20,66,77,12,95,26,4,35,78,41,31,99,89,29,42]


def get_train_labels():
    "to do"
    # 1. read ILSVRC2012_mapping.txt
    text_file = open("./data/ILSVRC2012_mapping.txt", "r")
    lines = text_file.read().split('\n')

    # 2. read origin dictionary
    text_file = open("./data/original_label.txt", "r")
    original_label_to_meaning_list = text_file.read().split('\n')
    original_label_to_meaning_dict = {}
    for line in original_label_to_meaning_list:
        if len(line.split(' ', 1)) > 1:
            key = line.split(' ', 1)[0]
            val = line.split(' ', 1)[1]
            original_label_to_meaning_dict[key] = val

    # 3. meaning to common dictionary
    text_file = open("./data/imagenet1000_clsidx_to_labels.txt", "r")
    meaning_to_common_label_list = text_file.read().split('\n')
    meaning_to_common_label_dict = {}
    for line in meaning_to_common_label_list:
        if len(line.split(' ', 1)) > 1:
            key = line.strip().split(' ', 1)[1]
            val = line.strip().split(' ', 1)[0]
            meaning_to_common_label_dict[key] = val

    common_label_lists = []
    for i in range(100):
        original_label = lines[i].split(' ')[1]
        meaning = original_label_to_meaning_dict[original_label]
        common_label = meaning_to_common_label_dict[meaning]
        common_label_lists.append(int(common_label))
    return common_label_lists, original_label_to_meaning_dict, meaning_to_common_label_dict


def label_to_common(common_label_lists, output_idx):
    #common_labels = []
    didx = damn_order[output_idx]
    common_labels=common_label_lists[didx]
    '''
    for idx in output_idx:
        didx = damn_order[idx]
        common_labels.append(common_label_lists[didx])
    '''
    return common_labels


def main():
    common_label_lists, original_label_to_meaning_dict, meaning_to_common_label_dict= get_train_labels()
    
    print('Num of labels: ', len(common_label_lists))
    print('Selected common labels: ', common_label_lists)


if __name__ == '__main__':
    main()


