import tensorflow as tf

constant = tf.constant([1, 2, 3])
tensor = constant * constant

with tf.Session() as sess:
	print(tensor.eval())
	p = tf.placeholder(tf.float32)
	t = p + 1.0
	print(t.eval(feed_dict={p:2.0}))