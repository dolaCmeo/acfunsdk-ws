# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Invitation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import InvitationOperator_pb2 as InvitationOperator__pb2
import JoinRequestStatus_pb2 as JoinRequestStatus__pb2
import User_pb2 as User__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10Invitation.proto\x12\x1b\x41\x63\x46unDanmu.Im.Cloud.Message\x1a\x18InvitationOperator.proto\x1a\x17JoinRequestStatus.proto\x1a\nUser.proto\"\xdc\x02\n\nInvitation\x12\x0e\n\x06reqSeq\x18\x01 \x01(\x03\x12\x0f\n\x07groupId\x18\x02 \x01(\t\x12.\n\x0brequestUser\x18\x03 \x01(\x0b\x32\x19.AcFunDanmu.Im.Basic.User\x12\x11\n\tgroupName\x18\x04 \x01(\t\x12\x10\n\x08\x66indType\x18\x05 \x01(\x05\x12\x13\n\x0b\x64\x65scContent\x18\x06 \x01(\t\x12\x15\n\rauditComments\x18\x07 \x01(\t\x12>\n\x06status\x18\x08 \x01(\x0e\x32..AcFunDanmu.Im.Cloud.Message.JoinRequestStatus\x12\x41\n\x08operator\x18\t \x01(\x0b\x32/.AcFunDanmu.Im.Cloud.Message.InvitationOperator\x12\x13\n\x0bgroupNumber\x18\n \x01(\t\x12\x14\n\x0cgroupHeadUrl\x18\x0b \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Invitation_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INVITATION._serialized_start=113
  _INVITATION._serialized_end=461
# @@protoc_insertion_point(module_scope)