# stdlib
import json
from typing import Dict
from typing import Optional

# third party
from google.protobuf.reflection import GeneratedProtocolMessageType
from typing_extensions import final

# syft absolute
from syft.core.common.message import ImmediateSyftMessageWithReply
from syft.core.common.message import ImmediateSyftMessageWithoutReply
from syft.core.common.serde.deserialize import _deserialize
from syft.core.common.serde.serializable import bind_protobuf
from syft.core.common.uid import UID
from syft.core.io.address import Address
from syft.proto.grid.messages.tensor_messages_pb2 import (
    CreateTensorMessage as CreateTensorMessage_PB,
)
from syft.proto.grid.messages.tensor_messages_pb2 import (
    CreateTensorResponse as CreateTensorResponse_PB,
)
from syft.proto.grid.messages.tensor_messages_pb2 import (
    DeleteTensorMessage as DeleteTensorMessage_PB,
)
from syft.proto.grid.messages.tensor_messages_pb2 import (
    DeleteTensorResponse as DeleteTensorResponse_PB,
)
from syft.proto.grid.messages.tensor_messages_pb2 import (
    GetTensorMessage as GetTensorMessage_PB,
)
from syft.proto.grid.messages.tensor_messages_pb2 import (
    GetTensorResponse as GetTensorResponse_PB,
)
from syft.proto.grid.messages.tensor_messages_pb2 import (
    GetTensorsMessage as GetTensorsMessage_PB,
)
from syft.proto.grid.messages.tensor_messages_pb2 import (
    GetTensorsResponse as GetTensorsResponse_PB,
)
from syft.proto.grid.messages.tensor_messages_pb2 import (
    UpdateTensorMessage as UpdateTensorMessage_PB,
)
from syft.proto.grid.messages.tensor_messages_pb2 import (
    UpdateTensorResponse as UpdateTensorResponse_PB,
)


@bind_protobuf
@final
class CreateTensorMessage(ImmediateSyftMessageWithReply):
    def __init__(
        self,
        address: Address,
        content: Dict,
        reply_to: Address,
        msg_id: Optional[UID] = None,
    ):
        super().__init__(address=address, msg_id=msg_id, reply_to=reply_to)
        self.content = content

    def _object2proto(self) -> CreateTensorMessage_PB:
        """Returns a protobuf serialization of self.
        As a requirement of all objects which inherit from Serializable,
        this method transforms the current object into the corresponding
        Protobuf object so that it can be further serialized.
        :return: returns a protobuf object
        :rtype: CreateTensorMessage_PB
        .. note::
            This method is purely an internal method. Please use object._sy_serialize() or one of
            the other public serialization methods if you wish to serialize an
            object.
        """
        return CreateTensorMessage_PB(
            msg_id=self.id._sy_serialize(),
            address=self.address._sy_serialize(),
            content=json.dumps(self.content),
            reply_to=self.reply_to._sy_serialize(),
        )

    @staticmethod
    def _proto2object(
        proto: CreateTensorMessage_PB,
    ) -> "CreateTensorMessage":
        """Creates a CreateTensorMessage from a protobuf
        As a requirement of all objects which inherit from Serializable,
        this method transforms a protobuf object into an instance of this class.
        :return: returns an instance of SignalingOfferMessage
        :rtype: CreateTensorMessage
        .. note::
            This method is purely an internal method. Please use syft.deserialize()
            if you wish to deserialize an object.
        """

        return CreateTensorMessage(
            msg_id=_deserialize(blob=proto.msg_id),
            address=_deserialize(blob=proto.address),
            content=json.loads(proto.content),
            reply_to=_deserialize(blob=proto.reply_to),
        )

    @staticmethod
    def get_protobuf_schema() -> GeneratedProtocolMessageType:
        """Return the type of protobuf object which stores a class of this type
        As a part of serialization and deserialization, we need the ability to
        lookup the protobuf object type directly from the object type. This
        static method allows us to do this.
        Importantly, this method is also used to create the reverse lookup ability within
        the metaclass of Serializable. In the metaclass, it calls this method and then
        it takes whatever type is returned from this method and adds an attribute to it
        with the type of this class attached to it. See the MetaSerializable class for
        details.
        :return: the type of protobuf object which corresponds to this class.
        :rtype: GeneratedProtocolMessageType
        """

        return CreateTensorMessage_PB


