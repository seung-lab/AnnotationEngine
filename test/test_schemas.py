import datetime

from annotationengine.schemas import (
    CreateTableSchema,
    DeleteAnnotationSchema,
    FullMetadataSchema,
    MetadataSchema,
    OptionalTableMetadataSchema,
    PutAnnotationSchema,
    TableSchema,
)


def test_table_schema():
    data = {"table_name": "test_table", "schema_type": "synapse"}
    schema = TableSchema()
    result = schema.load(data)

    assert result["table_name"] == "test_table"
    assert result["schema_type"] == "synapse"


def test_optional_table_metadata_schema():
    data = {"reference_table": "test_table", "track_target_id_updates": True}
    schema = OptionalTableMetadataSchema()
    result = schema.load(data)

    assert result["reference_table"] == "test_table"
    assert result["track_target_id_updates"] is True


def test_metadata_schema():
    data = {
        "user_id": "1",
        "description": "Test description",
        "flat_segmentation_source": "precomputed://gs://my_cloud_bucket/image",
        "voxel_resolution_x": 4,
        "voxel_resolution_y": 4,
        "voxel_resolution_z": 40,
    }
    schema = MetadataSchema()
    result = schema.load(data)

    assert result["user_id"] == "1"
    assert result["description"] == "Test description"
    assert (
        result["flat_segmentation_source"] == "precomputed://gs://my_cloud_bucket/image"
    )
    assert result["voxel_resolution_x"] == 4
    assert result["voxel_resolution_y"] == 4
    assert result["voxel_resolution_z"] == 40


def test_metadata_with_optional_metadata_schema():
    data = {
        "user_id": "1",
        "description": "Test description",
        "table_metadata": {
            "reference_table": "test_table",
            "track_target_id_updates": True,
        },
        "flat_segmentation_source": "precomputed://gs://my_cloud_bucket/image",
        "voxel_resolution_x": 4,
        "voxel_resolution_y": 4,
        "voxel_resolution_z": 40,
        "read_permission": "PUBLIC",
        "write_permission": "PRIVATE",
    }
    schema = MetadataSchema()
    result = schema.load(data)

    assert result["user_id"] == "1"
    assert result["description"] == "Test description"
    assert result["table_metadata"] == {
        "reference_table": "test_table",
        "track_target_id_updates": True,
    }
    assert (
        result["flat_segmentation_source"] == "precomputed://gs://my_cloud_bucket/image"
    )
    assert result["voxel_resolution_x"] == 4
    assert result["voxel_resolution_y"] == 4
    assert result["voxel_resolution_z"] == 40


def test_create_table_schema():
    data = {
        "table_name": "test_table",
        "schema_type": "synapse",
        "metadata": {
            "user_id": "1",
            "description": "Test description",
            "flat_segmentation_source": "precomputed://gs://my_cloud_bucket/image",
            "voxel_resolution_x": 4,
            "voxel_resolution_y": 4,
            "voxel_resolution_z": 40,
            "read_permission": "PUBLIC",
            "write_permission": "PRIVATE",
        },
    }
    schema = CreateTableSchema()
    result = schema.load(data)

    assert result["table_name"] == "test_table"
    assert result["schema_type"] == "synapse"
    assert result["metadata"]["user_id"] == "1"
    assert result["metadata"]["description"] == "Test description"
    assert (
        result["metadata"]["flat_segmentation_source"]
        == "precomputed://gs://my_cloud_bucket/image"
    )
    assert result["metadata"]["voxel_resolution_x"] == 4
    assert result["metadata"]["voxel_resolution_y"] == 4
    assert result["metadata"]["voxel_resolution_z"] == 40


def test_delete_annotation_schema():
    data = {"annotation_ids": [1, 2, 5]}
    schema = DeleteAnnotationSchema()
    result = schema.load(data)

    assert result["annotation_ids"] == [1, 2, 5]


def test_put_annotation_schema():
    data = {
        "annotations": [
            {
                "pre_pt": {"position": [31, 31, 0]},
                "ctr_pt": {"position": [32, 32, 0]},
                "post_pt": {"position": [33, 33, 0]},
            },
        ]
    }
    schema = PutAnnotationSchema()
    result = schema.load(data)

    assert result["annotations"] == [
        {
            "pre_pt": {"position": [31, 31, 0]},
            "ctr_pt": {"position": [32, 32, 0]},
            "post_pt": {"position": [33, 33, 0]},
        },
    ]


def test_full_metadata_schema():
    utc_time = datetime.datetime.utcnow()

    full_metadata = {
        "id": 1,
        "schema_type": "synapse",
        "table_name": "test_table",
        "valid": True,
        "created": str(utc_time),
        "deleted": None,
        "user_id": "1",
        "description": "Test description",
        "reference_table": None,
        "flat_segmentation_source": None,
        "voxel_resolution_x": 4,
        "voxel_resolution_y": 4,
        "voxel_resolution_z": 40,
        "read_permission": "PUBLIC",
        "write_permission": "PRIVATE",
    }
    schema = FullMetadataSchema()
    result = schema.load(full_metadata)
    assert result["id"] == 1
    assert result["table_name"] == "test_table"
    assert result["schema_type"] == "synapse"
    assert result["user_id"] == "1"
    assert result["valid"] is True
    assert result["reference_table"] is None
    assert result["flat_segmentation_source"] is None
    assert result["created"] == utc_time
    assert result["deleted"] is None
    assert result["description"] == "Test description"
    assert result["voxel_resolution_x"] == 4
    assert result["voxel_resolution_y"] == 4
    assert result["voxel_resolution_z"] == 40
    assert result["read_permission"] == "PUBLIC"
    assert result["write_permission"] == "PRIVATE"
