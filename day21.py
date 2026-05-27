# # without super
# class Emp:
#     def show(self):
#         print("employee")
# class Dev(Emp):
#     def show(self):
#         print("deveoper")

# d=Dev()
# d.show()

# # with super keyword
# class Emp:
#     def show(self):
#         print("employee")
# class Dev(Emp):
#     def show(self):
#         super().show()
#         print("deveoper")

# d=Dev()
# d.show()

# ----------------------------

# class E:
#     def __init__(self,name):
#         self.name=name

# class D(E):
#     def __init__(self, name,lang):
#         super().__init__(name)
#         self.language=lang

# d=D("tejas","python")
# print(d.name,d.language)

# -------------------------------

# Good — you attempted almost everything. I’ll **correct + refine + fill missing parts** in simple language. ⚡

# ---

# # ✅ Level 1 — Corrections

# ### 1. Class vs Instance Variable

# Your answer is **partially correct**, refine it like this:

# 👉 **Class Variable**

# * Shared by all objects
# * One copy in memory
# * Example: `company_name`

# 👉 **Instance Variable**

# * Unique for each object
# * Stored inside object
# * Example: `emp_name`

# ---

# ### 2. `__init__`

# ✔ Correct idea, just improve wording:

# 👉 It is a **constructor** used to:

# * Initialize object data
# * Automatically runs when object is created

# ---

# ### 3. Output

# ```python
# print(a.x, b.x)
# ```

# ✔ Your answer: `20, 10` ✅ Correct

# ---

# ### 4. Instance vs Static Method

# You didn’t answer — here is simple version:

# 👉 **Instance Method**

# * Uses `self`
# * Works with object data

# 👉 **Static Method**

# * No `self`
# * Independent (like normal function inside class)

# ---

# # ⚡ Level 2 — All Correct ✅

# 5 → A ✅
# 6 → B ✅
# 7 → A then B ✅ (Perfect)

# ---

# # 🚀 Level 3 — Important Corrections

# ### 8. Output

# ❌ You said: error
# 👉 **Correct answer:**

# ```
# B
# ```

# 👉 No error — only child constructor runs
# 👉 Parent constructor is ignored (because no `super()`)

# ---

# ### 9. Fix Code

# You were close — small mistake (`:`)

# ✔ Correct version:

# ```python
# class A:
#     def __init__(self):
#         print("A")

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("B")

# b = B()
# ```

# Output:

# ```
# A
# B
# ```

# ---

# ### 10. Output

# You wrote: `20 10` ❌

# 👉 Correct answer:

# ```
# 10 20
# ```

# ### Why?

# ```python
# A.x = 10
# B.x = 20
# ```

# 👉 Changing `B.x` does NOT change `A.x`

# ---

# # 🧠 Advanced — Fill Missing Answers

# ### 11. Why `super()` important?

# Your idea is good, improve:

# 👉 It helps to:

# * Reuse parent code
# * Avoid duplication
# * Extend functionality

# ---

# ### 12. MRO (Method Resolution Order)

# 👉 It is the **order in which Python searches for methods**

# Example:

# ```python
# B → A → object
# ```

# 👉 Python checks in this order to find method.

# ---

# ### 13. Overriding vs Overloading

# 👉 **Overriding**

# * Child changes parent method
# * Uses inheritance

# 👉 **Overloading**

# * Same method, different parameters
# * In Python → done using default args or `*args`

# ---

# ### 14. Static method accessing class variable

# 👉 Direct access ❌ not possible

# Wrong:

# ```python
# print(x)
# ```

# Correct:

# ```python
# print(ClassName.x)
# ```

# ---

# ### 15. Why OOP useful?

# Good answer — refine:

# 👉 OOP helps in:

# * Code reusability
# * Better structure
# * Easy maintenance
# * Scalable systems (used in Django, APIs)

# ---

# # 📊 Final Evaluation

# | Level    | Status               |
# | -------- | -------------------- |
# | Basic    | ✅ Good               |
# | Core OOP | ✅ Strong             |
# | Advanced | ⚠️ Needs improvement |

# ---

# # 🔥 Next Step (Recommended)

# You’re ready for **real interview-level coding** now.

# Say:

# 👉 **"give coding problems"**
# or
# 👉 **"take mock interview"**

# I’ll level you up to placement-ready 🚀

