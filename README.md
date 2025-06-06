# WorldOfGames
A cli games project with small frontend, docker compose and jenkins pipeline integration

# Tech Stack
![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![image](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white) ![image](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) ![image](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=Jenkins&logoColor=white) ![image](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)

# Project Contents
project content as follows:
- `CurrencyRouletteGame.py`: Currency guessing game
- `Dockerfile`: Docker file for frontend image
- `GuessGame.py`: Number guessing game
- `Jenkinsfile`: Jenkinsfile for pipeline integration
- `Live.py`: Game choosing logic and results
- `MainGame.py`: Running game from different file
- `MainScore.py`: Frontend logic
- `MemoryGame.py`: Number memory game
- `Score.py`: Scores file handling logic
- `Scores.txt`: Hold user score data
- `Utils.py`: Utils file
- `docker-compose.yaml`: Docker compose file definition
- `requirements.txt`: library requirements for python
- `/tests/e2e.py`: Selenium test for fronend
- `/upload/Scores.txt`: Dummy Scores file to be loaded during pipeline

# Steps to run it yourself
1. Download required files
```commandline
git clone https://github.com/ShaharRubel/WorldOfGames.git
pip install -r requirements.txt
```
2. cd to directiory
```commandline
cd WorldOfGames
```
3. Run frontend with compose
```commandline
docker-compose up -d
```