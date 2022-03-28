### Running the application

_You must have Docker and WSL installed in your machine in order for the app to work properly in windows as it uses Redis and Celery_

1. Run setup.sh in the backend folder
   ```sh
   sh setup.sh
   ```
2. Start a Redis server using Docker (if using windows)
    ```sh
    docker pull redis
    docker run -dp 6379:6379 redis
    ```
3. Start the flask server with gunicorn using run.sh in the backend
    ```sh
    sh run.sh
    ```
4. Start Celery workers by running celery_workers.sh
    ```sh
    sh celery_workers.sh
    ```
5. (Optional) Start Celery Beat in order to run scheduled jobs
    ```sh
    sh celery_beat.sh
    ```
6. In the frontend folder, start the development server
    ```sh
    npm run dev
    ```
7. The app can now be accessed in the browser through,
    ```sh
    http://localhost:3000
    ```