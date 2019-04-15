# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alameda_api/v1alpha1/datahub/types.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='alameda_api/v1alpha1/datahub/types.proto',
  package='containers_ai.alameda.v1alpha1.datahub',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n(alameda_api/v1alpha1/datahub/types.proto\x12&containers_ai.alameda.v1alpha1.datahub\x1a\x1fgoogle/protobuf/timestamp.proto\"8\n\x15\x43ontainerStateWaiting\x12\x0e\n\x06reason\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"G\n\x15\x43ontainerStateRunning\x12.\n\nstarted_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xaf\x01\n\x18\x43ontainerStateTerminated\x12\x11\n\texit_code\x18\x01 \x01(\x05\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12.\n\nstarted_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x66inished_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x86\x02\n\x0e\x43ontainerState\x12N\n\x07waiting\x18\x01 \x01(\x0b\x32=.containers_ai.alameda.v1alpha1.datahub.ContainerStateWaiting\x12N\n\x07running\x18\x02 \x01(\x0b\x32=.containers_ai.alameda.v1alpha1.datahub.ContainerStateRunning\x12T\n\nterminated\x18\x03 \x01(\x0b\x32@.containers_ai.alameda.v1alpha1.datahub.ContainerStateTerminated\"\xc7\x01\n\x0f\x43ontainerStatus\x12\x45\n\x05state\x18\x01 \x01(\x0b\x32\x36.containers_ai.alameda.v1alpha1.datahub.ContainerState\x12V\n\x16last_termination_state\x18\x02 \x01(\x0b\x32\x36.containers_ai.alameda.v1alpha1.datahub.ContainerState\x12\x15\n\rrestart_count\x18\x03 \x01(\x05\"m\n\tPodStatus\x12?\n\x05phase\x18\x01 \x01(\x0e\x32\x30.containers_ai.alameda.v1alpha1.datahub.PodPhase\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0e\n\x06reason\x18\x03 \x01(\t*\x80\x01\n\x08PodPhase\x12\r\n\tUndefined\x10\x00\x12\x0b\n\x07Pending\x10\x01\x12\x0b\n\x07Running\x10\x02\x12\r\n\tSucceeded\x10\x03\x12\n\n\x06\x46\x61iled\x10\x04\x12\x0b\n\x07Unknown\x10\x05\x12\r\n\tCompleted\x10\x06\x12\x14\n\x10\x43rashLoopBackOff\x10\x07\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_PODPHASE = _descriptor.EnumDescriptor(
  name='PodPhase',
  full_name='containers_ai.alameda.v1alpha1.datahub.PodPhase',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Undefined', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Pending', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Running', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Succeeded', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Failed', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Completed', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CrashLoopBackOff', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1005,
  serialized_end=1133,
)
_sym_db.RegisterEnumDescriptor(_PODPHASE)

PodPhase = enum_type_wrapper.EnumTypeWrapper(_PODPHASE)
Undefined = 0
Pending = 1
Running = 2
Succeeded = 3
Failed = 4
Unknown = 5
Completed = 6
CrashLoopBackOff = 7



_CONTAINERSTATEWAITING = _descriptor.Descriptor(
  name='ContainerStateWaiting',
  full_name='containers_ai.alameda.v1alpha1.datahub.ContainerStateWaiting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reason', full_name='containers_ai.alameda.v1alpha1.datahub.ContainerStateWaiting.reason', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='containers_ai.alameda.v1alpha1.datahub.ContainerStateWaiting.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=117,
  serialized_end=173,
)


_CONTAINERSTATERUNNING = _descriptor.Descriptor(
  name='ContainerStateRunning',
  full_name='containers_ai.alameda.v1alpha1.datahub.ContainerStateRunning',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='started_at', full_name='containers_ai.alameda.v1alpha1.datahub.ContainerStateRunning.started_at', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=175,
  serialized_end=246,
)


_CONTAINERSTATETERMINATED = _descriptor.Descriptor(
  name='ContainerStateTerminated',
  full_name='containers_ai.alameda.v1alpha1.datahub.ContainerStateTerminated',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exit_code', full_name='containers_ai.alameda.v1alpha1.datahub.ContainerStateTerminated.exit_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='containers_ai.alameda.v1alpha1.datahub.ContainerStateTerminated.reason', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='containers_ai.alameda.v1alpha1.datahub.ContainerStateTerminated.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='started_at', full_name='containers_ai.alameda.v1alpha1.datahub.ContainerStateTerminated.started_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finished_at', full_name='containers_ai.alameda.v1alpha1.datahub.ContainerStateTerminated.finished_at', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=249,
  serialized_end=424,
)


_CONTAINERSTATE = _descriptor.Descriptor(
  name='ContainerState',
  full_name='containers_ai.alameda.v1alpha1.datahub.ContainerState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='waiting', full_name='containers_ai.alameda.v1alpha1.datahub.ContainerState.waiting', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='running', full_name='containers_ai.alameda.v1alpha1.datahub.ContainerState.running', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='terminated', full_name='containers_ai.alameda.v1alpha1.datahub.ContainerState.terminated', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=427,
  serialized_end=689,
)


_CONTAINERSTATUS = _descriptor.Descriptor(
  name='ContainerStatus',
  full_name='containers_ai.alameda.v1alpha1.datahub.ContainerStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='containers_ai.alameda.v1alpha1.datahub.ContainerStatus.state', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_termination_state', full_name='containers_ai.alameda.v1alpha1.datahub.ContainerStatus.last_termination_state', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='restart_count', full_name='containers_ai.alameda.v1alpha1.datahub.ContainerStatus.restart_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=692,
  serialized_end=891,
)


_PODSTATUS = _descriptor.Descriptor(
  name='PodStatus',
  full_name='containers_ai.alameda.v1alpha1.datahub.PodStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phase', full_name='containers_ai.alameda.v1alpha1.datahub.PodStatus.phase', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='containers_ai.alameda.v1alpha1.datahub.PodStatus.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='containers_ai.alameda.v1alpha1.datahub.PodStatus.reason', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=893,
  serialized_end=1002,
)

_CONTAINERSTATERUNNING.fields_by_name['started_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CONTAINERSTATETERMINATED.fields_by_name['started_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CONTAINERSTATETERMINATED.fields_by_name['finished_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CONTAINERSTATE.fields_by_name['waiting'].message_type = _CONTAINERSTATEWAITING
_CONTAINERSTATE.fields_by_name['running'].message_type = _CONTAINERSTATERUNNING
_CONTAINERSTATE.fields_by_name['terminated'].message_type = _CONTAINERSTATETERMINATED
_CONTAINERSTATUS.fields_by_name['state'].message_type = _CONTAINERSTATE
_CONTAINERSTATUS.fields_by_name['last_termination_state'].message_type = _CONTAINERSTATE
_PODSTATUS.fields_by_name['phase'].enum_type = _PODPHASE
DESCRIPTOR.message_types_by_name['ContainerStateWaiting'] = _CONTAINERSTATEWAITING
DESCRIPTOR.message_types_by_name['ContainerStateRunning'] = _CONTAINERSTATERUNNING
DESCRIPTOR.message_types_by_name['ContainerStateTerminated'] = _CONTAINERSTATETERMINATED
DESCRIPTOR.message_types_by_name['ContainerState'] = _CONTAINERSTATE
DESCRIPTOR.message_types_by_name['ContainerStatus'] = _CONTAINERSTATUS
DESCRIPTOR.message_types_by_name['PodStatus'] = _PODSTATUS
DESCRIPTOR.enum_types_by_name['PodPhase'] = _PODPHASE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ContainerStateWaiting = _reflection.GeneratedProtocolMessageType('ContainerStateWaiting', (_message.Message,), dict(
  DESCRIPTOR = _CONTAINERSTATEWAITING,
  __module__ = 'alameda_api.v1alpha1.datahub.types_pb2'
  # @@protoc_insertion_point(class_scope:containers_ai.alameda.v1alpha1.datahub.ContainerStateWaiting)
  ))
_sym_db.RegisterMessage(ContainerStateWaiting)

ContainerStateRunning = _reflection.GeneratedProtocolMessageType('ContainerStateRunning', (_message.Message,), dict(
  DESCRIPTOR = _CONTAINERSTATERUNNING,
  __module__ = 'alameda_api.v1alpha1.datahub.types_pb2'
  # @@protoc_insertion_point(class_scope:containers_ai.alameda.v1alpha1.datahub.ContainerStateRunning)
  ))
_sym_db.RegisterMessage(ContainerStateRunning)

ContainerStateTerminated = _reflection.GeneratedProtocolMessageType('ContainerStateTerminated', (_message.Message,), dict(
  DESCRIPTOR = _CONTAINERSTATETERMINATED,
  __module__ = 'alameda_api.v1alpha1.datahub.types_pb2'
  # @@protoc_insertion_point(class_scope:containers_ai.alameda.v1alpha1.datahub.ContainerStateTerminated)
  ))
_sym_db.RegisterMessage(ContainerStateTerminated)

ContainerState = _reflection.GeneratedProtocolMessageType('ContainerState', (_message.Message,), dict(
  DESCRIPTOR = _CONTAINERSTATE,
  __module__ = 'alameda_api.v1alpha1.datahub.types_pb2'
  # @@protoc_insertion_point(class_scope:containers_ai.alameda.v1alpha1.datahub.ContainerState)
  ))
_sym_db.RegisterMessage(ContainerState)

ContainerStatus = _reflection.GeneratedProtocolMessageType('ContainerStatus', (_message.Message,), dict(
  DESCRIPTOR = _CONTAINERSTATUS,
  __module__ = 'alameda_api.v1alpha1.datahub.types_pb2'
  # @@protoc_insertion_point(class_scope:containers_ai.alameda.v1alpha1.datahub.ContainerStatus)
  ))
_sym_db.RegisterMessage(ContainerStatus)

PodStatus = _reflection.GeneratedProtocolMessageType('PodStatus', (_message.Message,), dict(
  DESCRIPTOR = _PODSTATUS,
  __module__ = 'alameda_api.v1alpha1.datahub.types_pb2'
  # @@protoc_insertion_point(class_scope:containers_ai.alameda.v1alpha1.datahub.PodStatus)
  ))
_sym_db.RegisterMessage(PodStatus)


# @@protoc_insertion_point(module_scope)