@bind_protobuf
@final
class CreateTensorResponse(ImmediateSyftMessageWithoutReply):
    def __init__(
        self,
        address: Address,
        status_code: int,
        content: Dict,
        msg_id: Optional[UID] = None,
    ):
        super().__init__(address=address, msg_id=msg_id)
        self.status_code = status_code
        self.content = content

    def _object2proto(self) -> CreateTensorResponse_PB:
        """Returns a protobuf serialization of self.
        As a requirement of all objects which inherit from Serializable,
        this method transforms the current object into the corresponding
        Protobuf object so that it can be further serialized.
        :return: returns a protobuf object
        :rtype: SignalingOfferMessage_PB
        .. note::
            This method is purely an internal method. Please use object._sy_serialize() or one of
            the other public serialization methods if you wish to serialize an
            object.
        """
        return CreateTensorResponse_PB(
            msg_id=self.id._sy_serialize(),
            address=self.address._sy_serialize(),
            status_code=self.status_code,
            content=json.dumps(self.content),
        )

    @staticmethod
    def _proto2object(
        proto: CreateTensorResponse_PB,
    ) -> "CreateTensorResponse":
        """Creates a SignalingOfferMessage from a protobuf
        As a requirement of all objects which inherit from Serializable,
        this method transforms a protobuf object into an instance of this class.
        :return: returns an instance of SignalingOfferMessage
        :rtype: SignalingOfferMessage
        .. note::
            This method is purely an internal method. Please use syft.deserialize()
            if you wish to deserialize an object.
        """

        return CreateTensorResponse(
            msg_id=_deserialize(blob=proto.msg_id),
            address=_deserialize(blob=proto.address),
            status_code=proto.status_code,
            content=json.loads(proto.content),
        )

    @staticmethod
    def get_protobuf_schema() -> GeneratedProtocolMessageType:
        """Return the type of protobuf object which stores a class of this type
        As a part of serialization and deserialization, we need the ability to
        lookup the protobuf object type directly from the object type. This
        static method allows us to do this.
        Importantly, this method is also used to create the reverse lookup ability within
        the metaclass of Serializable. In the metaclass, it calls this method and then
        it takes whatever type is returned from this method and adds an attribute to it
        with the type of this class attached to it. See the MetaSerializable class for
        details.
        :return: the type of protobuf object which corresponds to this class.
        :rtype: GeneratedProtocolMessageType
        """

        return CreateTensorResponse_PB


@bind_protobuf
@final
class GetTensorMessage(ImmediateSyftMessageWithReply):
    def __init__(
        self,
        address: Address,
        content: Dict,
        reply_to: Address,
        msg_id: Optional[UID] = None,
    ):
        super().__init__(address=address, msg_id=msg_id, reply_to=reply_to)
        self.content = content

    def _object2proto(self) -> GetTensorMessage_PB:
        """Returns a protobuf serialization of self.
        As a requirement of all objects which inherit from Serializable,
        this method transforms the current object into the corresponding
        Protobuf object so that it can be further serialized.
        :return: returns a protobuf object
        :rtype: GetTensorMessage_PB
        .. note::
            This method is purely an internal method. Please use object._sy_serialize() or one of
            the other public serialization methods if you wish to serialize an
            object.
        """
        return GetTensorMessage_PB(
            msg_id=self.id._sy_serialize(),
            address=self.address._sy_serialize(),
            content=json.dumps(self.content),
            reply_to=self.reply_to._sy_serialize(),
        )

    @staticmethod
    def _proto2object(
        proto: GetTensorMessage_PB,
    ) -> "GetTensorMessage":
        """Creates a GetTensorMessage from a protobuf
        As a requirement of all objects which inherit from Serializable,
        this method transforms a protobuf object into an instance of this class.
        :return: returns an instance of SignalingOfferMessage
        :rtype: GetTensorMessage
        .. note::
            This method is purely an internal method. Please use syft.deserialize()
            if you wish to deserialize an object.
        """

        return GetTensorMessage(
            msg_id=_deserialize(blob=proto.msg_id),
            address=_deserialize(blob=proto.address),
            content=json.loads(proto.content),
            reply_to=_deserialize(blob=proto.reply_to),
        )

    @staticmethod
    def get_protobuf_schema() -> GeneratedProtocolMessageType:
        """Return the type of protobuf object which stores a class of this type
        As a part of serialization and deserialization, we need the ability to
        lookup the protobuf object type directly from the object type. This
        static method allows us to do this.
        Importantly, this method is also used to create the reverse lookup ability within
        the metaclass of Serializable. In the metaclass, it calls this method and then
        it takes whatever type is returned from this method and adds an attribute to it
        with the type of this class attached to it. See the MetaSerializable class for
        details.
        :return: the type of protobuf object which corresponds to this class.
        :rtype: GeneratedProtocolMessageType
        """

        return GetTensorMessage_PB


