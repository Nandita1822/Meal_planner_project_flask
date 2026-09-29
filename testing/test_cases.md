# 🧪 Test Cases - Meal Tracker

**Application:** Meal Management & Nutrition Tracker
**Live URL:** https://nandita2205.pythonanywhere.com/register
**Testing Type:** Manual Functional Testing
**Tester:** Nandita Shukla

| ID | Module | Scenario | Steps | Expected Result | Actual Result | Status |
|----|--------|----------|-------|-----------------|---------------|--------|
| TC01 | Meal Plan | Submit meal plan without selecting any meal | Open Meal Plan page, do not select any meal, submit | App handles it safely (no crash) | Page loaded normally with empty result | ✅ Pass |
| TC02 | Add Meal | Add meal with empty calories field | Open Add Meal, leave calories blank, submit | Empty field is not accepted | Browser blocked the submission (required field) | ✅ Pass |
| TC03 | Add Meal | Add meal with negative calories | Enter -100 in calories, fill other fields, submit | Negative value should be rejected | Meal was added with -100 calories | ❌ Fail |
| TC04 | Add Meal | Add meal with a very large calories value | Enter 99999999999 in calories, submit | Value beyond a sensible limit should be rejected | Meal was added successfully | ❌ Fail |
| TC05 | Add Meal | Add the same meal twice | Add a meal, then add the same meal again | Duplicate entry should be prevented | Duplicate was prevented | ✅ Pass |
| TC06 | Add Meal | Enter text in a numeric field | Enter "abc" in protein, submit | Invalid text should be rejected | Meal was added successfully | ❌ Fail |
| TC07 | Edit Meal | Edit meal with negative calories | Open a meal, edit calories to -50, save | Negative value should be rejected | Changes were saved with -50 calories | ❌ Fail |
| TC08 | Meal Plan | Verify total nutrition of selected meals | Select 2-3 meals, add values manually, compare with app total | Total matches manual calculation | Total was correct | ✅ Pass |

## 📊 Summary

- Total test cases executed: 8
- Passed: 4
- Failed: 4
- Defects raised: see [bug_report.md](bug_report.md)
