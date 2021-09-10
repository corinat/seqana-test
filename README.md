

# Dockerizing Leaflet with Flask, Postgres, Gunicorn, and Nginx

This is a demo to demonstrate the use of Leaflet with Nginex and Docker. Although PotgreSQL and Flask also have their own containers, these are not used for this specific project.
To spead up the  creation of the Leaflet map, the QGIS plugin qgis2web has been used.

### Development

Uses the default Flask development server.

1. Build the images and run the containers:

    ```sh
    docker-compose up -d --build
    ```

    Test it out at [http://127.0.0.1:5000/template/qgis2web/index.html](http://127.0.0.1:5000/template/qgis2web/index.html). 

### Production

Uses gunicorn + nginx.

1. Build the images and run the containers:

    ```sh
    docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1337/template/qgis2web/index.html](http://localhost:1337/template/qgis2web/index.html). 


To terminate containers for both environments (dev and prod):

    ```sh
    docker-compose down
    ``` 
