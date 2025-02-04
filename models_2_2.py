import tensorflow as tf

class MNIST_DNN:
    def __init__(self, name):
        self.name = name
        return 
    def __call__(self, x, reuse=False):
        
        with tf.variable_scope(self.name) as scope:
            if reuse:
                scope.reuse_variables()
                
            dense1 = tf.layers.dense(inputs=x, units=512, activation=tf.nn.relu, use_bias=False)
            dense2 = tf.layers.dense(inputs=dense1, units=512, activation=tf.nn.relu, use_bias=False)
            dense3 = tf.layers.dense(inputs=dense2, units=512, activation=tf.nn.relu, use_bias=False)
            dense4 = tf.layers.dense(inputs=dense3, units=512, activation=tf.nn.relu, use_bias=False)
            logits = tf.layers.dense(inputs=dense4, units=10, use_bias=False)
        
        
            return [dense1, dense2,dense3,dense4, logits],logits
    
    @property
    def vars(self):
        return tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=self.name)
            
            