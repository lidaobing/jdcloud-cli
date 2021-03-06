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

import unittest
import os
import json


class VpcTest(unittest.TestCase):

    def test_describe_elastic_ips(self):
        cmd = """python ../../main.py vpc describe-elastic-ips """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_elastic_ips(self):
        cmd = """python ../../main.py vpc create-elastic-ips  --max-count '5' --elastic-ip-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_elastic_ip(self):
        cmd = """python ../../main.py vpc describe-elastic-ip  --elastic-ip-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_elastic_ip(self):
        cmd = """python ../../main.py vpc delete-elastic-ip  --elastic-ip-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_associate_elastic_ip(self):
        cmd = """python ../../main.py vpc associate-elastic-ip  --network-interface-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_disassociate_elastic_ip(self):
        cmd = """python ../../main.py vpc disassociate-elastic-ip  --network-interface-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_assign_secondary_ips(self):
        cmd = """python ../../main.py vpc assign-secondary-ips  --network-interface-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_unassign_secondary_ips(self):
        cmd = """python ../../main.py vpc unassign-secondary-ips  --network-interface-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_network_security_groups(self):
        cmd = """python ../../main.py vpc describe-network-security-groups """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_network_security_group(self):
        cmd = """python ../../main.py vpc describe-network-security-group  --network-security-group-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_subnets(self):
        cmd = """python ../../main.py vpc describe-subnets """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_subnet(self):
        cmd = """python ../../main.py vpc describe-subnet  --subnet-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_vpcs(self):
        cmd = """python ../../main.py vpc describe-vpcs """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_vpc(self):
        cmd = """python ../../main.py vpc describe-vpc  --vpc-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_vpc_peerings(self):
        cmd = """python ../../main.py vpc describe-vpc-peerings """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_vpc_peering(self):
        cmd = """python ../../main.py vpc create-vpc-peering  --vpc-peering-name 'xxx' --vpc-id 'xxx' --remote-vpc-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_vpc_peering(self):
        cmd = """python ../../main.py vpc describe-vpc-peering  --vpc-peering-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_vpc_peering(self):
        cmd = """python ../../main.py vpc modify-vpc-peering  --vpc-peering-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_vpc_peering(self):
        cmd = """python ../../main.py vpc delete-vpc-peering  --vpc-peering-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

