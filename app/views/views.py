# ACA VAN LAS RUTAS O ENDPOINTS
from flask import (
    jsonify, 
    request,
    
)
from flask.views import MethodView
from app import app,db 
from app.models.models import (Usuario,Post,Comentario,Categoria)
from app.schemas.schemas import (UsuarioSchema, CategoriaSchema, PostSchema, ComentarioSchema)

class UsuarioView(MethodView):
    def get(self, usuario_id=None):
        if usuario_id is not None:
            usuario = Usuario.query.get(usuario_id)
            if usuario:
                usuario_schema = UsuarioSchema().dump(usuario)
                return jsonify(usuario_schema)
            else:
                return jsonify(MENSAJE="Usuario no encontrado"), 404
        else:
            usuarios = Usuario.query.all()
            usuarios_schema = UsuarioSchema(many=True).dump(usuarios)
            return jsonify(usuarios_schema)

    def post(self):
        data = request.get_json()
        nombre = data.get('nombre')
        correo = data.get('correo')
        contraseña = data.get('contraseña')

        nuevo_usuario = Usuario(
            nombre=nombre,
            correo=correo,
            contraseña=contraseña
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        return jsonify(MENSAJE=f"Se creó el usuario {nombre} correctamente")

    def put(self, usuario_id):
        usuario = Usuario.query.get(usuario_id)
        if not usuario:
            return jsonify(MENSAJE="Usuario no encontrado"), 404

        data = request.get_json()
        nombre = data.get('nombre')
        correo = data.get('correo')
        contraseña = data.get('contraseña')

        usuario.nombre = nombre
        usuario.correo = correo
        usuario.contraseña = contraseña

        db.session.commit()
        return jsonify(MENSAJE=f"Usuario {nombre} actualizado correctamente")

    def delete(self, usuario_id):
        usuario = Usuario.query.get(usuario_id)
        if not usuario:
            return jsonify(MENSAJE="Usuario no encontrado"), 404

        db.session.delete(usuario)
        db.session.commit()
        return jsonify(MENSAJE="Usuario eliminado correctamente")

usuario_view = UsuarioView.as_view('usuario_view')
app.add_url_rule('/usuario/', view_func=usuario_view, methods=['GET', 'POST'])
app.add_url_rule('/usuario/<int:usuario_id>', view_func=usuario_view, methods=['GET', 'PUT', 'DELETE'])


class CategoriaView(MethodView):
    def get(self, categoria_id=None):
        if categoria_id is not None:
            categoria = Categoria.query.get(categoria_id)
            if categoria:
                categoria_schema = CategoriaSchema().dump(categoria)
                return jsonify(categoria_schema)
            else:
                return jsonify(MENSAJE="Categoría no encontrada"), 404
        else:
            categorias = Categoria.query.all()
            categorias_schema = CategoriaSchema(many=True).dump(categorias)
            return jsonify(categorias_schema)

    def post(self):
        data = request.get_json()
        nombre = data.get('nombre')

        nueva_categoria = Categoria(
            nombre=nombre
        )
        db.session.add(nueva_categoria)
        db.session.commit()
        return jsonify(MENSAJE=f"Se creó la categoría {nombre} correctamente")

    def put(self, categoria_id):
        categoria = Categoria.query.get(categoria_id)
        if not categoria:
            return jsonify(MENSAJE="Categoría no encontrada"), 404

        data = request.get_json()
        nombre = data.get('nombre')

        categoria.nombre = nombre

        db.session.commit()
        return jsonify(MENSAJE=f"Categoría {nombre} actualizada correctamente")

    def delete(self, categoria_id):
        categoria = Categoria.query.get(categoria_id)
        if not categoria:
            return jsonify(MENSAJE="Categoría no encontrada"), 404

        db.session.delete(categoria)
        db.session.commit()
        return jsonify(MENSAJE="Categoría eliminada correctamente")

categoria_view = CategoriaView.as_view('categoria_view')
app.add_url_rule('/categoria/', view_func=categoria_view, methods=['GET', 'POST'])
app.add_url_rule('/categoria/<int:categoria_id>', view_func=categoria_view, methods=['GET', 'PUT', 'DELETE'])


class PostView(MethodView):
    def get(self, post_id=None):
        if post_id is not None:
            post = Post.query.get(post_id)
            if post:
                post_schema = PostSchema().dump(post)
                return jsonify(post_schema)
            else:
                return jsonify(MENSAJE="Post no encontrado"), 404
        else:
            posts = Post.query.all()
            posts_schema = PostSchema(many=True).dump(posts)
            return jsonify(posts_schema)

    def post(self):
        data = request.get_json()
        titulo = data.get("titulo")
        contenido = data.get("contenido")
        fecha_creacion = data.get("fecha_creacion")
        usuario_id = data.get("usuario_id")
        categorias = data.get("categorias")

        nuevo_post = Post(
            titulo=titulo,
            contenido=contenido,
            fecha_creacion=fecha_creacion,
            usuario_id=usuario_id
        )

        if categorias:
            for categoria_id in categorias:
                categoria = Categoria.query.get(categoria_id)
                if categoria:
                    nuevo_post.categorias.append(categoria)

        db.session.add(nuevo_post)
        db.session.commit()

        return jsonify(MENSAJE="Nuevo post creado")

    def put(self, post_id):
        post = Post.query.get(post_id)
        if not post:
            return jsonify(MENSAJE="Post no encontrado"), 404

        data = request.get_json()
        titulo = data.get("titulo")
        contenido = data.get("contenido")
        fecha_creacion = data.get("fecha_creacion")
        usuario_id = data.get("usuario_id")
        categorias = data.get("categorias")

        post.titulo = titulo
        post.contenido = contenido
        post.fecha_creacion = fecha_creacion
        post.usuario_id = usuario_id

        
        post.categorias.clear() # Elimina 

        if categorias:
            for categoria_id in categorias:
                categoria = Categoria.query.get(categoria_id)
                if categoria:
                    post.categorias.append(categoria)

        db.session.commit()
        return jsonify(MENSAJE=f"Post {post_id} actualizado correctamente")

    def delete(self, post_id):
        post = Post.query.get(post_id)
        if not post:
            return jsonify(MENSAJE="Post no encontrado"), 404

        db.session.delete(post)
        db.session.commit()
        return jsonify(MENSAJE="Post eliminado correctamente")

post_view = PostView.as_view('post_view')
app.add_url_rule('/post/', view_func=post_view, methods=['GET', 'POST'])
app.add_url_rule('/post/<int:post_id>', view_func=post_view, methods=['GET', 'PUT', 'DELETE'])

class ComentarioView(MethodView):
    def get(self, comentario_id=None):
        if comentario_id is not None:
            comentario = Comentario.query.get(comentario_id)
            if comentario:
                comentario_schema = ComentarioSchema().dump(comentario)
                return jsonify(comentario_schema)
            else:
                return jsonify(MENSAJE="Comentario no encontrado"), 404
        else:
            comentarios = Comentario.query.all()
            comentarios_schema = ComentarioSchema(many=True).dump(comentarios)
            return jsonify(comentarios_schema)

    def post(self):
        data = request.get_json()
        texto = data.get("texto")
        fecha_creacion = data.get("fecha_creacion")
        usuario_id = data.get("usuario_id")
        entrada_id = data.get("entrada_id")

        nuevo_comentario = Comentario(
            texto=texto,
            fecha_creacion=fecha_creacion,
            usuario_id=usuario_id,
            entrada_id=entrada_id
        )
        db.session.add(nuevo_comentario)
        db.session.commit()
        return jsonify(MENSAJE="Nuevo comentario creado")

    def put(self, comentario_id):
        comentario = Comentario.query.get(comentario_id)
        if not comentario:
            return jsonify(MENSAJE="Comentario no encontrado"), 404

        data = request.get_json()
        texto = data.get("texto")

        comentario.texto = texto

        db.session.commit()
        return jsonify(MENSAJE="Comentario actualizado correctamente")

    def delete(self, comentario_id):
        comentario = Comentario.query.get(comentario_id)
        if not comentario:
            return jsonify(MENSAJE="Comentario no encontrado"), 404

        db.session.delete(comentario)
        db.session.commit()
        return jsonify(MENSAJE="Comentario eliminado correctamente")

comentario_view = ComentarioView.as_view('comentario_view')
app.add_url_rule('/comentario/', view_func=comentario_view, methods=['GET', 'POST'])
app.add_url_rule('/comentario/<int:comentario_id>', view_func=comentario_view, methods=['GET', 'PUT', 'DELETE'])

