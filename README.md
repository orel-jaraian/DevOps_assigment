# Home Assigment: Nginx Server Testing with Docker and CI

This project configures a lightweight Nginx server environment with automated testing and continuous integration using Docker. The setup includes an Nginx server with a custom HTML response and a Python-based testing container to verify server availability, orchestrated through Docker Compose. A CI workflow further automates testing, ensuring the robustness of the setup.

## Project Structure

- **Dockerfile.nginx**: Configures an Nginx server with custom settings, optimized for small image size using a minimal Ubuntu base.
- **nginx.conf**: Configures two Nginx servers with different responses on ports 8080 and 8081.
- **Dockerfile.tester**: Sets up a Python environment to run a test script, which checks the availability and status of the Nginx servers.
- **check_servers.py**: Python script to test the availability and response of two Nginx servers (`http://nginx:8080` and `http://nginx:8081`). It logs results in a file, indicating success or failure based on server responses.
- **docker-compose.yml**: Defines and orchestrates the Nginx and tester services. Ensures the tester waits for Nginx to start before checking its availability.
- **docker_ci.yml**: GitHub Actions workflow that automates the build and test processes, capturing and storing test results as artifacts.

## Test Results
  The check_servers.py script checks the availability and response status of two Nginx servers (http://nginx:8080 and http://nginx:8081). It creates a result file indicating either success (succeeded) or failure 
  (fail) based on whether both servers returned status 200.

- **Passing the Test:** For the test to pass successfully, both servers must respond with HTTP status 200 OK. If both servers return this status, the result file will show "succeeded," indicating that both servers are functioning as expected and serving the correct responses.
- **Failing the Test:** If either server does not respond with status 200 (for example, if one server is down or returns a different status), the result file will indicate "fail."
The result file is stored in the container, allowing for easy inspection of test outcomes within the tester container after the script has run.