@bind_protobuf
@final
class GetTensorResponse(ImmediateSyftMessageWithoutReply):
    def __init__(
        self,
        address: Address,
        status_code: int,
        content: Dict,
        msg_id: Optional[UID] = None,
    ):
        super().__init__(address=address, msg_id=msg_id)
        self.status_code = status_code
        self.content = content

    def _object2proto(self) -> GetTensorResponse_PB:
        """Returns a protobuf serialization of self.
        As a requirement of all objects which inherit from Serializable,
        this method transforms the current object into the corresponding
        Protobuf object so that it can be further serialized.
        :return: returns a protobuf object
        :rtype: SignalingOfferMessage_PB
        .. note::
            This method is purely an internal method. Please use object._sy_serialize() or one of
            the other public serialization methods if you wish to serialize an
            object.
        """
        return GetTensorResponse_PB(
            msg_id=self.id._sy_serialize(),
            address=self.address._sy_serialize(),
            status_code=self.status_code,
            content=json.dumps(self.content),
        )

    @staticmethod
    def _proto2object(
        proto: GetTensorResponse_PB,
    ) -> "GetTensorResponse":
        """Creates a SignalingOfferMessage from a protobuf
        As a requirement of all objects which inherit from Serializable,
        this method transforms a protobuf object into an instance of this class.
        :return: returns an instance of SignalingOfferMessage
        :rtype: SignalingOfferMessage
        .. note::
            This method is purely an internal method. Please use syft.deserialize()
            if you wish to deserialize an object.
        """

        return GetTensorResponse(
            msg_id=_deserialize(blob=proto.msg_id),
            address=_deserialize(blob=proto.address),
            status_code=proto.status_code,
            content=json.loads(proto.content),
        )

    @staticmethod
    def get_protobuf_schema() -> GeneratedProtocolMessageType:
        """Return the type of protobuf object which stores a class of this type
        As a part of serialization and deserialization, we need the ability to
        lookup the protobuf object type directly from the object type. This
        static method allows us to do this.
        Importantly, this method is also used to create the reverse lookup ability within
        the metaclass of Serializable. In the metaclass, it calls this method and then
        it takes whatever type is returned from this method and adds an attribute to it
        with the type of this class attached to it. See the MetaSerializable class for
        details.
        :return: the type of protobuf object which corresponds to this class.
        :rtype: GeneratedProtocolMessageType
        """

        return GetTensorResponse_PB


@bind_protobuf
@final
class GetTensorsMessage(ImmediateSyftMessageWithReply):
    def __init__(
        self,
        address: Address,
        content: Dict,
        reply_to: Address,
        msg_id: Optional[UID] = None,
    ):
        super().__init__(address=address, msg_id=msg_id, reply_to=reply_to)
        self.content = content

    def _object2proto(self) -> GetTensorsMessage_PB:
        """Returns a protobuf serialization of self.
        As a requirement of all objects which inherit from Serializable,
        this method transforms the current object into the corresponding
        Protobuf object so that it can be further serialized.
        :return: returns a protobuf object
        :rtype: GetTensorsMessage_PB
        .. note::
            This method is purely an internal method. Please use object._sy_serialize() or one of
            the other public serialization methods if you wish to serialize an
            object.
        """
        return GetTensorsMessage_PB(
            msg_id=self.id._sy_serialize(),
            address=self.address._sy_serialize(),
            content=json.dumps(self.content),
            reply_to=self.reply_to._sy_serialize(),
        )

    @staticmethod
    def _proto2object(
        proto: GetTensorsMessage_PB,
    ) -> "GetTensorsMessage":
        """Creates a GetTensorsMessage from a protobuf
        As a requirement of all objects which inherit from Serializable,
        this method transforms a protobuf object into an instance of this class.
        :return: returns an instance of SignalingOfferMessage
        :rtype: GetTensorsMessage
        .. note::
            This method is purely an internal method. Please use syft.deserialize()
            if you wish to deserialize an object.
        """

        return GetTensorsMessage(
            msg_id=_deserialize(blob=proto.msg_id),
            address=_deserialize(blob=proto.address),
            content=json.loads(proto.content),
            reply_to=_deserialize(blob=proto.reply_to),
        )

    @staticmethod
    def get_protobuf_schema() -> GeneratedProtocolMessageType:
        """Return the type of protobuf object which stores a class of this type
        As a part of serialization and deserialization, we need the ability to
        lookup the protobuf object type directly from the object type. This
        static method allows us to do this.
        Importantly, this method is also used to create the reverse lookup ability within
        the metaclass of Serializable. In the metaclass, it calls this method and then
        it takes whatever type is returned from this method and adds an attribute to it
        with the type of this class attached to it. See the MetaSerializable class for
        details.
        :return: the type of protobuf object which corresponds to this class.
        :rtype: GeneratedProtocolMessageType
        """

        return GetTensorsMessage_PB


