#!/usr/bin/env python
# coding:utf-8
# -*- coding: UTF-8 -*-

from hdfs import *

client = Client("http://127.0.0.1:50070")

dir(client)

print client.list("/user/hadoop/")
#count如果不是数字的话，直接忽略掉

##status——获取路径的具体信息
print client.status("/")

#makedirs——创建目录
client.makedirs("/user/hadoop/test",permission=777) #permission：设置权限(可选)
print client.list("/user/hadoop/")

#rename—重命名
client.rename("/user/hadoop/test","/user/hadoop/new_test")
print client.list("/user/hadoop/")

#upload——上传数据
client.upload("/user/hadoop/new_test","/data_test")
client.rename("/user/hadoop/new_test/data_test","/user/hadoop/new_test/data_updata")
print client.list("/user/hadoop/new_test")
#pload(hdfs_path, local_path, overwrite=False, n_threads=1, temp_dir=None,
# chunk_size=65536,progress=None, cleanup=True, **kwargs)
#overwrite：是否是覆盖性上传文件
#n_threads：启动的线程数目
#temp_dir：当overwrite=true时，远程文件一旦存在，则会在上传完之后进行交换
#chunk_size：文件上传的大小区间
#progress：回调函数来跟踪进度，为每一chunk_size字节。它将传递两个参数，文件上传的路径和传输的字节数。一旦完成，-1将作为第二个参数
#cleanup：如果在上传任何文件时发生错误，则删除该文件

#read——读取文件
with client.read("/user/hadoop/new_test/data_updata") as reader:
    print reader.read()
#hdfs_path：hdfs路径
#offset：设置开始的字节位置
#length：读取的长度（字节为单位）
#buffer_size：用于传输数据的字节的缓冲区的大小。默认值设置在HDFS配置。
#encoding：制定编码

#download——下载
client.download("/user/hadoop/new_test/data_updata","/usr/local/hadoop/",overwrite=True)
#download(hdfs_path, local_path, overwrite=False, n_threads=1, temp_dir=None, **kwargs)

#delete—删除
client.delete("/user/hadoop/new_test",recursive=True)#(true)删除文件和其子目录，默认为false(可不写)
print client.list("/user/hadoop/")

