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

class CreateCertificateWithCsrRequestRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cas', '2020-04-07', 'CreateCertificateWithCsrRequest')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Csr(self): # String
		return self.get_query_params().get('Csr')

	def set_Csr(self, Csr):  # String
		self.add_query_param('Csr', Csr)
	def get_ProductCode(self): # String
		return self.get_query_params().get('ProductCode')

	def set_ProductCode(self, ProductCode):  # String
		self.add_query_param('ProductCode', ProductCode)
	def get_Username(self): # String
		return self.get_query_params().get('Username')

	def set_Username(self, Username):  # String
		self.add_query_param('Username', Username)
	def get_Phone(self): # String
		return self.get_query_params().get('Phone')

	def set_Phone(self, Phone):  # String
		self.add_query_param('Phone', Phone)
	def get_Email(self): # String
		return self.get_query_params().get('Email')

	def set_Email(self, Email):  # String
		self.add_query_param('Email', Email)
	def get_ValidateType(self): # String
		return self.get_query_params().get('ValidateType')

	def set_ValidateType(self, ValidateType):  # String
		self.add_query_param('ValidateType', ValidateType)
