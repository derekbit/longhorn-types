# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spdkrpc/spdk.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12spdkrpc/spdk.proto\x12\x07spdkrpc\x1a\x1bgoogle/protobuf/empty.proto\"\x83\x02\n\x04Lvol\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x11\n\tspec_size\x18\x03 \x01(\x04\x12\x13\n\x0b\x61\x63tual_size\x18\x04 \x01(\x04\x12\x0e\n\x06parent\x18\x05 \x01(\t\x12-\n\x08\x63hildren\x18\x06 \x03(\x0b\x32\x1b.spdkrpc.Lvol.ChildrenEntry\x12\x15\n\rcreation_time\x18\x07 \x01(\t\x12\x14\n\x0cuser_created\x18\x08 \x01(\x08\x12\x1a\n\x12snapshot_timestamp\x18\t \x01(\t\x1a/\n\rChildrenEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\"\xdd\x02\n\x07Replica\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08lvs_name\x18\x02 \x01(\t\x12\x10\n\x08lvs_uuid\x18\x03 \x01(\t\x12\x11\n\tspec_size\x18\x04 \x01(\x04\x12\x13\n\x0b\x61\x63tual_size\x18\x05 \x01(\x04\x12\n\n\x02ip\x18\x06 \x01(\t\x12\x12\n\nport_start\x18\x07 \x01(\x05\x12\x10\n\x08port_end\x18\x08 \x01(\x05\x12\x1b\n\x04head\x18\t \x01(\x0b\x32\r.spdkrpc.Lvol\x12\x32\n\tsnapshots\x18\n \x03(\x0b\x32\x1f.spdkrpc.Replica.SnapshotsEntry\x12\x12\n\nrebuilding\x18\x0b \x01(\x08\x12\r\n\x05state\x18\x0c \x01(\t\x12\x11\n\terror_msg\x18\r \x01(\t\x1a?\n\x0eSnapshotsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.spdkrpc.Lvol:\x02\x38\x01\"o\n\x14ReplicaCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08lvs_name\x18\x02 \x01(\t\x12\x10\n\x08lvs_uuid\x18\x03 \x01(\t\x12\x11\n\tspec_size\x18\x04 \x01(\x04\x12\x12\n\nport_count\x18\x05 \x01(\x05\">\n\x14ReplicaDeleteRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10\x63leanup_required\x18\x02 \x01(\x08\"!\n\x11ReplicaGetRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x96\x01\n\x13ReplicaListResponse\x12<\n\x08replicas\x18\x01 \x03(\x0b\x32*.spdkrpc.ReplicaListResponse.ReplicasEntry\x1a\x41\n\rReplicasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.spdkrpc.Replica:\x02\x38\x01\"\x86\x01\n ReplicaRebuildingSrcStartRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10\x64st_replica_name\x18\x02 \x01(\t\x12\x1b\n\x13\x64st_replica_address\x18\x03 \x01(\t\x12\x1d\n\x15\x65xposed_snapshot_name\x18\x04 \x01(\t\"J\n!ReplicaRebuildingSrcStartResponse\x12%\n\x1d\x65xposed_snapshot_lvol_address\x18\x01 \x01(\t\"K\n!ReplicaRebuildingSrcFinishRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10\x64st_replica_name\x18\x02 \x01(\t\"p\n!ReplicaRebuildingSrcAttachRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10\x64st_replica_name\x18\x02 \x01(\t\x12#\n\x1b\x64st_rebuilding_lvol_address\x18\x03 \x01(\t\"K\n!ReplicaRebuildingSrcDetachRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10\x64st_replica_name\x18\x02 \x01(\t\"R\n+ReplicaRebuildingSrcShallowCopyStartRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rsnapshot_name\x18\x02 \x01(\t\"J\n,ReplicaRebuildingSrcShallowCopyStartResponse\x12\x1a\n\x12shallow_copy_op_id\x18\x01 \x01(\r\"\x88\x01\n+ReplicaRebuildingSrcShallowCopyCheckRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10\x64st_replica_name\x18\x02 \x01(\t\x12\x15\n\rsnapshot_name\x18\x03 \x01(\t\x12\x1a\n\x12shallow_copy_op_id\x18\x04 \x01(\r\"\x81\x01\n,ReplicaRebuildingSrcShallowCopyCheckResponse\x12\r\n\x05state\x18\x01 \x01(\t\x12\x17\n\x0f\x63opied_clusters\x18\x02 \x01(\x04\x12\x16\n\x0etotal_clusters\x18\x03 \x01(\x04\x12\x11\n\terror_msg\x18\x04 \x01(\t\"\xdb\x01\n ReplicaRebuildingDstStartRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10src_replica_name\x18\x02 \x01(\t\x12\x1b\n\x13src_replica_address\x18\x03 \x01(\t\x12\x1e\n\x16\x65xternal_snapshot_name\x18\x04 \x01(\t\x12!\n\x19\x65xternal_snapshot_address\x18\x05 \x01(\t\x12/\n\x18rebuilding_snapshot_list\x18\x06 \x03(\x0b\x32\r.spdkrpc.Lvol\"B\n!ReplicaRebuildingDstStartResponse\x12\x1d\n\x15\x64st_head_lvol_address\x18\x01 \x01(\t\"1\n!ReplicaRebuildingDstFinishRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"R\n+ReplicaRebuildingDstShallowCopyStartRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rsnapshot_name\x18\x02 \x01(\t\";\n+ReplicaRebuildingDstShallowCopyCheckRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xd9\x01\n,ReplicaRebuildingDstShallowCopyCheckResponse\x12\x18\n\x10src_replica_name\x18\x01 \x01(\t\x12\x1b\n\x13src_replica_address\x18\x02 \x01(\t\x12\x15\n\rsnapshot_name\x18\x03 \x01(\t\x12\r\n\x05state\x18\x04 \x01(\t\x12\x10\n\x08progress\x18\x05 \x01(\r\x12\x13\n\x0btotal_state\x18\x06 \x01(\t\x12\x16\n\x0etotal_progress\x18\x07 \x01(\r\x12\r\n\x05\x65rror\x18\x08 \x01(\t\"Q\n*ReplicaRebuildingDstSnapshotRevertResponse\x12#\n\x1b\x64st_rebuilding_lvol_address\x18\x01 \x01(\t\"\x94\x05\n\x06\x45ngine\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bvolume_name\x18\x02 \x01(\t\x12\x11\n\tspec_size\x18\x03 \x01(\x04\x12\x13\n\x0b\x61\x63tual_size\x18\x04 \x01(\x04\x12\n\n\x02ip\x18\x05 \x01(\t\x12\x0c\n\x04port\x18\x06 \x01(\x05\x12\x43\n\x13replica_address_map\x18\x07 \x03(\x0b\x32&.spdkrpc.Engine.ReplicaAddressMapEntry\x12=\n\x10replica_mode_map\x18\x08 \x03(\x0b\x32#.spdkrpc.Engine.ReplicaModeMapEntry\x12\x1b\n\x04head\x18\t \x01(\x0b\x32\r.spdkrpc.Lvol\x12\x31\n\tsnapshots\x18\n \x03(\x0b\x32\x1e.spdkrpc.Engine.SnapshotsEntry\x12\x10\n\x08\x66rontend\x18\x0b \x01(\t\x12\x10\n\x08\x65ndpoint\x18\x0c \x01(\t\x12\r\n\x05state\x18\r \x01(\t\x12\x11\n\terror_msg\x18\x0e \x01(\t\x12\x11\n\ttarget_ip\x18\x0f \x01(\t\x12\x13\n\x0btarget_port\x18\x10 \x01(\x05\x12\x1b\n\x13standby_target_port\x18\x11 \x01(\x05\x1a\x38\n\x16ReplicaAddressMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aK\n\x13ReplicaModeMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0e\x32\x14.spdkrpc.ReplicaMode:\x02\x38\x01\x1a?\n\x0eSnapshotsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.spdkrpc.Lvol:\x02\x38\x01\"\xe5\x02\n\x13\x45ngineCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bvolume_name\x18\x02 \x01(\t\x12\x11\n\tspec_size\x18\x03 \x01(\x04\x12P\n\x13replica_address_map\x18\x04 \x03(\x0b\x32\x33.spdkrpc.EngineCreateRequest.ReplicaAddressMapEntry\x12\x10\n\x08\x66rontend\x18\x05 \x01(\t\x12\x12\n\nport_count\x18\x06 \x01(\x05\x12\x18\n\x10upgrade_required\x18\x07 \x01(\x08\x12\x19\n\x11initiator_address\x18\x08 \x01(\t\x12\x16\n\x0etarget_address\x18\t \x01(\t\x12\x19\n\x11salvage_requested\x18\n \x01(\x08\x1a\x38\n\x16ReplicaAddressMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"#\n\x13\x45ngineDeleteRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\" \n\x10\x45ngineGetRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"$\n\x14\x45ngineSuspendRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"#\n\x13\x45ngineResumeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"E\n\x1d\x45ngineSwitchOverTargetRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0etarget_address\x18\x02 \x01(\t\")\n\x19\x45ngineDeleteTargetRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x90\x01\n\x12\x45ngineListResponse\x12\x39\n\x07\x65ngines\x18\x01 \x03(\x0b\x32(.spdkrpc.EngineListResponse.EnginesEntry\x1a?\n\x0c\x45nginesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.spdkrpc.Engine:\x02\x38\x01\"]\n\x17\x45ngineReplicaAddRequest\x12\x13\n\x0b\x65ngine_name\x18\x01 \x01(\t\x12\x14\n\x0creplica_name\x18\x02 \x01(\t\x12\x17\n\x0freplica_address\x18\x03 \x01(\t\"/\n\x18\x45ngineReplicaListRequest\x12\x13\n\x0b\x65ngine_name\x18\x01 \x01(\t\"\xa2\x01\n\x19\x45ngineReplicaListResponse\x12\x42\n\x08replicas\x18\x01 \x03(\x0b\x32\x30.spdkrpc.EngineReplicaListResponse.ReplicasEntry\x1a\x41\n\rReplicasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.spdkrpc.Replica:\x02\x38\x01\"`\n\x1a\x45ngineReplicaDeleteRequest\x12\x13\n\x0b\x65ngine_name\x18\x01 \x01(\t\x12\x14\n\x0creplica_name\x18\x02 \x01(\t\x12\x17\n\x0freplica_address\x18\x03 \x01(\t\"N\n!EngineReplicaRebuildStatusRequest\x12\x13\n\x0b\x65ngine_name\x18\x01 \x01(\t\x12\x14\n\x0creplica_name\x18\x02 \x01(\t\"\xb8\x01\n\"EngineReplicaRebuildStatusResponse\x12\x14\n\x0creplica_name\x18\x01 \x01(\t\x12\x15\n\rsnapshot_name\x18\x02 \x01(\t\x12\r\n\x05state\x18\x03 \x01(\t\x12\x10\n\x08progress\x18\x04 \x01(\x05\x12\r\n\x05\x65rror\x18\x05 \x01(\t\x12\x18\n\x10src_replica_name\x18\x06 \x01(\t\x12\x1b\n\x13src_replica_address\x18\x07 \x01(\t\"h\n\x0fSnapshotRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rsnapshot_name\x18\x02 \x01(\t\x12\x14\n\x0cuser_created\x18\x03 \x01(\x08\x12\x1a\n\x12snapshot_timestamp\x18\x04 \x01(\t\")\n\x10SnapshotResponse\x12\x15\n\rsnapshot_name\x18\x01 \x01(\t\"\xef\x01\n\rVersionOutput\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x11\n\tgitCommit\x18\x02 \x01(\t\x12\x11\n\tbuildDate\x18\x03 \x01(\t\x12\x15\n\rcliAPIVersion\x18\x04 \x01(\x03\x12\x18\n\x10\x63liAPIMinVersion\x18\x05 \x01(\x03\x12\x1c\n\x14\x63ontrollerAPIVersion\x18\x06 \x01(\x03\x12\x1f\n\x17\x63ontrollerAPIMinVersion\x18\x07 \x01(\x03\x12\x19\n\x11\x64\x61taFormatVersion\x18\x08 \x01(\x03\x12\x1c\n\x14\x64\x61taFormatMinVersion\x18\t \x01(\x03\"@\n\x15VersionDetailGetReply\x12\'\n\x07version\x18\x01 \x01(\x0b\x32\x16.spdkrpc.VersionOutput\"\xb9\x03\n\x13\x42\x61\x63kupCreateRequest\x12\x15\n\rsnapshot_name\x18\x01 \x01(\t\x12\x15\n\rbackup_target\x18\x02 \x01(\t\x12\x13\n\x0bvolume_name\x18\x03 \x01(\t\x12\x0c\n\x04size\x18\x04 \x01(\x03\x12\x13\n\x0b\x65ngine_name\x18\x05 \x01(\t\x12\x14\n\x0creplica_name\x18\x06 \x01(\t\x12\x0e\n\x06labels\x18\x07 \x03(\t\x12@\n\ncredential\x18\x08 \x03(\x0b\x32,.spdkrpc.BackupCreateRequest.CredentialEntry\x12\x1a\n\x12\x62\x61\x63king_image_name\x18\t \x01(\t\x12\x1e\n\x16\x62\x61\x63king_image_checksum\x18\n \x01(\t\x12\x13\n\x0b\x62\x61\x63kup_name\x18\x0b \x01(\t\x12\x1a\n\x12\x63ompression_method\x18\x0c \x01(\t\x12\x18\n\x10\x63oncurrent_limit\x18\r \x01(\x05\x12\x1a\n\x12storage_class_name\x18\x0e \x01(\t\x1a\x31\n\x0f\x43redentialEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"W\n\x14\x42\x61\x63kupCreateResponse\x12\x0e\n\x06\x62\x61\x63kup\x18\x01 \x01(\t\x12\x16\n\x0eis_incremental\x18\x02 \x01(\x08\x12\x17\n\x0freplica_address\x18\x03 \x01(\t\"S\n\x13\x42\x61\x63kupStatusRequest\x12\x0e\n\x06\x62\x61\x63kup\x18\x01 \x01(\t\x12\x13\n\x0b\x65ngine_name\x18\x02 \x01(\t\x12\x17\n\x0freplica_address\x18\x03 \x01(\t\"\x8a\x01\n\x14\x42\x61\x63kupStatusResponse\x12\x10\n\x08progress\x18\x01 \x01(\x05\x12\x12\n\nbackup_url\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x15\n\rsnapshot_name\x18\x04 \x01(\t\x12\r\n\x05state\x18\x05 \x01(\t\x12\x17\n\x0freplica_address\x18\x06 \x01(\t\"\xf2\x01\n\x1a\x45ngineBackupRestoreRequest\x12\x12\n\nbackup_url\x18\x01 \x01(\t\x12\x13\n\x0b\x65ngine_name\x18\x02 \x01(\t\x12\x15\n\rsnapshot_name\x18\x03 \x01(\t\x12G\n\ncredential\x18\x04 \x03(\x0b\x32\x33.spdkrpc.EngineBackupRestoreRequest.CredentialEntry\x12\x18\n\x10\x63oncurrent_limit\x18\x05 \x01(\x05\x1a\x31\n\x0f\x43redentialEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8e\x01\n\x1b\x45ngineBackupRestoreResponse\x12@\n\x06\x65rrors\x18\x04 \x03(\x0b\x32\x30.spdkrpc.EngineBackupRestoreResponse.ErrorsEntry\x1a-\n\x0b\x45rrorsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"7\n EngineBackupRestoreFinishRequest\x12\x13\n\x0b\x65ngine_name\x18\x01 \x01(\t\"\xf5\x01\n\x1bReplicaBackupRestoreRequest\x12\x12\n\nbackup_url\x18\x01 \x01(\t\x12\x14\n\x0creplica_name\x18\x02 \x01(\t\x12\x15\n\rsnapshot_name\x18\x03 \x01(\t\x12H\n\ncredential\x18\x04 \x03(\x0b\x32\x34.spdkrpc.ReplicaBackupRestoreRequest.CredentialEntry\x12\x18\n\x10\x63oncurrent_limit\x18\x05 \x01(\x05\x1a\x31\n\x0f\x43redentialEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"+\n\x14RestoreStatusRequest\x12\x13\n\x0b\x65ngine_name\x18\x01 \x01(\t\"3\n\x1bReplicaRestoreStatusRequest\x12\x14\n\x0creplica_name\x18\x02 \x01(\t\"\xf8\x01\n\x1cReplicaRestoreStatusResponse\x12\x14\n\x0creplica_name\x18\x01 \x01(\t\x12\x17\n\x0freplica_address\x18\x02 \x01(\t\x12\x14\n\x0cis_restoring\x18\x03 \x01(\x08\x12\x15\n\rlast_restored\x18\x04 \x01(\t\x12\x10\n\x08progress\x18\x05 \x01(\x05\x12\r\n\x05\x65rror\x18\x06 \x01(\t\x12\x16\n\x0e\x64\x65st_file_name\x18\x07 \x01(\t\x12\r\n\x05state\x18\x08 \x01(\t\x12\x12\n\nbackup_url\x18\t \x01(\t\x12 \n\x18\x63urrent_restoring_backup\x18\n \x01(\t\"\xa9\x01\n\x15RestoreStatusResponse\x12:\n\x06status\x18\x01 \x03(\x0b\x32*.spdkrpc.RestoreStatusResponse.StatusEntry\x1aT\n\x0bStatusEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.spdkrpc.ReplicaRestoreStatusResponse:\x02\x38\x01\"\xd6\x01\n\x04\x44isk\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x12\n\ntotal_size\x18\x05 \x01(\x03\x12\x11\n\tfree_size\x18\x06 \x01(\x03\x12\x14\n\x0ctotal_blocks\x18\x07 \x01(\x03\x12\x13\n\x0b\x66ree_blocks\x18\x08 \x01(\x03\x12\x12\n\nblock_size\x18\t \x01(\x03\x12\x14\n\x0c\x63luster_size\x18\n \x01(\x03\x12\x0e\n\x06\x64river\x18\x0b \x01(\t\x12\x0c\n\x04name\x18\x0c \x01(\t\"u\n\x11\x44iskCreateRequest\x12\x11\n\tdisk_name\x18\x01 \x01(\t\x12\x11\n\tdisk_uuid\x18\x02 \x01(\t\x12\x11\n\tdisk_path\x18\x03 \x01(\t\x12\x12\n\nblock_size\x18\x04 \x01(\x03\x12\x13\n\x0b\x64isk_driver\x18\x05 \x01(\t\"K\n\x0e\x44iskGetRequest\x12\x11\n\tdisk_name\x18\x01 \x01(\t\x12\x13\n\x0b\x64isk_driver\x18\x02 \x01(\t\x12\x11\n\tdisk_path\x18\x03 \x01(\t\"a\n\x11\x44iskDeleteRequest\x12\x11\n\tdisk_name\x18\x01 \x01(\t\x12\x11\n\tdisk_uuid\x18\x02 \x01(\t\x12\x11\n\tdisk_path\x18\x03 \x01(\t\x12\x13\n\x0b\x64isk_driver\x18\x04 \x01(\t\"#\n\x12LogSetLevelRequest\x12\r\n\x05level\x18\x01 \x01(\t\"#\n\x12LogSetFlagsRequest\x12\r\n\x05\x66lags\x18\x01 \x01(\t\"$\n\x13LogGetLevelResponse\x12\r\n\x05level\x18\x01 \x01(\t\"$\n\x13LogGetFlagsResponse\x12\r\n\x05\x66lags\x18\x01 \x01(\t*&\n\x0bReplicaMode\x12\x06\n\x02WO\x10\x00\x12\x06\n\x02RW\x10\x01\x12\x07\n\x03\x45RR\x10\x02\x32\xf3#\n\x0bSPDKService\x12@\n\rReplicaCreate\x12\x1d.spdkrpc.ReplicaCreateRequest\x1a\x10.spdkrpc.Replica\x12\x46\n\rReplicaDelete\x12\x1d.spdkrpc.ReplicaDeleteRequest\x1a\x16.google.protobuf.Empty\x12:\n\nReplicaGet\x12\x1a.spdkrpc.ReplicaGetRequest\x1a\x10.spdkrpc.Replica\x12\x43\n\x15ReplicaSnapshotCreate\x12\x18.spdkrpc.SnapshotRequest\x1a\x10.spdkrpc.Replica\x12I\n\x15ReplicaSnapshotDelete\x12\x18.spdkrpc.SnapshotRequest\x1a\x16.google.protobuf.Empty\x12I\n\x15ReplicaSnapshotRevert\x12\x18.spdkrpc.SnapshotRequest\x1a\x16.google.protobuf.Empty\x12H\n\x14ReplicaSnapshotPurge\x12\x18.spdkrpc.SnapshotRequest\x1a\x16.google.protobuf.Empty\x12\x43\n\x0bReplicaList\x12\x16.google.protobuf.Empty\x1a\x1c.spdkrpc.ReplicaListResponse\x12\x42\n\x0cReplicaWatch\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x30\x01\x12t\n\x19ReplicaRebuildingSrcStart\x12).spdkrpc.ReplicaRebuildingSrcStartRequest\x1a*.spdkrpc.ReplicaRebuildingSrcStartResponse\"\x00\x12\x62\n\x1aReplicaRebuildingSrcFinish\x12*.spdkrpc.ReplicaRebuildingSrcFinishRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x62\n\x1aReplicaRebuildingSrcAttach\x12*.spdkrpc.ReplicaRebuildingSrcAttachRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x62\n\x1aReplicaRebuildingSrcDetach\x12*.spdkrpc.ReplicaRebuildingSrcDetachRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x93\x01\n$ReplicaRebuildingSrcShallowCopyStart\x12\x34.spdkrpc.ReplicaRebuildingSrcShallowCopyStartRequest\x1a\x35.spdkrpc.ReplicaRebuildingSrcShallowCopyStartResponse\x12\x95\x01\n$ReplicaRebuildingSrcShallowCopyCheck\x12\x34.spdkrpc.ReplicaRebuildingSrcShallowCopyCheckRequest\x1a\x35.spdkrpc.ReplicaRebuildingSrcShallowCopyCheckResponse\"\x00\x12t\n\x19ReplicaRebuildingDstStart\x12).spdkrpc.ReplicaRebuildingDstStartRequest\x1a*.spdkrpc.ReplicaRebuildingDstStartResponse\"\x00\x12\x62\n\x1aReplicaRebuildingDstFinish\x12*.spdkrpc.ReplicaRebuildingDstFinishRequest\x1a\x16.google.protobuf.Empty\"\x00\x12t\n$ReplicaRebuildingDstShallowCopyStart\x12\x34.spdkrpc.ReplicaRebuildingDstShallowCopyStartRequest\x1a\x16.google.protobuf.Empty\x12\x95\x01\n$ReplicaRebuildingDstShallowCopyCheck\x12\x34.spdkrpc.ReplicaRebuildingDstShallowCopyCheckRequest\x1a\x35.spdkrpc.ReplicaRebuildingDstShallowCopyCheckResponse\"\x00\x12V\n\"ReplicaRebuildingDstSnapshotCreate\x12\x18.spdkrpc.SnapshotRequest\x1a\x16.google.protobuf.Empty\x12u\n\"ReplicaRebuildingDstSnapshotRevert\x12\x18.spdkrpc.SnapshotRequest\x1a\x33.spdkrpc.ReplicaRebuildingDstSnapshotRevertResponse\"\x00\x12T\n\x13ReplicaBackupCreate\x12\x1c.spdkrpc.BackupCreateRequest\x1a\x1d.spdkrpc.BackupCreateResponse\"\x00\x12T\n\x13ReplicaBackupStatus\x12\x1c.spdkrpc.BackupStatusRequest\x1a\x1d.spdkrpc.BackupStatusResponse\"\x00\x12V\n\x14ReplicaBackupRestore\x12$.spdkrpc.ReplicaBackupRestoreRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x65\n\x14ReplicaRestoreStatus\x12$.spdkrpc.ReplicaRestoreStatusRequest\x1a%.spdkrpc.ReplicaRestoreStatusResponse\"\x00\x12=\n\x0c\x45ngineCreate\x12\x1c.spdkrpc.EngineCreateRequest\x1a\x0f.spdkrpc.Engine\x12\x44\n\x0c\x45ngineDelete\x12\x1c.spdkrpc.EngineDeleteRequest\x1a\x16.google.protobuf.Empty\x12\x37\n\tEngineGet\x12\x19.spdkrpc.EngineGetRequest\x1a\x0f.spdkrpc.Engine\x12\x46\n\rEngineSuspend\x12\x1d.spdkrpc.EngineSuspendRequest\x1a\x16.google.protobuf.Empty\x12\x44\n\x0c\x45ngineResume\x12\x1c.spdkrpc.EngineResumeRequest\x1a\x16.google.protobuf.Empty\x12X\n\x16\x45ngineSwitchOverTarget\x12&.spdkrpc.EngineSwitchOverTargetRequest\x1a\x16.google.protobuf.Empty\x12P\n\x12\x45ngineDeleteTarget\x12\".spdkrpc.EngineDeleteTargetRequest\x1a\x16.google.protobuf.Empty\x12K\n\x14\x45ngineSnapshotCreate\x12\x18.spdkrpc.SnapshotRequest\x1a\x19.spdkrpc.SnapshotResponse\x12H\n\x14\x45ngineSnapshotDelete\x12\x18.spdkrpc.SnapshotRequest\x1a\x16.google.protobuf.Empty\x12H\n\x14\x45ngineSnapshotRevert\x12\x18.spdkrpc.SnapshotRequest\x1a\x16.google.protobuf.Empty\x12G\n\x13\x45ngineSnapshotPurge\x12\x18.spdkrpc.SnapshotRequest\x1a\x16.google.protobuf.Empty\x12\x41\n\nEngineList\x12\x16.google.protobuf.Empty\x1a\x1b.spdkrpc.EngineListResponse\x12\x41\n\x0b\x45ngineWatch\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x30\x01\x12\\\n\x11\x45ngineReplicaList\x12!.spdkrpc.EngineReplicaListRequest\x1a\".spdkrpc.EngineReplicaListResponse\"\x00\x12N\n\x10\x45ngineReplicaAdd\x12 .spdkrpc.EngineReplicaAddRequest\x1a\x16.google.protobuf.Empty\"\x00\x12T\n\x13\x45ngineReplicaDelete\x12#.spdkrpc.EngineReplicaDeleteRequest\x1a\x16.google.protobuf.Empty\"\x00\x12S\n\x12\x45ngineBackupCreate\x12\x1c.spdkrpc.BackupCreateRequest\x1a\x1d.spdkrpc.BackupCreateResponse\"\x00\x12S\n\x12\x45ngineBackupStatus\x12\x1c.spdkrpc.BackupStatusRequest\x1a\x1d.spdkrpc.BackupStatusResponse\"\x00\x12\x62\n\x13\x45ngineBackupRestore\x12#.spdkrpc.EngineBackupRestoreRequest\x1a$.spdkrpc.EngineBackupRestoreResponse\"\x00\x12`\n\x19\x45ngineBackupRestoreFinish\x12).spdkrpc.EngineBackupRestoreFinishRequest\x1a\x16.google.protobuf.Empty\"\x00\x12V\n\x13\x45ngineRestoreStatus\x12\x1d.spdkrpc.RestoreStatusRequest\x1a\x1e.spdkrpc.RestoreStatusResponse\"\x00\x12\x37\n\nDiskCreate\x12\x1a.spdkrpc.DiskCreateRequest\x1a\r.spdkrpc.Disk\x12@\n\nDiskDelete\x12\x1a.spdkrpc.DiskDeleteRequest\x1a\x16.google.protobuf.Empty\x12\x31\n\x07\x44iskGet\x12\x17.spdkrpc.DiskGetRequest\x1a\r.spdkrpc.Disk\x12\x42\n\x0bLogSetLevel\x12\x1b.spdkrpc.LogSetLevelRequest\x1a\x16.google.protobuf.Empty\x12\x42\n\x0bLogSetFlags\x12\x1b.spdkrpc.LogSetFlagsRequest\x1a\x16.google.protobuf.Empty\x12\x43\n\x0bLogGetLevel\x12\x16.google.protobuf.Empty\x1a\x1c.spdkrpc.LogGetLevelResponse\x12\x43\n\x0bLogGetFlags\x12\x16.google.protobuf.Empty\x1a\x1c.spdkrpc.LogGetFlagsResponse\x12J\n\x10VersionDetailGet\x12\x16.google.protobuf.Empty\x1a\x1e.spdkrpc.VersionDetailGetReplyB1Z/github.com/longhorn/types/pkg/generated/spdkrpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spdkrpc.spdk_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/github.com/longhorn/types/pkg/generated/spdkrpc'
  _LVOL_CHILDRENENTRY._options = None
  _LVOL_CHILDRENENTRY._serialized_options = b'8\001'
  _REPLICA_SNAPSHOTSENTRY._options = None
  _REPLICA_SNAPSHOTSENTRY._serialized_options = b'8\001'
  _REPLICALISTRESPONSE_REPLICASENTRY._options = None
  _REPLICALISTRESPONSE_REPLICASENTRY._serialized_options = b'8\001'
  _ENGINE_REPLICAADDRESSMAPENTRY._options = None
  _ENGINE_REPLICAADDRESSMAPENTRY._serialized_options = b'8\001'
  _ENGINE_REPLICAMODEMAPENTRY._options = None
  _ENGINE_REPLICAMODEMAPENTRY._serialized_options = b'8\001'
  _ENGINE_SNAPSHOTSENTRY._options = None
  _ENGINE_SNAPSHOTSENTRY._serialized_options = b'8\001'
  _ENGINECREATEREQUEST_REPLICAADDRESSMAPENTRY._options = None
  _ENGINECREATEREQUEST_REPLICAADDRESSMAPENTRY._serialized_options = b'8\001'
  _ENGINELISTRESPONSE_ENGINESENTRY._options = None
  _ENGINELISTRESPONSE_ENGINESENTRY._serialized_options = b'8\001'
  _ENGINEREPLICALISTRESPONSE_REPLICASENTRY._options = None
  _ENGINEREPLICALISTRESPONSE_REPLICASENTRY._serialized_options = b'8\001'
  _BACKUPCREATEREQUEST_CREDENTIALENTRY._options = None
  _BACKUPCREATEREQUEST_CREDENTIALENTRY._serialized_options = b'8\001'
  _ENGINEBACKUPRESTOREREQUEST_CREDENTIALENTRY._options = None
  _ENGINEBACKUPRESTOREREQUEST_CREDENTIALENTRY._serialized_options = b'8\001'
  _ENGINEBACKUPRESTORERESPONSE_ERRORSENTRY._options = None
  _ENGINEBACKUPRESTORERESPONSE_ERRORSENTRY._serialized_options = b'8\001'
  _REPLICABACKUPRESTOREREQUEST_CREDENTIALENTRY._options = None
  _REPLICABACKUPRESTOREREQUEST_CREDENTIALENTRY._serialized_options = b'8\001'
  _RESTORESTATUSRESPONSE_STATUSENTRY._options = None
  _RESTORESTATUSRESPONSE_STATUSENTRY._serialized_options = b'8\001'
  _globals['_REPLICAMODE']._serialized_start=7938
  _globals['_REPLICAMODE']._serialized_end=7976
  _globals['_LVOL']._serialized_start=61
  _globals['_LVOL']._serialized_end=320
  _globals['_LVOL_CHILDRENENTRY']._serialized_start=273
  _globals['_LVOL_CHILDRENENTRY']._serialized_end=320
  _globals['_REPLICA']._serialized_start=323
  _globals['_REPLICA']._serialized_end=672
  _globals['_REPLICA_SNAPSHOTSENTRY']._serialized_start=609
  _globals['_REPLICA_SNAPSHOTSENTRY']._serialized_end=672
  _globals['_REPLICACREATEREQUEST']._serialized_start=674
  _globals['_REPLICACREATEREQUEST']._serialized_end=785
  _globals['_REPLICADELETEREQUEST']._serialized_start=787
  _globals['_REPLICADELETEREQUEST']._serialized_end=849
  _globals['_REPLICAGETREQUEST']._serialized_start=851
  _globals['_REPLICAGETREQUEST']._serialized_end=884
  _globals['_REPLICALISTRESPONSE']._serialized_start=887
  _globals['_REPLICALISTRESPONSE']._serialized_end=1037
  _globals['_REPLICALISTRESPONSE_REPLICASENTRY']._serialized_start=972
  _globals['_REPLICALISTRESPONSE_REPLICASENTRY']._serialized_end=1037
  _globals['_REPLICAREBUILDINGSRCSTARTREQUEST']._serialized_start=1040
  _globals['_REPLICAREBUILDINGSRCSTARTREQUEST']._serialized_end=1174
  _globals['_REPLICAREBUILDINGSRCSTARTRESPONSE']._serialized_start=1176
  _globals['_REPLICAREBUILDINGSRCSTARTRESPONSE']._serialized_end=1250
  _globals['_REPLICAREBUILDINGSRCFINISHREQUEST']._serialized_start=1252
  _globals['_REPLICAREBUILDINGSRCFINISHREQUEST']._serialized_end=1327
  _globals['_REPLICAREBUILDINGSRCATTACHREQUEST']._serialized_start=1329
  _globals['_REPLICAREBUILDINGSRCATTACHREQUEST']._serialized_end=1441
  _globals['_REPLICAREBUILDINGSRCDETACHREQUEST']._serialized_start=1443
  _globals['_REPLICAREBUILDINGSRCDETACHREQUEST']._serialized_end=1518
  _globals['_REPLICAREBUILDINGSRCSHALLOWCOPYSTARTREQUEST']._serialized_start=1520
  _globals['_REPLICAREBUILDINGSRCSHALLOWCOPYSTARTREQUEST']._serialized_end=1602
  _globals['_REPLICAREBUILDINGSRCSHALLOWCOPYSTARTRESPONSE']._serialized_start=1604
  _globals['_REPLICAREBUILDINGSRCSHALLOWCOPYSTARTRESPONSE']._serialized_end=1678
  _globals['_REPLICAREBUILDINGSRCSHALLOWCOPYCHECKREQUEST']._serialized_start=1681
  _globals['_REPLICAREBUILDINGSRCSHALLOWCOPYCHECKREQUEST']._serialized_end=1817
  _globals['_REPLICAREBUILDINGSRCSHALLOWCOPYCHECKRESPONSE']._serialized_start=1820
  _globals['_REPLICAREBUILDINGSRCSHALLOWCOPYCHECKRESPONSE']._serialized_end=1949
  _globals['_REPLICAREBUILDINGDSTSTARTREQUEST']._serialized_start=1952
  _globals['_REPLICAREBUILDINGDSTSTARTREQUEST']._serialized_end=2171
  _globals['_REPLICAREBUILDINGDSTSTARTRESPONSE']._serialized_start=2173
  _globals['_REPLICAREBUILDINGDSTSTARTRESPONSE']._serialized_end=2239
  _globals['_REPLICAREBUILDINGDSTFINISHREQUEST']._serialized_start=2241
  _globals['_REPLICAREBUILDINGDSTFINISHREQUEST']._serialized_end=2290
  _globals['_REPLICAREBUILDINGDSTSHALLOWCOPYSTARTREQUEST']._serialized_start=2292
  _globals['_REPLICAREBUILDINGDSTSHALLOWCOPYSTARTREQUEST']._serialized_end=2374
  _globals['_REPLICAREBUILDINGDSTSHALLOWCOPYCHECKREQUEST']._serialized_start=2376
  _globals['_REPLICAREBUILDINGDSTSHALLOWCOPYCHECKREQUEST']._serialized_end=2435
  _globals['_REPLICAREBUILDINGDSTSHALLOWCOPYCHECKRESPONSE']._serialized_start=2438
  _globals['_REPLICAREBUILDINGDSTSHALLOWCOPYCHECKRESPONSE']._serialized_end=2655
  _globals['_REPLICAREBUILDINGDSTSNAPSHOTREVERTRESPONSE']._serialized_start=2657
  _globals['_REPLICAREBUILDINGDSTSNAPSHOTREVERTRESPONSE']._serialized_end=2738
  _globals['_ENGINE']._serialized_start=2741
  _globals['_ENGINE']._serialized_end=3401
  _globals['_ENGINE_REPLICAADDRESSMAPENTRY']._serialized_start=3203
  _globals['_ENGINE_REPLICAADDRESSMAPENTRY']._serialized_end=3259
  _globals['_ENGINE_REPLICAMODEMAPENTRY']._serialized_start=3261
  _globals['_ENGINE_REPLICAMODEMAPENTRY']._serialized_end=3336
  _globals['_ENGINE_SNAPSHOTSENTRY']._serialized_start=609
  _globals['_ENGINE_SNAPSHOTSENTRY']._serialized_end=672
  _globals['_ENGINECREATEREQUEST']._serialized_start=3404
  _globals['_ENGINECREATEREQUEST']._serialized_end=3761
  _globals['_ENGINECREATEREQUEST_REPLICAADDRESSMAPENTRY']._serialized_start=3203
  _globals['_ENGINECREATEREQUEST_REPLICAADDRESSMAPENTRY']._serialized_end=3259
  _globals['_ENGINEDELETEREQUEST']._serialized_start=3763
  _globals['_ENGINEDELETEREQUEST']._serialized_end=3798
  _globals['_ENGINEGETREQUEST']._serialized_start=3800
  _globals['_ENGINEGETREQUEST']._serialized_end=3832
  _globals['_ENGINESUSPENDREQUEST']._serialized_start=3834
  _globals['_ENGINESUSPENDREQUEST']._serialized_end=3870
  _globals['_ENGINERESUMEREQUEST']._serialized_start=3872
  _globals['_ENGINERESUMEREQUEST']._serialized_end=3907
  _globals['_ENGINESWITCHOVERTARGETREQUEST']._serialized_start=3909
  _globals['_ENGINESWITCHOVERTARGETREQUEST']._serialized_end=3978
  _globals['_ENGINEDELETETARGETREQUEST']._serialized_start=3980
  _globals['_ENGINEDELETETARGETREQUEST']._serialized_end=4021
  _globals['_ENGINELISTRESPONSE']._serialized_start=4024
  _globals['_ENGINELISTRESPONSE']._serialized_end=4168
  _globals['_ENGINELISTRESPONSE_ENGINESENTRY']._serialized_start=4105
  _globals['_ENGINELISTRESPONSE_ENGINESENTRY']._serialized_end=4168
  _globals['_ENGINEREPLICAADDREQUEST']._serialized_start=4170
  _globals['_ENGINEREPLICAADDREQUEST']._serialized_end=4263
  _globals['_ENGINEREPLICALISTREQUEST']._serialized_start=4265
  _globals['_ENGINEREPLICALISTREQUEST']._serialized_end=4312
  _globals['_ENGINEREPLICALISTRESPONSE']._serialized_start=4315
  _globals['_ENGINEREPLICALISTRESPONSE']._serialized_end=4477
  _globals['_ENGINEREPLICALISTRESPONSE_REPLICASENTRY']._serialized_start=972
  _globals['_ENGINEREPLICALISTRESPONSE_REPLICASENTRY']._serialized_end=1037
  _globals['_ENGINEREPLICADELETEREQUEST']._serialized_start=4479
  _globals['_ENGINEREPLICADELETEREQUEST']._serialized_end=4575
  _globals['_ENGINEREPLICAREBUILDSTATUSREQUEST']._serialized_start=4577
  _globals['_ENGINEREPLICAREBUILDSTATUSREQUEST']._serialized_end=4655
  _globals['_ENGINEREPLICAREBUILDSTATUSRESPONSE']._serialized_start=4658
  _globals['_ENGINEREPLICAREBUILDSTATUSRESPONSE']._serialized_end=4842
  _globals['_SNAPSHOTREQUEST']._serialized_start=4844
  _globals['_SNAPSHOTREQUEST']._serialized_end=4948
  _globals['_SNAPSHOTRESPONSE']._serialized_start=4950
  _globals['_SNAPSHOTRESPONSE']._serialized_end=4991
  _globals['_VERSIONOUTPUT']._serialized_start=4994
  _globals['_VERSIONOUTPUT']._serialized_end=5233
  _globals['_VERSIONDETAILGETREPLY']._serialized_start=5235
  _globals['_VERSIONDETAILGETREPLY']._serialized_end=5299
  _globals['_BACKUPCREATEREQUEST']._serialized_start=5302
  _globals['_BACKUPCREATEREQUEST']._serialized_end=5743
  _globals['_BACKUPCREATEREQUEST_CREDENTIALENTRY']._serialized_start=5694
  _globals['_BACKUPCREATEREQUEST_CREDENTIALENTRY']._serialized_end=5743
  _globals['_BACKUPCREATERESPONSE']._serialized_start=5745
  _globals['_BACKUPCREATERESPONSE']._serialized_end=5832
  _globals['_BACKUPSTATUSREQUEST']._serialized_start=5834
  _globals['_BACKUPSTATUSREQUEST']._serialized_end=5917
  _globals['_BACKUPSTATUSRESPONSE']._serialized_start=5920
  _globals['_BACKUPSTATUSRESPONSE']._serialized_end=6058
  _globals['_ENGINEBACKUPRESTOREREQUEST']._serialized_start=6061
  _globals['_ENGINEBACKUPRESTOREREQUEST']._serialized_end=6303
  _globals['_ENGINEBACKUPRESTOREREQUEST_CREDENTIALENTRY']._serialized_start=5694
  _globals['_ENGINEBACKUPRESTOREREQUEST_CREDENTIALENTRY']._serialized_end=5743
  _globals['_ENGINEBACKUPRESTORERESPONSE']._serialized_start=6306
  _globals['_ENGINEBACKUPRESTORERESPONSE']._serialized_end=6448
  _globals['_ENGINEBACKUPRESTORERESPONSE_ERRORSENTRY']._serialized_start=6403
  _globals['_ENGINEBACKUPRESTORERESPONSE_ERRORSENTRY']._serialized_end=6448
  _globals['_ENGINEBACKUPRESTOREFINISHREQUEST']._serialized_start=6450
  _globals['_ENGINEBACKUPRESTOREFINISHREQUEST']._serialized_end=6505
  _globals['_REPLICABACKUPRESTOREREQUEST']._serialized_start=6508
  _globals['_REPLICABACKUPRESTOREREQUEST']._serialized_end=6753
  _globals['_REPLICABACKUPRESTOREREQUEST_CREDENTIALENTRY']._serialized_start=5694
  _globals['_REPLICABACKUPRESTOREREQUEST_CREDENTIALENTRY']._serialized_end=5743
  _globals['_RESTORESTATUSREQUEST']._serialized_start=6755
  _globals['_RESTORESTATUSREQUEST']._serialized_end=6798
  _globals['_REPLICARESTORESTATUSREQUEST']._serialized_start=6800
  _globals['_REPLICARESTORESTATUSREQUEST']._serialized_end=6851
  _globals['_REPLICARESTORESTATUSRESPONSE']._serialized_start=6854
  _globals['_REPLICARESTORESTATUSRESPONSE']._serialized_end=7102
  _globals['_RESTORESTATUSRESPONSE']._serialized_start=7105
  _globals['_RESTORESTATUSRESPONSE']._serialized_end=7274
  _globals['_RESTORESTATUSRESPONSE_STATUSENTRY']._serialized_start=7190
  _globals['_RESTORESTATUSRESPONSE_STATUSENTRY']._serialized_end=7274
  _globals['_DISK']._serialized_start=7277
  _globals['_DISK']._serialized_end=7491
  _globals['_DISKCREATEREQUEST']._serialized_start=7493
  _globals['_DISKCREATEREQUEST']._serialized_end=7610
  _globals['_DISKGETREQUEST']._serialized_start=7612
  _globals['_DISKGETREQUEST']._serialized_end=7687
  _globals['_DISKDELETEREQUEST']._serialized_start=7689
  _globals['_DISKDELETEREQUEST']._serialized_end=7786
  _globals['_LOGSETLEVELREQUEST']._serialized_start=7788
  _globals['_LOGSETLEVELREQUEST']._serialized_end=7823
  _globals['_LOGSETFLAGSREQUEST']._serialized_start=7825
  _globals['_LOGSETFLAGSREQUEST']._serialized_end=7860
  _globals['_LOGGETLEVELRESPONSE']._serialized_start=7862
  _globals['_LOGGETLEVELRESPONSE']._serialized_end=7898
  _globals['_LOGGETFLAGSRESPONSE']._serialized_start=7900
  _globals['_LOGGETFLAGSRESPONSE']._serialized_end=7936
  _globals['_SPDKSERVICE']._serialized_start=7979
  _globals['_SPDKSERVICE']._serialized_end=12574
# @@protoc_insertion_point(module_scope)
