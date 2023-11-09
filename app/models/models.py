# Aca van los modelos
from app import db
from sqlalchemy import ForeignKey


class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable = False)
    correo = db.Column(db.String(100), nullable = False)
    contraseña = db.Column(db.String(100), nullable = False)

    def __str__(self):
        return self.nombre

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    contenido = db.Column(db.String(1000), nullable=False)
    fecha_creacion = db.Column(db.String(100), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    usuario = db.relationship('Usuario', backref=db.backref('posts', lazy=True))
    categorias = db.relationship("Categoria", secondary="post_categoria", backref=db.backref('posts', lazy=True))

    def __str__(self):
        return self.titulo
    

class Comentario(db.Model):
    __tablename__ = 'comentario'
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(100), nullable=False)
    fecha_creacion = db.Column(db.String(100), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    entrada_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    usuario = db.relationship('Usuario',backref=db.backref('comentarios', lazy=True))
    entrada = db.relationship('Post',backref=db.backref('comentarios', lazy=True))

    def __str__(self):
        return self.texto


class Categoria(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def __str__(self):
        return self.nombre

post_categoria = db.Table('post_categoria', 
    db.Column('entrada_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
    db.Column('categoria_id', db.Integer, db.ForeignKey('categoria.id'), primary_key=True)
)