@bind_protobuf
@final
class GetTensorsResponse(ImmediateSyftMessageWithoutReply):
    def __init__(
        self,
        address: Address,
        status_code: int,
        content: Dict,
        msg_id: Optional[UID] = None,
    ):
        super().__init__(address=address, msg_id=msg_id)
        self.status_code = status_code
        self.content = content

    def _object2proto(self) -> GetTensorsResponse_PB:
        """Returns a protobuf serialization of self.
        As a requirement of all objects which inherit from Serializable,
        this method transforms the current object into the corresponding
        Protobuf object so that it can be further serialized.
        :return: returns a protobuf object
        :rtype: SignalingOfferMessage_PB
        .. note::
            This method is purely an internal method. Please use object._sy_serialize() or one of
            the other public serialization methods if you wish to serialize an
            object.
        """
        return GetTensorsResponse_PB(
            msg_id=self.id._sy_serialize(),
            address=self.address._sy_serialize(),
            status_code=self.status_code,
            content=json.dumps(self.content),
        )

    @staticmethod
    def _proto2object(
        proto: GetTensorsResponse_PB,
    ) -> "GetTensorsResponse":
        """Creates a SignalingOfferMessage from a protobuf
        As a requirement of all objects which inherit from Serializable,
        this method transforms a protobuf object into an instance of this class.
        :return: returns an instance of SignalingOfferMessage
        :rtype: SignalingOfferMessage
        .. note::
            This method is purely an internal method. Please use syft.deserialize()
            if you wish to deserialize an object.
        """

        return GetTensorsResponse(
            msg_id=_deserialize(blob=proto.msg_id),
            address=_deserialize(blob=proto.address),
            status_code=proto.status_code,
            content=json.loads(proto.content),
        )

    @staticmethod
    def get_protobuf_schema() -> GeneratedProtocolMessageType:
        """Return the type of protobuf object which stores a class of this type
        As a part of serialization and deserialization, we need the ability to
        lookup the protobuf object type directly from the object type. This
        static method allows us to do this.
        Importantly, this method is also used to create the reverse lookup ability within
        the metaclass of Serializable. In the metaclass, it calls this method and then
        it takes whatever type is returned from this method and adds an attribute to it
        with the type of this class attached to it. See the MetaSerializable class for
        details.
        :return: the type of protobuf object which corresponds to this class.
        :rtype: GeneratedProtocolMessageType
        """

        return GetTensorsResponse_PB


