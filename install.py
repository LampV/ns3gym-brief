import os
import argparse
from pathlib import Path


parser = argparse.ArgumentParser(description='安装参数')
parser.add_argument('--wafdir', default='/ns3-gym', type=str, help='安装目录')
parser.add_argument('--norebuild', default=False, action='store_true', help='是否跳过waf rebuild')
args = parser.parse_args()

cur_path = Path().resolve()
ns3_path = (cur_path / args.wafdir).resolve()


def file_copy():
    """
    进行文件复制操作
    """
    # 将opengym文件夹复制到 ns3path/src下

    # 将ns3src/下文件夹复制到 ns3path/src 对应文件夹下
    src_path = ns3_path / 'src'
    opengym_path = cur_path / 'opengym'

    os.system(f"cp -r {opengym_path.resolve()} {src_path.resolve()}")
    print('文件复制完成')


def waf_rebuild():
    # 定位waf
    waf_path = ns3_path / 'waf'
    os.chdir(ns3_path.resolve())
    # 执行指令
    print(f'\n{waf_path} configure\n')
    os.system(f'{waf_path} configure')
    print(f'\n\n{waf_path} build\n\n')
    os.system(f'{waf_path} build')


if __name__ == '__main__':
    file_copy()
    if not args.norebuild:
        waf_rebuild()
