# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GroupMsgSearchResult.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Message_pb2 as Message__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aGroupMsgSearchResult.proto\x12\x1a\x41\x63\x46unDanmu.Im.Cloud.Search\x1a\rMessage.proto\"\x86\x01\n\x14GroupMsgSearchResult\x12\x0f\n\x07groupId\x18\x01 \x01(\t\x12\x0f\n\x07msgSize\x18\x02 \x01(\x05\x12+\n\x03msg\x18\x03 \x03(\x0b\x32\x1e.AcFunDanmu.Im.Message.Message\x12\x0e\n\x06offset\x18\x04 \x01(\t\x12\x0f\n\x07hasMore\x18\x05 \x01(\x08\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GroupMsgSearchResult_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GROUPMSGSEARCHRESULT._serialized_start=74
  _GROUPMSGSEARCHRESULT._serialized_end=208
# @@protoc_insertion_point(module_scope)
