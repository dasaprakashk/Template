import falcon
import tensorflow as tf
import json

class Resource(object):
    def on_get(self, req, resp):
        with tf.Session() as sess:
            saver = tf.train.import_meta_graph('../../../models/my_test_model.meta')
            saver.restore(sess,tf.train.latest_checkpoint('../../../models'))
            print(sess.run('w1:0'))
            data = [str(i) for i in sess.run('w1:0')]
            data = 'Value is {}'.format(data[0])
            resp.body = data
