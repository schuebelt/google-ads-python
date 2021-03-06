# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/services/billing_setup_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.resources import billing_setup_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_billing__setup__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/services/billing_setup_service.proto',
  package='google.ads.googleads.v0.services',
  syntax='proto3',
  serialized_pb=_b('\nBgoogle/ads/googleads_v0/proto/services/billing_setup_service.proto\x12 google.ads.googleads.v0.services\x1a;google/ads/googleads_v0/proto/resources/billing_setup.proto\x1a\x1cgoogle/api/annotations.proto\"/\n\x16GetBillingSetupRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"|\n\x19MutateBillingSetupRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12J\n\toperation\x18\x02 \x01(\x0b\x32\x37.google.ads.googleads.v0.services.BillingSetupOperation\"y\n\x15\x42illingSetupOperation\x12\x41\n\x06\x63reate\x18\x02 \x01(\x0b\x32/.google.ads.googleads.v0.resources.BillingSetupH\x00\x12\x10\n\x06remove\x18\x01 \x01(\tH\x00\x42\x0b\n\toperation\"h\n\x1aMutateBillingSetupResponse\x12J\n\x06result\x18\x01 \x01(\x0b\x32:.google.ads.googleads.v0.services.MutateBillingSetupResult\"1\n\x18MutateBillingSetupResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\x9e\x03\n\x13\x42illingSetupService\x12\xb5\x01\n\x0fGetBillingSetup\x12\x38.google.ads.googleads.v0.services.GetBillingSetupRequest\x1a/.google.ads.googleads.v0.resources.BillingSetup\"7\x82\xd3\xe4\x93\x02\x31\x12//v0/{resource_name=customers/*/billingSetups/*}\x12\xce\x01\n\x12MutateBillingSetup\x12;.google.ads.googleads.v0.services.MutateBillingSetupRequest\x1a<.google.ads.googleads.v0.services.MutateBillingSetupResponse\"=\x82\xd3\xe4\x93\x02\x37\"2/v0/customers/{customer_id=*}/billingSetups:mutate:\x01*B\xd8\x01\n$com.google.ads.googleads.v0.servicesB\x18\x42illingSetupServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V0.Services\xca\x02 Google\\Ads\\GoogleAds\\V0\\Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_billing__setup__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GETBILLINGSETUPREQUEST = _descriptor.Descriptor(
  name='GetBillingSetupRequest',
  full_name='google.ads.googleads.v0.services.GetBillingSetupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.GetBillingSetupRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=195,
  serialized_end=242,
)


_MUTATEBILLINGSETUPREQUEST = _descriptor.Descriptor(
  name='MutateBillingSetupRequest',
  full_name='google.ads.googleads.v0.services.MutateBillingSetupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v0.services.MutateBillingSetupRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='google.ads.googleads.v0.services.MutateBillingSetupRequest.operation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=244,
  serialized_end=368,
)


_BILLINGSETUPOPERATION = _descriptor.Descriptor(
  name='BillingSetupOperation',
  full_name='google.ads.googleads.v0.services.BillingSetupOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v0.services.BillingSetupOperation.create', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v0.services.BillingSetupOperation.remove', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='operation', full_name='google.ads.googleads.v0.services.BillingSetupOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=370,
  serialized_end=491,
)


_MUTATEBILLINGSETUPRESPONSE = _descriptor.Descriptor(
  name='MutateBillingSetupResponse',
  full_name='google.ads.googleads.v0.services.MutateBillingSetupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='google.ads.googleads.v0.services.MutateBillingSetupResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=493,
  serialized_end=597,
)


_MUTATEBILLINGSETUPRESULT = _descriptor.Descriptor(
  name='MutateBillingSetupResult',
  full_name='google.ads.googleads.v0.services.MutateBillingSetupResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.MutateBillingSetupResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=599,
  serialized_end=648,
)

_MUTATEBILLINGSETUPREQUEST.fields_by_name['operation'].message_type = _BILLINGSETUPOPERATION
_BILLINGSETUPOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_billing__setup__pb2._BILLINGSETUP
_BILLINGSETUPOPERATION.oneofs_by_name['operation'].fields.append(
  _BILLINGSETUPOPERATION.fields_by_name['create'])
_BILLINGSETUPOPERATION.fields_by_name['create'].containing_oneof = _BILLINGSETUPOPERATION.oneofs_by_name['operation']
_BILLINGSETUPOPERATION.oneofs_by_name['operation'].fields.append(
  _BILLINGSETUPOPERATION.fields_by_name['remove'])
