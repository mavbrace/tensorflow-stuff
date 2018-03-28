# Python
# NOTE TO SELF: when using atom (and anything) must open from
# the virtualenv. See tensorflow install page for more.
# Basically: cd ~/tensorflow
# Then ./bin/activate (this activates the virtualenv)
# Then open atom FROM THE CONSOLE!
# Then all goooood - use cmd-i to use the script package, which runs this program.
# Once done, type 'deactivate' in the console to deactivate the virtualenv
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
