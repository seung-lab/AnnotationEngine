from annotationengine.anno_database import get_db
import logging


def test_create_db(app_config, mocker):
    with app_config.app_context():
        db = get_db("test_aligned_volume")
        logging.info(db.__dict__)
        assert db.aligned_volume == "test_aligned_volume"
