pipeline {
    agent any

     stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git 'https://github.com/2206-devops-batch/BryonS-Project1.git'

                // force stop docker and clean up
                sh "docker system prune -af"
                // re-download everything
                sh "docker build -t flask1 $WORKSPACE"
                // Run flask docker container.
                sh "docker-compose -f $WORKSPACE/docker-compose.yaml up -d"

            }
        }
    }
}