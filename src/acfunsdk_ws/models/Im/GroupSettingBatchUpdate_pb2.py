# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GroupSettingBatchUpdate.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Location_pb2 as Location__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dGroupSettingBatchUpdate.proto\x12\x1b\x41\x63\x46unDanmu.Im.Cloud.Message\x1a\x0eLocation.proto\"\xe0\x02\n\x17GroupSettingBatchUpdate\x12P\n\x06\x66ields\x18\x01 \x03(\x0e\x32@.AcFunDanmu.Im.Cloud.Message.GroupSettingBatchUpdate.UpdateField\x12\x11\n\tgroupName\x18\x02 \x01(\t\x12\x14\n\x0cgroupHeadUrl\x18\x03 \x01(\t\x12\x37\n\x08location\x18\x04 \x01(\x0b\x32%.AcFunDanmu.Im.Cloud.Message.Location\x12\x0b\n\x03tag\x18\x05 \x01(\t\x12\x14\n\x0cintroduction\x18\x06 \x01(\t\"n\n\x0bUpdateField\x12\x12\n\x0eUN_KNOWN_FIELD\x10\x00\x12\x0e\n\nGROUP_NAME\x10\x01\x12\x12\n\x0eGROUP_HEAD_URL\x10\x02\x12\x0c\n\x08LOCATION\x10\x03\x12\x07\n\x03TAG\x10\x04\x12\x10\n\x0cINTRODUCTION\x10\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GroupSettingBatchUpdate_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GROUPSETTINGBATCHUPDATE._serialized_start=79
  _GROUPSETTINGBATCHUPDATE._serialized_end=431
  _GROUPSETTINGBATCHUPDATE_UPDATEFIELD._serialized_start=321
  _GROUPSETTINGBATCHUPDATE_UPDATEFIELD._serialized_end=431
# @@protoc_insertion_point(module_scope)
