# RDB(Redis DB) 储存到磁盘  默认开启 存数据
        #save 阻塞的 使用此命令后不能进行其他的操作
        # BGSAVE  异步的 服务器单独fork一个子线程去完成保存的操作
        # 时间上 save要快一点
# AOF (AppendOnlyFile) 命令  默认不开启 存操作
#         redis为持久化提供了appendfsync选项: 默认为everysec
                # always 服务器每写入一个命令 就调用一次fdatasync，将缓存区的操作命令写入硬盘，比较影响性能 因为
                # everysec 服务器每一秒，就调用一次fdatasync ,这种模式下 遇到意外最多丢失一秒的命令数据
                # no  服务器不主动调用fdatasync，由操作系统决定将缓冲区的命令写入硬盘，如果数据丢失，丢失情况不能估计
        # 运行速度
#           always  慢
#             everysec  no  快
# 以上两种可以将储存在内存里面的数据库数据以文件形式(二进制文件)保存到硬盘里

