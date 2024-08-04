# Docker Running Instruction
1. The docker and project is designed to run on Linux/Ubuntu system. Because this docker is created based on Ubuntu 22.04. The Ubuntu version before 22.04 will have error when running the docker.
2. Download the whole project
3. Go into Docker diretory
4. To load docker using the command `docker load -i webmain.tar`
6. Open the frontend.html
7. Start up docker using the command `docker run -p 5000:5000 webmain`
8. In the frontend.html, click `Choose files` button.
9. Then select two input data files in 'data' directory, which are,
  - seacell_data_C3.csv
  - seacell_data_C4.csv
9. Then click `Start Training` button to start the computing process.
10. The computing process will be about 2 minutes. After the finish of the computing, four pictures will be shown on the front end webpage.
11. To stop the docker
   - use the command `docker ps` to show the current running docker ID
   - use the command `docker stop ID` replacing the ID with the docker ID shown in the `docker ps` output.
   - then the docker can be restart by using `docker run -p 5000:5000 webmain`
