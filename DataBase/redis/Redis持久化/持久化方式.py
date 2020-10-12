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
#           everysec  no  快
#          AOF文件中的冗余命令(AOF重写）
#                 原因：由于AOF不停的往文件中写入命令，为了让AOF文件的大小控制在合理的范围避免胡乱增长
#                      redis提供了重写的功能，服务器可以产生一个新的AOF文件
#                   原理:1 新的AOF文件记录的数据库和原来的AOF文件记录的数据库数据完全一样 2 新的AOF文件会使用尽可能更少的命令来记录数据库数据，所以文件体积更小
#                        3 AOF 重写期间，服务器不会被阻塞，可以正常处理客户端啊发送的命令请求
#                     ex:
#                 old AOF:                             new  AOF:
#                     select 0                               select 0
#                     SADD  fruit  "apple"                    SADD  fruit   "apple"   "orager" "cherry"
#                     SADD  fruit  "orager"
#                     SADD  fruit  "cherry"
#         触发AOF重写的两种方法：
#                    1  客户端发送bgrewriteAOf命令
#                    2   通过配置文件选项让服务器自动执行bgrewriteAOf命令
#                             auto-aof-rewrite-min-size<size> （ auto-aof-rewrite-min-size 64mb）
#                             当AOF文件体积大于等于size的时候，服务器会考虑是否进行重写，用于避免对体积过小的aof文件进行重写
#                     auto-aof-rewrite-percentage<percent> 当前AOF文件大小和最后一次重写后的大小之间的比率等于或者等于指定的增长百分比
 # 以上两种可以将储存在内存里面的数据库数据以文件形式(二进制文件)保存到硬盘里

