import random
import time


def sleep(n_secs):
    time.sleep(n_secs)


def get_random_user_agent():
    """获取随机的user_agent"""
    users_agent = ['Mozilla/5.0 Ally01', 'Mozilla/5.0 Ally02',
                   'Mozilla/5.0 Ally03', 'Mozilla/5.0 Ally04,'
                   ]
    # random.choice：随机选择
    u_agent = random.choice(users_agent)
    print(u_agent)
    return u_agent


def get_accounts():
    # 如果要实现参数化（数据驱动），那么要返回一个嵌套字典的列表
    # a.每个字典代表一条用例
    # b.每一个字典的key为变量名
    accounts = [
        {"title": "正常登录", "username": "keyou1", "password": "123456",
         "status_code": 200, "contain_msg": "token"},
        {"title": "密码错误", "username": "keyou1", "password": "123457",
         "status_code": 400, "contain_msg": "non_field_errors"},
        {"title": "账号错误", "username": "keyou1111", "password": "123456",
         "status_code": 400, "contain_msg": "non_field_errors"},
        {"title": "用户名为空", "username": "", "password": "123456",
         "status_code": 400, "contain_msg": "username"},
        {"title": "密码为空", "username": "keyou1", "password": "",
         "status_code": 400, "contain_msg": "password"},
    ]
    return accounts


if __name__ == '__main__':
    get_random_user_agent()
