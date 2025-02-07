from fastapi import FastAPI, HTTPException, Query
from typing import Dict, List, Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
students=[
  {
    "name": "kH4J3EaBsP",
    "marks": 69
  },
  {
    "name": "sCi17Psy",
    "marks": 97
  },
  {
    "name": "P8amdcNUhs",
    "marks": 53
  },
  {
    "name": "0byDMNXX",
    "marks": 25
  },
  {
    "name": "0lGuunS1Y",
    "marks": 29
  },
  {
    "name": "QUcG3bXJO",
    "marks": 9
  },
  {
    "name": "j2Vv",
    "marks": 58
  },
  {
    "name": "Rp",
    "marks": 72
  },
  {
    "name": "Gfl9Cl",
    "marks": 98
  },
  {
    "name": "KQaaP",
    "marks": 66
  },
  {
    "name": "q",
    "marks": 97
  },
  {
    "name": "RAgLm6iuK",
    "marks": 15
  },
  {
    "name": "K4ffOL",
    "marks": 24
  },
  {
    "name": "rX3g",
    "marks": 74
  },
  {
    "name": "yTFYjpSKU",
    "marks": 11
  },
  {
    "name": "y3eyWF",
    "marks": 32
  },
  {
    "name": "xswAhhC4LU",
    "marks": 72
  },
  {
    "name": "6",
    "marks": 76
  },
  {
    "name": "c",
    "marks": 43
  },
  {
    "name": "1ztv",
    "marks": 72
  },
  {
    "name": "Sly0W",
    "marks": 46
  },
  {
    "name": "M7",
    "marks": 65
  },
  {
    "name": "rm3VDwL5z",
    "marks": 72
  },
  {
    "name": "8WGmdXO8sK",
    "marks": 30
  },
  {
    "name": "iqwukx",
    "marks": 61
  },
  {
    "name": "Z",
    "marks": 15
  },
  {
    "name": "hH",
    "marks": 94
  },
  {
    "name": "y1jeKIT",
    "marks": 89
  },
  {
    "name": "cC2Cra",
    "marks": 97
  },
  {
    "name": "IvIjOpQR6",
    "marks": 35
  },
  {
    "name": "hp5CzyQQ",
    "marks": 61
  },
  {
    "name": "rt",
    "marks": 13
  },
  {
    "name": "Nn9jJ4",
    "marks": 88
  },
  {
    "name": "Z9JLcx2",
    "marks": 92
  },
  {
    "name": "S5",
    "marks": 70
  },
  {
    "name": "1IOE",
    "marks": 67
  },
  {
    "name": "JI376vFUa",
    "marks": 67
  },
  {
    "name": "3wo",
    "marks": 0
  },
  {
    "name": "slC0",
    "marks": 35
  },
  {
    "name": "bpMo1",
    "marks": 67
  },
  {
    "name": "f2SgMOx",
    "marks": 66
  },
  {
    "name": "JERs5",
    "marks": 90
  },
  {
    "name": "Cn",
    "marks": 26
  },
  {
    "name": "seR6k0YL",
    "marks": 25
  },
  {
    "name": "7",
    "marks": 80
  },
  {
    "name": "ojv",
    "marks": 48
  },
  {
    "name": "oBuiBVwdaE",
    "marks": 47
  },
  {
    "name": "zoOz",
    "marks": 99
  },
  {
    "name": "xTJIO7KT",
    "marks": 5
  },
  {
    "name": "pxsQJ5",
    "marks": 49
  },
  {
    "name": "A",
    "marks": 90
  },
  {
    "name": "lG6",
    "marks": 3
  },
  {
    "name": "2pHys",
    "marks": 88
  },
  {
    "name": "j5XxLT",
    "marks": 95
  },
  {
    "name": "dVlo",
    "marks": 97
  },
  {
    "name": "2",
    "marks": 18
  },
  {
    "name": "9kjb",
    "marks": 79
  },
  {
    "name": "9",
    "marks": 57
  },
  {
    "name": "XQyoBDhCGx",
    "marks": 59
  },
  {
    "name": "zy",
    "marks": 46
  },
  {
    "name": "Al",
    "marks": 94
  },
  {
    "name": "LL4uVS",
    "marks": 43
  },
  {
    "name": "fTXvsoPL",
    "marks": 97
  },
  {
    "name": "7bFLmwy",
    "marks": 76
  },
  {
    "name": "gq",
    "marks": 12
  },
  {
    "name": "AhEiidq6t",
    "marks": 9
  },
  {
    "name": "aBbqkV",
    "marks": 86
  },
  {
    "name": "JacFar",
    "marks": 73
  },
  {
    "name": "W1KtR",
    "marks": 47
  },
  {
    "name": "HL0NMuL",
    "marks": 71
  },
  {
    "name": "XPm9hLiK",
    "marks": 75
  },
  {
    "name": "Z4ZM",
    "marks": 33
  },
  {
    "name": "Vvi",
    "marks": 57
  },
  {
    "name": "KqUd5gMz",
    "marks": 28
  },
  {
    "name": "MDZI",
    "marks": 93
  },
  {
    "name": "nMwMD7",
    "marks": 58
  },
  {
    "name": "XG89HyQ4MY",
    "marks": 46
  },
  {
    "name": "cBm",
    "marks": 29
  },
  {
    "name": "UsEomP",
    "marks": 66
  },
  {
    "name": "44tSjq97",
    "marks": 82
  },
  {
    "name": "d5d4Xfdej",
    "marks": 30
  },
  {
    "name": "JY",
    "marks": 83
  },
  {
    "name": "3hD752be",
    "marks": 90
  },
  {
    "name": "oQxjYsb",
    "marks": 76
  },
  {
    "name": "01Tfq",
    "marks": 73
  },
  {
    "name": "SA",
    "marks": 59
  },
  {
    "name": "lTfL",
    "marks": 47
  },
  {
    "name": "qliKsHW",
    "marks": 23
  },
  {
    "name": "ISf7Wo",
    "marks": 21
  },
  {
    "name": "VYe7T",
    "marks": 71
  },
  {
    "name": "Uh6st6",
    "marks": 53
  },
  {
    "name": "rnk2f1FZU",
    "marks": 83
  },
  {
    "name": "h5",
    "marks": 43
  },
  {
    "name": "6uJGLdI",
    "marks": 26
  },
  {
    "name": "vnxpVjVwN",
    "marks": 83
  },
  {
    "name": "Trcxab64",
    "marks": 37
  },
  {
    "name": "0",
    "marks": 90
  },
  {
    "name": "nsCqGnIhMw",
    "marks": 62
  },
  {
    "name": "GMfK",
    "marks": 40
  },
  {
    "name": "uoEZvg",
    "marks": 42
  }
]
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/api")
async def get_students(name_: Optional[List[str]] = Query(None, alias="name")) -> Dict[str, List[str]]:
    if class_:
        filtered_students = [student["marks"] for student in students if student["name"] in name_]
        return {"marks": filtered_students}
    return students
