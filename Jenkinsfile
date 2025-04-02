// Jenkinsfile (Declarative Pipeline)

pipeline {
    // 1. Agent Configuration: Where will this pipeline run?
    //    'any' means Jenkins can use any available agent.
    //    You could specify labels like 'linux' or 'python-builder' if you have configured agents.
    agent any

    // 2. Environment Variables (Optional)
    // environment {
    //     PYTHON_VERSION = '3.10' // Example if needed elsewhere
    // }

    // 3. Tools (Optional - if Jenkins Tool Installations are configured)
    // tools {
    //     python 'python3.10' // Use a Python tool configured in Jenkins Global Tool Configuration
    // }

    // 4. Stages: Define the sequence of steps in your pipeline
    stages {
        // Stage 1: Checkout Code
        stage('Checkout') {
            steps {
                echo 'Checking out code from repository...'
                // Uses the Git plugin to check out the code for the branch being built
                checkout scm
            }
        }

        // Stage 2: Setup & Install Dependencies
        stage('Install Dependencies') {
            steps {
                echo 'Setting up Python environment and installing dependencies...'
                // Execute shell commands on the agent
                // Ensure the correct Python/pip are in the PATH on the Jenkins agent
                sh '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
                // If using Jenkins Tool 'python', the sh commands would run within that context
            }
        }

        // Stage 3: Linting (Optional)
        // stage('Lint') {
        //     steps {
        //         echo 'Running linter...'
        //         sh 'pip install flake8'
        //         sh 'flake8 . --count --show-source --statistics' // Adjust flake8 command as needed
        //     }
        // }

        // Stage 4: Run Tests
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'pytest' // Execute pytest
            }
        }

        Stage 5: Build (Optional - if you have build.py)
        stage('Build') {
            steps {
                echo 'Building application package...'
                sh 'python build.py'
                // Archive the build artifact so it can be used later or downloaded
                archiveArtifacts artifacts: 'dist/*.zip', fingerprint: true
            }
        }

        // Stage 6: Deploy (Conditional - e.g., only for the main branch)
        // stage('Deploy') {
        //     // Only run this stage for pushes to the 'main' branch
        //     when {
        //         branch 'main'
        //     }
        //     steps {
        //         echo 'Deploying application (Simulated)...'
        //         // In a real scenario:
        //         // 1. Might need to unarchive artifact if built in a previous stage
        //         //    (e.g., using stash/unstash or CopyArtifact plugin)
        //         // 2. Use credentials stored securely in Jenkins (e.g., SSH keys, tokens)
        //         //    withCredentials([sshUserPrivateKey(credentialsId: 'your-ssh-key-id', keyFileVariable: 'SSH_KEY_FILE')]) {
        //         //        sh "scp -i ${SSH_KEY_FILE} dist/*.zip user@your-server:/path/to/deploy"
        //         //        sh "ssh -i ${SSH_KEY_FILE} user@your-server 'cd /path/to/deploy && unzip *.zip && ./restart_app.sh'"
        //         //    }
        //
        //         // Placeholder using the example deploy script
        //         sh 'chmod +x deploy.sh' // Ensure script is executable
        //         sh './deploy.sh'
        //     }
        // }
    }

    // 5. Post Actions: Actions to run after the pipeline completes (success, failure, etc.)
    post {
        always {
            echo 'Pipeline finished.'
            // Clean up the workspace
            cleanWs()
        }
        success {
            echo 'Pipeline succeeded!'
            // Maybe send a success notification
        }
        failure {
            echo 'Pipeline failed!'
            // Maybe send a failure notification (e.g., email, Slack)
        }
    }
}