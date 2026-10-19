import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Image size and batch
img_size = 224
batch_size = 16

# Data preprocessing + augmentation
datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=30,
    zoom_range=0.2,
    horizontal_flip=True
)

# Load training data
train_data = datagen.flow_from_directory(
    "dataset",
    target_size=(img_size, img_size),
    batch_size=batch_size,
    subset='training'
)

# Load validation data
val_data = datagen.flow_from_directory(
    "dataset",
    target_size=(img_size, img_size),
    batch_size=batch_size,
    subset='validation'
)

# Load pretrained model
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)

# Freeze base model
base_model.trainable = False

# Build model
model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(train_data.num_classes, activation='softmax')
])

# Compile model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train model
model.fit(
    train_data,
    validation_data=val_data,
    epochs=5
)

# Save model
model.save("model/gemstone_model.h5")

print("✅ Training complete! Model saved.")