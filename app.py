from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import io
import requests
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# Variables
hyperparams = [
    'manhattan',
    5]

no_of_cylinders = {
    "0": 0,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "8": 8,
    "10": 10,
    "12": 12,
    "16": 16
}

drivetrain = {
    "rear wheel drive": 0,
    "front wheel drive": 1,
    "four wheel drive": 2,
    "all wheel drive": 3
}

no_of_doors = {
    "2": 2,
    "3": 3,
    "4": 4
}

car_makers = {
    "Nissan": 0,
    "Ferrari": 1,
    "Mazda": 2,
    "Honda": 3,
    "Volkswagen": 4,
    "Chevrolet": 5,
    "Chrysler": 6,
    "Dodge": 7,
    "Ford": 8,
    "Audi": 9,
    "Cadillac": 10,
    "Mitsubishi": 11,
    "Porsche": 12,
    "Toyota": 13,
    "GMC": 14,
    "Lotus": 15,
    "Land Rover": 16,
    "Subaru": 17,
    "Mercedes-Benz": 18,
    "Hyundai": 19,
    "BMW": 20,
    "Bentley": 21,
    "Maybach": 22,
    "Suzuki": 23,
    "Saab": 24,
    "Lamborghini": 25,
    "Oldsmobile": 26,
    "Kia": 27,
    "Acura": 28,
    "Pontiac": 29,
    "Lincoln": 30,
    "Scion": 31,
    "FIAT": 32,
    "Plymouth": 33,
    "Buick": 34,
    "Infiniti": 35,
    "Lexus": 36,
    "Aston Martin": 37,
    "Volvo": 38,
    "Alfa Romeo": 39,
    "Genesis": 40,
    "McLaren": 41,
    "Maserati": 42,
    "Rolls-Royce": 43,
    "HUMMER": 44,
    "Spyker": 45,
    "Tesla": 46,
    "Bugatti": 47
}

fuel_type = {
    "premium unleaded (required)": 0,
    "regular unleaded": 1,
    "premium unleaded (recommended)": 2,
    "flex-fuel (unleaded/E85)": 3,
    "diesel": 4,
    "flex-fuel (premium unleaded recommended/E85)": 5,
    "electric": 6,
    "flex-fuel (premium unleaded required/E85)": 7,
    "natural gas": 8,
    "flex-fuel (unleaded/natural gas)": 9
}

transmission_types = {
    "AUTOMATIC": 0,
    "MANUAL": 1,
    "AUTOMATED_MANUAL": 2,
    "DIRECT_DRIVE": 3
}

vehicle_size_types = {
    "Compact": 0,
    "Large": 1,
    "Midsize": 2
}

vehicle_style_types = {
    "Convertible": 0,
    "Coupe": 1,
    "Sedan": 2,
    "Regular Cab Pickup": 3,
    "Extended Cab Pickup": 4,
    "2dr Hatchback": 5,
    "Passenger Van": 6,
    "4dr Hatchback": 7,
    "Passenger Minivan": 8,
    "Crew Cab Pickup": 9,
    "Cargo Minivan": 10,
    "4dr SUV": 11,
    "Wagon": 12,
    "2dr SUV": 13,
    "Cargo Van": 14,
    "Convertible SUV": 15
}

font_size = ("Courier", 14)

