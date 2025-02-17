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

class UpdateTopicConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'UpdateTopicConfig')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_TopicFullName(self):
		return self.get_query_params().get('TopicFullName')

	def set_TopicFullName(self,TopicFullName):
		self.add_query_param('TopicFullName',TopicFullName)

	def get_EnableBroadcast(self):
		return self.get_query_params().get('EnableBroadcast')

	def set_EnableBroadcast(self,EnableBroadcast):
		self.add_query_param('EnableBroadcast',EnableBroadcast)

	def get_EnableProxySubscribe(self):
		return self.get_query_params().get('EnableProxySubscribe')

	def set_EnableProxySubscribe(self,EnableProxySubscribe):
		self.add_query_param('EnableProxySubscribe',EnableProxySubscribe)

	def get_ProductKey(self):
		return self.get_query_params().get('ProductKey')

	def set_ProductKey(self,ProductKey):
		self.add_query_param('ProductKey',ProductKey)

	def get_Codec(self):
		return self.get_query_params().get('Codec')

	def set_Codec(self,Codec):
		self.add_query_param('Codec',Codec)

	def get_Operation(self):
		return self.get_query_params().get('Operation')

	def set_Operation(self,Operation):
		self.add_query_param('Operation',Operation)