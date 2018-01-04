import tensorflow as tf

my_variable = tf.get_variable("my_variable", [1, 2, 3])
my_int_variable = tf.get_variable("my_int_variable", [1, 2, 3], dtype=tf.int32, 
  initializer=tf.zeros_initializer)
other_variable = tf.get_variable("other_variable", dtype=tf.int32, 
  initializer=tf.constant([23, 42]))

with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	print(my_variable.eval())
	print(my_int_variable.eval())
	print(other_variable.eval())