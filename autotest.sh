#!/bin/sh

# 执行错误退出脚本
set -e


# 加载驱动
./vpsetup.sh

# 创建output目录
if [ ! -d output  ];then
    mkdir output
fi


# 查看loadable
for name in ./*.nvdla;do
    echo ${name}
done

# 运行runtime
for file in ./*.nvdla;do
    command="./nvdla_runtime --loadable ${file} --image ./cat.jpg --rawdump"
    echo " ----sun---- ${command}"
    $command
    mv output.dimg  output/${file}.output.dimg
    printf "\n\n\n ----sun---- ${file}  test ok !!!  ------------------------------\n\n\n"
done

