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
from aliyunsdkmse.endpoint import endpoint_data

class CreateNacosServiceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mse', '2019-05-31', 'CreateNacosService','mse')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Ephemeral(self): # Boolean
		return self.get_query_params().get('Ephemeral')

	def set_Ephemeral(self, Ephemeral):  # Boolean
		self.add_query_param('Ephemeral', Ephemeral)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_GroupName(self): # String
		return self.get_query_params().get('GroupName')

	def set_GroupName(self, GroupName):  # String
		self.add_query_param('GroupName', GroupName)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_NamespaceId(self): # String
		return self.get_query_params().get('NamespaceId')

	def set_NamespaceId(self, NamespaceId):  # String
		self.add_query_param('NamespaceId', NamespaceId)
	def get_AcceptLanguage(self): # String
		return self.get_query_params().get('AcceptLanguage')

	def set_AcceptLanguage(self, AcceptLanguage):  # String
		self.add_query_param('AcceptLanguage', AcceptLanguage)
	def get_ServiceName(self): # String
		return self.get_query_params().get('ServiceName')

	def set_ServiceName(self, ServiceName):  # String
		self.add_query_param('ServiceName', ServiceName)
	def get_ProtectThreshold(self): # String
		return self.get_query_params().get('ProtectThreshold')

	def set_ProtectThreshold(self, ProtectThreshold):  # String
		self.add_query_param('ProtectThreshold', ProtectThreshold)
