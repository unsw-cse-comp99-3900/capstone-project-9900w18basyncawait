# Docker Running Instruction
1. The docker and project is designed to run on Linux/Ubuntu system.
2. Download the whole project
3. Go into Docker diretory
4. To load docker using the command 'docker load -i webmain.tar'
5. Open the frontend.html
6. Start up docker using the command 'docker run -p 5000:5000 webmain'
7. In the frontend.html, click 'Choose files' button.
8. Then select all four input data files in 'data' directory, which are,
  - feature_C3.npy
  - feature_C4.npy
  - seacell_data_C3.csv
  - seacell_data_C4.csv
9. Then click 'Start Training' button to start the computing process.
10. The computing process will be about 2 minutes. After the finish of the computing, four pictures will be shown on the front end webpage.
11. To stop the docker
   - use the command 'docker ps' to show the current running docker ID
   - use the command 'docker stop ID' replacing the ID with the docker ID shown in the 'docker ps' output.
   - then the docker can be restart by using 'docker run -p 5000:5000 webmain'
