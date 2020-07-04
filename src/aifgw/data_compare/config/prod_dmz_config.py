# !/usr/bin/python3
# -*- coding: utf-8 -*-

from rediscluster import RedisCluster


class Config():
    env_name = '项目测试环境'
    env_code = "test"

    sd_nodes = [{"host": "10.76.224.228", "port": "6301"}]
    sq_nodes = [{"host": "10.78.134.70", "port": "6201"}]
    redis_cluster_dict = {"prod_dmz_sd": sd_nodes, "prod_dmz_sq": sq_nodes}

    mysql_config = {
        'host': '10.76.224.65',
        'port': 7001,
        'database': 'aiosp_cfg',
        'user': 'aiosp_cfg',
        'password': 'aiosp_cfg',
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
            # Note: decode_responses must be set to True when used with python3
            rc = RedisCluster(startup_nodes=value, max_connections=200, decode_responses=True, password='cmVkaXM=')
            cur_dict[key] = rc
        return cur_dict

    def getMySQLConfig(slef):
        return slef.mysql_config
