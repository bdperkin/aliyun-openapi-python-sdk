# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkiot.endpoint import endpoint_data

class CreateEdgeInstanceChannelRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'CreateEdgeInstanceChannel')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Configss(self):
		return self.get_query_params().get('Configs')

	def set_Configss(self, Configss):
		for depth1 in range(len(Configss)):
			if Configss[depth1].get('Format') is not None:
				self.add_query_param('Configs.' + str(depth1 + 1) + '.Format', Configss[depth1].get('Format'))
			if Configss[depth1].get('Content') is not None:
				self.add_query_param('Configs.' + str(depth1 + 1) + '.Content', Configss[depth1].get('Content'))
			if Configss[depth1].get('Key') is not None:
				self.add_query_param('Configs.' + str(depth1 + 1) + '.Key', Configss[depth1].get('Key'))

	def get_DriverId(self):
		return self.get_query_params().get('DriverId')

	def set_DriverId(self,DriverId):
		self.add_query_param('DriverId',DriverId)

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_ChannelName(self):
		return self.get_query_params().get('ChannelName')

	def set_ChannelName(self,ChannelName):
		self.add_query_param('ChannelName',ChannelName)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)