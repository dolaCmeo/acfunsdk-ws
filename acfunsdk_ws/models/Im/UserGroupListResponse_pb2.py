# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UserGroupListResponse.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import SyncCookie_pb2 as SyncCookie__pb2
import UserGroupInfo_pb2 as UserGroupInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bUserGroupListResponse.proto\x12\x1b\x41\x63\x46unDanmu.Im.Cloud.Message\x1a\x10SyncCookie.proto\x1a\x13UserGroupInfo.proto\"\xa5\x01\n\x15UserGroupListResponse\x12\x41\n\ruserGroupInfo\x18\x01 \x03(\x0b\x32*.AcFunDanmu.Im.Cloud.Message.UserGroupInfo\x12\x33\n\nsyncCookie\x18\x02 \x01(\x0b\x32\x1f.AcFunDanmu.Im.Basic.SyncCookie\x12\x14\n\x0cnotFullFetch\x18\x03 \x01(\x08\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'UserGroupListResponse_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USERGROUPLISTRESPONSE._serialized_start=100
  _USERGROUPLISTRESPONSE._serialized_end=265
# @@protoc_insertion_point(module_scope)
