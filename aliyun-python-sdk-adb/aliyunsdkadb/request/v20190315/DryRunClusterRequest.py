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
from aliyunsdkadb.endpoint import endpoint_data

class DryRunClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'adb', '2019-03-15', 'DryRunCluster','ads')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DBClusterDescription(self): # String
		return self.get_query_params().get('DBClusterDescription')

	def set_DBClusterDescription(self, DBClusterDescription):  # String
		self.add_query_param('DBClusterDescription', DBClusterDescription)
	def get_EnableDefaultResourcePool(self): # Boolean
		return self.get_query_params().get('EnableDefaultResourcePool')

	def set_EnableDefaultResourcePool(self, EnableDefaultResourcePool):  # Boolean
		self.add_query_param('EnableDefaultResourcePool', EnableDefaultResourcePool)
	def get_StorageResource(self): # String
		return self.get_query_params().get('StorageResource')

	def set_StorageResource(self, StorageResource):  # String
		self.add_query_param('StorageResource', StorageResource)
	def get_DBClusterNetworkType(self): # String
		return self.get_query_params().get('DBClusterNetworkType')

	def set_DBClusterNetworkType(self, DBClusterNetworkType):  # String
		self.add_query_param('DBClusterNetworkType', DBClusterNetworkType)
	def get_Period(self): # String
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # String
		self.add_query_param('Period', Period)
	def get_DBClusterId(self): # String
		return self.get_query_params().get('DBClusterId')

	def set_DBClusterId(self, DBClusterId):  # String
		self.add_query_param('DBClusterId', DBClusterId)
	def get_DBClusterVersion(self): # String
		return self.get_query_params().get('DBClusterVersion')

	def set_DBClusterVersion(self, DBClusterVersion):  # String
		self.add_query_param('DBClusterVersion', DBClusterVersion)
	def get_UsedTime(self): # String
		return self.get_query_params().get('UsedTime')

	def set_UsedTime(self, UsedTime):  # String
		self.add_query_param('UsedTime', UsedTime)
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_VPCId(self): # String
		return self.get_query_params().get('VPCId')

	def set_VPCId(self, VPCId):  # String
		self.add_query_param('VPCId', VPCId)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
	def get_ComputeResource(self): # String
		return self.get_query_params().get('ComputeResource')

	def set_ComputeResource(self, ComputeResource):  # String
		self.add_query_param('ComputeResource', ComputeResource)
	def get_PayType(self): # String
		return self.get_query_params().get('PayType')

	def set_PayType(self, PayType):  # String
		self.add_query_param('PayType', PayType)
	def get_Operation(self): # String
		return self.get_query_params().get('Operation')

	def set_Operation(self, Operation):  # String
		self.add_query_param('Operation', Operation)
