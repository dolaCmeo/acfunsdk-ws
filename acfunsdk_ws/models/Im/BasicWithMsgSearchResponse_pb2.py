# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BasicWithMsgSearchResponse.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import GroupMsgSearchResult_pb2 as GroupMsgSearchResult__pb2
import GroupSearchResult_pb2 as GroupSearchResult__pb2
import UserMsgSearchResult_pb2 as UserMsgSearchResult__pb2
import UserSearchResult_pb2 as UserSearchResult__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n BasicWithMsgSearchResponse.proto\x12\x1a\x41\x63\x46unDanmu.Im.Cloud.Search\x1a\x1aGroupMsgSearchResult.proto\x1a\x17GroupSearchResult.proto\x1a\x19UserMsgSearchResult.proto\x1a\x16UserSearchResult.proto\"\xb4\x02\n\x1a\x42\x61sicWithMsgSearchResponse\x12@\n\nuserResult\x18\x01 \x03(\x0b\x32,.AcFunDanmu.Im.Cloud.Search.UserSearchResult\x12\x42\n\x0bgroupResult\x18\x02 \x03(\x0b\x32-.AcFunDanmu.Im.Cloud.Search.GroupSearchResult\x12\x46\n\ruserMsgResult\x18\x03 \x03(\x0b\x32/.AcFunDanmu.Im.Cloud.Search.UserMsgSearchResult\x12H\n\x0egroupMsgResult\x18\x04 \x03(\x0b\x32\x30.AcFunDanmu.Im.Cloud.Search.GroupMsgSearchResultb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'BasicWithMsgSearchResponse_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BASICWITHMSGSEARCHRESPONSE._serialized_start=169
  _BASICWITHMSGSEARCHRESPONSE._serialized_end=477
# @@protoc_insertion_point(module_scope)
