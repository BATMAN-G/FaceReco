from face_recognition_prediction import predict

# change this to your test image
image_path = "test.jpg"

results = predict(image_path)

if len(results) == 0:
    print("❌ No face detected")
else:
    for name, location in results:
        print(f"✅ Prediction: {name}")