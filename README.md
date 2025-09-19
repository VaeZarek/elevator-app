# elevator-app
Coding challenge for Bluestaq, September 19th 2025

# How to run Docker container
First, navigate to the directory the repo is contained in. Once there, execute the following to build the Docker image from the provided Dockerfile:

```docker build -t elevator-app .``` _(Might need to use sudo if Docker is installed by root)_

Once the build is done, use the following to run the Docker container:

```docker run -it elevator-app```

This will open an interactive shell and run the Python script for the Elevator application. 

# Running the application
You will start at the lobby and can only request an elevator going up. The program will prompt you to wait while simulating an elevator being called. Once the elevator is present, you are automatically placed inside, where you can then push a button for the floor you would like to go to. The program will simulate the elevator moving between floors until you get to your destination, where you can choose to exit the elevator or request another floor. Once you have left the elevator, you can call another one by using the given commands. 

**NOTE**: The program will only let you exit the building (and therefore the application) when you are in the Lobby.

