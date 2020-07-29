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


if __name__ == '__main__':
    get_random_user_agent()
