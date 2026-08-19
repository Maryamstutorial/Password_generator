# 🔐 Password Generator

A beginner-friendly Python project that generates random passwords based on the length selected by the user. It also checks the generated password and gives it a strength rating.

## ✨ Features

* Generate random passwords
* Choose the password length
* Option to include symbols
* Uses letters and numbers
* Checks password strength
* Gives a rating: Weak, Medium, or Strong

## 🛠️ Technologies Used

* Python
* `random` module
* `string` module

## 🚀 How to Run

1. Make sure Python is installed on your computer.
2. Clone this repository:

```bash
git clone https://github.com/your-username/password-generator.git
```

3. Open the project folder:

```bash
cd password-generator
```

4. Run the program:

```bash
python password_generator.py
```

## 💻 How It Works

The program first asks the user for the desired password length and whether they want to include symbols.

It then creates a list of possible characters using Python's `string` module and randomly selects characters to generate the password.

After generating the password, the program checks:

* Password length
* Numbers
* Uppercase letters
* Symbols

Based on these checks, the password receives a strength score.

## 📸 Example

```text
Enter the length of your password: 12
Wanna include symbol (yes/no): yes

Password Generated
aK7@pQ2!xL9#

Strong Password
```

## 📚 What I Learned

While building this project, I learned:

* How to use Python's `random` module
* How to work with `string.ascii_letters`, `string.digits`, and `string.punctuation`
* How to use `if/elif/else`
* How loops work
* How `any()` can be used to check characters
* How to create a basic password-strength checker
* How to organize and upload a Python project to GitHub

## 🔮 Future Improvements

I would like to improve this project by adding:

* A stronger password-generation method
* Separate options for uppercase, lowercase, numbers, and symbols
* Better input validation
* A graphical user interface (GUI)
* A copy-to-clipboard feature
* A more advanced password-strength system

⭐ If you find this project useful, feel free to star the repository!
