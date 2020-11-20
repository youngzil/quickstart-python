# !/usr/bin/python3
# -*- coding: utf-8 -*-

from rediscluster import RedisCluster


class Config():
    env_name = '南京测试环境'
    env_code = "test"

    sd_nodes = [{"host": "10.1.243.23", "port": "28001"}]
    redis_cluster_dict = {"nj_test": sd_nodes}

    mysql_config = {
        'host': '10.1.243.24',
        'port': 3306,
        'database': 'apidb',
        'user': 'XXXX',
        'password': 'XXXX',
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
