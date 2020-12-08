#!/usr/bin/env python
# encoding: utf-8
# Date: 2020/12/08
# file: vsc_file_chang_test.py
# Email:
# Author: 唐政 

import os
from pathlib import Path

# with open('.git', 'w+') as f:
#     pass

coding = """[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://e.coding.net/xiaodaxiaonao/graduation/graduation.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
[branch "2020-12-7"]
	remote = origin
	merge = refs/heads/2020-12-7
"""

github = """[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/tangzheng-git/graduation.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
[branch "2020-12-7"]
	remote = origin
	merge = refs/heads/2020-12-7
"""

BASE_DIR = Path(__file__).resolve().parent.parent
with open(BASE_DIR / '.git/config', 'w') as f:
    # print(f.write(coding))
    print(f.write(github))