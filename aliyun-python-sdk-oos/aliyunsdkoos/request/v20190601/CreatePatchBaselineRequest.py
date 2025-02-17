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
from aliyunsdkoos.endpoint import endpoint_data
import json

class CreatePatchBaselineRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'oos', '2019-06-01', 'CreatePatchBaseline','oos')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_ApprovalRules(self): # String
		return self.get_query_params().get('ApprovalRules')

	def set_ApprovalRules(self, ApprovalRules):  # String
		self.add_query_param('ApprovalRules', ApprovalRules)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_OperationSystem(self): # String
		return self.get_query_params().get('OperationSystem')

	def set_OperationSystem(self, OperationSystem):  # String
		self.add_query_param('OperationSystem', OperationSystem)
	def get_RejectedPatches(self): # Array
		return self.get_query_params().get('RejectedPatches')

	def set_RejectedPatches(self, RejectedPatches):  # Array
		self.add_query_param("RejectedPatches", json.dumps(RejectedPatches))
	def get_RejectedPatchesAction(self): # String
		return self.get_query_params().get('RejectedPatchesAction')

	def set_RejectedPatchesAction(self, RejectedPatchesAction):  # String
		self.add_query_param('RejectedPatchesAction', RejectedPatchesAction)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
