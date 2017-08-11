node('master') {
    stage('Preparation'){
        git changelog: false, poll: false, url: 'https://github.com/r-bergundy/practice'
    }
    }
    stage('Build') {
        sh "echo Build"
        sh "python -m unittest tests.test_unit_account.TestAccount"
    }
 }
