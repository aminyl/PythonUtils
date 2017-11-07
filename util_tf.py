"""
Utils for TensorFlow.
"""

import tensorflow as tf
 
def make_session(gpu_id='0', allow_growth=True):
    """
    for TensorFlow 0.12
    """
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = allow_growth
    config.gpu_options.visible_device_list = gpu_id
    sess = tf.Session(config=config)
    sess.run(tf.global_variables_initializer())
    return sess
