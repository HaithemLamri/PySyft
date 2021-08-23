# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/grid/messages/success_resp_message.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)
from syft.proto.core.io import address_pb2 as proto_dot_core_dot_io_dot_address__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/grid/messages/success_resp_message.proto",
    package="syft.grid.messages",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n.proto/grid/messages/success_resp_message.proto\x12\x12syft.grid.messages\x1a%proto/core/common/common_object.proto\x1a\x1bproto/core/io/address.proto"y\n\x16SuccessResponseMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12\x10\n\x08resp_msg\x18\x03 \x01(\t\x12&\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Addressb\x06proto3',
    dependencies=[
        proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,
        proto_dot_core_dot_io_dot_address__pb2.DESCRIPTOR,
    ],
)


_SUCCESSRESPONSEMESSAGE = _descriptor.Descriptor(
    name="SuccessResponseMessage",
    full_name="syft.grid.messages.SuccessResponseMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.grid.messages.SuccessResponseMessage.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="resp_msg",
            full_name="syft.grid.messages.SuccessResponseMessage.resp_msg",
            index=1,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.grid.messages.SuccessResponseMessage.address",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=138,
    serialized_end=259,
)

_SUCCESSRESPONSEMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_SUCCESSRESPONSEMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
DESCRIPTOR.message_types_by_name["SuccessResponseMessage"] = _SUCCESSRESPONSEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SuccessResponseMessage = _reflection.GeneratedProtocolMessageType(
    "SuccessResponseMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _SUCCESSRESPONSEMESSAGE,
        "__module__": "proto.grid.messages.success_resp_message_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.SuccessResponseMessage)
    },
)
_sym_db.RegisterMessage(SuccessResponseMessage)


# @@protoc_insertion_point(module_scope)
