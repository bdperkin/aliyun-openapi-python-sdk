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
from aliyunsdkcas.endpoint import endpoint_data

class VerifyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cas', '2020-04-07', 'Verify')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MessageType(self): # String
		return self.get_query_params().get('MessageType')

	def set_MessageType(self, MessageType):  # String
		self.add_query_param('MessageType', MessageType)
	def get_SigningAlgorithm(self): # String
		return self.get_query_params().get('SigningAlgorithm')

	def set_SigningAlgorithm(self, SigningAlgorithm):  # String
		self.add_query_param('SigningAlgorithm', SigningAlgorithm)
	def get_Message(self): # String
		return self.get_query_params().get('Message')

	def set_Message(self, Message):  # String
		self.add_query_param('Message', Message)
	def get_SignatureValue(self): # String
		return self.get_query_params().get('SignatureValue')

	def set_SignatureValue(self, SignatureValue):  # String
		self.add_query_param('SignatureValue', SignatureValue)
	def get_CertIdentifier(self): # String
		return self.get_query_params().get('CertIdentifier')

	def set_CertIdentifier(self, CertIdentifier):  # String
		self.add_query_param('CertIdentifier', CertIdentifier)
