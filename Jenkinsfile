node {
  stage 'Checkout'
  git 'ssh://git@github.com:sharminakteranee/flask-api.git'
 
  stage 'Docker build'
  docker.build('demo')
 
  stage 'Docker push'
  docker.withRegistry('https://852015740547.dkr.ecr.us-east-1.amazonaws.com', 'ecr:us-east-1:852015740547.dkr.ecr.us-east-1.amazonaws.com/demo') {
    docker.image('demo').push('latestflask')
  }
}
