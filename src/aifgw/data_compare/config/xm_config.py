# !/usr/bin/python3
# -*- coding: utf-8 -*-

from rediscluster import RedisCluster


class Config():
    env_name = '项目测试环境'
    env_code = "test"

    sd_nodes = [{"host": "20.26.37.179", "port": "28001"}]
    sq_nodes = [{"host": "20.26.103.195", "port": "6601"}]
    redis_cluster_dict = {"xm_sd": sd_nodes, "xm_sq": sq_nodes}

    mysql_config = {
        'host': '20.26.103.149',
        'port': 3306,
        'database': 'test',
        'user': 'XXXX',
        'password': 'XXX',
        'charset': 'utf8',
        'use_unicode': True,
        'get_warnings': True,
    }

    def __init__(self, env_code):
        self.env_code = env_code  # public

    def getRedisConnect(slef):
        cur_dict = {}
        for key, value in slef.redis_cluster_dict.items():
            # redis connect
            # Requires at least one node for cluster discovery. Multiple nodes is recommended.
            rc = RedisCluster(startup_nodes=value, max_connections=200, decode_responses=True)
            cur_dict[key] = rc
        return cur_dict

    def getMySQLConfig(slef):
        return slef.mysql_config
