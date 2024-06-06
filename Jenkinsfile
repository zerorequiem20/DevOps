pipeline {
  agent any
  stages {
    stage("make directory") {
        steps{
          sh "mkdir ~/jenkins-pipeline"
        }
    }
    stage("add some files") {
      steps {
        sh "touch ~/jenkins-pipeline/file1.txt"
        sh "ls -al"
      }
    }
  }  
}
