# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: prediction.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='prediction.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10prediction.proto\"k\n\x11PredictionRequest\x12*\n\x07\x41nswers\x18\x01 \x03(\x0b\x32\x19.PredictionRequest.Answer\x1a*\n\x06\x41nswer\x12\x10\n\x08Question\x18\x01 \x01(\t\x12\x0e\n\x06\x41nswer\x18\x02 \x01(\t\"(\n\x12PredictionResponse\x12\x12\n\nprediction\x18\x01 \x01(\x02\x32?\n\tPredictor\x12\x32\n\x07Predict\x12\x12.PredictionRequest\x1a\x13.PredictionResponseb\x06proto3'
)




_PREDICTIONREQUEST_ANSWER = _descriptor.Descriptor(
  name='Answer',
  full_name='PredictionRequest.Answer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Question', full_name='PredictionRequest.Answer.Question', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Answer', full_name='PredictionRequest.Answer.Answer', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=127,
)

_PREDICTIONREQUEST = _descriptor.Descriptor(
  name='PredictionRequest',
  full_name='PredictionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Answers', full_name='PredictionRequest.Answers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PREDICTIONREQUEST_ANSWER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=127,
)


_PREDICTIONRESPONSE = _descriptor.Descriptor(
  name='PredictionResponse',
  full_name='PredictionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='prediction', full_name='PredictionResponse.prediction', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=169,
)

_PREDICTIONREQUEST_ANSWER.containing_type = _PREDICTIONREQUEST
_PREDICTIONREQUEST.fields_by_name['Answers'].message_type = _PREDICTIONREQUEST_ANSWER
DESCRIPTOR.message_types_by_name['PredictionRequest'] = _PREDICTIONREQUEST
DESCRIPTOR.message_types_by_name['PredictionResponse'] = _PREDICTIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PredictionRequest = _reflection.GeneratedProtocolMessageType('PredictionRequest', (_message.Message,), {

  'Answer' : _reflection.GeneratedProtocolMessageType('Answer', (_message.Message,), {
    'DESCRIPTOR' : _PREDICTIONREQUEST_ANSWER,
    '__module__' : 'prediction_pb2'
    # @@protoc_insertion_point(class_scope:PredictionRequest.Answer)
    })
  ,
  'DESCRIPTOR' : _PREDICTIONREQUEST,
  '__module__' : 'prediction_pb2'
  # @@protoc_insertion_point(class_scope:PredictionRequest)
  })
_sym_db.RegisterMessage(PredictionRequest)
_sym_db.RegisterMessage(PredictionRequest.Answer)

PredictionResponse = _reflection.GeneratedProtocolMessageType('PredictionResponse', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTIONRESPONSE,
  '__module__' : 'prediction_pb2'
  # @@protoc_insertion_point(class_scope:PredictionResponse)
  })
_sym_db.RegisterMessage(PredictionResponse)



_PREDICTOR = _descriptor.ServiceDescriptor(
  name='Predictor',
  full_name='Predictor',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=171,
  serialized_end=234,
  methods=[
  _descriptor.MethodDescriptor(
    name='Predict',
    full_name='Predictor.Predict',
    index=0,
    containing_service=None,
    input_type=_PREDICTIONREQUEST,
    output_type=_PREDICTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PREDICTOR)

DESCRIPTOR.services_by_name['Predictor'] = _PREDICTOR

# @@protoc_insertion_point(module_scope)
