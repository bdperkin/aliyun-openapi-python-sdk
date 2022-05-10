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
from aliyunsdkcompanyreg.endpoint import endpoint_data

class BindProduceAuthorizationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'companyreg', '2020-03-06', 'BindProduceAuthorization','companyreg')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_BizType(self): # String
		return self.get_body_params().get('BizType')

	def set_BizType(self, BizType):  # String
		self.add_body_params('BizType', BizType)
	def get_AuthorizedUserIds(self): # String
		return self.get_body_params().get('AuthorizedUserIds')

	def set_AuthorizedUserIds(self, AuthorizedUserIds):  # String
		self.add_body_params('AuthorizedUserIds', AuthorizedUserIds)
	def get_BizId(self): # String
		return self.get_body_params().get('BizId')

	def set_BizId(self, BizId):  # String
		self.add_body_params('BizId', BizId)
