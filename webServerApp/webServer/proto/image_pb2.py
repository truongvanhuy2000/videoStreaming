# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: image.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bimage.proto\x12\x05image\"\x15\n\x05image\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"-\n\rimage_request\x12\r\n\x05video\x18\x01 \x01(\t\x12\r\n\x05model\x18\x02 \x01(\t\"2\n\x0eimage_response\x12 \n\nimage_sent\x18\x01 \x01(\x0b\x32\x0c.image.image\"\'\n\x08image_up\x12\x1b\n\x05image\x18\x01 \x01(\x0b\x32\x0c.image.image\"\x1a\n\x0b\x61\x63k_request\x12\x0b\n\x03req\x18\x01 \x01(\t\"\x1b\n\x0c\x61\x63k_response\x12\x0b\n\x03rep\x18\x01 \x01(\t2\xb7\x01\n\rimage_tranfer\x12>\n\rsend_me_image\x12\x14.image.image_request\x1a\x15.image.image_response0\x01\x12\x36\n\x0cupload_image\x12\x0f.image.image_up\x1a\x13.image.ack_response(\x01\x12.\n\x03\x61\x63k\x12\x12.image.ack_request\x1a\x13.image.ack_responseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'image_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _IMAGE._serialized_start=22
  _IMAGE._serialized_end=43
  _IMAGE_REQUEST._serialized_start=45
  _IMAGE_REQUEST._serialized_end=90
  _IMAGE_RESPONSE._serialized_start=92
  _IMAGE_RESPONSE._serialized_end=142
  _IMAGE_UP._serialized_start=144
  _IMAGE_UP._serialized_end=183
  _ACK_REQUEST._serialized_start=185
  _ACK_REQUEST._serialized_end=211
  _ACK_RESPONSE._serialized_start=213
  _ACK_RESPONSE._serialized_end=240
  _IMAGE_TRANFER._serialized_start=243
  _IMAGE_TRANFER._serialized_end=426
# @@protoc_insertion_point(module_scope)
