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
from aliyunsdklinkwan.endpoint import endpoint_data

class SubmitNodeLocalConfigAddingTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'LinkWAN', '2019-03-01', 'SubmitNodeLocalConfigAddingTask','linkwan')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Freq(self):
		return self.get_query_params().get('Freq')

	def set_Freq(self,Freq):
		self.add_query_param('Freq',Freq)

	def get_Datr(self):
		return self.get_query_params().get('Datr')

	def set_Datr(self,Datr):
		self.add_query_param('Datr',Datr)

	def get_D2dKey(self):
		return self.get_query_params().get('D2dKey')

	def set_D2dKey(self,D2dKey):
		self.add_query_param('D2dKey',D2dKey)

	def get_DevEui(self):
		return self.get_query_params().get('DevEui')

	def set_DevEui(self,DevEui):
		self.add_query_param('DevEui',DevEui)

	def get_D2dAddr(self):
		return self.get_query_params().get('D2dAddr')

	def set_D2dAddr(self,D2dAddr):
		self.add_query_param('D2dAddr',D2dAddr)