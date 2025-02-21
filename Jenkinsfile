pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/yourusername/yourrepository.git'
            }
        }
        stage('Run ETL Pipeline') {
            steps {
                sh 'python etl_pipeline.py'
            }
        }
    }
    triggers {
        pollSCM('* * * * *') // Polls every minute for changes
    }
}
