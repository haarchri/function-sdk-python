# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crossplane/function/proto/v1/run_function.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/crossplane/function/proto/v1/run_function.proto\x12\x19\x61piextensions.fn.proto.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/duration.proto\"\x8d\x05\n\x12RunFunctionRequest\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32&.apiextensions.fn.proto.v1.RequestMeta\x12\x32\n\x08observed\x18\x02 \x01(\x0b\x32 .apiextensions.fn.proto.v1.State\x12\x31\n\x07\x64\x65sired\x18\x03 \x01(\x0b\x32 .apiextensions.fn.proto.v1.State\x12+\n\x05input\x18\x04 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x88\x01\x01\x12-\n\x07\x63ontext\x18\x05 \x01(\x0b\x32\x17.google.protobuf.StructH\x01\x88\x01\x01\x12Z\n\x0f\x65xtra_resources\x18\x06 \x03(\x0b\x32\x41.apiextensions.fn.proto.v1.RunFunctionRequest.ExtraResourcesEntry\x12S\n\x0b\x63redentials\x18\x07 \x03(\x0b\x32>.apiextensions.fn.proto.v1.RunFunctionRequest.CredentialsEntry\x1a[\n\x13\x45xtraResourcesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.apiextensions.fn.proto.v1.Resources:\x02\x38\x01\x1aZ\n\x10\x43redentialsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32&.apiextensions.fn.proto.v1.Credentials:\x02\x38\x01\x42\x08\n\x06_inputB\n\n\x08_context\"]\n\x0b\x43redentials\x12\x44\n\x0f\x63redential_data\x18\x01 \x01(\x0b\x32).apiextensions.fn.proto.v1.CredentialDataH\x00\x42\x08\n\x06source\"\x80\x01\n\x0e\x43redentialData\x12\x41\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x33.apiextensions.fn.proto.v1.CredentialData.DataEntry\x1a+\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"?\n\tResources\x12\x32\n\x05items\x18\x01 \x03(\x0b\x32#.apiextensions.fn.proto.v1.Resource\"\xe7\x02\n\x13RunFunctionResponse\x12\x35\n\x04meta\x18\x01 \x01(\x0b\x32\'.apiextensions.fn.proto.v1.ResponseMeta\x12\x31\n\x07\x64\x65sired\x18\x02 \x01(\x0b\x32 .apiextensions.fn.proto.v1.State\x12\x32\n\x07results\x18\x03 \x03(\x0b\x32!.apiextensions.fn.proto.v1.Result\x12-\n\x07\x63ontext\x18\x04 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x88\x01\x01\x12=\n\x0crequirements\x18\x05 \x01(\x0b\x32\'.apiextensions.fn.proto.v1.Requirements\x12\x38\n\nconditions\x18\x06 \x03(\x0b\x32$.apiextensions.fn.proto.v1.ConditionB\n\n\x08_context\"\x1a\n\x0bRequestMeta\x12\x0b\n\x03tag\x18\x01 \x01(\t\"\xc8\x01\n\x0cRequirements\x12T\n\x0f\x65xtra_resources\x18\x01 \x03(\x0b\x32;.apiextensions.fn.proto.v1.Requirements.ExtraResourcesEntry\x1a\x62\n\x13\x45xtraResourcesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b\x32+.apiextensions.fn.proto.v1.ResourceSelector:\x02\x38\x01\"\x94\x01\n\x10ResourceSelector\x12\x13\n\x0b\x61pi_version\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12\x14\n\nmatch_name\x18\x03 \x01(\tH\x00\x12>\n\x0cmatch_labels\x18\x04 \x01(\x0b\x32&.apiextensions.fn.proto.v1.MatchLabelsH\x00\x42\x07\n\x05match\"\x80\x01\n\x0bMatchLabels\x12\x42\n\x06labels\x18\x01 \x03(\x0b\x32\x32.apiextensions.fn.proto.v1.MatchLabels.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"P\n\x0cResponseMeta\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12+\n\x03ttl\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationH\x00\x88\x01\x01\x42\x06\n\x04_ttl\"\xda\x01\n\x05State\x12\x36\n\tcomposite\x18\x01 \x01(\x0b\x32#.apiextensions.fn.proto.v1.Resource\x12\x42\n\tresources\x18\x02 \x03(\x0b\x32/.apiextensions.fn.proto.v1.State.ResourcesEntry\x1aU\n\x0eResourcesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x32\n\x05value\x18\x02 \x01(\x0b\x32#.apiextensions.fn.proto.v1.Resource:\x02\x38\x01\"\xf8\x01\n\x08Resource\x12)\n\x08resource\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12V\n\x12\x63onnection_details\x18\x02 \x03(\x0b\x32:.apiextensions.fn.proto.v1.Resource.ConnectionDetailsEntry\x12/\n\x05ready\x18\x03 \x01(\x0e\x32 .apiextensions.fn.proto.v1.Ready\x1a\x38\n\x16\x43onnectionDetailsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\xb3\x01\n\x06Result\x12\x35\n\x08severity\x18\x01 \x01(\x0e\x32#.apiextensions.fn.proto.v1.Severity\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x13\n\x06reason\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x36\n\x06target\x18\x04 \x01(\x0e\x32!.apiextensions.fn.proto.v1.TargetH\x01\x88\x01\x01\x42\t\n\x07_reasonB\t\n\x07_target\"\xc1\x01\n\tCondition\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x31\n\x06status\x18\x02 \x01(\x0e\x32!.apiextensions.fn.proto.v1.Status\x12\x0e\n\x06reason\x18\x03 \x01(\t\x12\x14\n\x07message\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x36\n\x06target\x18\x05 \x01(\x0e\x32!.apiextensions.fn.proto.v1.TargetH\x01\x88\x01\x01\x42\n\n\x08_messageB\t\n\x07_target*?\n\x05Ready\x12\x15\n\x11READY_UNSPECIFIED\x10\x00\x12\x0e\n\nREADY_TRUE\x10\x01\x12\x0f\n\x0bREADY_FALSE\x10\x02*c\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x12\n\x0eSEVERITY_FATAL\x10\x01\x12\x14\n\x10SEVERITY_WARNING\x10\x02\x12\x13\n\x0fSEVERITY_NORMAL\x10\x03*V\n\x06Target\x12\x16\n\x12TARGET_UNSPECIFIED\x10\x00\x12\x14\n\x10TARGET_COMPOSITE\x10\x01\x12\x1e\n\x1aTARGET_COMPOSITE_AND_CLAIM\x10\x02*\x7f\n\x06Status\x12 \n\x1cSTATUS_CONDITION_UNSPECIFIED\x10\x00\x12\x1c\n\x18STATUS_CONDITION_UNKNOWN\x10\x01\x12\x19\n\x15STATUS_CONDITION_TRUE\x10\x02\x12\x1a\n\x16STATUS_CONDITION_FALSE\x10\x03\x32\x87\x01\n\x15\x46unctionRunnerService\x12n\n\x0bRunFunction\x12-.apiextensions.fn.proto.v1.RunFunctionRequest\x1a..apiextensions.fn.proto.v1.RunFunctionResponse\"\x00\x42\x41Z?github.com/crossplane/crossplane/apis/apiextensions/fn/proto/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'crossplane.function.proto.v1.run_function_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z?github.com/crossplane/crossplane/apis/apiextensions/fn/proto/v1'
  _globals['_RUNFUNCTIONREQUEST_EXTRARESOURCESENTRY']._loaded_options = None
  _globals['_RUNFUNCTIONREQUEST_EXTRARESOURCESENTRY']._serialized_options = b'8\001'
  _globals['_RUNFUNCTIONREQUEST_CREDENTIALSENTRY']._loaded_options = None
  _globals['_RUNFUNCTIONREQUEST_CREDENTIALSENTRY']._serialized_options = b'8\001'
  _globals['_CREDENTIALDATA_DATAENTRY']._loaded_options = None
  _globals['_CREDENTIALDATA_DATAENTRY']._serialized_options = b'8\001'
  _globals['_REQUIREMENTS_EXTRARESOURCESENTRY']._loaded_options = None
  _globals['_REQUIREMENTS_EXTRARESOURCESENTRY']._serialized_options = b'8\001'
  _globals['_MATCHLABELS_LABELSENTRY']._loaded_options = None
  _globals['_MATCHLABELS_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_STATE_RESOURCESENTRY']._loaded_options = None
  _globals['_STATE_RESOURCESENTRY']._serialized_options = b'8\001'
  _globals['_RESOURCE_CONNECTIONDETAILSENTRY']._loaded_options = None
  _globals['_RESOURCE_CONNECTIONDETAILSENTRY']._serialized_options = b'8\001'
  _globals['_READY']._serialized_start=2894
  _globals['_READY']._serialized_end=2957
  _globals['_SEVERITY']._serialized_start=2959
  _globals['_SEVERITY']._serialized_end=3058
  _globals['_TARGET']._serialized_start=3060
  _globals['_TARGET']._serialized_end=3146
  _globals['_STATUS']._serialized_start=3148
  _globals['_STATUS']._serialized_end=3275
  _globals['_RUNFUNCTIONREQUEST']._serialized_start=141
  _globals['_RUNFUNCTIONREQUEST']._serialized_end=794
  _globals['_RUNFUNCTIONREQUEST_EXTRARESOURCESENTRY']._serialized_start=589
  _globals['_RUNFUNCTIONREQUEST_EXTRARESOURCESENTRY']._serialized_end=680
  _globals['_RUNFUNCTIONREQUEST_CREDENTIALSENTRY']._serialized_start=682
  _globals['_RUNFUNCTIONREQUEST_CREDENTIALSENTRY']._serialized_end=772
  _globals['_CREDENTIALS']._serialized_start=796
  _globals['_CREDENTIALS']._serialized_end=889
  _globals['_CREDENTIALDATA']._serialized_start=892
  _globals['_CREDENTIALDATA']._serialized_end=1020
  _globals['_CREDENTIALDATA_DATAENTRY']._serialized_start=977
  _globals['_CREDENTIALDATA_DATAENTRY']._serialized_end=1020
  _globals['_RESOURCES']._serialized_start=1022
  _globals['_RESOURCES']._serialized_end=1085
  _globals['_RUNFUNCTIONRESPONSE']._serialized_start=1088
  _globals['_RUNFUNCTIONRESPONSE']._serialized_end=1447
  _globals['_REQUESTMETA']._serialized_start=1449
  _globals['_REQUESTMETA']._serialized_end=1475
  _globals['_REQUIREMENTS']._serialized_start=1478
  _globals['_REQUIREMENTS']._serialized_end=1678
  _globals['_REQUIREMENTS_EXTRARESOURCESENTRY']._serialized_start=1580
  _globals['_REQUIREMENTS_EXTRARESOURCESENTRY']._serialized_end=1678
  _globals['_RESOURCESELECTOR']._serialized_start=1681
  _globals['_RESOURCESELECTOR']._serialized_end=1829
  _globals['_MATCHLABELS']._serialized_start=1832
  _globals['_MATCHLABELS']._serialized_end=1960
  _globals['_MATCHLABELS_LABELSENTRY']._serialized_start=1915
  _globals['_MATCHLABELS_LABELSENTRY']._serialized_end=1960
  _globals['_RESPONSEMETA']._serialized_start=1962
  _globals['_RESPONSEMETA']._serialized_end=2042
  _globals['_STATE']._serialized_start=2045
  _globals['_STATE']._serialized_end=2263
  _globals['_STATE_RESOURCESENTRY']._serialized_start=2178
  _globals['_STATE_RESOURCESENTRY']._serialized_end=2263
  _globals['_RESOURCE']._serialized_start=2266
  _globals['_RESOURCE']._serialized_end=2514
  _globals['_RESOURCE_CONNECTIONDETAILSENTRY']._serialized_start=2458
  _globals['_RESOURCE_CONNECTIONDETAILSENTRY']._serialized_end=2514
  _globals['_RESULT']._serialized_start=2517
  _globals['_RESULT']._serialized_end=2696
  _globals['_CONDITION']._serialized_start=2699
  _globals['_CONDITION']._serialized_end=2892
  _globals['_FUNCTIONRUNNERSERVICE']._serialized_start=3278
  _globals['_FUNCTIONRUNNERSERVICE']._serialized_end=3413
# @@protoc_insertion_point(module_scope)
