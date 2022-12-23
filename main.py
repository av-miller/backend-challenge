import uvicorn as uvicorn
from fastapi import FastAPI, Depends

from config.dependency import get_sprocket_dao
from dao.sprocket_dao import SprocketDao
from dto.sprocket import SprocketDto
from orm.sprocket import Sprocket

app = FastAPI()


@app.get("/sprockets")
def list_sprockets(sprocket_dao: SprocketDao = Depends(get_sprocket_dao)):
    # no pagination or chunking, so it will fold for larger datasets
    return sprocket_dao.list()


@app.get("/sprockets/{identifier}")
def find_sprocket(identifier: str, sprocket_dao: SprocketDao = Depends(get_sprocket_dao)):
    return sprocket_dao.find(identifier)


@app.post("/sprockets")
def create_sprocket(s: SprocketDto, sprocket_dao: SprocketDao = Depends(get_sprocket_dao)):
    return sprocket_dao.add(Sprocket(teeth=s.teeth,
                                     pitch_diameter=s.pitch_diameter,
                                     outside_diameter=s.outside_diameter,
                                     pitch=s.pitch))


@app.put("/sprockets/{identifier}")
def update_sprocket(identifier: str, s: SprocketDto, sprocket_dao: SprocketDao = Depends(get_sprocket_dao)):
    return sprocket_dao.update(identifier, {'teeth': s.teeth,
                                            'pitch_diameter': s.pitch_diameter,
                                            'outside_diameter': s.outside_diameter,
                                            'pitch': s.pitch})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
