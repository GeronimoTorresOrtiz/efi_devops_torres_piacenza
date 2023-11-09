# EFI DEVOPS 

Este miniblog es una aplicación básica que demuestra cómo construir una aplicación web simple utilizando Flask y cómo desplegarla de manera eficiente con Docker.

## Instalación

1. Clona este repositorio en tu máquina local:

```bash
git clone git@github.com:GeronimoTorresOrtiz/efi_devops_torres_piacenza.git
```

2. Navega al directorio del proyecto:

```bash
cd tu-proyecto
```

## Configuración

Copia el archivo `.env.sample` y renómbralo como `.env`:

```bash
cp .env.sample .env
```

Edita el archivo `.env` y proporciona los valores necesarios para tu aplicación, como las claves secretas y las configuraciones de base de datos.

## Ejecución

Para ejecutar la aplicación, utiliza Docker Compose. Ejecuta el siguiente comando:

```bash
sudo docker-compose up 
```

Esto creará y ejecutará los contenedores de Docker según las especificaciones del archivo `docker-compose.yml`.

## Acceso a la aplicación

Una vez que los contenedores estén en funcionamiento, podrás acceder a la aplicación en tu navegador web a través de `http://localhost:5005`, donde `5005` es el puerto especificado en tu archivo `docker-compose.yml`.

## Detener la aplicación

Para detener la aplicación y los contenedores en ejecución, puedes presionar `Ctrl+C` en la terminal donde se está ejecutando `docker-compose up`. Luego, puedes detener los contenedores por completo utilizando el siguiente comando:

```bash
sudo docker-compose down
```

## Integrantes
- Torres Ortiz Geronimo
- Piacenza Lautaro


- Repositorio: [URL de GitHub](git@github.com:GeronimoTorresOrtiz/efi_devops_torres_piacenza.git)

