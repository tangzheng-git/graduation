#!/usr/bin/env python
# encoding: utf-8
# Date: 2020/12/08
# file: vsc_test.py
# Email:
# Author: 唐政 

# git remote
# git push github 2020-12-8
# git push coding 2020-12-8

import os
from threading import Thread




class VersionControl:
    def __init__(self, branch, remote):
        self.branch = branch
        self.remote = remote

    def create_branch(self, new_branch):
        if new_branch not in self.branch:
            self.branch.append(new_branch)

    def create_remote(self, new_remote):
        if new_remote not in self.remote:
            self.remote.append(new_remote)

    def push_branch(self, branch):
        """
        同时推送到远端仓库
        :param branch: 推送分支
        :return: cmd命令 list
        """
        git_list = []
        for item in self.remote:
            git_list.append('git push {} {}'.format(item, branch))

        return git_list

    @staticmethod
    def commit_branch(message, filename=None):
        """
        提交到本地仓库
        :param message: 提交信息
        :param filename: 提交文件
        :return: cmd命令 str
        """
        git_str = 'git commit -m {} {}'.format(message, filename)

        return git_str

    @staticmethod
    def thread_cmd(cmd_str, number):
        print('{} {} 开始'.format(number, cmd_str))

        print('{} {} 结束'.format(number, cmd_str))

    @staticmethod
    def consumer():
        i = 0
        while True:
            get = yield i
            if not get:
                return
            i += 1

    def run(self, cmd_list=None, cmd_str=None):
        print('开始cmd')
        consumer = self.consumer()
        consumer.send(None)

        if cmd_list is not None:
            for item in cmd_list:
                num = consumer.send('get')
                t = Thread(target=self.thread_cmd, args=(item, num))
                t.start()

        if cmd_str is not None:
            num = consumer.send('get')
            t = Thread(target=self.thread_cmd, args=(cmd_str, num))
            t.start()

        num = consumer.send('get')
        consumer.close()
        print('结束cmd')
        print('执行了{}个任务'.format(num-1))


vsc = VersionControl(['2020-12-7'], ['github', 'coding'])

message = ''
filename = ''
branch = '2020-12-7'

commit_str = vsc.commit_branch(message, filename)
command_list = vsc.push_branch(branch)
cmd_dict = {
    'cmd_list': command_list,
    'cmd_str': commit_str,
}

vsc.run(**cmd_dict)


