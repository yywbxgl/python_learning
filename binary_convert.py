import math
# from binascii import unhexlify
# import numpy as np

# numpy进行fp16验证
# def conver_test():
#     # 注意输入的字节序
#     x=unhexlify(bytes('3432', 'utf-8'))
#     np.frombuffer(x, np.float16)

# 二进制字符串（16bit）转为fp16值
def bin_conver_fp16(input):
    # print('\n-------FP16-------')
    bitsgn = int(input[0])
    exp = int(input[1:6], 2) - 15
    data = 0
    for i in range(6,16):
        data = data + int(input[i]) * math.pow(0.5, i-5)
        
    ret = math.pow(-1, bitsgn) * math.pow(2, exp) * (1 + data)
    return ret
    
# 按fp16显示文件（每个16bit之间有个0x20，表示空格）
def read_file_by_fp16(file_name):
    f = open(file_name, 'rb')
    n = 0
    s = f.read(1)
    fp_tem = ''
    while s:
        byte = ord(s)
        n = n + 1
        # hex_str = '0x%02x '%(byte)
        bin_str = '{:08b}'.format(byte)
        fp_tem = fp_tem + bin_str
        if n % 3 == 0:
            # print(fp_tem[0:16])
            fp16 = bin_conver_fp16(fp_tem[0:16])
            print(fp16, end=' ')
            fp_tem = ''
        # 打印16进制, 或者二进制
        # print(hex_str, end='')

        # if n%10 == 0:
        #     print('')

        s = f.read(1)

    print('\n\ntotal bytes: %d'%n)
    f.close()

# 二进制显示文件
def read_file_by_bin(file_name):
    f = open(file_name, 'rb')
    n = 0
    s = f.read(1)
    fp_tem = ''
    while s:
        byte = ord(s)
        n = n + 1
        bin_str = '{:08b} '.format(byte)
        print(bin_str, end='')
        if n%18 == 0:
            print('')
        s = f.read(1)

    print('\n\ntotal bytes: %d'%n)
    f.close()

# 十六进制显示文件
def read_file_by_hex(file_name):
    f = open(file_name, 'rb')
    n = 0
    s = f.read(1)
    fp_tem = ''
    while s:
        byte = ord(s)
        n = n + 1
        hex_str = '%02x '%(byte)
        print(hex_str, end='')
        if n%18 == 0:
            print('')
        s = f.read(1)

    print('\n\ntotal bytes: %d'%n)
    f.close()


if __name__ == "__main__":
    read_file_by_fp16('input/output.dimg')
    # read_file_by_hex('output.dimg')
    # read_file_by_bin('output.dimg')