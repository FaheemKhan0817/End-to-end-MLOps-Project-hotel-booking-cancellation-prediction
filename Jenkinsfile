pipeline {
    agent any
    stages {

        stage('Cloning Github repository to Jenkins') 
        {
            steps {
                script{
                       echo 'Cloning Github repository to Jenkins ...........'
                      checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/FaheemKhan0817/End-to-end-MLOps-Project-hotel-booking-cancellation-prediction.git']])

                      }
                
                
                  }
        }
          }
}