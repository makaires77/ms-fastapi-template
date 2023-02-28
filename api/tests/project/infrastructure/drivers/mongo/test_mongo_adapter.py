import pytest
from project.helpers.pydantic_typo import ObjectId
from project.infrastructure.drivers.mongo.adapter import MongoAdapter


@pytest.mark.asyncio
async def test_get_buildinfo():
    mongo_client = MongoAdapter("mstemplate")
    if await mongo_client.get_buildinfo() is not True:
        raise AssertionError


@pytest.mark.asyncio
async def test_get_one_success():
    mongo = MongoAdapter("mstemplate")
    data: dict = {"key": "value", "key2": "value2"}
    id = await mongo.insert_one(data)
    result = await mongo.get_one(id=id)
    if result != data:
        raise AssertionError


@pytest.mark.asyncio
async def test_get_one_error():
    with pytest.raises(Exception):
        mongo = MongoAdapter("mstemplate")
        id = 123456 + True
        await mongo.get_one(id=id)


@pytest.mark.asyncio
async def test_get_many_success():
    mongo = MongoAdapter("mstemplate")
    data: dict = {"key": "value", "key2": "value2"}
    await mongo.insert_one(data)
    result = await mongo.get_many(filter=data)
    if result != [data]:
        raise AssertionError


@pytest.mark.asyncio
async def test_get_many_error():
    with pytest.raises(Exception):
        mongo = MongoAdapter("mstemplate")
        await mongo.get_many(filter={"key": "pineapple"})


@pytest.mark.asyncio
async def test_insert_one_success():
    mongo = MongoAdapter("mstemplate")
    result = await mongo.insert_one({"key": "value"})
    if type(result) != ObjectId:
        raise AssertionError


@pytest.mark.asyncio
async def test_insert_one_error():
    with pytest.raises(Exception):
        mongo = MongoAdapter("mstemplate")
        result = await mongo.insert_one({"key": Exception("")})


@pytest.mark.asyncio
async def test_insert_many_success():
    list_of_itens = [{"key": "value"}]
    mongo = MongoAdapter("mstemplate")
    result = await mongo.insert_many(list_of_itens)
    if type(result) != list:
        raise AssertionError
    if len(result) != 1:
        raise AssertionError


@pytest.mark.asyncio
async def test_insert_many_error():
    with pytest.raises(Exception):
        mongo = MongoAdapter("mstemplate")
        await mongo.insert_many({"key": Exception("")})


@pytest.mark.asyncio
async def test_update_one_success():
    mongo = MongoAdapter("mstemplate")
    data: dict = {"person": "jhon", "age": 32}
    id = await mongo.insert_one(data)
    acknowledged, modified_count = await mongo.update_one(id, {"age": "35"})
    if acknowledged is not True:
        raise AssertionError
    if modified_count > 1:
        raise AssertionError


@pytest.mark.asyncio
async def test_update_one_error():
    with pytest.raises(Exception):
        mongo = MongoAdapter("mstemplate")
        await mongo.update_one({"key": Exception("")}, {})


@pytest.mark.asyncio
async def test_update_many_success():
    mongo = MongoAdapter("mstemplate")
    data: dict = [
        {"person": "jhon", "age": 32},
        {"person": "carl", "age": 32},
        {"person": "jake", "age": 32},
        {"person": "samy", "age": 32},
        {"person": "moes", "age": 32},
        {"person": "jean", "age": 32},
        {"person": "Cler", "age": 32},
        {"person": "Nast", "age": 32},
    ]
    await mongo.insert_many(data)

    acknowledged, modified_count = await mongo.update_many(
        {"age": {"$gt": 30}}, {"age": 29}
    )
    if acknowledged is not True:
        raise AssertionError
    if modified_count != len(data):
        raise AssertionError


@pytest.mark.asyncio
async def test_update_many_error():
    with pytest.raises(Exception):
        mongo = MongoAdapter("mstemplate")
        await mongo.update_many({"age": {"$gt": Exception()}}, {"age": 29})


@pytest.mark.asyncio
async def test_delete_success():
    mongo = MongoAdapter("mstemplate")
    data: dict = {"person": "jhon", "age": 32}
    await mongo.insert_one(data)
    acknowledged, deleted_count = await mongo.delete({"age": {"$gt": 30}})
    if acknowledged is not True:
        raise AssertionError
    if deleted_count != 1:
        raise AssertionError


@pytest.mark.asyncio
async def test_delete_error():
    with pytest.raises(Exception):
        mongo = MongoAdapter("mstemplate")
        await mongo.delete({"key": Exception()})
