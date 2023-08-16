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
import json

class AttachApplication2ConnectorRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'AttachApplication2Connector')
		self.set_method('POST')

	def get_ConnectorId(self): # String
		return self.get_body_params().get('ConnectorId')

	def set_ConnectorId(self, ConnectorId):  # String
		self.add_body_params('ConnectorId', ConnectorId)
	def get_ApplicationIds(self): # Array
		return self.get_body_params().get('ApplicationIds')

	def set_ApplicationIds(self, ApplicationIds):  # Array
		self.add_body_params("ApplicationIds", json.dumps(ApplicationIds))
