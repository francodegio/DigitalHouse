# Defiance 4, Digital House, Data Science, 2019, Grupo 3
El objetivo de este desafio fué crear un detector de noticias falsas ó FAKE NEWS.
Hicimos la pruebas y generamos el modelo predictor con python en la Jupyter Notebook y disponibilizamos el predictor en una pagina web hosteada con docker y docker compose.

## Requirements
- Debes tener instalado docker y docker-compose (nativo en docker hace 2 años).
- Debes haber generado los pickle model.pkl y vectorizer.pkl
- Descargate este repositorio
fin de los requerimientos

## Installation
- Ubicarse en la raiz de este ReadMe.md
- Crear la carpeta pkls
- Copiar el modelo en pkls/model.pkl
- Copiar el vectorizador en pkls/vectorizer.pkl
- Ubicarse en la carpeta docker y colocar lo siguiente
```bash
docker-compose build
docker-compose up -d
```

## Usage
Una vez instalado y con los docker corriendo
- Ingresar en tu navegador a: http://localhost:81/
- Copiar tu noticia en ingles en el campo y apretá el boton para checkear.


## Make requests to the API:
```console
$ curl -H "Content-Type: application/json" -X POST -d '{"text":"Argentian Governant decided to remove all taxes to residents."}' http://localhost:81/predict

$ curl -H "Content-Type: application/json" -X POST -d '{"text":"Aliens Attacks Buenos Aires."}' http://localhost:81/predict_proba
```

## License
TBD