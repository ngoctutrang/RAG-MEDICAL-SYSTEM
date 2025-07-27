data_loader
uv run ./app/components/data_loader.py

create folder custom_jenkins
cd custom_jenkins
docker build -t jenkins-dind .

docker run -d ^
    --name jenkins-dind ^
    --privileged ^
    -p 8080:8080 ^
    -p 50000:50000 ^
    -v /var/run/docker.sock:/var/run/docker.sock ^
    -v jenkins_home:/var/jenkins_home ^
    jenkins-dind