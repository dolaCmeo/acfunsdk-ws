# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MessageReadPush.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ChatTargetType_pb2 as ChatTargetType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15MessageReadPush.proto\x12\x15\x41\x63\x46unDanmu.Im.Message\x1a\x14\x43hatTargetType.proto\"\x88\x01\n\x0fMessageReadPush\x12\x10\n\x08targetId\x18\x01 \x01(\x03\x12\x0f\n\x07readSeq\x18\x02 \x01(\x03\x12=\n\x0e\x63hatTargetType\x18\x03 \x01(\x0e\x32%.AcFunDanmu.Im.Message.ChatTargetType\x12\x13\n\x0bstrTargetId\x18\x04 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'MessageReadPush_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MESSAGEREADPUSH._serialized_start=71
  _MESSAGEREADPUSH._serialized_end=207
# @@protoc_insertion_point(module_scope)
