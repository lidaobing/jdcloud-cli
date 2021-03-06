# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

from jdcloud_sdk.core.config import Config
from jdcloud_sdk.core.credential import Credential
from jdcloud_sdk.services.vm.client.VmClient import VmClient
from jdcloud_sdk.services.iam.client.IamClient import IamClient
from jdcloud_sdk.services.disk.client.DiskClient import DiskClient
from jdcloud_sdk.services.mongodb.client.MongodbClient import MongodbClient
from jdcloud_sdk.services.mps.client.MpsClient import MpsClient
from jdcloud_sdk.services.streambus.client.StreambusClient import StreambusClient
from jdcloud_sdk.services.ipanti.client.IpantiClient import IpantiClient
from jdcloud_sdk.services.rds.client.RdsClient import RdsClient
from jdcloud_sdk.services.redis.client.RedisClient import RedisClient
from jdcloud_sdk.services.monitor.client.MonitorClient import MonitorClient
from jdcloud_sdk.services.vpc.client.VpcClient import VpcClient
from jdcloud_sdk.services.xdata.client.XdataClient import XdataClient
from jdcloud_sdk.services.nc.client.NcClient import NcClient
from jdcloud_sdk.services.oss.client.OssClient import OssClient
from jdcloud_cli.config import ProfileManager
from jdcloud_cli.logger import get_logger


class ClientFactory(object):

    def __init__(self, service):
        self.__service = service

    def get(self, app):
        client_map = {
            'vm': VmClient,
            'iam': IamClient,
            'disk': DiskClient,
            'mongodb': MongodbClient,
            'mps': MpsClient,
            'streambus': StreambusClient,
            'ipanti': IpantiClient,
            'rds': RdsClient,
            'redis': RedisClient,
            'monitor': MonitorClient,
            'vpc': VpcClient,
            'xdata': XdataClient,
            'nc': NcClient,
            'oss': OssClient,
        }

        profile_manager = ProfileManager()
        cli_config = profile_manager.load_current_profile()
        if cli_config is None:
            return None

        logger = get_logger(app.pargs.debug)

        config = Config(cli_config.endpoint, cli_config.scheme)
        credential = Credential(cli_config.access_key, cli_config.secret_key)
        if self.__service not in client_map:
            return None

        client = client_map[self.__service](credential, config, logger)
        return client
