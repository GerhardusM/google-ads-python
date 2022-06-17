# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore

from google.ads.googleads.v10.enums.types import (
    response_content_type as gage_response_content_type,
)
from google.ads.googleads.v10.resources.types import (
    extension_feed_item as gagr_extension_feed_item,
)
from google.protobuf import field_mask_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v10.services",
    marshal="google.ads.googleads.v10",
    manifest={
        "MutateExtensionFeedItemsRequest",
        "ExtensionFeedItemOperation",
        "MutateExtensionFeedItemsResponse",
        "MutateExtensionFeedItemResult",
    },
)


class MutateExtensionFeedItemsRequest(proto.Message):
    r"""Request message for
    [ExtensionFeedItemService.MutateExtensionFeedItems][google.ads.googleads.v10.services.ExtensionFeedItemService.MutateExtensionFeedItems].

    Attributes:
        customer_id (str):
            Required. The ID of the customer whose
            extension feed items are being modified.
        operations (Sequence[google.ads.googleads.v10.services.types.ExtensionFeedItemOperation]):
            Required. The list of operations to perform
            on individual extension feed items.
        partial_failure (bool):
            If true, successful operations will be
            carried out and invalid operations will return
            errors. If false, all operations will be carried
            out in one transaction if and only if they are
            all valid. Default is false.
        validate_only (bool):
            If true, the request is validated but not
            executed. Only errors are returned, not results.
        response_content_type (google.ads.googleads.v10.enums.types.ResponseContentTypeEnum.ResponseContentType):
            The response content type setting. Determines
            whether the mutable resource or just the
            resource name should be returned post mutation.
    """

    customer_id = proto.Field(
        proto.STRING,
        number=1,
    )
    operations = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ExtensionFeedItemOperation",
    )
    partial_failure = proto.Field(
        proto.BOOL,
        number=3,
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=4,
    )
    response_content_type = proto.Field(
        proto.ENUM,
        number=5,
        enum=gage_response_content_type.ResponseContentTypeEnum.ResponseContentType,
    )


class ExtensionFeedItemOperation(proto.Message):
    r"""A single operation (create, update, remove) on an extension
    feed item.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            FieldMask that determines which resource
            fields are modified in an update.
        create (google.ads.googleads.v10.resources.types.ExtensionFeedItem):
            Create operation: No resource name is
            expected for the new extension feed item.

            This field is a member of `oneof`_ ``operation``.
        update (google.ads.googleads.v10.resources.types.ExtensionFeedItem):
            Update operation: The extension feed item is
            expected to have a valid resource name.

            This field is a member of `oneof`_ ``operation``.
        remove (str):
            Remove operation: A resource name for the removed extension
            feed item is expected, in this format:

            ``customers/{customer_id}/extensionFeedItems/{feed_item_id}``

            This field is a member of `oneof`_ ``operation``.
    """

    update_mask = proto.Field(
        proto.MESSAGE,
        number=4,
        message=field_mask_pb2.FieldMask,
    )
    create = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="operation",
        message=gagr_extension_feed_item.ExtensionFeedItem,
    )
    update = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="operation",
        message=gagr_extension_feed_item.ExtensionFeedItem,
    )
    remove = proto.Field(
        proto.STRING,
        number=3,
        oneof="operation",
    )


class MutateExtensionFeedItemsResponse(proto.Message):
    r"""Response message for an extension feed item mutate.

    Attributes:
        partial_failure_error (google.rpc.status_pb2.Status):
            Errors that pertain to operation failures in the partial
            failure mode. Returned only when partial_failure = true and
            all errors occur inside the operations. If any errors occur
            outside the operations (e.g. auth errors), we return an RPC
            level error.
        results (Sequence[google.ads.googleads.v10.services.types.MutateExtensionFeedItemResult]):
            All results for the mutate.
    """

    partial_failure_error = proto.Field(
        proto.MESSAGE,
        number=3,
        message=status_pb2.Status,
    )
    results = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="MutateExtensionFeedItemResult",
    )


class MutateExtensionFeedItemResult(proto.Message):
    r"""The result for the extension feed item mutate.

    Attributes:
        resource_name (str):
            Returned for successful operations.
        extension_feed_item (google.ads.googleads.v10.resources.types.ExtensionFeedItem):
            The mutated extension feed item with only mutable fields
            after mutate. The field will only be returned when
            response_content_type is set to "MUTABLE_RESOURCE".
    """

    resource_name = proto.Field(
        proto.STRING,
        number=1,
    )
    extension_feed_item = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gagr_extension_feed_item.ExtensionFeedItem,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
