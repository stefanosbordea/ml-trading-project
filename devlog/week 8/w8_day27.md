Day 27:

Overview:
- Chose optimal polynomial(Degree = 1)
- Combined the training and cv sets
- Saved both using joblib
- Made a function for splitting the data data_split()

What/How I learned:
- Looked at results after increasing polynomials, as degree increased accuracy decreased
- Combined training sets because we chose polynomial degree 
- Made a function for splitting the data so i dont repeat in model.py and final_train.py
- Used joblib.dump() to save the model and scaler so they dont re-run every time i import

What's next:
- Implement model in analyst 
- Add new features
