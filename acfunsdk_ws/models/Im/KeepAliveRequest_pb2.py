# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: KeepAliveRequest.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import PushServiceToken_pb2 as PushServiceToken__pb2
import RegisterRequest_pb2 as RegisterRequest__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16KeepAliveRequest.proto\x12\x13\x41\x63\x46unDanmu.Im.Basic\x1a\x16PushServiceToken.proto\x1a\x15RegisterRequest.proto\"\xe6\x02\n\x10KeepAliveRequest\x12K\n\x0epresenceStatus\x18\x01 \x01(\x0e\x32\x33.AcFunDanmu.Im.Basic.RegisterRequest.PresenceStatus\x12J\n\x0f\x61ppActiveStatus\x18\x02 \x01(\x0e\x32\x31.AcFunDanmu.Im.Basic.RegisterRequest.ActiveStatus\x12?\n\x10pushServiceToken\x18\x03 \x01(\x0b\x32%.AcFunDanmu.Im.Basic.PushServiceToken\x12\x43\n\x14pushServiceTokenList\x18\x04 \x03(\x0b\x32%.AcFunDanmu.Im.Basic.PushServiceToken\x12\x1c\n\x14keepaliveIntervalSec\x18\x05 \x01(\x05\x12\x15\n\ripv6Available\x18\x06 \x01(\x08\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'KeepAliveRequest_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _KEEPALIVEREQUEST._serialized_start=95
  _KEEPALIVEREQUEST._serialized_end=453
# @@protoc_insertion_point(module_scope)