# Machine Learning model
class MLModel:
    def __init__(self):
        url = "https://raw.githubusercontent.com/S-Mann/hyperparameter_optimization/master/dataset/dataset.csv"
        s = requests.get(url).content
        self.dataset = pd.read_csv(io.StringIO(s.decode('utf-8')))
        self.excluded_columns = [x not in ['model', 'msrp', 'model_year', 'popularity', 'profit_per_unit', 'units_sold']
                                 for x in self.dataset.columns]
        self.X = self.dataset.iloc[:, self.excluded_columns].values
        self.y = self.dataset.iloc[:, self.dataset.columns == 'msrp'].values

    def train_test_dataset_split(self, test_size):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=123)
        # Create our imputer to replace missing values with the mean e.g.
        imp = SimpleImputer(missing_values=np.nan, strategy='mean')
        imp = imp.fit(self.X_train)
        self.X_train = imp.transform(self.X_train)
        imp = imp.fit(self.X_test)
        self.X_test = imp.transform(self.X_test)

        self.scaler = StandardScaler()
        self.scaler.fit(self.X_train)

        self.X_train = self.scaler.transform(self.X_train)
        self.X_test = self.scaler.transform(self.X_test)

    def fit(self, hyperparams):
        self.classifier = KNeighborsClassifier(
            n_neighbors=hyperparams[1], metric=hyperparams[0])
        self.classifier.fit(self.X_train, np.ravel(self.y_train, order='C'))

    def predict(self, input_val):
        input_val = self.scaler.transform(input_val)
        return self.classifier.predict(input_val)

# Model initialization
model = MLModel()
model.train_test_dataset_split(0.1)
model.fit(hyperparams)

# GUI Design and Logic
root = Tk()
root.title("Car Price Predictor")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

labels_dict = dict({"Engine Hp": {"dropdown": False},
                    "Engine Cylinders": {"dropdown": True, "dropdown_values": no_of_cylinders},
                    "Drivetrain": {"dropdown": True, "dropdown_values": drivetrain},
                    "Number of Doors": {"dropdown": True, "dropdown_values": no_of_doors},
                    "Highway Mileage": {"dropdown": False},
                    "City Mileage": {"dropdown": False},
                    "Manufacturer": {"dropdown": True, "dropdown_values": car_makers},
                    "Fuel Type": {"dropdown": True, "dropdown_values": fuel_type},
                    "Transmission": {"dropdown": True, "dropdown_values": transmission_types},
                    "Size Category": {"dropdown": True, "dropdown_values": vehicle_size_types},
                    "Style Category": {"dropdown": True, "dropdown_values": vehicle_style_types},
                    "Cost To Make": {"dropdown": False}})


def change_dropdown(element, *args):
    print(element.get())
    return True


def label_maker(index, label_name):
    lab = ttk.Label(mainframe, text=label_name)
    lab.config(font=font_size)
    lab.grid(column=1, row=index, pady=(5, 5))
    if(labels_dict[label_name]["dropdown"]):
        input_value = StringVar(root)
        # Dictionary with options
        choices = labels_dict[label_name]["dropdown_values"]
        input_value.set(list(choices)[0])
        popupMenu = OptionMenu(mainframe, input_value, *choices.keys())
        popupMenu.config(font=font_size)
        popupMenu.grid(column=2, row=index)
    else:
        input_value = StringVar()
        input_field = ttk.Entry(mainframe, width=10, textvariable=input_value)
        input_field.config(font=font_size)
        input_field.grid(column=2, row=index)
    labels_dict[label_name].update({"input_value": input_value})
    return True


for id, key in enumerate(labels_dict):
    label_maker(id, key)


def testing(event=None):
    input_list = []
    for key in labels_dict:
        if(not labels_dict[key]["input_value"].get()):
            messagebox.showinfo("Error", "All fields are compulsory!")
            return False
        else:
            if(labels_dict[key]["dropdown"]):
                input_list.append(int(labels_dict[key]["dropdown_values"]
                                      [labels_dict[key]["input_value"].get()]))
            else:
                input_list.append(int(labels_dict[key]["input_value"].get()))

    input_list = np.asarray(input_list).reshape(1, -1)
    labelText.set(str(model.predict(input_list)[0])+"$")
    print(model.predict(input_list))
    return True


labelText = StringVar()
lab = ttk.Label(mainframe, textvariable=labelText)
lab.config(font=font_size)
lab.grid(column=2, pady=(5, 5))

button = ttk.Button(mainframe, text="Calculate",
                    command=testing)
button.grid(column=1)
root.bind('<Return>', testing)


root.mainloop()
