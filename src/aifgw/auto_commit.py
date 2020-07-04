# !/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import subprocess
import time
import random

import click

vpn_command = 'nohup /Applications/MotionPro.app/Contents/MacOS/MotionPro'
code_base = '/Users/hydro/work/aicache'


def connect_vpn_network():
    """连接到公司的VPN，如果已连接则跳过，否则要求手动登录"""
    connect_ok = False
    vpn_connect_times = 0
    click.echo('正在检测公司VPN连接情况...')
    while not connect_ok:
        try:
            content = subprocess.getstatusoutput('curl 10.19.14.241:80 --connect-timeout 2')[1]
            if content.find('timed out') > 0:
                vpn_connect_times = vpn_connect_times + 1
                if vpn_connect_times == 1 or vpn_connect_times > 5:
                    click.echo('网络不通，请求连接VPN.')
                    token = click.prompt('请连接SVN或输入VPN口令', type=str, default='Auto')
                    if token and token != 'Auto':
                        vpn_connect_times = 1
                        os.system(vpn_command + ' -connectwithui sslnj.asiainfo.com 443 zhuanghd ' + token + ' 0 0 0 0 > /dev/null 2>&1 &')
            else:
                connect_ok = True
                click.echo('VPN已连接成功.')
        except:
            pass
        finally:
            if not connect_ok:
                click.echo('VPN连接中...')
                time.sleep(3)


pull_script = """cd {{dir}}
git clean -df
git pull origin master
"""

push_script = """cd {{dir}}
git add ./* -f
git commit -m 'feature-%s'
git push origin master
""" % str(time.strftime("%Y%m%d%H%M%S", time.gmtime(time.time())))


def pull_files_from_remote():
    """拉取远程文件"""
    click.echo('正在将仓库代码更新到本地...')
    subprocess.call(pull_script.replace('{{dir}}', code_base), shell=True)


def push_files_to_remote():
    """推送代码到远程"""
    click.echo('正在本地代码推送到仓库...')
    subprocess.call(push_script.replace('{{dir}}', code_base), shell=True)


def walk_file(file):
    """遍历文件夹"""
    files = []
    for parent, dirnames, filenames in os.walk(file, followlinks=True):
        for filename in filenames:
            if filename.startswith('.'):
                continue
            path = os.path.join(parent, filename)
            if os.path.isfile(path):
                files.append(path)
    return files


def get_move_files():
    """"获取剩余可提交的代码文件"""
    files = walk_file('/Users/hydro/work/auto-commit')
    total = len(files)
    if total <= 20:
        mv_files = files
    else:
        mv_files = random.sample(files, 20)
    return mv_files


def make_the_changes():
    """修改代码，蹭活跃度"""
    click.echo('正在自动修改代码...')
    move_files = get_move_files()
    if len(move_files) == 0:
        click.echo('提交失败，已经没有文件可以提交了，请补充 ' + click.style('✖️', bold=True, fg='red'))
        return False
    for mf in move_files:
        target_file = mf.replace('/Users/hydro/work/auto-commit/', '/Users/hydro/work/aicache/')
        target_dir = target_file[:target_file.rfind('/')+1]
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        os.system('mv -f %s %s' % (mf, target_dir))
    return True


@click.command()
def auto_push():
    """自动修改代码，并提交到代码仓库..."""
    connect_vpn_network()
    pull_files_from_remote()
    if make_the_changes():
        push_files_to_remote()
        click.echo('本次自动提交已完成 ' + click.style('✔️', bold=True, fg='green'))


if __name__ == '__main__':
    auto_push()

