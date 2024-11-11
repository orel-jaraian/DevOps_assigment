# Home Assigment: Nginx Server Testing with Docker and CI

This project configures a lightweight Nginx server environment with automated testing and continuous integration using Docker. The setup includes an Nginx server with a custom HTML response and a Python-based testing container to verify server availability, orchestrated through Docker Compose. A CI workflow further automates testing, ensuring the robustness of the setup.

## Project Structure

- **Dockerfile.nginx**: Configures an Nginx server with custom settings, optimized for small image size using a minimal Ubuntu base.
- **Dockerfile.tester**: Sets up a Python environment to run a test script, which checks the availability and status of the Nginx servers.
- **check_servers.py**: Python script to test the availability and response of two Nginx servers (`http://nginx:8080` and `http://nginx:8081`). It logs results in a file, indicating success or failure based on server responses.
- **docker-compose.yml**: Defines and orchestrates the Nginx and tester services. Ensures the tester waits for Nginx to start before checking its availability.
- **docker_ci.yml**: GitHub Actions workflow that automates the build and test processes, capturing and storing test results as artifacts.

## Getting Started

### Prerequisites

Ensure you have Docker and Docker Compose installed on your machine.

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
