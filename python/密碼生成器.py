import os
file_name = "wifi_number_password.txt"
f = open(file_name, "w+")
# 打开文件
for i in range(10):
    # 第一层循环
    for j in range(10):
        # 第二层循环
        for k in range(10):
            # 第三层循环
            for q in range(10):
                # 第四层循环
                for m in range(10):
                    # 第五层循环
                    for n in range(10):
                        # 第六层循环
                        for o in range(10):
                            # 第七层循环
                            for p in range(10):
                                # 第八层循环
                                insert_str = str(i) + str(j) + str(k) + str(q) + \
                                             str(m) + str(n) + str(o) + str(p)
                                # 数据的拼接以及数据类型的转换。
                                #print(insert_str)
                                f.write(insert_str)
                                # 写入密码
                                f.write("\n")
                                # 一个密码换一次行
f.close()
# 关闭文件
print("一个密码本生成完毕了！")