_BILLINGSETUPOPERATION.fields_by_name['remove'].containing_oneof = _BILLINGSETUPOPERATION.oneofs_by_name['operation']
_MUTATEBILLINGSETUPRESPONSE.fields_by_name['result'].message_type = _MUTATEBILLINGSETUPRESULT
DESCRIPTOR.message_types_by_name['GetBillingSetupRequest'] = _GETBILLINGSETUPREQUEST
DESCRIPTOR.message_types_by_name['MutateBillingSetupRequest'] = _MUTATEBILLINGSETUPREQUEST
DESCRIPTOR.message_types_by_name['BillingSetupOperation'] = _BILLINGSETUPOPERATION
DESCRIPTOR.message_types_by_name['MutateBillingSetupResponse'] = _MUTATEBILLINGSETUPRESPONSE
DESCRIPTOR.message_types_by_name['MutateBillingSetupResult'] = _MUTATEBILLINGSETUPRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetBillingSetupRequest = _reflection.GeneratedProtocolMessageType('GetBillingSetupRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETBILLINGSETUPREQUEST,
  __module__ = 'google.ads.google_ads.v0.proto.services.billing_setup_service_pb2'
  ,
  __doc__ = """Request message for
  [BillingSetupService.GetBillingSetup][google.ads.googleads.v0.services.BillingSetupService.GetBillingSetup].
  
  
  Attributes:
      resource_name:
          The resource name of the billing setup to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.GetBillingSetupRequest)
  ))
_sym_db.RegisterMessage(GetBillingSetupRequest)

MutateBillingSetupRequest = _reflection.GeneratedProtocolMessageType('MutateBillingSetupRequest', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEBILLINGSETUPREQUEST,
  __module__ = 'google.ads.google_ads.v0.proto.services.billing_setup_service_pb2'
  ,
  __doc__ = """Request message for billing setup mutate operations.
  
  
  Attributes:
      customer_id:
          Id of the customer to apply the billing setup mutate operation
          to.
      operation:
          The operation to perform.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateBillingSetupRequest)
  ))
_sym_db.RegisterMessage(MutateBillingSetupRequest)

BillingSetupOperation = _reflection.GeneratedProtocolMessageType('BillingSetupOperation', (_message.Message,), dict(
  DESCRIPTOR = _BILLINGSETUPOPERATION,
  __module__ = 'google.ads.google_ads.v0.proto.services.billing_setup_service_pb2'
  ,
  __doc__ = """A single operation on a billing setup, which describes the cancellation
  of an existing billing setup.
  
  
  Attributes:
      operation:
          Only one of these operations can be set. "Update" operations
          are not supported.
      create:
          Creates a billing setup. No resource name is expected for the
          new billing setup.
      remove:
          Resource name of the billing setup to remove. A setup cannot
          be removed unless it is in a pending state or its scheduled
          start time is in the future. The resource name looks like
          ``customers/{customer_id}/billingSetups/{billing_id}``.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.BillingSetupOperation)
  ))
_sym_db.RegisterMessage(BillingSetupOperation)

MutateBillingSetupResponse = _reflection.GeneratedProtocolMessageType('MutateBillingSetupResponse', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEBILLINGSETUPRESPONSE,
  __module__ = 'google.ads.google_ads.v0.proto.services.billing_setup_service_pb2'
  ,
  __doc__ = """Response message for a billing setup operation.
  
  
  Attributes:
      result:
          A result that identifies the resource affected by the mutate
          request.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateBillingSetupResponse)
  ))
_sym_db.RegisterMessage(MutateBillingSetupResponse)

MutateBillingSetupResult = _reflection.GeneratedProtocolMessageType('MutateBillingSetupResult', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEBILLINGSETUPRESULT,
  __module__ = 'google.ads.google_ads.v0.proto.services.billing_setup_service_pb2'
  ,
  __doc__ = """Result for a single billing setup mutate.
  
  
  Attributes:
      resource_name:
          Returned for successful operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateBillingSetupResult)
  ))
_sym_db.RegisterMessage(MutateBillingSetupResult)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$com.google.ads.googleads.v0.servicesB\030BillingSetupServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V0.Services\312\002 Google\\Ads\\GoogleAds\\V0\\Services'))

_BILLINGSETUPSERVICE = _descriptor.ServiceDescriptor(
  name='BillingSetupService',
  full_name='google.ads.googleads.v0.services.BillingSetupService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=651,
  serialized_end=1065,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetBillingSetup',
    full_name='google.ads.googleads.v0.services.BillingSetupService.GetBillingSetup',
    index=0,
    containing_service=None,
    input_type=_GETBILLINGSETUPREQUEST,
    output_type=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_billing__setup__pb2._BILLINGSETUP,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0021\022//v0/{resource_name=customers/*/billingSetups/*}')),
  ),
  _descriptor.MethodDescriptor(
    name='MutateBillingSetup',
    full_name='google.ads.googleads.v0.services.BillingSetupService.MutateBillingSetup',
    index=1,
    containing_service=None,
    input_type=_MUTATEBILLINGSETUPREQUEST,
    output_type=_MUTATEBILLINGSETUPRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0027\"2/v0/customers/{customer_id=*}/billingSetups:mutate:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_BILLINGSETUPSERVICE)

DESCRIPTOR.services_by_name['BillingSetupService'] = _BILLINGSETUPSERVICE

# @@protoc_insertion_point(module_scope)
