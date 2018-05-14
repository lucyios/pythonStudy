
import sys

import fibo  #导入模块

import sound.effects.echo


print('命令行参数:')

for i in sys.argv:
    print(i)

print('/n/n the PYTHONPATH is',sys.path,'/n')


fibo.fibonacci()

