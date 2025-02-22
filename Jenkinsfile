pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/anshnub/devops1.git'
            }
        }
        stage('Run ETL Pipeline') {
            steps {
                sh 'python etl_pipeline.py'
            }
        }
    }
}
