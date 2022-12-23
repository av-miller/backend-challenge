import uvicorn as uvicorn
from fastapi import FastAPI, Depends, HTTPException

from app.config.dependency import get_sprocket_dao, get_factory_dao
from app.dao.factory_dao import FactoryDao
from app.dao.sprocket_dao import SprocketDao
from app.dto.sprocket import SprocketDto
from app.orm.sprocket import Sprocket

app = FastAPI()


@app.get("/factories/{identifier}")
def find_factory(identifier: str, factory_dao: FactoryDao = Depends(get_factory_dao)):
    """
    Finds a factory by its identifier
    """
    factory = factory_dao.find(identifier)
    if factory:
        return factory
    else:
        raise HTTPException(status_code=404, detail="Factory not found")


@app.get("/factories")
def list_factories(factory_dao: FactoryDao = Depends(get_factory_dao)):
    """
    Lists all factories
    """
    # no pagination or chunking, so it will fold for larger datasets
    return factory_dao.list()


@app.get("/sprockets")
def list_sprockets(sprocket_dao: SprocketDao = Depends(get_sprocket_dao)):
    """
    Lists all sprockets
    """
    # no pagination or chunking, so it will fold for larger datasets
    return sprocket_dao.list()


@app.get("/sprockets/{identifier}")
def find_sprocket(identifier: str, sprocket_dao: SprocketDao = Depends(get_sprocket_dao)):
    """
    Finds a sprocket by identifier
    """
    sprocket = sprocket_dao.find(identifier)
    if sprocket:
        return sprocket
    else:
        raise HTTPException(status_code=404, detail="Sprocket not found")


@app.post("/sprockets")
def create_sprocket(s: SprocketDto, sprocket_dao: SprocketDao = Depends(get_sprocket_dao)):
    """
    Creates a new sprocket
    """
    sprocket = Sprocket(teeth=s.teeth,
                        pitch_diameter=s.pitch_diameter,
                        outside_diameter=s.outside_diameter,
                        pitch=s.pitch)
    sprocket_dao.add(sprocket)
    s.id = sprocket.id
    return s


@app.put("/sprockets/{identifier}")
def update_sprocket(identifier: str, s: SprocketDto, sprocket_dao: SprocketDao = Depends(get_sprocket_dao)):
    """
    Updates an existing sprocket. Only updates the fields that are passed in.
    """
    sprocket_dao.update(identifier, {'teeth': s.teeth,
                                     'pitch_diameter': s.pitch_diameter,
                                     'outside_diameter': s.outside_diameter,
                                     'pitch': s.pitch})
    return sprocket_dao.find(identifier)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
