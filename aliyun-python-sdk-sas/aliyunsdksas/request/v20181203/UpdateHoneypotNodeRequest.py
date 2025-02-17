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
from aliyunsdksas.endpoint import endpoint_data

class UpdateHoneypotNodeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'UpdateHoneypotNode')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AvailableProbeNum(self): # Integer
		return self.get_query_params().get('AvailableProbeNum')

	def set_AvailableProbeNum(self, AvailableProbeNum):  # Integer
		self.add_query_param('AvailableProbeNum', AvailableProbeNum)
	def get_NodeId(self): # String
		return self.get_query_params().get('NodeId')

	def set_NodeId(self, NodeId):  # String
		self.add_query_param('NodeId', NodeId)
	def get_NodeName(self): # String
		return self.get_query_params().get('NodeName')

	def set_NodeName(self, NodeName):  # String
		self.add_query_param('NodeName', NodeName)
	def get_SecurityGroupProbeIpLists(self): # RepeatList
		return self.get_query_params().get('SecurityGroupProbeIpList')

	def set_SecurityGroupProbeIpLists(self, SecurityGroupProbeIpList):  # RepeatList
		for depth1 in range(len(SecurityGroupProbeIpList)):
			self.add_query_param('SecurityGroupProbeIpList.' + str(depth1 + 1), SecurityGroupProbeIpList[depth1])
