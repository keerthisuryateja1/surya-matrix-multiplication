# Surya Matrix Multiplication
Optimized 2-multiplication method for 2x2 symmetric circulant matrices.
---

# 🔢 Surya Matrix Multiplication (SMM)

This project implements **three methods** for multiplying 2×2 matrices:

1. 🧠 **Standard Multiplication** (8 multiplications)
2. 🧠 **Strassen’s Algorithm** (7 multiplications)
3. 🧠 **Surya’s Method** (2 multiplications) – optimized for *symmetric circulant matrices*

---
```
## 📂 Project Structure

surya-matrix-multiplication/
├── src/
│   ├── standard\_multiply.py     # Standard 2x2 multiplication
│   ├── strassen\_multiply.py     # Strassen's 2x2 algorithm
│   ├── surya\_multiply.py        # Surya's optimized method
│   └── demo.py                  # Demo: Compare all methods
├── docs/
│   └── SMM.pdf                  # (Upload manually) Project report
├── README.md                    # You're reading it 😎
├── LICENSE                      # MIT License
└── .gitignore                   # Python cache ignores


```
---

## 🧪 How to Run

1. **Clone the repo**
```
git clone https://github.com/keerthisuryateja1/surya-matrix-multiplication.git
cd surya-matrix-multiplication/src
```

2. **Run the demo**

```
python demo.py
```

---

## 💡 What's a Symmetric Circulant Matrix?

It looks like this:

```
[a, b]
[b, a]
```

It has a beautiful property that allows multiplication using only **2 multiplications** (instead of 7 or 8).

---

## ✨ Results Comparison

| Method    | Multiplications | Additions/Subtractions |
| --------- | --------------- | ---------------------- |
| Standard  | 8               | 4                      |
| Strassen  | 7               | 14                     |
| **Surya** | **2**           | 2                      |

🚀 Surya's method is the fastest — but only for symmetric circulant matrices.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Suryateja Keerthi**

* GitHub: [keerthisuryateja1](https://github.com/keerthisuryateja1)
* LinkedIn: [suryateja-keerthi](https://www.linkedin.com/in/suryateja-keerthi)
* Email: [keerthisuryateja2005@gmail.com](mailto:keerthisuryateja2005@gmail.com)

---
