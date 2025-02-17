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

class QueryEventRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eventbridge', '2020-04-01', 'QueryEvent')
		self.set_method('POST')

	def get_EventId(self): # String
		return self.get_query_params().get('EventId')

	def set_EventId(self, EventId):  # String
		self.add_query_param('EventId', EventId)
	def get_EventBusName(self): # String
		return self.get_query_params().get('EventBusName')

	def set_EventBusName(self, EventBusName):  # String
		self.add_query_param('EventBusName', EventBusName)
