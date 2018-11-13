
from keras.utils import np_utils
from sklearn.metrics import classification_report
from keras.datasets import imdb
from keras.preprocessing import sequence
from keras.models import load_model

max_features = 20000
maxlen = 80  # cut texts after this number of words (among top max_features most common words)
batch_size = 32
nb_classes = 2

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
model = load_model('model_keras.mdl')
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
target_names = ['positive reviews', 'negative reviews']
y_pred =  model.predict_classes(x_test)
y_vec = np_utils.to_categorical(y_test, nb_classes)
y_pdk = np_utils.to_categorical(y_pred,nb_classes)
a = classification_report(y_vec, y_pdk, target_names=target_names)

score, acc = model.evaluate(x_test, y_test,
                            batch_size=batch_size)

print('Test score:', score)
print('Test accuracy:', acc)
print(a)