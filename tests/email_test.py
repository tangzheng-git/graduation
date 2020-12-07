#!/usr/bin/env python
# encoding: utf-8
# Date: 2020/12/07
# file: email_test.py
# Email:
# Author: 唐政 

from django.core.mail import send_mail

send_mail('Subject here', 'Here is the message.', 'tangzheng972631576@163.com', ['972631576@qq.com'], fail_silently=False)