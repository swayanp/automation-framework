pipeline {
    agent any

    parameters {
        booleanParam(
            name: 'RUN_REGRESSION',
            defaultValue: false,
            description: 'Run full regression test suite'
        )
        booleanParam(
            name: 'RUN_DB_TESTS',
            defaultValue: false,
            description: 'Run database tests'
        )
    }

    environment {
        PYTHONUNBUFFERED = '1'
        DB_USER = credentials('db_user')
        DB_PASSWORD = credentials('db_password')
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/swayanp/automation-framework.git'
            }
        }

        stage('Setup Python') {
            steps {
                bat '''
                python -m venv .venv
                .venv\\Scripts\\pip install --upgrade pip
                .venv\\Scripts\\pip install -r requirements.txt
                '''
            }
        }

        stage('Smoke Tests') {
            steps {
                bat '''
                .venv\\Scripts\\pytest -m smoke
                '''
            }
        }

        stage('API Tests') {
            steps {
                bat '''
                .venv\\Scripts\\pytest -m api
                '''
            }
        }

        stage('Regression Tests') {
            when {
                expression { params.RUN_REGRESSION == true }
            }
            steps {
                bat '''
                .venv\\Scripts\\pytest -m regression
                '''
            }
        }

        stage('DB Tests') {
            when {
                expression { params.RUN_DB_TESTS == true }
            }
            steps {
                bat '''
                .venv\\Scripts\\pytest -m db
                '''
            }
        }
    }

    post {
        always {
           allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}
