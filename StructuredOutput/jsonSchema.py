''' Json Schema is used when our whole project is not in one language.Then we not used typedDict and pydantic 
    Like For Backend we are Using : Python & for Frontend : using React


'''
{
    "title": "student",
    "description": "schema about Students",
    "type": " object",
    "properties": {
        "name": "string",
        "age": "integer",
    },
    "required":["name"]
}

''' Now Schema is created go to fil {with_structured_output_json.py}'''
