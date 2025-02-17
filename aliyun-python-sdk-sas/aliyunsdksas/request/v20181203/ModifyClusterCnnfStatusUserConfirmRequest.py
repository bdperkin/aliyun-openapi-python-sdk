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

class ModifyClusterCnnfStatusUserConfirmRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'ModifyClusterCnnfStatusUserConfirm')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClusterIdss(self): # RepeatList
		return self.get_query_params().get('ClusterIds')

	def set_ClusterIdss(self, ClusterIds):  # RepeatList
		for depth1 in range(len(ClusterIds)):
			self.add_query_param('ClusterIds.' + str(depth1 + 1), ClusterIds[depth1])
	def get_UserConfirm(self): # Boolean
		return self.get_query_params().get('UserConfirm')

	def set_UserConfirm(self, UserConfirm):  # Boolean
		self.add_query_param('UserConfirm', UserConfirm)
