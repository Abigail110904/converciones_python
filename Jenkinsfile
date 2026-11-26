pipeline {
    agent {
        label 'python'
    }

    stages {
        stage('Entorno') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version'
                sh 'pip install pytest'
            }
        }

        stage('Descarga') {
            steps {
                git url: 'https://github.com/Abigail110904/converciones_python.git', branch: 'main'
            }
        }

        stage('Ejecutar') {
            steps {
                sh 'python3 Converciones.py'
            }
        }

        stage('Probar') {
            steps {
                sh 'python -m pytest --junitxml=reports/results.xml'
            }
            post {
                always {
                    junit 'reports/results.xml'
                }
            }
        }
    }
}
