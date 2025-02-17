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
from aliyunsdkvideoenhan.endpoint import endpoint_data

class MergeVideoModelFaceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'videoenhan', '2020-03-20', 'MergeVideoModelFace','videoenhan')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_FaceImageURL(self): # String
		return self.get_body_params().get('FaceImageURL')

	def set_FaceImageURL(self, FaceImageURL):  # String
		self.add_body_params('FaceImageURL', FaceImageURL)
	def get_MergeInfoss(self): # RepeatList
		return self.get_body_params().get('MergeInfos')

	def set_MergeInfoss(self, MergeInfos):  # RepeatList
		for depth1 in range(len(MergeInfos)):
			if MergeInfos[depth1].get('TemplateFaceURL') is not None:
				self.add_body_params('MergeInfos.' + str(depth1 + 1) + '.TemplateFaceURL', MergeInfos[depth1].get('TemplateFaceURL'))
			if MergeInfos[depth1].get('ImageURL') is not None:
				self.add_body_params('MergeInfos.' + str(depth1 + 1) + '.ImageURL', MergeInfos[depth1].get('ImageURL'))
			if MergeInfos[depth1].get('TemplateFaceID') is not None:
				self.add_body_params('MergeInfos.' + str(depth1 + 1) + '.TemplateFaceID', MergeInfos[depth1].get('TemplateFaceID'))
	def get_TemplateId(self): # String
		return self.get_body_params().get('TemplateId')

	def set_TemplateId(self, TemplateId):  # String
		self.add_body_params('TemplateId', TemplateId)
