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

from argparse import RawTextHelpFormatter
from cement.ext.ext_argparse import expose
from jdcloud_cli.controllers.base_controller import BaseController
from jdcloud_cli.client_factory import ClientFactory
from jdcloud_cli.parameter_builder import collect_user_args
from jdcloud_cli.printer import Printer
from jdcloud_cli.skeleton import Skeleton


class StreambusController(BaseController):
    class Meta:
        label = 'streambus'
        help = '使用该子命令操作streambus相关资源'
        description = '''
        streambus cli 子命令，可以使用该子命令操作streambus相关资源。
        OpenAPI文档地址为：https://www.jdcloud.com/help/detail/390/isCatalog/0
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--keyword'], dict(help="""(string) NA """, dest='keyword', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询topic ''',
        description='''
            查询topic。

            示例: jdc streambus get-topic-list 
        ''',
    )
    def get_topic_list(self):
        client_factory = ClientFactory('streambus')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.streambus.apis.GetTopicListRequest import GetTopicListRequest
            params_dict = collect_user_args(self.app)
            req = GetTopicListRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--topic-model'], dict(help="""(addTopic) NA """, dest='topicModel', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 创建topic ''',
        description='''
            创建topic。

            示例: jdc streambus add-topic  --topic-model {"":""}
        ''',
    )
    def add_topic(self):
        client_factory = ClientFactory('streambus')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.streambus.apis.AddTopicRequest import AddTopicRequest
            params_dict = collect_user_args(self.app)
            req = AddTopicRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--topic-model'], dict(help="""(addTopic) NA """, dest='topicModel', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 更新topic ''',
        description='''
            更新topic。

            示例: jdc streambus update-topic  --topic-model {"":""}
        ''',
    )
    def update_topic(self):
        client_factory = ClientFactory('streambus')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.streambus.apis.UpdateTopicRequest import UpdateTopicRequest
            params_dict = collect_user_args(self.app)
            req = UpdateTopicRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['get-topic-list','add-topic','update-topic',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('streambus', self.app.pargs.api)
        skeleton.show()
