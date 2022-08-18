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
from aliyunsdkalidns.endpoint import endpoint_data

class AddGtmAddressPoolRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alidns', '2015-01-09', 'AddGtmAddressPool','alidns')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MonitorExtendInfo(self): # String
		return self.get_query_params().get('MonitorExtendInfo')

	def set_MonitorExtendInfo(self, MonitorExtendInfo):  # String
		self.add_query_param('MonitorExtendInfo', MonitorExtendInfo)
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_Timeout(self): # Integer
		return self.get_query_params().get('Timeout')

	def set_Timeout(self, Timeout):  # Integer
		self.add_query_param('Timeout', Timeout)
	def get_MinAvailableAddrNum(self): # Integer
		return self.get_query_params().get('MinAvailableAddrNum')

	def set_MinAvailableAddrNum(self, MinAvailableAddrNum):  # Integer
		self.add_query_param('MinAvailableAddrNum', MinAvailableAddrNum)
	def get_EvaluationCount(self): # Integer
		return self.get_query_params().get('EvaluationCount')

	def set_EvaluationCount(self, EvaluationCount):  # Integer
		self.add_query_param('EvaluationCount', EvaluationCount)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_Addrs(self): # RepeatList
		return self.get_query_params().get('Addr')

	def set_Addrs(self, Addr):  # RepeatList
		for depth1 in range(len(Addr)):
			if Addr[depth1].get('Mode') is not None:
				self.add_query_param('Addr.' + str(depth1 + 1) + '.Mode', Addr[depth1].get('Mode'))
			if Addr[depth1].get('LbaWeight') is not None:
				self.add_query_param('Addr.' + str(depth1 + 1) + '.LbaWeight', Addr[depth1].get('LbaWeight'))
			if Addr[depth1].get('Value') is not None:
				self.add_query_param('Addr.' + str(depth1 + 1) + '.Value', Addr[depth1].get('Value'))
	def get_MonitorStatus(self): # String
		return self.get_query_params().get('MonitorStatus')

	def set_MonitorStatus(self, MonitorStatus):  # String
		self.add_query_param('MonitorStatus', MonitorStatus)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_ProtocolType(self): # String
		return self.get_query_params().get('ProtocolType')

	def set_ProtocolType(self, ProtocolType):  # String
		self.add_query_param('ProtocolType', ProtocolType)
	def get_Interval(self): # Integer
		return self.get_query_params().get('Interval')

	def set_Interval(self, Interval):  # Integer
		self.add_query_param('Interval', Interval)
	def get_IspCityNodes(self): # RepeatList
		return self.get_query_params().get('IspCityNode')

	def set_IspCityNodes(self, IspCityNode):  # RepeatList
		for depth1 in range(len(IspCityNode)):
			if IspCityNode[depth1].get('CityCode') is not None:
				self.add_query_param('IspCityNode.' + str(depth1 + 1) + '.CityCode', IspCityNode[depth1].get('CityCode'))
			if IspCityNode[depth1].get('IspCode') is not None:
				self.add_query_param('IspCityNode.' + str(depth1 + 1) + '.IspCode', IspCityNode[depth1].get('IspCode'))
