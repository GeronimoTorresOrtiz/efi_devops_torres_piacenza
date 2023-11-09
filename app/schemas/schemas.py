#un esquema es basicamente un serializador
from app import ma
from marshmallow import fields, post_load
from app.models.models import Post


class UsuarioSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String()
    correo = fields.Email(required=True)
    contraseña = fields.String()

class CategoriaSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String()


class PostSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    titulo = fields.String()
    contenido = fields.String()
    fecha_creacion = fields.String(dump_only=True)
    usuario_id = fields.Integer(required=True)
    categorias = fields.Nested(CategoriaSchema, many=True, only=("id", "nombre"))

    @post_load
    def make_post(self, data, **kwargs):
        return Post(**data)
    
class ComentarioSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    texto = fields.String(required=True)
    fecha_creacion = fields.String(dump_only=True)
    usuario_id = fields.Integer(required=True)
    entrada_id = fields.Integer(required=True)
