pipeline {
    agent any
    environment {
        VENV_DIR = 'venv'
    }
    stages {
        stage('Cloning Github repository to Jenkins') {
            steps {
                script {
                    echo 'Cloning Github repository to Jenkins ...........'
                    checkout scmGit(
                        branches: [[name: '*/main']], 
                        extensions: [], 
                        userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/FaheemKhan0817/End-to-end-MLOps-Project-hotel-booking-cancellation-prediction.git']]
                    )
                }
            }
        }
        stage('Setting up our Virtual Environment and Installing dependancies') {
            steps {
                script {
                    echo 'Setting up our Virtual Environment and Installing dependancies............'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }
    }
}