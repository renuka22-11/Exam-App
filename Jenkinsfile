pipeline {
    agent any
    
    stages {
        stage ('SCM checkout') {
            steps {
            git branch: 'main', url: 'https://github.com/renuka22-11/Exam-App.git'
            }
                
        }
        stage ('docker image build') {
            steps {
            sh '/usr/bin/docker image build -t renuka1711/examapp .'
            }
        }
        stage ('docker login') {
            steps {
                sh 'echo dckr_pat_06GfbV79siW2nGsGAZJ2uz97a7I | docker login -u renuka1711 --password-stdin'
            }
        }
        stage ('docker image push') {
            steps {
                sh '/usr/bin/docker image push renuka1711/examapp '
            }
        }
        stage ('get the confirmation') {
            steps {
                input 'Do you want to Deploy ?'
            }
        }
        stage ('Confirm') {
            steps {
                git branch: 'main', url: 'https://github.com/EIVOR0717/examm.git'
            }
        }
        stage ('Remove Existing Service') {
            steps {
                sh '/usr/bin/docker service rm exam'
            }
        }
        stage ('create docker servcie') {
            steps {
                sh '/usr/bin/docker service create --name exam -p 4000:4000 renuka1711/examapp'
            }
        }
        
    }
}
