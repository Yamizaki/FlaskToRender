from config.mongodb import mongo
from flask import request, Response


def createTodoService():

    title = request.form["title"]
    description = request.form["description"]
    file = request.files["file"]
    technologies = request.form["technologies"]
    proyect_link = request.form["proyect_link"]
    code_source = request.form["code_source"]

    try:
        image_data = file.read()
        image_id = mongo.db.proyectos.insert_one(
            {
                "title": title,
                "image": image_data,
                "description": description,
                "technologies": technologies,
                "proyect_link": proyect_link,
                "code_source": code_source,
            }
        ).inserted_id

        return "Se agregó correctamente"

    except ():
        return "Hubo un error al agregar un proyecto"


def getTodoService():
    from bson import json_util

    data = mongo.db.proyectos.find()
    result = json_util.dumps(data)
    return Response(result, mimetype="application/json")


def getOneTodoService(id):
    from bson import json_util, ObjectId

    data = mongo.db.proyectos.find_one({"_id": ObjectId(id)})
    result = json_util.dumps(data)
    return Response(result, mimetype="application/json")


def updateTodoService(id):
    from bson import ObjectId

    data = request.get_json()
    if len(data) == 0:
        return "Invalid Update", 400

    result = mongo.db.proyectos.find_one({"_id": ObjectId(id)}, {"$set": data})

    if result.modified_count > 1:
        return "Succefully update", 200
    else:
        return "Something went wrong", 404


def deleteTodoService(id):
    from bson import json_util, ObjectId

    data = mongo.db.proyectos.delete_one({"_id": ObjectId(id)})

    return "Todo selected was delete"




### CERTIFICADO 
def createCertificadoService():

    title = request.form["title"]
    description = request.form["description"]
    file = request.files["file"]
    technologies = request.form["technologies"]
    proyect_link = request.form["certificado_link"]
   

    try:
        image_data = file.read()
        image_id = mongo.db.certificado.insert_one(
            {
                "title": title,
                "image": image_data,
                "description": description,
                "technologies": technologies,
                "proyect_link": proyect_link,
                
            }
        ).inserted_id

        return "Se agregó correctamente"

    except ():
        return "Hubo un error al agregar un proyecto"


def getCertificadoService():
    from bson import json_util

    data = mongo.db.certificado.find()
    result = json_util.dumps(data)
    return Response(result, mimetype="application/json")