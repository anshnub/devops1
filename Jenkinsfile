pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/anshnub/devops1'
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
