"""
@ Author: glmgr
@ Email: 36040944@qq.com
@ Time: 2018/9/17 18:07
"""

import pika
import account

connection = pika.BlockingConnection(pika.ConnectionParameters(host=account.host))