@bind_protobuf
@final
class UpdateTensorMessage(ImmediateSyftMessageWithReply):
    def __init__(
        self,
        address: Address,
        content: Dict,
        reply_to: Address,
        msg_id: Optional[UID] = None,
    ):
        super().__init__(address=address, msg_id=msg_id, reply_to=reply_to)
        self.content = content

    def _object2proto(self) -> UpdateTensorMessage_PB:
        """Returns a protobuf serialization of self.
        As a requirement of all objects which inherit from Serializable,
        this method transforms the current object into the corresponding
        Protobuf object so that it can be further serialized.
        :return: returns a protobuf object
        :rtype: UpdateTensorMessage_PB
        .. note::
            This method is purely an internal method. Please use object._sy_serialize() or one of
            the other public serialization methods if you wish to serialize an
            object.
        """
        return UpdateTensorMessage_PB(
            msg_id=self.id._sy_serialize(),
            address=self.address._sy_serialize(),
            content=json.dumps(self.content),
            reply_to=self.reply_to._sy_serialize(),
        )

    @staticmethod
    def _proto2object(
        proto: UpdateTensorMessage_PB,
    ) -> "UpdateTensorMessage":
        """Creates a UpdateTensorMessage from a protobuf
        As a requirement of all objects which inherit from Serializable,
        this method transforms a protobuf object into an instance of this class.
        :return: returns an instance of SignalingOfferMessage
        :rtype: UpdateTensorMessage
        .. note::
            This method is purely an internal method. Please use syft.deserialize()
            if you wish to deserialize an object.
        """

        return UpdateTensorMessage(
            msg_id=_deserialize(blob=proto.msg_id),
            address=_deserialize(blob=proto.address),
            content=json.loads(proto.content),
            reply_to=_deserialize(blob=proto.reply_to),
        )

    @staticmethod
    def get_protobuf_schema() -> GeneratedProtocolMessageType:
        """Return the type of protobuf object which stores a class of this type
        As a part of serialization and deserialization, we need the ability to
        lookup the protobuf object type directly from the object type. This
        static method allows us to do this.
        Importantly, this method is also used to create the reverse lookup ability within
        the metaclass of Serializable. In the metaclass, it calls this method and then
        it takes whatever type is returned from this method and adds an attribute to it
        with the type of this class attached to it. See the MetaSerializable class for
        details.
        :return: the type of protobuf object which corresponds to this class.
        :rtype: GeneratedProtocolMessageType
        """

        return UpdateTensorMessage_PB


@bind_protobuf
@final
class UpdateTensorResponse(ImmediateSyftMessageWithoutReply):
    def __init__(
        self,
        address: Address,
        status_code: int,
        content: Dict,
        msg_id: Optional[UID] = None,
    ):
        super().__init__(address=address, msg_id=msg_id)
        self.status_code = status_code
        self.content = content

    def _object2proto(self) -> UpdateTensorResponse_PB:
        """Returns a protobuf serialization of self.
        As a requirement of all objects which inherit from Serializable,
        this method transforms the current object into the corresponding
        Protobuf object so that it can be further serialized.
        :return: returns a protobuf object
        :rtype: SignalingOfferMessage_PB
        .. note::
            This method is purely an internal method. Please use object._sy_serialize() or one of
            the other public serialization methods if you wish to serialize an
            object.
        """
        return UpdateTensorResponse_PB(
            msg_id=self.id._sy_serialize(),
            address=self.address._sy_serialize(),
            status_code=self.status_code,
            content=json.dumps(self.content),
        )

    @staticmethod
    def _proto2object(
        proto: UpdateTensorResponse_PB,
    ) -> "UpdateTensorResponse":
        """Creates a SignalingOfferMessage from a protobuf
        As a requirement of all objects which inherit from Serializable,
        this method transforms a protobuf object into an instance of this class.
        :return: returns an instance of SignalingOfferMessage
        :rtype: SignalingOfferMessage
        .. note::
            This method is purely an internal method. Please use syft.deserialize()
            if you wish to deserialize an object.
        """

        return UpdateTensorResponse(
            msg_id=_deserialize(blob=proto.msg_id),
            address=_deserialize(blob=proto.address),
            status_code=proto.status_code,
            content=json.loads(proto.content),
        )

    @staticmethod
    def get_protobuf_schema() -> GeneratedProtocolMessageType:
        """Return the type of protobuf object which stores a class of this type
        As a part of serialization and deserialization, we need the ability to
        lookup the protobuf object type directly from the object type. This
        static method allows us to do this.
        Importantly, this method is also used to create the reverse lookup ability within
        the metaclass of Serializable. In the metaclass, it calls this method and then
        it takes whatever type is returned from this method and adds an attribute to it
        with the type of this class attached to it. See the MetaSerializable class for
        details.
        :return: the type of protobuf object which corresponds to this class.
        :rtype: GeneratedProtocolMessageType
        """

        return UpdateTensorResponse_PB


