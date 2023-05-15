import pytest
from core.modelfactory import create_model_object

def test_create_model_object_response():
    
    invalid_table_name = "User"
    valid_table_name = "BOARD"
    model_object = None

    with pytest.raises(ValueError) as excinfo:
    
        model_object = create_model_object(invalid_table_name)
        assert None is model_object

    assert "Table name {} not recognized".format(invalid_table_name) in str(excinfo)
    
    model_object = create_model_object(valid_table_name)
    assert None is not model_object
    # assert model_object = board