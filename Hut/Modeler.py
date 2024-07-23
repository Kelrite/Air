import tensorflow as tf

from tensorflow.keras import Model

from tensorflow.keras.layers import RandomFlip, RandomRotation, RandomTranslation, RandomZoom

class Helper(Model):
  def __init__(self):
    super(Helper, self).__init__()
    self.flip_left_right = RandomFlip()
    self.random_rotation = RandomRotation(0.4)
    self.random_translation = RandomTranslation(0.2, 0.2)
    self.random_size = RandomZoom(0.4)
  
  def call(self, i):
    x = self.flip_left_right(i)
    x = self.random_rotation(x)
    x = self.random_translation(x)
    x = self.random_size(x)
    return x

from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dense, Dropout

class Hantu(Model):
  def __init__(self, outlen):
    super(Hantu, self).__init__()
    self.imasatu = Conv2D(16, 3, activation="relu")
    self.imanida = Conv2D(32, 3, activation="relu")
    self.imatiga = Conv2D(64, 3, activation="relu")
    self.pooling = MaxPool2D((2, 2))

    self.flatten = Flatten()
    self.dropout = Dropout(0.2)
    self.denseri = Dense(64, activation="relu")
    self.classes = Dense(outlen, activation="softmax")

  def call(self, i):
    x = self.pooling(self.imasatu(i))
    x = self.pooling(self.imanida(x))
    x = self.pooling(self.imatiga(x))
    x = self.flatten(x)
    x = self.dropout(x)
    x = self.denseri(x)
    j = self.classes(x)
    return j
