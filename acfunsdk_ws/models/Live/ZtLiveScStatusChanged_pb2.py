# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ZtLiveScStatusChanged.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bZtLiveScStatusChanged.proto\x12\nAcFunDanmu\"\xb7\x02\n\x15ZtLiveScStatusChanged\x12\x34\n\x04type\x18\x01 \x01(\x0e\x32&.AcFunDanmu.ZtLiveScStatusChanged.Type\x12\x18\n\x10maxRandomDelayMs\x18\x02 \x01(\x03\x12@\n\nbannedInfo\x18\x03 \x01(\x0b\x32,.AcFunDanmu.ZtLiveScStatusChanged.BannedInfo\x1a*\n\nBannedInfo\x12\x11\n\tbanReason\x18\x01 \x01(\t\x12\t\n\x01\x62\x18\x02 \x01(\t\"`\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0f\n\x0bLIVE_CLOSED\x10\x01\x12\x13\n\x0fNEW_LIVE_OPENED\x10\x02\x12\x14\n\x10LIVE_URL_CHANGED\x10\x03\x12\x0f\n\x0bLIVE_BANNED\x10\x04\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ZtLiveScStatusChanged_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ZTLIVESCSTATUSCHANGED._serialized_start=44
  _ZTLIVESCSTATUSCHANGED._serialized_end=355
  _ZTLIVESCSTATUSCHANGED_BANNEDINFO._serialized_start=215
  _ZTLIVESCSTATUSCHANGED_BANNEDINFO._serialized_end=257
  _ZTLIVESCSTATUSCHANGED_TYPE._serialized_start=259
  _ZTLIVESCSTATUSCHANGED_TYPE._serialized_end=355
# @@protoc_insertion_point(module_scope)