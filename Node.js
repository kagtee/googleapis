const {PubSub} = require('@google-cloud/pubsub');

// Automatically uses GOOGLE_APPLICATION_CREDENTIALS
const pubsub = new PubSub({projectId: 'mystic-pier-481708-c2'});
