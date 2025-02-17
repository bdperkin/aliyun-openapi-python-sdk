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

class ListSnapshotsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'SWAS-OPEN', '2020-06-01', 'ListSnapshots','SWAS-OPEN')
		self.set_method('POST')

	def get_SnapshotIds(self): # String
		return self.get_query_params().get('SnapshotIds')

	def set_SnapshotIds(self, SnapshotIds):  # String
		self.add_query_param('SnapshotIds', SnapshotIds)
	def get_SourceDiskType(self): # String
		return self.get_query_params().get('SourceDiskType')

	def set_SourceDiskType(self, SourceDiskType):  # String
		self.add_query_param('SourceDiskType', SourceDiskType)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_DiskId(self): # String
		return self.get_query_params().get('DiskId')

	def set_DiskId(self, DiskId):  # String
		self.add_query_param('DiskId', DiskId)
