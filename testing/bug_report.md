# 🐞 Bug Reports - Meal Tracker

**Environment:** Live app (PythonAnywhere), manual testing

---

## BUG-01: Negative calories accepted while adding a meal

| Field | Details |
|-------|---------|
| **Module** | Add Meal |
| **Related Test Case** | TC03 |
| **Severity** | Medium |

**Steps to Reproduce:**
1. Open the Add Meal page.
2. Fill all fields and enter -100 in Calories.
3. Submit the form.

**Expected Result:** Negative value is rejected with an error message.

**Actual Result:** Meal is added with -100 calories.

---

## BUG-02: No upper limit on calories value

| Field | Details |
|-------|---------|
| **Module** | Add Meal |
| **Related Test Case** | TC04 |
| **Severity** | Low |

**Steps to Reproduce:**
1. Open the Add Meal page.
2. Enter 99999999999 in Calories and fill other fields.
3. Submit the form.

**Expected Result:** Unrealistic values are rejected.

**Actual Result:** Meal is added successfully.

---

## BUG-03: Invalid text accepted in a numeric field

| Field | Details |
|-------|---------|
| **Module** | Add Meal |
| **Related Test Case** | TC06 |
| **Severity** | Medium |

**Steps to Reproduce:**
1. Open the Add Meal page.
2. Enter "abc" in Protein and fill other fields.
3. Submit the form.

**Expected Result:** Non-numeric input is rejected with a message.

**Actual Result:** Meal is added successfully.

---

## BUG-04: Negative calories accepted while editing a meal

| Field | Details |
|-------|---------|
| **Module** | Edit Meal |
| **Related Test Case** | TC07 |
| **Severity** | Medium |

**Steps to Reproduce:**
1. Open an existing meal and click Edit.
2. Change Calories to -50.
3. Save.

**Expected Result:** Negative value is rejected.

**Actual Result:** Changes are saved with -50 calories.

---

### Severity guide
- **High:** app crashes or a main feature does not work
- **Medium:** a feature works incorrectly, data becomes invalid
- **Low:** minor issue with limited impact