@bind_protobuf
@final
class DeleteTensorMessage(ImmediateSyftMessageWithReply):
    def __init__(
        self,
        address: Address,
        content: Dict,
        reply_to: Address,
        msg_id: Optional[UID] = None,
    ):
        super().__init__(address=address, msg_id=msg_id, reply_to=reply_to)
        self.content = content

    def _object2proto(self) -> DeleteTensorMessage_PB:
        """Returns a protobuf serialization of self.
        As a requirement of all objects which inherit from Serializable,
        this method transforms the current object into the corresponding
        Protobuf object so that it can be further serialized.
        :return: returns a protobuf object
        :rtype: DeleteTensorMessage_PB
        .. note::
            This method is purely an internal method. Please use object._sy_serialize() or one of
            the other public serialization methods if you wish to serialize an
            object.
        """
        return DeleteTensorMessage_PB(
            msg_id=self.id._sy_serialize(),
            address=self.address._sy_serialize(),
            content=json.dumps(self.content),
            reply_to=self.reply_to._sy_serialize(),
        )

    @staticmethod
    def _proto2object(
        proto: DeleteTensorMessage_PB,
    ) -> "DeleteTensorMessage":
        """Creates a DeleteTensorMessage from a protobuf
        As a requirement of all objects which inherit from Serializable,
        this method transforms a protobuf object into an instance of this class.
        :return: returns an instance of SignalingOfferMessage
        :rtype: DeleteTensorMessage
        .. note::
            This method is purely an internal method. Please use syft.deserialize()
            if you wish to deserialize an object.
        """

        return DeleteTensorMessage(
            msg_id=_deserialize(blob=proto.msg_id),
            address=_deserialize(blob=proto.address),
            content=json.loads(proto.content),
            reply_to=_deserialize(blob=proto.reply_to),
        )

    @staticmethod
    def get_protobuf_schema() -> GeneratedProtocolMessageType:
        """Return the type of protobuf object which stores a class of this type
        As a part of serialization and deserialization, we need the ability to
        lookup the protobuf object type directly from the object type. This
        static method allows us to do this.
        Importantly, this method is also used to create the reverse lookup ability within
        the metaclass of Serializable. In the metaclass, it calls this method and then
        it takes whatever type is returned from this method and adds an attribute to it
        with the type of this class attached to it. See the MetaSerializable class for
        details.
        :return: the type of protobuf object which corresponds to this class.
        :rtype: GeneratedProtocolMessageType
        """

        return DeleteTensorMessage_PB


@bind_protobuf
@final
class DeleteTensorResponse(ImmediateSyftMessageWithoutReply):
    def __init__(
        self,
        address: Address,
        status_code: int,
        content: Dict,
        msg_id: Optional[UID] = None,
    ):
        super().__init__(address=address, msg_id=msg_id)
        self.status_code = status_code
        self.content = content

    def _object2proto(self) -> DeleteTensorResponse_PB:
        """Returns a protobuf serialization of self.
        As a requirement of all objects which inherit from Serializable,
        this method transforms the current object into the corresponding
        Protobuf object so that it can be further serialized.
        :return: returns a protobuf object
        :rtype: SignalingOfferMessage_PB
        .. note::
            This method is purely an internal method. Please use object._sy_serialize() or one of
            the other public serialization methods if you wish to serialize an
            object.
        """
        return DeleteTensorResponse_PB(
            msg_id=self.id._sy_serialize(),
            address=self.address._sy_serialize(),
            status_code=self.status_code,
            content=json.dumps(self.content),
        )

    @staticmethod
    def _proto2object(
        proto: DeleteTensorResponse_PB,
    ) -> "DeleteTensorResponse":
        """Creates a SignalingOfferMessage from a protobuf
        As a requirement of all objects which inherit from Serializable,
        this method transforms a protobuf object into an instance of this class.
        :return: returns an instance of SignalingOfferMessage
        :rtype: SignalingOfferMessage
        .. note::
            This method is purely an internal method. Please use syft.deserialize()
            if you wish to deserialize an object.
        """

        return DeleteTensorResponse(
            msg_id=_deserialize(blob=proto.msg_id),
            address=_deserialize(blob=proto.address),
            status_code=proto.status_code,
            content=json.loads(proto.content),
        )

    @staticmethod
    def get_protobuf_schema() -> GeneratedProtocolMessageType:
        """Return the type of protobuf object which stores a class of this type
        As a part of serialization and deserialization, we need the ability to
        lookup the protobuf object type directly from the object type. This
        static method allows us to do this.
        Importantly, this method is also used to create the reverse lookup ability within
        the metaclass of Serializable. In the metaclass, it calls this method and then
        it takes whatever type is returned from this method and adds an attribute to it
        with the type of this class attached to it. See the MetaSerializable class for
        details.
        :return: the type of protobuf object which corresponds to this class.
        :rtype: GeneratedProtocolMessageType
        """

        return DeleteTensorResponse_PB
