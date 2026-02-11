// pipeline {
//     agent any

//     parameters {
//         booleanParam(
//             name: 'RUN_REGRESSION',
//             defaultValue: false,
//             description: 'Run full regression test suite'
//         )
//         booleanParam(
//             name: 'RUN_DB_TESTS',
//             defaultValue: false,
//             description: 'Run database tests'
//         )
//     }

//     environment {
//         PYTHONUNBUFFERED = '1'
//         DB_USER = credentials('db_user')
//         DB_PASSWORD = credentials('db_password')
//     }

//     stages {

//         stage('Checkout') {
//             steps {
//                 git branch: 'main',
//                     url: 'https://github.com/swayanp/automation-framework.git'
//             }
//         }

//         stage('Setup Python') {
//             steps {
//                 bat '''
//                 python -m venv .venv
//                 .venv\\Scripts\\pip install --upgrade pip
//                 .venv\\Scripts\\pip install -r requirements.txt
//                 '''
//             }
//         }

//         stage('Smoke Tests') {
//             steps {
//                 bat '''
//                 .venv\\Scripts\\pytest -m smoke
//                 '''
//             }
//         }

//         stage('API Tests') {
//             steps {
//                 bat '''
//                 .venv\\Scripts\\pytest -m api
//                 '''
//             }
//         }

//         stage('Regression Tests') {
//             when {
//                 expression { params.RUN_REGRESSION == true }
//             }
//             steps {
//                 bat '''
//                 .venv\\Scripts\\pytest -m regression
//                 '''
//             }
//         }

//         stage('DB Tests') {
//             when {
//                 expression { params.RUN_DB_TESTS == true }
//             }
//             steps {
//                 bat '''
//                 .venv\\Scripts\\pytest -m db
//                 '''
//             }
//         }
//     }

//     post {
//         always {
//            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
//         }
//     }
// }
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)   // Prevent Jenkins double checkout (fixes UNSTABLE issue)
        timestamps()
    }

    environment {
        DOCKER_BUILDKIT = '1'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-creds',
                    url: 'https://github.com/swayanp/automation-framework.git'
            }
        }

        stage('Clean Workspace') {
            steps {
                bat 'if exist allure-results rmdir /s /q allure-results'
            }
        }

        stage('Docker Compose Test Run') {
            steps {
                bat '''
                docker compose down -v
                docker compose up --build --abort-on-container-exit
                '''
            }
        }
    }

    post {

        always {
            bat 'docker compose down'

            allure(
                includeProperties: false,
                jdk: '',
                results: [[path: 'allure-results']]
            )
        }

        success {
            echo 'Build SUCCESS ✅'
        }

        failure {
            echo 'Build FAILED ❌'
        }
    }
}
